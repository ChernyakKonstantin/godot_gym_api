extends Spatial
class_name RLEnvWorld, "icons/world_node_icon.png"

# Optional method to implement the world reset.
func reset():
	pass

# Optional method to perform additional logic on configuration
func configure(agent_config: Dictionary):
	pass

func get_data(observation_request):
	push_error("One should override the method in his own subclass.")

