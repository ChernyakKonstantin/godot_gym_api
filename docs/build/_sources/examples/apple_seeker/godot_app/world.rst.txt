Creating World
==============

Now we are going to create a *World*. 
In **Godot Gym API** *World* (``RLEnvWorld`` node) is assumed to be everything in the environment 
the agent can interact with. For this tutotial, the *World* is a room with an apple inside. 
The apple can be located anywhere inside the room and its location is assigned on the *World* reset.

1. Open ``World.tscn`` file.

2. Change ``World`` node type from ``Spatial`` to ``RLEnvWorld``.

3. Open ``World`` node script.

4. Change script as follows:

    .. tabs::
        .. code-tab:: gdscript Modified script

            extends RLEnvWorld

            onready var apple = $Apple
            onready var spawn_areas = $SpawnAreas
            onready var apple_caught: bool = false

            func _ready():
                apple.get_node("AppleCatchArea").connect("body_entered", self, "_on_catch_apple")

            func reset(arguments=null):
                apple_caught = false
                apple.set_global_translation(_sample_initial_position())

            func _on_catch_apple(_body):
                apple_caught = true
                
            func get_data(observation_request, storage) -> void:
                storage.set_apple_caught(apple_caught)

            func _sample_initial_position() -> Vector3:
                var i = randi() % spawn_areas.get_children().size()
                return spawn_areas.get_child(i).get_global_translation()

        .. code-tab:: gdscript Original script

            extends Spatial

            onready var apple = $Apple
            onready var spawn_areas = $SpawnAreas

            func _ready():
                apple.get_node("AppleCatchArea").connect("body_entered", self, "_on_catch_apple")

            func reset():
                apple.set_global_translation(_sample_initial_position())

            func _on_catch_apple(_body):
                reset()

            func _sample_initial_position() -> Vector3:
                var i = randi() % spawn_areas.get_children().size()
                return spawn_areas.get_child(i).get_global_translation()

Let's examine what we changed.

1. We changed parent class from ``Spatial`` to ``RLEnvWorld``.

2. We introduced new variable to store current world state since we want to know it.

    .. code-block:: gdscript

        onready var apple_caught: bool = false

3. ``RLEnvWorld`` class have optional method ``reset`` to reset world that does nothing be default. 
In original game we already had it implemented. 
However, we need to modify it to match ``RLEnvWorld`` signature.

    .. tabs::

        .. code-tab:: gdscript Modified script

            func reset(arguments=null):

        .. code-tab:: gdscript Original script

            func reset():

    Then we need to add reset of our new variable:

    .. code-block:: gdscript

        apple_caught = false

4. Original game is reseted once robot touches the apple. Now we want our new variable to be set on this event.

    .. tabs::

        .. code-tab:: gdscript Modified script

            func _on_catch_apple(_body):
                apple_caught = true

        .. code-tab:: gdscript Original script

            func _on_catch_apple(_body):
                reset()

5. By default, ``RLEnvWorld.get_data`` method raise an error, since no data to return is specified.
Here, we override it to set ``storage.apple_caught`` field with ``apple_caught`` value. 
``storage`` is ``world_data`` field in protobuf message we have defined earlier. 
In case you define various possible observations but you want to experiment with particular ones, 
you can define logic of the storage filling with help of observation keys in ``observation_request``.

    .. code-block:: gdscript

        # The method does not depend on `observation_request` argument in this example.
        func get_data(observation_request, storage) -> void:
            storage.set_apple_caught(apple_caught)

Thats's it for ``World``! Let's summarize:

1. ``RLEnvWorld`` must have ``get_data`` method implemented.
2. ``RLEnvWorld`` can have ``reset`` method implemented.  
