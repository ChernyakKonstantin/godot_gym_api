extends Spatial

# How fast the agent moves in meters per second.
var speed = 5
# Current velocity of the agent.
var velocity: Vector3 = Vector3.ZERO

onready var body = $Body

func move_body():
	var direction = Vector3.ZERO
	
	if Input.is_action_pressed("ui_right"):
		direction.x -= 1
	elif Input.is_action_pressed("ui_left"):
		direction.x += 1
	elif Input.is_action_pressed("ui_up"):
		direction.z += 1
	elif Input.is_action_pressed("ui_down"):
		direction.z -= 1

	if direction != Vector3.ZERO:
		direction = direction.normalized()

	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	velocity = body.move_and_slide(velocity, Vector3.UP)

func _ready():
	body.set_axis_lock(PhysicsServer.BODY_AXIS_LINEAR_Y, true)

func _physics_process(delta):
	move_body()
