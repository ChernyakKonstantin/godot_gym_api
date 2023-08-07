extends Spatial
class_name RLEnvironment, "../icons/env_node_icon.png"

const STATUS_KEY = "status"
const CONFIG_KEY = "config"
const RESET_KEY = "reset"
const ACTION_KEY = "action"
const OBSERVATION_KEY = "observation"

# Amount of physics steps to repeat same action.
onready var repeat_action: int = 4  # TODO: make configurable

# Timer in terms of physics frames.
onready var physics_frames_timer = PhysicsFramesTimer.new(repeat_action)

# Communication server to handle request via TCP protocol.
onready var communication = Communication.new()

func _ready():
	get_tree().set_pause(true)
	set_pause_mode(2)
	communication.connect("got_connection", self, "_on_got_connection")

func _process(delta):
	communication.server_poll()

func _physics_process(delta):
	physics_frames_timer.step()

# One can extend the method to perform additional logic before or after or override it.
# Generally, the method enables physics processing to emulate real-time interaction.  
# Example:
# ```
#	func _step(action):
#		agent.set_action(action)
#		yield(._step(action), "completed")
# ```
# or
# ```
# 	func _step(action):
# 		agent.set_action(action)
# 		get_tree().set_pause(false)  # Enable physics	
# 		yield(physics_frames_timer.start(), "timer_end")
# 		get_tree().set_pause(true)  # Disable physics	
# ```
func _step(action):
	get_tree().set_pause(false)  # Enable physics
	physics_frames_timer.start()
	yield(physics_frames_timer, "timer_end")
	get_tree().set_pause(true)  # Disable physics
	
# One should override the method in his own subclass.
# Generally, the method should reset a world and an agent.
func _reset():
	push_error("One should override the method in his own subclass.")

# Handle incoming connection
func _on_got_connection(request: Dictionary):
	if request.has(RESET_KEY):
		_reset()
	elif request.has(ACTION_KEY):
		yield(_step(request[ACTION_KEY]), "completed")
	elif request.has(CONFIG_KEY):
		_configure(request[CONFIG_KEY])
	elif request.has(STATUS_KEY):
		pass
	if request.has(OBSERVATION_KEY):
		_send_response(request[OBSERVATION_KEY])
		_after_send_response()
	communication.close()

# One should override the method in his own subclass.
# Generally, the method should send state with help of `communication` object.
func _send_response(observation_request: Array):
	push_error("One should override the method in his own subclass.")

# Optional method to perform additional logic after response is sent.
func _after_send_response():
	pass

# Optional method to perform additional logic on configuration
func _configure(configuration_request: Dictionary):
	pass
