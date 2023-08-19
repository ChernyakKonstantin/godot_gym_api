# About
Godot-RL is an Open-Source framework to enable use of Godot 3.5 as an environment to train Reinforcement Learning (RL) algorithms.

The framework is grown from a custom project on self-driving topic, so current ready-to-use sensors available are LIDAR and RGB-Camera.

# Programming Languages Support
Currently, there is support of Python as the programming language to implement the RL-algorithms. In Python, the environmnet provides `gym` / `gymnasium` interface.

If one has a desire to implement the client for any other languages, submit pull request, please.

# How It Works
The application implemented in Godot serves as TCP-server, accepting requests from a client, that can be a `gym.Env` with `GodotClient` under hood.

# Installation

1. Install `protobuf` into your OS following [Protocol Buffers repository](https://github.com/protocolbuffers/protobuf/releases).
2. Install `godobuf` plugin into Godot, follow instruction in the [Godobuf repository](https://github.com/oniksan/godobuf).
3. Currently there is no plugin in Godot Assets Library. One should copy-paste `godot_addon` content into `addons` directory of his own project and enable the `Reinforcement Learning` plugin in `Project/Project Settings/Plugins`.
4. Currently, there is no PyPy package. One can copy-paste `python` directory content into his own code.

# Running Examples
To run an example launch main scene of Godot project `examples/apple_seeker/godot` from Godot engine, then launch python training code with `python examples/apple_seeker/python/train.py ` command.

# Coming soon
* Vectorized Environment support;
* Multi-agent Environment support;
* Documentation.

# Communication
Join this [Telegram channel](https://t.me/godot_rl) to watch for new updates.

You can contact me through [E-mail](chernyakonstantin@gmail.com) or [Telegram](https://t.me/kainrehck).
