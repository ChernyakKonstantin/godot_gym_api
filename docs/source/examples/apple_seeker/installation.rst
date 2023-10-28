Installation
============

1. Install ``protobuf`` into your OS following 
`Protocol Buffers repository <https://github.com/protocolbuffers/protobuf/releases>`_ if you do not have one.

2. Create and activate a virtual environment *(recomended)*.

3. Install Python package with the following command from your terminal:

.. code-block:: bash

   pip3 install git+https://github.com/ChernyakKonstantin/godot_gym_api.git

3. Install Godot addons to your project with the following command from your terminal:

.. code-block:: bash

   godot_gym_api install_addon <YOUR_PATH>/apple_seeker/godot

4. Enable the ``Reinforcement Learning`` and ``Godobuf`` plugins in Godot through ``Project/Project Settings/Plugins`` tab.
