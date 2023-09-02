import json
import socket
from typing import Any, Dict, Tuple

import numpy as np


class GodotClient:
    # Predefined keys to enable consistency with Godot application.
    STATUS_KEY = "status"
    CONFIG_KEY = "config"
    RESET_KEY = "reset"
    ACTION_KEY = "action"
    OBSERVATION_KEY = "observation"
    WORLD_KEY = "world"
    AGENT_KEY = "agent"
    ENVIRONMENT_KEY = "environment"

    def __init__(
        self,
        protobuf_message_module,
        engine_address: Tuple[str, int],
        chunk_size: int = 65536
    ) -> None:
        """
        Simulator engine client class.
        It requests for current state and send the RL-agent action.

        protobuf_message_module: module to load protobuf message from.
        engine_address: tuple of (`IP-address`, `port`).
        chunk_size: int: size of the chunk to receive response from engine.
        """
        self.protobuf_message_module = protobuf_message_module
        self.engine_address = engine_address
        self.chunk_size = chunk_size
        self.connection = socket.create_connection(self.engine_address)

    def _get_protobuf(self, raw_value: bytes) -> Any:
        value = self.protobuf_message_module.Message()
        value.ParseFromString(raw_value)
        return value

    def _get_data_from_stream(self, connection: socket.socket) -> bytes:
        package_size = int.from_bytes(connection.recv(4), "little")
        chunks = b''
        while len(chunks) < package_size:
            recv_size = min(package_size, self.chunk_size)
            chunk = connection.recv(recv_size)
            chunks += chunk
        return chunks

    def _get_response(self, connection: socket.socket) -> Dict[str, Any]:
        data = self._get_data_from_stream(connection)
        response_protobuf = self._get_protobuf(data)
        agent_data_keys = [f.name for f in response_protobuf.agent_data.DESCRIPTOR.fields]
        world_data_keys = [f.name for f in response_protobuf.world_data.DESCRIPTOR.fields]
        response = {
            self.AGENT_KEY: {k: getattr(response_protobuf.agent_data, k) for k in agent_data_keys},
            self.WORLD_KEY: {k: getattr(response_protobuf.world_data, k) for k in world_data_keys},
        }
        return response

    # TODO: implement timeout and return False if timeout is exceeded.
    def request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        request_bytes = json.dumps(request).encode("utf-8")
        request_size = len(request_bytes)
        self.connection.sendall(request_size.to_bytes(4, "little") + request_bytes)
        response = self._get_response(self.connection)
        return response

    def check_if_server_is_ready(self) -> bool:
        """
        Check if server is started.
        """
        # The value under `STATUS_KEY` has no meaning.
        request = {self.STATUS_KEY: 1}
        try:
            self.request(request)
            return True
        except ConnectionRefusedError:
            return False

    def configure(self, config: Dict[str, Any]):
        """
        Configure the engine.
        """
        request = {self.CONFIG_KEY: config}
        return self.request(request)

    def step(
            self,
            action: Any,
            requested_observation: Dict[str, Any],
        ) -> Dict[str, Any]:
        """
        Request engine to perform given action and return specified observations.
        """
        request = {
            self.ACTION_KEY: action,
            self.OBSERVATION_KEY: requested_observation,
        }
        response = self.request(request)
        return response

    def reset(
            self,
            requested_observation: Dict[str, Any],
        ) -> Dict[str, Any]:
        """
        Request engine to reset environment and return specified observations.
        """
        # The value under `STATUS_KEY` has no meaning.
        request = {
            self.RESET_KEY: 1,
            self.OBSERVATION_KEY: requested_observation,
        }
        return self.request(request)
