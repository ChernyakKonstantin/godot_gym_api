extends Spatial

# The maximum distance of the agent sensors.
const max_sensor_distance = 5
# Target node
var target

func get_data() -> Dictionary:
	var distances_to_obstacle = []
	var distances_to_target = []
	for ray in get_children():
		var distance: float = max_sensor_distance
		var distance_to_target: float = max_sensor_distance
		if ray.is_colliding():
			distance = ray.global_translation.distance_to(ray.get_collision_point())
			if ray.get_collider() == target:
				distance_to_target = distance
		distances_to_obstacle.append(distance)
		distances_to_target.append(distance_to_target)
	var data = {
		"distances_to_obstacle": distances_to_obstacle, 
		"distances_to_target": distances_to_target
		}
	return data
