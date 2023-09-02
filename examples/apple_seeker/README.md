# Before launch
Copy-paste `./godot_addon/reinforcement_learning` directory to `examples/apple_seeker/godot/addons` directory and activate the addon in the project settings.

# Using protobuf
Protobuf support is made with [Godobuf](https://github.com/oniksan/godobuf) addon.

Data transfer message is described in `message.proto` file.

To obtain a protobuf message module for Python execute `protoc --python_out=./python ./message.proto` command and then rename `data_pb2.py` into `protobuf_message_module.py` in `python` directory.

To obtain a protobuf message module for Godot follow [guide from Godobuf repository](https://github.com/oniksan/godobuf#usage). Use `message.proto` as input protobuf file and `godot/protobuf_message.gd` as output GDScipt file.