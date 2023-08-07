extends Object
class_name PhysicsFramesTimer, "../icons/custom_node_icon.png"

signal timer_end

var _limit: int

var _counter: int = 0
var is_started: bool = false

func _init(limit: int = 4):
	_limit = limit

func step():
	if is_started:
		_counter += 1
		if _counter > _limit:
			_counter = 0
			is_started = false
			emit_signal("timer_end")
	
func start():
	_counter = 0	
	is_started = true
	return self
	
func set_limit(new_limit: int):
	_limit = new_limit
