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
		connection.set_no_delay(true)
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

func put_message(message):
	var message_bytes = message.to_bytes()
	connection.put_32(message_bytes.size())  # Data lenght in bytes
	connection.put_data(message_bytes)

func close():
	have_connection = false
	connection.disconnect_from_host()
	emit_signal("closed_connection")
