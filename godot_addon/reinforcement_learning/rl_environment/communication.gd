extends Object
class_name Communication, "../icons/custom_node_icon.png"

signal got_connection
signal closed_connection

var thread

var server = TCP_Server.new()
var connection: StreamPeerTCP
var have_connection: bool = false

func start_server(port: int, address: String):
	# Listen for incoming connections
	server.listen(port, address)
	print("Listen on address: ", address, ", port: ", port)

func server_poll():
	if not have_connection and server.is_connection_available():
		connection = server.take_connection()
		var request = _read_request()
		if request != null and not request.empty():
			have_connection = true
			emit_signal("got_connection", request)

func _read_request() -> Dictionary:
	var request_package_size = connection.get_available_bytes()
	var request_data = connection.get_utf8_string(request_package_size)
	if len(request_data) == 0:
		return {}
	var request = JSON.parse(request_data)
	if request.error == OK:
		return request.result
	else:
		return {}

func put_json(value):
	# value can be Array or Dictionary
	var value_: PoolByteArray = JSON.print(value).to_utf8() # Encode to bytes
	connection.put_32(value_.size())  # Data lenght in bytes
	connection.put_data(value_)

#func put_images(value: Dictionary):
#	connection.put_32(DataType.IMAGES)  # Data type
#	connection.put_32(value.size())  # Number of keys
#	for key in value.keys():
#		connection.put_string(key)  # Image name
#		connection.put_32(value[key].size())  # Number of images
#		for image in value[key]:
#			image.convert(Image.FORMAT_RGB8)
#			var image_data = image.get_data()
#			connection.put_32(image_data.size()) # Image length in bytes
#			connection.put_data(image_data)

func close():
	have_connection = false
	connection.disconnect_from_host()
	emit_signal("closed_connection")
