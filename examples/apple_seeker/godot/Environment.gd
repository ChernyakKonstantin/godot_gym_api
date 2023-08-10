extends RLEnvironment

func _ready():
	world = $World
	agent = $Agent
	communication.start_server(9090, "127.0.0.1")

func _reset():
	world.reset()
	agent.reset(world.sample_initial_position())
