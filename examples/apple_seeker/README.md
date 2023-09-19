# Before launch
Copy-paste `./godot_addon` directory content to `examples/apple_seeker/godot/addons` directory and activate the addons in the project settings.

# Using protobuf
Data transfer message is described in `message.proto` file.

To obtain a protobuf message module for Python execute `protoc --python_out=./python ./message.proto` command and then rename `data_pb2.py` into `protobuf_message_module.py` in `python` directory.

To obtain a protobuf message module for Godot follow [Godobuf README](../../godobuf_readme/README.md#usage). Use `message.proto` as input protobuf file and `godot/protobuf_message.gd` as output GDScipt file.