#!/usr/bin/env python3
"""
EPD brand composite helper.

Use this AFTER generating a background image with an image model to composite
real, pixel-perfect brand assets on top: logos, motifs, credit-card mockups,
dashboard cards, etc.

Why: image models paraphrase visual references and cannot reproduce logos,
motifs, or UI elements exactly. The correct workflow is:

  1) Generate a background image with an image model, instructing it to leave
     specific regions EMPTY (top strip for logo, side edges for motif, a
     content well for dashboard mockup, etc.)
  2) Run this script to paste the real brand PNGs on top of those empty
     regions with pixel-perfect fidelity.

Usage examples:

  # Composite motif on both edges + logo top-center (default for square social)
  python composite.py \\
    --base /tmp/generated-square.png \\
    --motif side-both \\
    --logo top-center \\
    --out /tmp/final-square.png

  # Composite motif on right edge + logo top-left (wide banner)
  python composite.py --base bg.png --motif side-right --logo top-left \\
    --out banner.png

  # Composite motif + approved dashboard graphic
  python composite.py --base bg.png --motif side-left --logo top-center \\
    --graphic dashboard-card-donut-composite --graphic-pos center-right \\
    --out ad.png

Requires:  Pillow  (pip install pillow)
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS = REPO_ROOT / "assets"

MOTIFS = {
    "hero": ASSETS / "motif" / "motif-hero.png",
    "side-left": ASSETS / "motif" / "motif-side-left.png",
    "side-right": ASSETS / "motif" / "motif-side-right.png",
    "side-both": ASSETS / "motif" / "motif-side-both.png",
    "side-right-on-brand-blue": ASSETS / "motif" / "motif-side-right-on-brand-blue.png",
}

LOGOS = {
    "white": ASSETS / "logo" / "epd-logo-white.png",
    "dark": ASSETS / "logo" / "epd-logo-dark.png",
}

APPROVED_GRAPHICS = {
    "dashboard-card-donut-composite": ASSETS / "approved-graphics" / "dashboard-card-donut-composite.png",
    "credit-card-mockup": ASSETS / "approved-graphics" / "credit-card-mockup.png",
    "credit-card-wave": ASSETS / "approved-graphics" / "credit-card-wave.png",
    "metrics-card-revenue": ASSETS / "approved-graphics" / "metrics-card-revenue.png",
    "net-sales-breakdown": ASSETS / "approved-graphics" / "net-sales-breakdown.png",
    "retry-success": ASSETS / "approved-graphics" / "retry-success.png",
    "average-order-value": ASSETS / "approved-graphics" / "average-order-value.png",
    "top-failure-reasons": ASSETS / "approved-graphics" / "top-failure-reasons.png",
    "products-dashboard": ASSETS / "approved-graphics" / "products-dashboard.png",
    "partnership-blueprint": ASSETS / "approved-graphics" / "partnership-blueprint.png",
    "epd-commerce-hero": ASSETS / "approved-graphics" / "epd-commerce-hero.png",
}


def load_rgba(path: Path) -> Image.Image:
    if not path.exists():
        raise FileNotFoundError(f"Asset not found: {path}")
    return Image.open(path).convert("RGBA")


def composite_motif(base: Image.Image, motif_name: str) -> Image.Image:
    """Composite the chosen motif variant onto the base image, full canvas.

    The motif PNGs are baked at ~78% max alpha so they render correctly in any
    tool that reads them directly. No alpha boost is needed here.
    """
    if motif_name not in MOTIFS:
        raise ValueError(f"Unknown motif '{motif_name}'. Choices: {list(MOTIFS)}")
    motif = load_rgba(MOTIFS[motif_name])
    W, H = base.size
    # Scale motif to match base canvas while preserving aspect ratio (fit width)
    mw, mh = motif.size
    ratio = W / mw
    new_h = int(mh * ratio)
    motif_scaled = motif.resize((W, new_h))
    # Center vertically
    y_offset = (H - new_h) // 2
    base.alpha_composite(motif_scaled, (0, y_offset))
    return base


LOGO_POSITIONS = {
    "top-center":  lambda W, H, lw, lh: ((W - lw) // 2, int(H * 0.05)),
    "top-left":    lambda W, H, lw, lh: (int(W * 0.05), int(H * 0.05)),
    "top-right":   lambda W, H, lw, lh: (W - lw - int(W * 0.05), int(H * 0.05)),
    "bottom-center": lambda W, H, lw, lh: ((W - lw) // 2, H - lh - int(H * 0.05)),
    "bottom-left":   lambda W, H, lw, lh: (int(W * 0.05), H - lh - int(H * 0.05)),
    "bottom-right":  lambda W, H, lw, lh: (W - lw - int(W * 0.05), H - lh - int(H * 0.05)),
}


def composite_logo(base: Image.Image, logo_variant: str, position: str,
                   width_pct: float = 0.25) -> Image.Image:
    """Composite the EPD logo at the requested corner or center."""
    if logo_variant not in LOGOS:
        raise ValueError(f"Unknown logo '{logo_variant}'. Choices: {list(LOGOS)}")
    if position not in LOGO_POSITIONS:
        raise ValueError(f"Unknown position '{position}'. Choices: {list(LOGO_POSITIONS)}")
    logo = load_rgba(LOGOS[logo_variant])
    W, H = base.size
    target_w = int(W * width_pct)
    ratio = target_w / logo.size[0]
    logo_scaled = logo.resize((target_w, int(logo.size[1] * ratio)))
    x, y = LOGO_POSITIONS[position](W, H, logo_scaled.size[0], logo_scaled.size[1])
    base.alpha_composite(logo_scaled, (x, y))
    return base


GRAPHIC_POSITIONS = {
    "center":       lambda W, H, gw, gh: ((W - gw) // 2, (H - gh) // 2),
    "center-right": lambda W, H, gw, gh: (W - gw - int(W * 0.06), (H - gh) // 2),
    "center-left":  lambda W, H, gw, gh: (int(W * 0.06), (H - gh) // 2),
    "bottom-right": lambda W, H, gw, gh: (W - gw - int(W * 0.06), H - gh - int(H * 0.06)),
    "bottom-left":  lambda W, H, gw, gh: (int(W * 0.06), H - gh - int(H * 0.06)),
}


def composite_graphic(base: Image.Image, graphic_name: str, position: str,
                      width_pct: float = 0.42) -> Image.Image:
    """Composite one of the approved brand graphics onto the base."""
    if graphic_name not in APPROVED_GRAPHICS:
        raise ValueError(
            f"Unknown graphic '{graphic_name}'. Choices: {list(APPROVED_GRAPHICS)}"
        )
    if position not in GRAPHIC_POSITIONS:
        raise ValueError(
            f"Unknown position '{position}'. Choices: {list(GRAPHIC_POSITIONS)}"
        )
    graphic = load_rgba(APPROVED_GRAPHICS[graphic_name])
    W, H = base.size
    target_w = int(W * width_pct)
    ratio = target_w / graphic.size[0]
    graphic_scaled = graphic.resize((target_w, int(graphic.size[1] * ratio)))
    x, y = GRAPHIC_POSITIONS[position](W, H, graphic_scaled.size[0], graphic_scaled.size[1])
    base.alpha_composite(graphic_scaled, (x, y))
    return base


def main():
    p = argparse.ArgumentParser(
        description="Composite real EPD brand assets on top of a generated background."
    )
    p.add_argument("--base", required=True, help="Path to generated background PNG")
    p.add_argument("--out", required=True, help="Path to save final composite")
    p.add_argument("--motif", choices=list(MOTIFS.keys()),
                   help="Motif variant to composite (optional)")
    p.add_argument("--logo", choices=list(LOGO_POSITIONS.keys()),
                   help="Logo position (optional)")
    p.add_argument("--logo-variant", choices=list(LOGOS.keys()), default="white")
    p.add_argument("--logo-width-pct", type=float, default=0.25,
                   help="Logo width as fraction of canvas width (default 0.25)")
    p.add_argument("--graphic", choices=list(APPROVED_GRAPHICS.keys()),
                   help="Approved brand graphic to add (optional)")
    p.add_argument("--graphic-pos", choices=list(GRAPHIC_POSITIONS.keys()),
                   default="center-right")
    p.add_argument("--graphic-width-pct", type=float, default=0.42)
    args = p.parse_args()

    base = load_rgba(Path(args.base))

    if args.motif:
        base = composite_motif(base, args.motif)
    if args.graphic:
        base = composite_graphic(base, args.graphic, args.graphic_pos,
                                 args.graphic_width_pct)
    if args.logo:
        base = composite_logo(base, args.logo_variant, args.logo,
                              args.logo_width_pct)

    base.convert("RGB").save(args.out, optimize=True)
    print(f"Saved {args.out}")


if __name__ == "__main__":
    sys.exit(main())
