#!/usr/bin/env python3
"""Draw the 'Hormuz Shock' news image (1024x1024) entirely in code.

Scene: an oil tanker crossing a narrow strait at dusk, an explosion
fireball behind it, smoke, and a price chart spiking to $95.82.
All shapes are drawn with Pillow primitives; no copied assets.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
random.seed(1311)

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_REG, size)


img = Image.new("RGB", (W, H), (18, 20, 34))
d = ImageDraw.Draw(img, "RGBA")

# ---- sky: dusk gradient ----
for y in range(0, 620):
    t = y / 620
    r = int(18 + (150 - 18) * t)
    g = int(20 + (60 - 20) * t)
    b = int(34 + (40 - 34) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# sun glow low on the horizon
for r in range(220, 0, -6):
    a = max(0, 26 - r // 12)
    d.ellipse([512 - r, 540 - r, 512 + r, 540 + r], fill=(255, 140, 40, a))

# ---- distant rocky cliffs framing the strait ----
d.polygon([(0, 620), (0, 300), (120, 380), (210, 470), (260, 620)],
          fill=(38, 34, 48))
d.polygon([(1024, 620), (1024, 330), (900, 400), (820, 480), (770, 620)],
          fill=(32, 30, 44))
# cliff highlights
d.polygon([(0, 300), (120, 380), (90, 430), (0, 400)], fill=(58, 52, 68))
d.polygon([(1024, 330), (900, 400), (930, 450), (1024, 420)], fill=(52, 46, 62))

# ---- explosion fireball behind the tanker (right of centre) ----
cx, cy = 700, 470
for r, col in [(150, (255, 90, 20)), (120, (255, 140, 30)),
               (88, (255, 190, 60)), (55, (255, 235, 150))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
# flame tongues
for ang in range(0, 360, 24):
    a = math.radians(ang)
    L = 150 + random.randint(0, 70)
    x2 = cx + int(math.cos(a) * L)
    y2 = cy + int(math.sin(a) * L * 0.8) - 40
    d.polygon([(cx, cy), (x2 - 14, y2), (x2 + 14, y2)],
              fill=(255, random.choice([110, 150, 180]), 40))

# ---- smoke plume ----
for i in range(26):
    sx = cx - 90 + i * 9 + random.randint(-14, 14)
    sy = cy - 150 - i * 9 + random.randint(-10, 10)
    sr = 26 + i * 2
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(60, 58, 62, 150))
for i in range(14):
    sx = cx - 60 + i * 12 + random.randint(-10, 10)
    sy = cy - 170 - i * 8 + random.randint(-8, 8)
    sr = 18 + i
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(110, 105, 108, 130))

# ---- sea ----
for y in range(620, H):
    t = (y - 620) / (H - 620)
    r = int(14 + (8 - 14) * t)
    g = int(38 + (16 - 38) * t)
    b = int(64 + (30 - 64) * t)
    d.line([(0, y), (W, y)], fill=(r, g, b))
# waves / reflections
for i in range(90):
    x = random.randint(0, W)
    y = random.randint(640, 1000)
    ln = random.randint(20, 90)
    d.line([(x, y), (x + ln, y)], fill=(90, 150, 180, 120), width=2)
# fire reflection on the water
for i in range(40):
    x = cx + random.randint(-110, 110)
    y = random.randint(640, 900)
    ln = random.randint(30, 120)
    d.line([(x, y), (x + ln, y)], fill=(255, 150, 50, 140), width=3)

# ---- oil tanker (left-centre, crossing the strait) ----
# hull
d.polygon([(180, 600), (640, 600), (680, 640), (660, 690),
           (200, 690), (160, 640)], fill=(120, 30, 28))
d.rectangle([180, 600, 660, 612], fill=(200, 60, 40))
d.rectangle([180, 678, 660, 690], fill=(30, 30, 34))
# deck / cargo tanks
for i, x in enumerate([230, 330, 430, 530]):
    d.rectangle([x, 540, x + 80, 600], fill=(215, 205, 190))
    d.ellipse([x, 528, x + 80, 556], fill=(240, 232, 218))
    d.line([(x + 40, 528), (x + 40, 512)], fill=(160, 150, 140), width=4)
# bridge tower
d.rectangle([600, 480, 660, 600], fill=(235, 235, 228))
d.rectangle([600, 480, 660, 500], fill=(40, 60, 90))
for wx in (608, 628, 648):
    d.rectangle([wx, 516, wx + 12, 536], fill=(30, 50, 80))
d.rectangle([596, 500, 664, 508], fill=(200, 60, 40))
# funnel
d.polygon([(610, 480), (650, 480), (646, 440), (614, 440)], fill=(40, 40, 46))
d.rectangle([610, 452, 650, 462], fill=(255, 180, 40))
# bow wake removed (arcs read as scribble)

# ---- chart panel (bottom) ----
d.rounded_rectangle([48, 736, 976, 992], radius=18,
                    fill=(10, 12, 22, 235), outline=(255, 180, 60), width=3)
d.text((80, 760), "BRENT CRUDE  •  13 NOVEMBER 2026",
       font=font(30), fill=(255, 200, 90))
d.text((80, 800), "$95.82", font=font(84), fill=(255, 255, 255))
d.text((80, 902), "+3.3%", font=font(44), fill=(80, 220, 120))
d.text((250, 914), "after tanker blasts", font=font(28, bold=False),
       fill=(200, 205, 215))

# chart (right side of the panel): axes + spiking line
ox, oy, cw, ch = 560, 950, 384, 150
d.line([(ox, oy), (ox + cw, oy)], fill=(120, 130, 150), width=2)
pts = []
n = 12
for i in range(n):
    x = ox + i * cw / (n - 1)
    if i < 7:
        y = oy - 8 - i * 3
    else:
        y = oy - 8 - 18 - (i - 6) * 22
    pts.append((x, y))
# area under the line
d.polygon(pts + [(ox + cw, oy), (ox, oy)], fill=(255, 150, 40, 70))
d.line(pts, fill=(255, 170, 50), width=5, joint="curve")
# spike marker (price already shown large at left, so no label here)
d.ellipse([pts[-1][0] - 8, pts[-1][1] - 8, pts[-1][0] + 8, pts[-1][1] + 8],
          fill=(255, 80, 40), outline=(255, 255, 255), width=2)

# ---- headline banner (top) ----
d.rectangle([0, 0, W, 118], fill=(12, 10, 14, 235))
d.rectangle([0, 118, W, 126], fill=(255, 60, 40))
d.text((48, 30), "HORMUZ SHOCK", font=font(60), fill=(255, 255, 255))
d.text((740, 40), "STRAIT OF HORMUZ", font=font(24), fill=(255, 120, 80))
d.text((740, 74), "tankers hit by blasts", font=font(22, bold=False),
       fill=(210, 210, 215))

img.save("entry.png", optimize=True)
print("saved entry.png")
