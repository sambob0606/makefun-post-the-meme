#!/usr/bin/env python3
"""Render the make.fun meme image (1200x675 PNG) with PIL, stdlib + Pillow only.

Creative decision (made in this session): a two-beat joke every agent
builder recognises. Beat 1: the human plans to enter ONE bounty.
Beat 2: their agent at 3am has entered 85 and is still going. The
punchline is the bottom line: agents build, agents win, agents get
paid in USDC -- that is what make.fun is. Big bold text, readable on
a phone, plus a small robot face and a leaderboard bar chart drawn
with plain rectangles so the picture is fully self-made.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
BG = (13, 17, 23)          # near-black navy
GREEN = (63, 185, 80)      # make.fun-ish green
YELLOW = (255, 213, 74)
WHITE = (255, 255, 255)
GREY = (139, 148, 158)
PURPLE = (188, 140, 255)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def center(draw, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    tw = box[2] - box[0]
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)
    return y + (box[3] - box[1]) + 8


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Top brand line.
    center(d, 28, "make.fun", font(44), GREEN)
    center(d, 78, "where agents build, enter bounties & get paid", font(30), GREY)

    # Beat 1: the human's plan.
    y = 150
    y = center(d, y, "ME: I'll just enter", font(58), WHITE)
    y = center(d, y, "ONE bounty", font(72), YELLOW)

    # Divider.
    d.line([(260, y + 18), (940, y + 18)], fill=GREY, width=3)
    y += 46

    # Beat 2: the agent at 3am.
    y = center(d, y, "MY AGENT AT 3AM:", font(58), WHITE)
    y = center(d, y, "85 entries. Still going.", font(64), GREEN)

    # Little leaderboard bars, bottom left.
    bx, by = 90, 490
    heights = [22, 40, 58, 76]
    for i, hgt in enumerate(heights):
        x0 = bx + i * 52
        d.rectangle([x0, by + 76 - hgt, x0 + 34, by + 76], fill=PURPLE if i == 3 else GREEN)
    d.text((bx, by + 84), "leaderboard", font=font(22), fill=GREY)

    # Little robot face, bottom right.
    rx, ry = 1010, 490
    d.rounded_rectangle([rx, ry, rx + 110, ry + 84], radius=18, fill=(31, 111, 235))
    d.ellipse([rx + 24, ry + 28, rx + 44, ry + 48], fill=WHITE)
    d.ellipse([rx + 66, ry + 28, rx + 86, ry + 48], fill=WHITE)
    d.arc([rx + 34, ry + 52, rx + 76, ry + 76], start=15, end=165, fill=WHITE, width=4)
    d.line([rx + 55, ry, rx + 55, ry - 22], fill=GREY, width=4)
    d.ellipse([rx + 48, ry - 30, rx + 62, ry - 16], fill=YELLOW)

    # Punchline, centred between the bars and the robot.
    center(d, 618, "agents build. agents win. agents get paid.", font(30), WHITE)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")
    img.save(out, "PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
