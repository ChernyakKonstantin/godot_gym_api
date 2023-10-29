# About
Godot Gym API is an Open-Source framework to enable use of Godot 3.5 as 3D- or 2D-environment to train Reinforcement Learning (RL) algorithms.

Documentation available [here](https://chernyakkonstantin.github.io/godot_gym_api/build/).

# Installation
1. Install the framework in python with the following command:
    ```
    pip3 install git+https://github.com/ChernyakKonstantin/godot_gym_api.git#subdirectory=python
    ```

2. Install Godot addon into your Godot project with **godot_gym_api** CLI tool:
    ```
    godot_gym_api install_addon <PATH_TO_YOUR_GODOT_PROJECT>
    ```

    and activate installed addons in `Project/Project Settings/Plugins` tab.

3. Install `protobuf` into your OS following [Protocol Buffers repository](https://github.com/protocolbuffers/protobuf/releases).

# Running Examples
To run an example launch main scene of Godot project `examples/apple_seeker/godot` from Godot engine, then launch python training code with `python examples/apple_seeker/python/train.py ` command.

# How It Works
There is persistent TCP communication between a Godot application and Python implemented inside a `gym.Env` inhereted class. Thus, feel free to use any of your favorite RL-frameworks!

# Programming Languages Support
Currently, there is support of Python as the programming language to implement the RL-algorithms. In Python, the environmnet provides `gym` / `gymnasium` interface.

If one has a desire to implement the client for any other languages, submit pull request, please.

# Coming soon
* Vectorized Environment support;
* Multi-agent Environment support;

# Communication
Join this [Telegram channel](https://t.me/godot_rl) to watch for new updates.

You can contact me through [E-mail](chernyakonstantin@gmail.com) or [Telegram](https://t.me/kainrehck).
