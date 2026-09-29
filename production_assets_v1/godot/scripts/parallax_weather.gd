extends Parallax2D
class_name ParallaxWeather
@export var base_scroll := Vector2(4.0,0.0)
@export var wind_multiplier := 1.0
func _process(delta):
    scroll_offset += base_scroll * wind_multiplier * delta
