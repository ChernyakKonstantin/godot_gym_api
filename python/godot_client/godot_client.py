import json
import socket
from collections import defaultdict
from io import BytesIO
from time import time
from typing import Any, Dict, Tuple

import numpy as np
from PIL import Image


class GodotClient:
    STATUS_KEY = "status"
    CONFIG_KEY = "config"
    RESET_KEY = "reset"
    ACTION_KEY = "action"
    OBSERVATION_KEY = "observation"

    IMAGE_DIMS = (240, 360, 3)

    TIMEOUT_EXCEEDED = -1

    def __init__(
        self,
        engine_address: Tuple[str, int],
        chunk_size: int = 65536
    ) -> None:
        """
        Simulator engine client class.
        It requests for current state and send the RL-agent action.
        engine_address: tuple of (`IP-address`, `port`).
        chunk_size: int: size of the chunk to receive response from engine.
        """
        self.engine_address = engine_address
        self.chunk_size = chunk_size


    def _get_int32(self, data: bytes) -> Tuple[bytes, int]:
        raw_value = data[:4]
        value = np.frombuffer(raw_value, dtype=np.int32)[0]
        return data[4:], value

    def _get_json(self, data: bytes) -> Tuple[bytes, Dict[str, Any]]:
        data, buffer_size = self._get_int32(data)
        raw_value = data[:buffer_size]
        value = json.loads(raw_value.decode("utf-8"))
        return data[buffer_size:], value

    def _get_data_from_stream(self, connection: socket.socket) -> bytes:
        chunks = b''
        while True:
            chunk = connection.recv(self.chunk_size)
            if not chunk:
                break
            chunks += chunk
        return chunks

    def _get_response(self, connection: socket.socket) -> Dict[str, Any]:
        data = self._get_data_from_stream(connection)
        data, respose_json = self._get_json(data)
        return respose_json

    # TODO: implement timeout and return False if timeout is exceeded.
    def request(self, request: Dict[str, Any], response_is_required: bool = True) -> Dict[str, Any]:
        request_bytes = json.dumps(request).encode("utf-8")
        with socket.create_connection(self.engine_address) as connection:
            connection.sendall(request_bytes)
            if response_is_required:
                response = self._get_response(connection)
            else:
                response = None
        return response

    def check_if_server_is_ready(self) -> bool:
        """
        Check if server is started.
        """
        request = {self.STATUS_KEY: 1}
        try:
            self.request(request, response_is_required=False)
            return True
        except ConnectionRefusedError:
            return False

    def configure(self, config: Dict[str, Any]) -> bool:
        """
        Configure the engine.
        """
        request = {self.CONFIG_KEY: config}
        return self.request(request, response_is_required=False)

    def request_step(
            self,
            action: Dict[str, Any],
            requested_observation: Tuple[int],
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
            requested_observation: Tuple[int],
        ) -> Dict[str, Any]:
        """
        Request engine to reset environment and return specified observations.
        """
        request = {
            self.RESET_KEY: 1,
            self.OBSERVATION_KEY: requested_observation,
        }
        return self.request(request)
