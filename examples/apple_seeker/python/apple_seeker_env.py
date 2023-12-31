from typing import Any, Dict, Tuple

import numpy as np
from gymnasium import spaces

from godot_gym_api import GodotEnvironment
import message_pb2 as protobuf_message_module

class AppleSeekerEnv(GodotEnvironment):
    def __init__(
        self,
        engine_address: Tuple[str, int] = ("127.0.0.1", 9090),
        engine_chunk_size: int = 65536,
        episode_length: int = 500,
    ):
        super().__init__(protobuf_message_module, engine_address, engine_chunk_size)
        self._episode_length = episode_length
        # Define observation space in accordance to the agent in Godot app.
        self._max_distance = 5
        self.observation_space = spaces.Dict(
            spaces={
                "distances_to_obstacle": spaces.Box(
                    low=0,
                    high=self._max_distance,
                    shape=[16,],
                    dtype=np.float32,
                ),
                "distances_to_target": spaces.Box(
                    low=0,
                    high=self._max_distance,
                    shape=[16,],
                    dtype=np.float32,
                ),
            },
        )
        # The example Godot app return all its observation for agent and world. There is no need to specife them.
        self._requested_observation = {self.AGENT_KEY: [], self.WORLD_KEY: []}
        # Define action space in accordance to the agent in Godot app.
        self.action_space = spaces.Discrete(4)
        # Set during reset
        self._step_counter = None
        # Speed up time in Godot to gather more samples per second.
        self._godot_set_time_speed(4.0)

    def _observe(self, state: Dict[str, Dict[str, Any]]) -> Dict:
        observation = {
            "distances_to_obstacle": np.asarray(state[self.AGENT_KEY].distances_to_obstacle),
            "distances_to_target": np.asarray(state[self.AGENT_KEY].distances_to_target),
        }
        return observation

    def _is_terminated(self, state) -> bool:
        episode_steps_limit_reached = self._step_counter == self._episode_length
        apple_caught = state[self.WORLD_KEY].apple_caught
        return episode_steps_limit_reached or apple_caught

    def _reward_function(self, state):
        if state[self.WORLD_KEY].apple_caught:
            return 100
        else:
            return -min(np.asarray(state[self.AGENT_KEY].distances_to_target)) / self._max_distance

    def step(self, action: np.ndarray) -> Tuple[np.ndarray, float, bool, dict]:
        state = self._godot_step(action.item())
        self._step_counter += 1
        observation = self._observe(state)
        terminated = self._is_terminated(state)
        reward = self._reward_function(state)
        return observation, reward, terminated, False, {}

    def reset(self, *args, **kwargs) -> np.ndarray:
        self._step_counter = 0
        state = self._godot_reset()
        observation = self._observe(state)
        return observation, {}

    def seed(self, *args, **kwargs):
        pass

    def render(self):
        pass

    def close(self):
        pass