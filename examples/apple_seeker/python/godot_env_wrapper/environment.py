from typing import Any, Dict, Tuple

import gymnasium as gym

from .godot_client import GodotClient


class GodotEnvironment(gym.Env):
    WORLD_KEY = GodotClient.WORLD_KEY
    AGENT_KEY = GodotClient.AGENT_KEY

    def __init__(
        self,
        protobuf_message_module,
        engine_address: Tuple[str, int] = ("127.0.0.1", 9090),
        engine_chunk_size: int = 65536,
    ):
        super().__init__()
        self._godot_client = GodotClient(protobuf_message_module, engine_address, engine_chunk_size)
        if not hasattr(self, "_requested_observation"):
            self._requested_observation = {}

    def _godot_step(self, action: Any) -> Dict[str, Any]:
        return self._godot_client.step(action, self._requested_observation)

    def _godot_reset(self) -> Dict[str, Any]:
        return self._godot_client.reset(self._requested_observation)

    def _godot_configure(self, config: Dict[str, Any]):
        self._godot_client.configure(config)
