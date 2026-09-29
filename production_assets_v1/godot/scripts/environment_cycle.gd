extends Node
class_name EnvironmentCycle

@export var minutes_per_real_second: float = 4.0
@export_range(0.0,24.0) var time_of_day: float = 6.0
var weather := "clear"
signal time_changed(hour: float)
signal weather_changed(name: String)

func _process(delta):
    time_of_day = fmod(time_of_day + delta * minutes_per_real_second / 60.0, 24.0)
    time_changed.emit(time_of_day)

func set_weather(next_weather: String):
    if next_weather == weather: return
    weather = next_weather
    weather_changed.emit(weather)
