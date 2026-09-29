extends AnimatedSprite2D
class_name AnimatedEnvironment

@export var random_start := true
@export var speed_variation := 0.15
func _ready():
    if random_start and sprite_frames and sprite_frames.get_frame_count(animation)>0:
        frame = randi() % sprite_frames.get_frame_count(animation)
    speed_scale = randf_range(1.0-speed_variation,1.0+speed_variation)
    play()
