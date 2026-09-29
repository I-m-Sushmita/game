shader_type canvas_item;
uniform float speed=10.0;
uniform float minimum=0.35;
void fragment(){
 float f=max(minimum,0.68+0.32*sin(TIME*speed)+0.12*sin(TIME*speed*3.7));
 vec4 c=texture(TEXTURE,UV); COLOR=vec4(c.rgb*f,c.a);
}
