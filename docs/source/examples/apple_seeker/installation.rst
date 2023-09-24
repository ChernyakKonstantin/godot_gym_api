Installation
============

1. Install ``protobuf`` into your OS following 
`Protocol Buffers repository <https://github.com/protocolbuffers/protobuf/releases>`_.

2. To install Python package, run the following command from your terminal 
(it is strongly recomended to use a python virtual environment):

.. code-block:: bash

   pip3 install git+https://github.com/ChernyakKonstantin/godot_gym_api.git

3. Create a project in Godot. For this tutorial, the project name is *AppleSeeker*.

4. To install Godot addons to your project, run the following command from your terminal:

.. code-block:: bash

   godot_gym_api install_addon <PATH_TO_YOUR_GODOT_PROJECT>

5. Enable the ``Reinforcement Learning`` and ``Godobuf`` plugins in Godot through ``Project/Project Settings/Plugins`` tab.
