extends Spatial
class_name RLAgent, "icons/agent_node_icon.png"

# If one implements custom `_ready` method in his own subclass the method will be called nevertheless.
func _ready():
	set_pause_mode(Node.PAUSE_MODE_STOP)

func set_action(action):
	push_error("One should override the method in his own subclass.")
	
func reset(new_position):
	# One should override the method in his own subclass.
	pass

# Optional method to perform additional logic on configuration
func configure(agent_config: Dictionary):
	pass

func get_data(observation_request, storage) -> void:
	push_error("One should override the method in his own subclass.")
