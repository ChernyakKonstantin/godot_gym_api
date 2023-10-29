Apple Seeker example
====================

In this step-by-step tutorial, you will create your first complete RL-project with **Godot Gym API**. 
By the end of tutorial you will have a trained agent capable of finding apples in the room.

You will learn to:

* Install **Godot Gym API** in Python and Godot.
* Create an environment in Godot with help of **Godot Gym API** base classes.
* Create Gym interface in Python with help of **Godot Gym API** base classes.
* Establish a connection between Godot and Python.
* Train your own agent with help of `Stable-Baselines3 library <https://github.com/DLR-RM/stable-baselines3>`_.

.. note::
    In this tutorial, it is assumed that you are already familiar with Godot. 
    If you are new to Godot, first learn Godot basics from 
    `this official tutorial series <https://docs.godotengine.org/en/3.5/getting_started/introduction/index.html>`_.

.. note::
    In this tutorial, *GDScript* language is used to code in Godot.

The complete example can be found 
`here <https://github.com/ChernyakKonstantin/godot_gym_api/tree/main/examples/apple_seeker>`_.

The original game can be found 
`here <https://github.com/ChernyakKonstantin/godot_gym_api/tree/main/examples/apple_seeker/original_game>`_.

Environment Description
-----------------------

In this tutorial, we develop a simple environment, consisting of a room with a robot and an apple inside. 
The robot has 16 sensors located in a circle. 
These sensors measure the distance to the room walls and to the apple. 
The robot can move *forward*, *backward*, *left*, *right*.
The robot task is to quickly reach the apple from any starting point. 
The apple can be located in any position in the room at the begging of an episode. 

To demonstate how it is easy to adapt yout existing Godot game to RL-environment we will use original game as source.

.. image:: ./images/environment_demo.gif
    :width: 600

Steps
-----

.. toctree::
    :maxdepth: 2
    
    project
    installation
    message_proto
    godot_app/index
    gym_env
    agent_training
    final


