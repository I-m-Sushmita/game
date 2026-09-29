# Godot 4 Import Guide

- Texture Filter: Nearest for pixel assets.
- Disable mipmaps for most character/foreground sprites.
- Use `TileMapLayer` for modular ground/building tiles.
- Use `Parallax2D` for `10_Parallax_Backgrounds`.
- Use `AnimatedSprite2D` for PNG strips in `07_Animated_Elements/game_ready_loops` and `08_VFX_Weather/game_ready_loops`.
- Each strip has a matching JSON file with frame size, count and FPS.
- Put glow PNGs from `09_Lighting/game_ready` into `PointLight2D` textures.
- Use wind shader only on foliage/cloth sprites, with the sprite pivot near the bottom.
- For wet-road reflection, render reflection source into a `SubViewportTexture` and bind it to `reflection_tex`.
