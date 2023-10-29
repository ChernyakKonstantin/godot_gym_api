extends Spatial

onready var apple = $Apple
onready var spawn_areas = $SpawnAreas

func _ready():
	apple.get_node("AppleCatchArea").connect("body_entered", self, "_on_catch_apple")

func reset():
	apple.set_global_translation(_sample_initial_position())

func _on_catch_apple(_body):
	reset()

func _sample_initial_position() -> Vector3:
	var i = randi() % spawn_areas.get_children().size()
	return spawn_areas.get_child(i).get_global_translation()
