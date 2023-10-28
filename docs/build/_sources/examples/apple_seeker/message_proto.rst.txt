Creating protobuf message
=========================

In this step, we create protobuf message. The message defines the data transfered from Godot to Python. 

1. Create template ``message.proto`` file with the following command from your terminal:
    
    .. code-block:: bash

        godot-gym-api create_proto <YOUR_PATH>/apple_seeker

2. Change the created ``message.proto`` file as follows:

    .. code-block::

        syntax = "proto3";

        message WorldData {
            bool apple_caught = 1;
        }

        message AgentData {
            repeated float distances_to_obstacle = 1;
            repeated float distances_to_target = 2;
        }

        message Message {
            AgentData agent_data = 1;
            WorldData world_data = 2;
        }

Let's breakdown, what's happening here.

In **Godot Gym API** every message is assumed to have both *Agent* data and *World* data. 

.. code-block::

    message Message {
        AgentData agent_data = 1;
        WorldData world_data = 2;
    }

For this project we want the agent to return distances to the room walls and distances 
to the apple *(float values)*. Thus, we define ``AgentData`` as follows:

.. code-block::

    message AgentData {
        repeated float distances_to_obstacle = 1;
        repeated float distances_to_target = 2;
    }

Also, we want to know whether the apple is caught *(boolean value)*. We will use this information 
in reward function and while checking the episode termination later. 
Thus, we define ``WorldData`` as follows:

.. code-block::

    message WorldData {
        bool apple_caught = 1;
    }