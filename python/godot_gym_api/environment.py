from typing import Any, Dict, Tuple

import gymnasium as gym

from .godot_client import GodotClient


class GodotEnvironment(gym.Env):
    """Base class to create custom environments to work with a Godot app."""

    WORLD_KEY = GodotClient.WORLD_KEY
    AGENT_KEY = GodotClient.AGENT_KEY

    def __init__(
        self,
        protobuf_message_module,
        engine_address: Tuple[str, int] = ("127.0.0.1", 9090),
        engine_chunk_size: int = 65536,
    ):
        """Initialize environment.

        User can override `self._requested_observation` with his own values.

        """
        super().__init__()
        self._godot_client = GodotClient(protobuf_message_module, engine_address, engine_chunk_size)
        if not hasattr(self, "_requested_observation"):
            self._requested_observation = {self.AGENT_KEY: [], self.WORLD_KEY: []}

    def _godot_step(self, action: Any) -> Dict[str, Any]:
        """Wrapper over `GodotClient.step`.

        The wrapper substitutues `requested_observation` argument with `self._requested_observation`.

        Args:
            action (Any): Action to perform by Agent.

        Returns:
            Dict[str, Any]: New observation.

        """
        return self._godot_client.step(action, self._requested_observation)

    def _godot_reset(self) -> Dict[str, Any]:
        """Wrapper over `GodotClient.reset`.

        The wrapper substitutues `requested_observation` argument with `self._requested_observation`.

        Returns:
            Dict[str, Any]: Initial observation.

        """
        return self._godot_client.reset(self._requested_observation)

    def _godot_configure(self, config: Dict[str, Any]) -> None:
        """Wrapper over `GodotClient.configure`.

        Args:
            config (Dict[str, Any]): Configuration to be set.

        """
        self._godot_client.configure(config)
