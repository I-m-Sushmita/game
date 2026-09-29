shader_type canvas_item;

uniform float strength : hint_range(0.0, 0.08) = 0.025;
uniform float speed : hint_range(0.0, 6.0) = 2.0;
uniform float frequency : hint_range(0.0, 12.0) = 4.0;

void vertex(){
    float anchor = 1.0 - UV.y;
    VERTEX.x += sin(TIME * speed + UV.y * frequency) * strength * anchor * 100.0;
}
