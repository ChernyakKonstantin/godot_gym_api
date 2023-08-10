# LIDAR orientation is along X-axis.
#tool
extends Spatial

# TODO: make lower/upper bound configurable
export var horizontal_resolution: float = 1 # Degrees
export var vertical_resolution: float = 1 # Degrees
export var horizontal_fov: float = 120 # Degrees
export var vertical_fov: float = 30 # Degrees
export var ray_max_len: float = 1000 # Meters
export var return_distances: bool = true

#func _debug_draw_lidar_range():
#	var visual = ImmediateGeometry.new()
#	visual.begin(Mesh.PRIMITIVE_TRIANGLES)
#	visual.add_vertex(Vector3(0,0,0))
#	visual.add_vertex(Vector3(0,1,1))
#	visual.add_vertex(Vector3(0,-1,1))
#	visual.end()
#	var material = SpatialMaterial.new()
#	material.albedo_color = Color(0.0, 0.0, 1.0) # Blue color
#	visual.set_material_override(material)
#	add_child(visual)
	
#
#func _enter_tree():
#	if Engine.is_editor_hint():
#		_debug_draw_lidar_range()

func _ready():
	_create()

func _create() -> void:
	var start_h: float = -horizontal_fov / 2
	var start_v: float = -vertical_fov / 2
	var n_vertical_points = int(vertical_fov / vertical_resolution)
	var n_horizontal_points = int(horizontal_fov / horizontal_resolution)

#	assert(fmod(vertical_fov, vertical_resolution) == 0, str(vertical_fov / vertical_resolution))
#	assert(fmod(horizontal_fov, horizontal_resolution) == 0, str(horizontal_fov / horizontal_resolution))
	for j in range(n_vertical_points):
		for i in range(n_horizontal_points):
			var ray = RayCast.new()
			ray.set_visible(true)
			ray.set_enabled(true)
			ray.set_exclude_parent_body(true)
			ray.set_collide_with_bodies(true)
			ray.set_collide_with_areas(false)
			ray.set_cast_to(Vector3(0, 0, ray_max_len))
			var rotation = Vector3(
				start_v + j * vertical_resolution,
				start_h + i * horizontal_resolution,
				0
			)
			ray.set_rotation_degrees(rotation)
			add_child(ray)

func get_data() -> Array:
	var data = []
	for ray in get_children():
		if return_distances:
			var rotation: Vector3 = ray.get_rotation_degrees()
			var distance: float = ray_max_len
			if ray.is_colliding():
				distance = ray.global_translation.distance_to(ray.get_collision_point())
			data.append([float(rotation.y), float(rotation.x), float(distance)])
		else:
			var colision_point_coordinates = Dictionary()
			if ray.is_colliding():
				var colision_point: Vector3 = ray.get_collision_point() - ray.global_translation
				colision_point_coordinates["x"] = colision_point.x
				colision_point_coordinates["y"] = colision_point.y
				colision_point_coordinates["z"] = colision_point.z
			data.append(colision_point_coordinates)
	return data

func configure(lidar_config: Dictionary):
	var recreate: bool = false
	if "horizontal_resolution" in lidar_config.keys():
		horizontal_resolution = lidar_config["horizontal_resolution"]
		recreate = true
	if "vertical_resolution" in lidar_config.keys():
		vertical_resolution = lidar_config["vertical_resolution"]
		recreate = true
	if "horizontal_fov" in lidar_config.keys():
		horizontal_fov = lidar_config["horizontal_fov"]
		recreate = true
	if "vertical_fov" in lidar_config.keys():
		vertical_fov = lidar_config["vertical_fov"]
		recreate = true
	if "ray_max_len" in lidar_config.keys():
		ray_max_len = lidar_config["ray_max_len"]
	if "return_distances" in lidar_config.keys():
		return_distances = lidar_config["return_distances"]
		
	if recreate:
		_delete_rays()
		_create()
	
func _delete_rays():
	for ray in get_children():
		remove_child(ray)
		ray.queue_free()
