extends Spatial
class_name RLAgent, "icons/agent_node_icon.png"

func set_action(action):
	push_error("One should override the method in his own subclass.")
	
func reset(new_position):
	# One should override the method in his own subclass.
	pass

# Optional method to perform additional logic on configuration
func configure(agent_config: Dictionary):
	pass

func get_data(observation_request):
	push_error("One should override the method in his own subclass.")
