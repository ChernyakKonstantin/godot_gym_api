RLEnvWorld
==========

**Inherits:** `Spatial <https://docs.godotengine.org/en/3.5/classes/class_spatial.html>`_ 
< `Node <https://docs.godotengine.org/en/3.5/classes/class_node.html#class-node>`_ 
< `Object <https://docs.godotengine.org/en/3.5/classes/class_object.html#class-object>`_

Base class for a world that ``RLAgent`` interacs with.

Description
-----------

This class provides interface to obtain the world state (though we also call it as `observation`), 
to configure and to reset the world. User must override the class to implement own World.

In **GodotGymAPI** ``RLEnvWorld`` is considered as everything that ``RLAgent`` can percieve through sensors or interact with. 
World is considered to be the sandbox your agent play in. The world can have NPCs, logic on agent's action response and etc.

Method Descriptions
-------------------

.. function:: (void) _ready()

    Called when the node is "ready", i.e. when both the node and its children have entered the scene tree. 
    If user overrides the method in own subclass the method is called anyway.


.. function:: (void) reset(arguments=null)

    Method to implement logic on world reset.

    Args:
        arguments: Any structure containing information for world reset.

.. function:: (void) configure(world_config: Dictionary)

    Optional method to implement logic on world configuration.
    
    Args:
        world_config (Dictionary): World configuration.

.. function:: (void) get_data(observation_request, storage)

    Method to be overriden to implement logic on filling protobuf message ``WorldData`` field to send data from Godot.

    Args:
        observation_request: Any structure containing information about requested observations.
        storage: ``WorldData`` field from protobuf message to send data from Godot.