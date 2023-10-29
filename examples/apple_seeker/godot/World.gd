extends RLEnvWorld

onready var apple = $Apple
onready var spawn_areas = $SpawnAreas
onready var apple_caught: bool = false

func _ready():
	apple.get_node("AppleCatchArea").connect("body_entered", self, "_on_catch_apple")

func reset(arguments=null):
	apple_caught = false
	apple.set_global_translation(_sample_initial_position())

func _on_catch_apple(_body):
	apple_caught = true

func _sample_initial_position() -> Vector3:
	var i = randi() % spawn_areas.get_children().size()
	return spawn_areas.get_child(i).get_global_translation()

# The method does not depend on `observation_request` argument in this example.
func get_data(observation_request, storage) -> void:
	storage.set_apple_caught(apple_caught)
