import json
import socket
import time
from types import ModuleType
from typing import Any, Dict, Tuple


class GodotClient:
    """Simulator engine client class.

    The class sends actions for RL-agent to a Godot app and gets current state from the Godot app.
    The class establish a persistent TCP connection.
    The class sends requests in form of JSON-files.
    The class recieve data in form of Protobuf messages.

    """

    # Predefined keys to enable consistency with Godot application.
    CONFIG_KEY = "config"
    RESET_KEY = "reset"
    ACTION_KEY = "action"
    OBSERVATION_KEY = "observation"
    WORLD_KEY = "world"
    AGENT_KEY = "agent"
    ENVIRONMENT_KEY = "environment"

    DEFAULT_TIME_SPEED: float = 1.0
    DEFAULT_REPEAT_ACTION: int = 4

    def __init__(
        self,
        protobuf_message_module: ModuleType,
        engine_address: Tuple[str, int],
        chunk_size: int = 65536,
    ) -> None:
        """Initialize Godot Client.

        Args:
            protobuf_message_module (ModuleType): A module to load protobuf message from.
            engine_address (Tuple[str, int]): Tuple of (`IP-address`, `port`).
            chunk_size (int): Size of the chunk to receive response from engine.

        """
        self.protobuf_message_module = protobuf_message_module
        self.engine_address = engine_address
        self.chunk_size = chunk_size
        self.connection = self._connect_to_server()

    def _connect_to_server(self) -> None:
        """Repeatedly try to establish a connection to Godot app."""
        print("Waiting for Godot server launch.")
        connection = None
        while connection is None:
            try:
                connection = socket.create_connection(self.engine_address)
            except ConnectionRefusedError:
                time.sleep(1)
                continue
        print("Connection is established.")
        return connection

    def _get_protobuf(self, raw_value: bytes) -> Any:
        """Parse bytes to restore Protobuf message.

        Args:
            raw_value (bytes): Raw data from TCP stream.

        Returns:
            Any: Restored Protobuf message.

        """
        value = self.protobuf_message_module.Message()
        value.ParseFromString(raw_value)
        return value

    def _get_data_from_stream(self) -> bytes:
        """Read data from TCP stream.

        Returns:
            bytes: Raw data from TCP stream.

        """
        package_size = int.from_bytes(self.connection.recv(4), "little")
        chunks = b""
        while len(chunks) < package_size:
            recv_size = min(package_size, self.chunk_size)
            chunk = self.connection.recv(recv_size)
            chunks += chunk
        return chunks

    def _get_response(self) -> Dict[str, Any]:
        """Read response from Godot app.

        The method can accept only Protobuf messages as Godot response.

        Returns:
            Dict[str, Any]: Received Protobuf message with Agent and World observations.

        """
        data = self._get_data_from_stream()
        response_protobuf = self._get_protobuf(data)
        response = {
            self.AGENT_KEY: response_protobuf.agent_data,
            self.WORLD_KEY: response_protobuf.world_data,
        }
        return response

    # TODO: implement timeout and return False if timeout is exceeded.
    def request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send request to Godot app and get response.

        Args:
            request (Dict[str, Any]): Request.

        Returns:
            Dict[str, Any]: Response.

        """
        request_bytes = json.dumps(request).encode("utf-8")
        request_size = len(request_bytes)
        self.connection.sendall(request_size.to_bytes(4, "little") + request_bytes)
        response = self._get_response()
        return response

    def configure(self, config: Dict[str, Any]) -> None:
        """Request engine to set configuration.

        Args:
            config (Dict[str, Any]): Configuration to be set.

        """
        request = {self.CONFIG_KEY: config}
        _ = self.request(request)

    def step(
        self,
        action: Any,
        requested_observation: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Request engine to perform given action and return new observations.

        Args:
            action (Any): Action to perform by Agent.
            requested_observation (Dict[str, Any]): Requested observations from World and Agent.

        Returns:
            Dict[str, Any]: New observation.

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
        Request Godot app to reset environment.

        Args:
            requested_observation (Dict[str, Any]): Requested observations from World and Agent.

        Returns:
            Dict[str, Any]: Initial observation.

        """
        request = {
            self.RESET_KEY: 1,
            self.OBSERVATION_KEY: requested_observation,
        }
        return self.request(request)

    def set_time_speed(self, time_speed: float) -> None:
        """Request engine to set time speed.

        Args:
            time_speed (float): Time speed to be set.

        """
        config = {self.ENVIRONMENT_KEY: {"time_speed": time_speed}}
        self.configure(config)

    def set_repeat_action(self, n_repeats: int) -> None:
        """Request engine to set repeat action.

        Args:
            n_repeats (int): Number of repeats to be set.

        """
        config = {self.ENVIRONMENT_KEY: {"repeat_action": n_repeats}}
        self.configure(config)
