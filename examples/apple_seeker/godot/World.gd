extends RLEnvWorld

onready var apple = $Apple
onready var apple_caught: bool = false

func _ready():
	apple.get_node("AppleCatchArea").connect("body_entered", self, "_on_catch_apple")
	
func reset():
	apple_caught = false
	apple.set_global_translation(sample_initial_position())
	
func sample_initial_position() -> Vector3:
	var x = rand_range(-4, 4)
	var y = 0.55
	var z = rand_range(-4, 4)
	return Vector3(x, y, z)

func _on_catch_apple(_body):
	apple_caught = true

# The method does not depend on `observation_request` argument.
func get_data(observation_request, storage) -> void:
	storage.set_apple_caught(apple_caught)
