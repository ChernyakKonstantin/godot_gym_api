extends RLAgent

const MOVE_RIGHT = 0
const MOVE_LEFT = 1
const MOVE_UP = 2
const MOVE_DOWN = 3

export var target_node_path: NodePath

var target

# The maximum distance of the agent sensors.
var max_sensor_distance = 5
# How fast the agent moves in meters per second.
var speed = 14
# Current velocity of the agent.
var velocity: Vector3 = Vector3.ZERO
# Current action the agent performs.
var current_action: int = -1

onready var body = $Body
onready var sensors = $Sensors

func _ready():
	target = get_node(target_node_path)
	print(target)
	body.set_axis_lock(PhysicsServer.BODY_AXIS_LINEAR_Y, true)
	
func reset(new_position):
	velocity = Vector3.ZERO
	current_action = -1
	body.set_global_translation(new_position)

# The method does not depend on `observation_request` argument.
func get_data(observation_request, storage) -> void:
	var distances_to_obstacle = []
	var distances_to_target = []
	for ray in sensors.get_children():
		var distance: float = max_sensor_distance
		var distance_to_target: float = max_sensor_distance
		if ray.is_colliding():
			distance = ray.global_translation.distance_to(ray.get_collision_point())
			if ray.get_collider() == target:
				distance_to_target = distance
		storage.add_distances_to_obstacle(float(distance))
		storage.add_distances_to_target(float(distance_to_target))
	
func set_action(action):
	current_action = action

func _physics_process(delta):
	move_body(delta)

# The definition of `Body._physics_process` method to avoid extra scripts for salke of simplicity.
func move_body(delta):
	var direction = Vector3.ZERO
	
	if current_action == MOVE_RIGHT:
		direction.x -= 1
	elif current_action == MOVE_LEFT:
		direction.x += 1
	elif current_action == MOVE_UP:
		direction.z += 1
	elif current_action == MOVE_DOWN:
		direction.z -= 1

	if direction != Vector3.ZERO:
		direction = direction.normalized()
		body.look_at(body.translation + direction, Vector3.UP)

	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	velocity = body.move_and_slide(velocity, Vector3.UP)

