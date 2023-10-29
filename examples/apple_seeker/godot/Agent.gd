extends RLAgent

export var target_node_path: NodePath

# How fast the agent moves in meters per second.
var speed = 5
# Current velocity of the agent.
var velocity: Vector3 = Vector3.ZERO

var current_action: int = -1

onready var body = $Body
onready var sensors = $Body/Sensors

func get_data(_observation_request, storage) -> void:
	var data = sensors.get_data()
	for distance in data["distances_to_obstacle"]:
		storage.add_distances_to_obstacle(float(distance))
	for distance in data["distances_to_target"]:
		storage.add_distances_to_target(float(distance))
	
func set_action(action):
	current_action = action
	
func reset(arguments=null):
	velocity = Vector3.ZERO
	current_action = -1
	body.set_global_translation(Vector3(0, 0, 2))

func move_body():
	var direction = Vector3.ZERO
	
	if current_action == 0:  # MOVE_RIGHT
		direction.x -= 1  
	elif current_action == 1:  # MOVE_LEFT
		direction.x += 1
	elif current_action == 2:  # MOVE_UP
		direction.z += 1
	elif current_action == 3:  # MOVE_DOWN
		direction.z -= 1

	if direction != Vector3.ZERO:
		direction = direction.normalized()

	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	velocity = body.move_and_slide(velocity, Vector3.UP)

func _ready():
	body.set_axis_lock(PhysicsServer.BODY_AXIS_LINEAR_Y, true)
	sensors.target = get_node(target_node_path)

func _physics_process(delta):
	move_body()
