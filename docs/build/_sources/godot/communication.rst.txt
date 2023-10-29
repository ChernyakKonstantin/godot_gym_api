Communication
=============

**Inherits:** `Object <https://docs.godotengine.org/en/3.5/classes/class_object.html#class-object>`_

Networking class.

Description
-----------

This class provides communication with clients via TCP protocol.

.. note::
    This class is not expected to be changed by user.

Signals
-------

.. attribute:: (signal) got_connection

    The signal is emitted when incomming request is got in ``server_poll`` method.

Method Descriptions
-------------------

.. function:: (void) start_server(port: int, address: String)

    Start `TCPServer <https://docs.godotengine.org/en/3.5/classes/class_tcp_server.html>`_.

    Args:
        port: TCP port to communicate with client.
        address: IP-address to communicate with client.


.. function:: (void) server_poll()

    Method to establish a connection to a client and to read incomming request from the client. 

    The methods emits `got_connection` signal with request dictionary if a request is got. 
    The signal is used in ``RLEnvironment`` class.

.. function:: (Dictionary) _read_request()

    Method to read incomming request.

    Request data consists of two parts: 
    1. Request message size in 4 bytes (int32).
    2. Bytes with serialized JSON string of a request dictionary.

.. function:: (void) put_message(message)

    Method to serialize Protobuf message and put it in TCP stream.
    
    Args:
        message: Protobuf message with responed data.
