extends Spatial

export var viewport_size: Vector2 = Vector2(360, 240)

onready var camera_handle: RemoteTransform = $CameraHandle
onready var viewport: Viewport = $Viewport
onready var viewport_texture: ViewportTexture = viewport.get_texture()

# -------- built-ins --------
func _ready():
	viewport.set_vflip(true)
	viewport.set_size(viewport_size)
	viewport.set_update_mode(Viewport.UPDATE_ALWAYS)

# -------- getters --------
func get_data() -> Image:
	var data = viewport_texture.get_data()
	data.convert(Image.FORMAT_RGB8)
	return data
	
