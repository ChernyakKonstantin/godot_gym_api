import os
from functools import partial

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.env_util import make_vec_env

from apple_seeker_env import AppleSeekerEnv

ADDRESS = "127.0.0.1"
PORT = 9090

LOG_DIR = "./logs/apple_seeker"
LOG_NAME = "PPO"
SUFFIX = "1"

TOTAL_TIMESTEPS = 150000
N_STEPS = 1000
CHECKPOINT_FREQUENCY = 1000
LR = 1e-3

def train():
    env_fn = partial(
        AppleSeekerEnv,
        engine_address=(ADDRESS, PORT)
    )
    env = make_vec_env(env_fn, n_envs=1, seed=0)

    model = PPO(
        "MultiInputPolicy",
        n_steps=N_STEPS,
        env=env,
        use_sde=False,
        learning_rate=LR,
        verbose=1,
        device="cpu",
        seed=0,
        tensorboard_log=LOG_DIR,
    )
    model.learn(
        callback=CheckpointCallback(
            save_freq = CHECKPOINT_FREQUENCY,
            save_path = os.path.join(LOG_DIR, LOG_NAME + "_" + SUFFIX, "checkpoints"),
        ),
        total_timesteps=TOTAL_TIMESTEPS,
        tb_log_name=LOG_NAME,
        progress_bar=True,
    )
    model.save(os.path.join(LOG_DIR, LOG_NAME + SUFFIX, "checkpoints", "last.zip"))

if __name__ == "__main__":
    train()