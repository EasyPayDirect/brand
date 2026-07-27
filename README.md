# Easy Pay Direct Brand Assets

This repository is the single source of truth for the Easy Pay Direct visual brand system. It exists so that any human or AI agent producing visual content for the EPD brand can pull the exact same reference assets from a stable public URL.

If you are an **AI assistant** asked to produce visual content for Easy Pay Direct, read [`AGENTS.md`](./AGENTS.md) first. It tells you exactly which files to attach to your image-generation call before you generate anything.

If you are a **human designer, affiliate partner, or vendor**, you can use everything in this repo directly. Assets are free to use in any EPD-affiliated marketing, ads, or content, as long as they are used according to the placement and treatment rules in the brand guidelines PDF.

## What's here

```
epd-brand/
├─ AGENTS.md                    # Rules for AI agents (read this first)
├─ brand-quick-prompt.md        # Copy-pasteable brand system prompt (~500 tokens)
├─ HOW-TO-PUBLISH.md            # For the EPD team: publishing and updating this repo
├─ docs/
│  └─ easy-pay-direct-brand-guidelines.pdf   # Full brand guide (for humans)
├─ .well-known/
│  └─ brand-assets.json         # Machine-readable manifest of every asset
└─ assets/
   ├─ motif/                    # Diamond motif (hero family + side family), on navy, light, and transparent
   ├─ logo/                     # EPD logo lockups (white, dark, SVG + PNG)
   ├─ palette/                  # Labeled color palette as a single image
   ├─ typography/               # Font pairing specimen
   ├─ examples/                 # Real EPD hero + social graphics as style references
   └─ dos-and-donts/            # Motif do / do not visual sheets for both families
```

## Canonical asset URLs

If this repo lives at `brand.easypaydirect.com`, the canonical URLs are:

**Motif family: hero** (concentric rounded diamonds fading up from bottom)

| Asset | URL |
|---|---|
| Hero motif on navy | `https://brand.easypaydirect.com/assets/motif/motif-hero-on-navy.png` |
| Hero motif on light | `https://brand.easypaydirect.com/assets/motif/motif-hero-on-light.png` |
| Hero motif tile (transparent) | `https://brand.easypaydirect.com/assets/motif/motif-hero-tile.png` |
| Hero motif SVG | `https://brand.easypaydirect.com/assets/motif/motif-hero.svg` |

**Motif family: side** (nested outlines anchored to an edge)

| Asset | URL |
|---|---|
| Side motif on navy, right edge (canonical) | `https://brand.easypaydirect.com/assets/motif/motif-side-on-navy.png` |
| Side motif on navy, left edge (mirrored) | `https://brand.easypaydirect.com/assets/motif/motif-side-on-navy-left.png` |
| Side motif on navy, both edges (for 1:1 social) | `https://brand.easypaydirect.com/assets/motif/motif-side-both-navy.png` |
| Side motif on light | `https://brand.easypaydirect.com/assets/motif/motif-side-on-light.png` |
| Side motif tile (transparent) | `https://brand.easypaydirect.com/assets/motif/motif-side-tile.png` |
| Side motif SVG, right | `https://brand.easypaydirect.com/assets/motif/motif-side-right.svg` |
| Side motif SVG, left | `https://brand.easypaydirect.com/assets/motif/motif-side-left.svg` |

**Logos, palette, typography, examples**

| Asset | URL |
|---|---|
| EPD logo (white, for dark backgrounds) | `https://brand.easypaydirect.com/assets/logo/epd-logo-white.png` |
| EPD logo (navy, for light backgrounds) | `https://brand.easypaydirect.com/assets/logo/epd-logo-dark.png` |
| Color palette (labeled swatch image) | `https://brand.easypaydirect.com/assets/palette/palette-swatch.png` |
| Typography specimen | `https://brand.easypaydirect.com/assets/typography/typography-specimen.png` |
| Example hero (positive style reference) | `https://brand.easypaydirect.com/assets/examples/example-hero.png` |
| Example social graphic, wide banner | `https://brand.easypaydirect.com/assets/examples/example-social-graphic.png` |
| Example social graphic, 1:1 square | `https://brand.easypaydirect.com/assets/examples/example-social-square.png` |
| Motif do / do not sheet, hero family | `https://brand.easypaydirect.com/assets/dos-and-donts/motif-dos-and-donts-hero-family.png` |
| Motif do / do not sheet, side family | `https://brand.easypaydirect.com/assets/dos-and-donts/motif-dos-and-donts-side-family.png` |
| **Full brand guidelines PDF (for humans)** | `https://brand.easypaydirect.com/docs/easy-pay-direct-brand-guidelines.pdf` |
| Machine manifest | `https://brand.easypaydirect.com/.well-known/brand-assets.json` |

## Full brand guidelines

The full written brand system (color rules, type scale, layout, voice, copy) is in [`docs/easy-pay-direct-brand-guidelines.pdf`](./docs/easy-pay-direct-brand-guidelines.pdf). Anyone can read it directly from the repo.

Agents: the PDF is a secondary reference. It is a human document translated into words. It cannot replace attaching the actual PNG references (motif, palette, example hero) to your image generation call. See `AGENTS.md` for the exact reference-attachment workflow.

## Contact

For asset requests, corrections, or questions, contact `directorofmarketing@easypaydirect.com`.

## License

These assets are copyright Easy Pay Direct. Free for use in EPD-affiliated marketing, ads, and content. Not licensed for use by unaffiliated parties.
