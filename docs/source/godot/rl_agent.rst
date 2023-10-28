RLAgent
=======

**Inherits:** `Spatial <https://docs.godotengine.org/en/3.5/classes/class_spatial.html>`_ 
< `Node <https://docs.godotengine.org/en/3.5/classes/class_node.html#class-node>`_ 
< `Object <https://docs.godotengine.org/en/3.5/classes/class_object.html#class-object>`_

Base class for RL agents.

Description
-----------

This class provides interface to set an agent action, to obtain the agent observation, 
to configure and to reset the agent. User must override the method to implement own agent.

Method Descriptions
-------------------

.. function:: (void) _ready()

    Called when the node is "ready", i.e. when both the node and its children have entered the scene tree. 
    If user overrides the method in own subclass the method is called anyway.


.. function:: (void) set_action(action)

    The method must be overriden to implement logic how action is used by the agent.

    Args:
        action: Any structure containing information about an action to be performed

.. function:: (void) reset(arguments=null)

    Method to implement logic on agent reset.

    Args:
        arguments: Any structure containing information for Agent reset.

.. function:: (void) configure(agent_config: Dictionary)

    Optional method to implement logic on agent configuration.
    
    Args:
        agent_config (Dictionary): Agent configuration.

.. function:: (void) get_data(observation_request, storage)

    Method to be overriden to implement logic on filling protobuf message `AgentData` field to send data from Godot.

    Args:
        observation_request: Any structure containing information about requested observations.
        storage: `AgentData` field from protobuf message to send data from Godot.