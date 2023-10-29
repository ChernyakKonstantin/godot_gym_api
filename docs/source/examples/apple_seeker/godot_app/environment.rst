Creating Environment
====================

Now we are going to create an *Environment*. 
In **Godot Gym API** *Environment* (``RLEnvironment`` node) is assumed as top node that manage communication and game loop. 
*World* and *Agent* is considered as *Environment* children. Environment can have only one *Agent* and only one *World*.

1. Open ``Environment.tscn`` file.

2. Change ``Environment`` node type from ``Spatial`` to ``RLEnvironmnt``.

3. Open ``Agent`` node Inspector tab and select ``Environmnet/World/Apple`` in ``Target Node Path`` field.

4. Attach a new scipt to ``Environment`` node and paste the following code:

    .. code-block:: gdscript

        extends RLEnvironment

        func _ready():
            world = $World
            agent = $Agent
            communication.start_server(9090, "127.0.0.1")

        func _reset():
            world.reset()
            agent.reset()

Let's examine what we added.

1. ``RLEnvironment`` class requires variables ``world`` and ``agent`` to be set.

    ..code-block:: gdscript

        func _ready():
            world = $World
            agent = $Agent

2. We start our TCP server (already defined in ``RLEnvironment`` class as ``communication``) at specific address and port:

    ..code-block:: gdscript
        
        communication.start_server(9090, "127.0.0.1")

3. ``RLEnvironment`` class required method ``reset`` do be implemented. 
In the method we define what should be done during environment reset:

    ..code-block:: gdscript
            
            func _reset():
                world.reset()
                agent.reset()

The reset logic can be more complex. E.g. our **World** can generate position to place the agent at in the begging of an episode:

    ..code-block:: gdscript
            
            func _reset():
                world.reset()
                agent.reset(world._sample_initial_position())

Thats's it for ``Environment``! Let's summarize:

1. ``RLEnvironment`` must have ``reset`` method implemented.
2. ``RLEnvironment`` must have ``agent`` and ``world`` properties defined.

That's it for Godot part!