extends Object
class_name Communication, "../icons/custom_node_icon.png"

signal got_connection

var thread

var server = TCP_Server.new()
var connection: StreamPeerTCP = null
var message_processing: bool = false

func start_server(port: int, address: String):
	# Listen for incoming connections
	server.listen(port, address)
	print("Listen on address: ", address, ", port: ", port)

func server_poll():
	if connection == null and server.is_connection_available():
		connection = server.take_connection()
		connection.set_no_delay(true)
		print("\nConnection is taken.\n")
		
	if connection != null and not message_processing:
		if connection.get_status() == StreamPeerTCP.STATUS_CONNECTED:
			var request = _read_request()
			message_processing = true
			emit_signal("got_connection", request)
		else:
			print("\nConnection is lost!\n")
			connection.disconnect_from_host()
			connection = null
		
func _read_request() -> Dictionary:
	var request_package_size = connection.get_32()
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
	message_processing = false
	
