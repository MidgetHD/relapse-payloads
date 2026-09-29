"""Render PNG buttons for the added payload tiles (requires Pillow)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ui"
BUTTONS = {
    "kstuff": ("Kstuff", "Load first", "kstuff.elf"),
    "shadow": ("ShadowMountPlus", "Load after Kstuff", "shadowmountplus.elf"),
    "etahen": ("etaHEN", "Load after Kstuff and ShadowMountPlus", "etaHEN.elf"),
}
STATES = {
    "default": ((33, 34, 38), None),
    "sending": ((43, 35, 17), (229, 181, 44)),
    "sent": ((19, 40, 27), (74, 211, 126)),
    "failed": ((50, 24, 27), (241, 93, 105)),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    windows = Path("C:/Windows/Fonts")
    filename = "arialbd.ttf" if bold else "arial.ttf"
    candidates = [windows / filename, Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    raise FileNotFoundError("No suitable TrueType font found")


def centered(draw: ImageDraw.ImageDraw, y: int, value: str, fill, face) -> None:
    box = draw.textbbox((0, 0), value, font=face)
    draw.text(((626 - (box[2] - box[0])) / 2, y), value, fill=fill, font=face)


for key, (title, subtitle, filename) in BUTTONS.items():
    for state, (background, border) in STATES.items():
        im = Image.new("RGBA", (626, 104), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        draw.rounded_rectangle((0, 0, 625, 103), radius=17, fill=background,
                               outline=border, width=3 if border else 1)
        centered(draw, 13, title, (245, 245, 246), font(25, bold=True))
        centered(draw, 47, subtitle, (207, 207, 211), font(18))
        centered(draw, 76, filename, (155, 155, 160), font(15))
        im.save(OUT / f"btn-{key}-{state}.png", optimize=True)
