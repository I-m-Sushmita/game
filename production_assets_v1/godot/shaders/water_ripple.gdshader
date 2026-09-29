shader_type canvas_item;
uniform float amplitude=0.008;
uniform float speed=1.5;
uniform float frequency=55.0;
void fragment(){
 vec2 uv=UV; uv.x += sin(UV.y*frequency + TIME*speed)*amplitude;
 uv.y += cos(UV.x*(frequency*0.5)+TIME*speed*0.7)*amplitude*0.35;
 COLOR=texture(TEXTURE,uv);
}
