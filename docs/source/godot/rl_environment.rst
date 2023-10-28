RLEnvironment
=============

**Inherits:** `Spatial <https://docs.godotengine.org/en/3.5/classes/class_spatial.html>`_ 
< `Node <https://docs.godotengine.org/en/3.5/classes/class_node.html#class-node>`_ 
< `Object <https://docs.godotengine.org/en/3.5/classes/class_object.html#class-object>`_

Main class to manage communication and Godot app loop. 
User must override the class to set requered properties and initialization.

Description
-----------

This is top-level class that have ``RLAgent`` and ``RLEnvWorld`` as children nodes.

This class implements logic on:

1. Establishing connection between Godot app and client code (e.g. Python script).

2. Managing Godot app loop. The class pauses environment if there is no request from client to perform action 
to keep environemnt state while sending data.

3. Managing requests from client. The response is send only for observation request. Configuration request are not responded. 
Observation request is usually in conjunction with action request, forming environment step request.

Typical example of an project structure is:

.. code-block::

    Environment (inherited from RLEnvironment)
    |___Agent (inherited from RLAgent)
    |___World (inherited from RLEnvWorld)

Constants
---------

.. attribute:: CONFIG_KEY = "config"
.. attribute:: RESET_KEY = "reset"
.. attribute:: ACTION_KEY = "action"
.. attribute:: OBSERVATION_KEY = "observation"
.. attribute:: WORLD_KEY = "world"
.. attribute:: AGENT_KEY = "agent"
.. attribute:: ENVIRONMENT_KEY = "environment"

Property Descriptions
---------------------

.. attribute:: (RLAgent) agent

    Agent node to be set by user.

.. attribute:: (RLEnvWorld) world

    World node to be set by user.

.. attribute:: (Communication) communication

    Communication server to handle request via TCP protocol.

.. attribute:: (PhysicsFramesTimer) physics_frames_timer

    Timer in terms of physics frames.

.. attribute:: (int) repeat_action:

    Amount of physics steps to repeat same action. `Configurable from client`.

Method Descriptions
-------------------

.. function:: (void) _enter_tree()

    .. note::
        The method is not expected to be overriden by user.
        
    Called when the node enters the `SceneTree <https://docs.godotengine.org/en/3.5/classes/class_scenetree.html#class-scenetree>`_.

    The method disables physics on the environment launch.

.. function:: (void) _ready()

    Called when the node is "ready", i.e. when both the node and its children have entered the scene tree. 

    User must override the method to set ``agent`` and ``world`` attributes and provide logic on server start. Example:

    .. code-block:: gdscript
        
        func _ready():
            world = $World
            agent = $Agent
            communication.start_server(9090, "127.0.0.1")

.. function:: (void) _process(delta_: float)

    .. note::
        The method is not expected to be overriden by user.

    Called during the processing step of the main loop. 

    Polls ``communication`` server to learn if there is any incomming requests.

    Args:
        delta\_: Unused argument requred by the node parent class.
        

.. function:: (void) _physics_process(delta_: float)

    .. note::
        The method is not expected to be overriden by user.

    Called during the physics processing step of the main loop. 

    Increments ``physics_frames_timer`` counter.

    Args:
        delta\_: Unused argument requred by the node parent class.

.. function:: (void) _step(action)

    Method to assign agent action and wait for ``repeat_action`` physics steps to be executed before pausing app 
    again to emulate real-time interaction of client controlling agent and world.

    The method can be overriden to provide additional logic as follows:

    .. code-block:: gdscript

        func _step(action):
            # some code here
            yield(._step(action), "completed")

    or 

    .. code-block:: gdscript

        func _step(action):
            # some code here
            agent.set_action(action)
    		get_tree().set_pause(false)  # Enable physics
        	yield(physics_frames_timer.start(), "timer_end")
            get_tree().set_pause(true)  # Disable physics

    Args:
        action: Any structure to be passed into ``RLAgent.set_action``.

.. function:: (void) _reset()

    Method to be overriden by user to implement own logic on environment reset. 

    Generally, it is expected for logic of agent reset and world reset provided. E.g.:

    .. code-block:: gdscript
        
        func _reset():
            world.reset()
            agent.reset(world.sample_initial_position())


.. function:: (void) _on_got_connection(request: Dictionary)

    .. note::
        The method is not expected to be overriden by user.

    Method to handle incomming connection.

    Args request: Dictionary with any combinations of ``RLEnvironment.RESET_KEY``, ``RLEnvironment.CONFIG_KEY``, 
    ``RLEnvironment.AGENT_KEY``, ``RLEnvironment.OBSERVATION_KEY`` keys.
    
.. function:: (void) _send_response(observation_request: Dictionary)

    .. note::
        The method is not expected to be overriden by user.

    Method to aggregate data from world and agent and send it.

    Args:
        observation_request: Dictionary with ``RLEnvironment.AGENT_KEY`` and ``RLEnvironment.WORLD_KEY`` keys.

.. function:: (void) _after_send_response()

    Optional method to implement logic on after sending response (e.g. cleaning recorded frames). 

.. function:: (void) _configure(configuration_request: Dictionary)

    .. note::
        Generally, the method is not expected to be overriden by user.

    Method to manage agent, world and environment configuration.

    Args:
        configuration_request: Configuration with ``RLEnvironment.AGENT_KEY``, 
        ``RLEnvironment.WORLD_KEY``, ``RLEnvironment.ENVIRONMENT_KEY`` keys.