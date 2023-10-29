PhysicsFramesTimer
==================

**Inherits:** `Object <https://docs.godotengine.org/en/3.5/classes/class_object.html#class-object>`_

Timer in terms of physics frames.

Description
-----------

This class is used to pause ``RLEnvironment`` after ``n_repeat`` physics step to emulate real-time Godot-Python interaction.

.. note::
    This class is not expected to be changed by user.

Signals
-------

.. attribute:: signal timer_end

    The signal is emitted in ``step`` method when passed number of physics frames exceeds ``_limit`` .

Property Descriptions
---------------------

.. attribute:: (int) _limit

    Number of physics steps to wait before ``timer_end`` signal is emitted.


Method Descriptions
-------------------

.. function:: (void) _init(limit: int = 4)

    Start `TCPServer <https://docs.godotengine.org/en/3.5/classes/class_tcp_server.html>`_.

    Args:
        limit:  Number of physics steps to wait before ``timer_end`` signal is emitted.


.. function:: (void) step()

    Increment counter. The method is called inside ``RLEnvironment._physics_process`` method.

.. function:: (PhysicsFramesTimer) start()

    Start timer. The method is called inside ``RLEnvironment._step`` method.


.. function:: (void) set_limit(new_limit: int)

    Assign new ``_limit`` value.

    Args:
        new_limit: New ``limit_`` value.
