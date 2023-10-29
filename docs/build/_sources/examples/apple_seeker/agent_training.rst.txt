Training
========

In this step, we train PPO algorithm with help of 
`Stable Baselines3 (SB3) <https://github.com/DLR-RM/stable-baselines3>`_ library. 
Basically, it is reproduction of the 
`SB3 example <https://stable-baselines3.readthedocs.io/en/master/guide/examples.html>`_.

Steps
-----

1. In your project directory create a file ``train.py``.

2. Import required packages as follows:

    .. code-block:: python

        import os
        from functools import partial

        # Import stable-baselines3 stuff
        from stable_baselines3 import PPO
        from stable_baselines3.common.callbacks import CheckpointCallback
        from stable_baselines3.common.env_util import make_vec_env

        # Import gym environment
        from apple_seeker_env import AppleSeekerEnv

3. Define Godot app address:

    .. code-block:: python

        ADDRESS = "127.0.0.1"
        PORT = 9090

4. Define directory to store logs and logname:

    .. code-block:: python

        LOG_DIR = "./logs/apple_seeker"
        LOG_NAME = "PPO"
        SUFFIX = "1"

5. Define training parameters:

    .. code-block:: python
        
        TOTAL_TIMESTEPS = 150000
        N_STEPS = 1000
        CHECKPOINT_FREQUENCY = 1000
        LR = 1e-3

6. Define training function:

    .. code-block:: python

        def train():
            # Instantiate gym environment
            env_fn = partial(
                AppleSeekerEnv,
                engine_address=(ADDRESS, PORT)
            )
            env = make_vec_env(env_fn, n_envs=1, seed=0)
            
            # Instatiate agent
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

            # Define agent training
            model.learn(
                callback=CheckpointCallback(
                    save_freq = CHECKPOINT_FREQUENCY,
                    save_path = os.path.join(LOG_DIR, LOG_NAME + "_" + SUFFIX, "checkpoints"),
                ),
                total_timesteps=TOTAL_TIMESTEPS,
                tb_log_name=LOG_NAME,
                progress_bar=True,
            )

            # Save final model
            model.save(os.path.join(LOG_DIR, LOG_NAME + SUFFIX, "checkpoints", "last.zip"))

7. Define module behaviour on launch:

    .. code-block:: python

        if __name__ == "__main__":
            train()

Complete code should look as follows:

.. code-block:: python

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

8. Run Godot app from Godot Editor.

.. note::

    You also can compile Godot app and run executable.

9. Run training process as follows:

.. code-block:: bash

    python3 train.py