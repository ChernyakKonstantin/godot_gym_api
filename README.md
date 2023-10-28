# About
Godot Gym API is an Open-Source framework to enable use of Godot 3.5 as an environment to train Reinforcement Learning (RL) algorithms.

Documentation available [here](https://chernyakkonstantin.github.io/godot_gym_api_docs/).

# Programming Languages Support
Currently, there is support of Python as the programming language to implement the RL-algorithms. In Python, the environmnet provides `gym` / `gymnasium` interface.

If one has a desire to implement the client for any other languages, submit pull request, please.

# How It Works
There is persistent TCP communication between a Godot application and Python implemented inside a `gym.Env` inhereted class. Thus, any of your favorite RL-frameworks are ready to work with it!

# Installation
## In Godot
1. Install `protobuf` into your OS following [Protocol Buffers repository](https://github.com/protocolbuffers/protobuf/releases).
2. Copy-paste `godot_addon` content into `addons` directory of his own project and enable the `Reinforcement Learning` and `Godobuf` plugins in `Project/Project Settings/Plugins`.
## In Python
Currently, there is local installation only. To install, perform the following command from the repo root:
```
    cd python
    pip install .
```

# Running Examples
To run an example launch main scene of Godot project `examples/apple_seeker/godot` from Godot engine, then launch python training code with `python examples/apple_seeker/python/train.py ` command.

# Coming soon
* Vectorized Environment support;
* Multi-agent Environment support;
* Documentation.

# Communication
Join this [Telegram channel](https://t.me/godot_rl) to watch for new updates.

You can contact me through [E-mail](chernyakonstantin@gmail.com) or [Telegram](https://t.me/kainrehck).
