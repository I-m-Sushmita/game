shader_type canvas_item;

uniform sampler2D reflection_tex : source_color;
uniform float reflection_strength : hint_range(0.0,1.0)=0.45;
uniform float ripple_strength : hint_range(0.0,0.03)=0.008;
uniform float ripple_speed=1.2;

void fragment(){
    vec4 base=texture(TEXTURE,UV);
    vec2 ruv=vec2(UV.x,1.0-UV.y);
    ruv.x += sin(UV.y*70.0 + TIME*ripple_speed)*ripple_strength;
    vec4 refl=texture(reflection_tex,ruv);
    COLOR=mix(base,refl,reflection_strength*refl.a);
}
