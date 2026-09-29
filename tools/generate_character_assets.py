from PIL import Image, ImageDraw
import json, os

ROOT = os.path.dirname(os.path.dirname(__file__))
MANIFEST = os.path.join(ROOT, 'characters', 'character_manifest.json')
OUT = os.path.join(ROOT, 'generated_characters')
W, H = 32, 48


def rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def draw_character(ch, frame=0, anim='walk'):
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    skin = rgb(ch['skin'])
    hair = rgb(ch['hair'])
    top = rgb(ch['top'])
    under = rgb(ch['undershirt'])
    pants = rgb(ch['pants'])
    shoes = rgb(ch['shoes'])
    accent = rgb(ch['accent'])

    if anim == 'walk':
        phase = [0, 1, 1, 0, 0, -1, -1, 0][frame % 8]
        leg_a = [0, 1, 2, 1, 0, -1, -2, -1][frame % 8]
    else:
        phase = [0, 0, 1, 0][frame % 4]
        leg_a = 0
    leg_b = -leg_a
    arm = [-1, 0, 1, 1, 0, -1, -1, 0][frame % 8] if anim == 'walk' else 0
    y = phase

    d.ellipse((8, 43, 24, 46), fill=(0, 0, 0, 55))

    acc = ch.get('accessory', 'none')
    if acc in ('backpack', 'delivery_bag', 'satchel'):
        d.rectangle((7, 20+y, 11, 31+y), fill=accent + (255,))
        d.rectangle((6, 22+y, 8, 29+y), fill=tuple(max(0, c-25) for c in accent) + (255,))

    d.rectangle((12 + leg_a//2, 31+y, 15 + leg_a//2, 40+y), fill=pants + (255,))
    d.rectangle((17 + leg_b//2, 31+y, 20 + leg_b//2, 40+y), fill=pants + (255,))
    d.rectangle((11 + leg_a, 40+y, 15 + leg_a, 43+y), fill=shoes + (255,))
    d.rectangle((17 + leg_b, 40+y, 21 + leg_b, 43+y), fill=shoes + (255,))

    d.rectangle((10, 18+y, 21, 31+y), fill=top + (255,))
    d.rectangle((14, 18+y, 18, 25+y), fill=under + (255,))
    d.rectangle((14, 15+y, 18, 19+y), fill=skin + (255,))

    d.rectangle((8+arm, 20+y, 11+arm, 31+y), fill=top + (255,))
    d.rectangle((21-arm, 20+y, 24-arm, 31+y), fill=top + (255,))
    d.rectangle((8+arm, 29+y, 11+arm, 33+y), fill=skin + (255,))
    d.rectangle((21-arm, 29+y, 24-arm, 33+y), fill=skin + (255,))

    d.rectangle((11, 7+y, 21, 16+y), fill=skin + (255,))
    d.rectangle((21, 10+y, 23, 13+y), fill=skin + (255,))

    if ch['sex'] == 'female':
        d.rectangle((10, 5+y, 21, 9+y), fill=hair + (255,))
        d.rectangle((9, 7+y, 12, 20+y), fill=hair + (255,))
        d.rectangle((19, 6+y, 22, 20+y), fill=hair + (255,))
        d.rectangle((8, 16+y, 11, 25+y), fill=hair + (255,))
    else:
        d.rectangle((10, 5+y, 21, 9+y), fill=hair + (255,))
        d.rectangle((9, 7+y, 12, 12+y), fill=hair + (255,))
        d.polygon([(11, 5+y), (13, 2+y), (14, 6+y)], fill=hair + (255,))
        d.polygon([(15, 5+y), (17, 2+y), (18, 6+y)], fill=hair + (255,))
        d.polygon([(19, 5+y), (21, 3+y), (22, 7+y)], fill=hair + (255,))

    d.point((20, 11+y), fill=(20, 16, 16, 255))

    if acc == 'glasses':
        d.rectangle((18, 10+y, 22, 12+y), outline=(35, 30, 28, 255))
    elif acc == 'cap':
        d.rectangle((9, 5+y, 21, 7+y), fill=accent + (255,))
        d.rectangle((19, 7+y, 24, 8+y), fill=accent + (255,))
    elif acc == 'phone':
        d.rectangle((23-arm, 30+y, 25-arm, 34+y), fill=(24, 27, 31, 255))
    elif acc == 'camera':
        d.rectangle((19, 25+y, 24, 29+y), fill=(28, 30, 32, 255))
    elif acc == 'tool':
        d.line((23-arm, 30+y, 26-arm, 36+y), fill=(120, 125, 126, 255), width=1)
    elif acc == 'id_card':
        d.rectangle((16, 23+y, 18, 26+y), fill=(215, 225, 232, 255))
    elif acc == 'stethoscope':
        d.arc((12, 20+y, 19, 28+y), 0, 180, fill=(70, 75, 80, 255), width=1)
    elif acc == 'dupatta':
        d.line((11, 20+y, 9, 34+y), fill=accent + (255,), width=2)
        d.line((20, 20+y, 23, 34+y), fill=accent + (255,), width=2)
    elif acc == 'chain':
        d.line((15, 20+y, 19, 24+y), fill=(190, 176, 132, 255), width=1)
    elif acc == 'watch':
        d.point((23-arm, 29+y), fill=(210, 185, 95, 255))

    return img


def make_sheet(ch, frames, anim, filename):
    sheet = Image.new('RGBA', (W * frames, H), (0, 0, 0, 0))
    for i in range(frames):
        sheet.alpha_composite(draw_character(ch, i, anim), (i * W, 0))
    sheet.save(filename)


def main():
    with open(MANIFEST, 'r', encoding='utf-8') as f:
        data = json.load(f)

    os.makedirs(OUT, exist_ok=True)
    for ch in data['characters']:
        folder = os.path.join(OUT, ch['id'])
        os.makedirs(folder, exist_ok=True)

        make_sheet(ch, 8, 'walk', os.path.join(folder, ch['id'] + '_walk.png'))
        make_sheet(ch, 4, 'idle', os.path.join(folder, ch['id'] + '_idle.png'))
        draw_character(ch, 0, 'idle').resize((128, 192), Image.Resampling.NEAREST).save(
            os.path.join(folder, ch['id'] + '_preview.png')
        )

        with open(os.path.join(folder, 'character.json'), 'w', encoding='utf-8') as f:
            json.dump(ch, f, indent=2)

    print(f'Generated {len(data["characters"])} characters in {OUT}')


if __name__ == '__main__':
    main()
