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

**Motif: four canonical variants** (SVG source is always preferred; PNGs are transparent-background fallbacks)

| Variant | Use for | SVG | PNG |
|---|---|---|---|
| **A. Hero** — concentric diamonds fading up from bottom | Homepage hero, tall vertical, 9:16 social | `motif/motif-hero.svg` | `motif/motif-hero.png` |
| **B. Side, right edge** — single outline spilling in from right | Testimonial sections, wide 1.91:1 banners, blog headers | `motif/motif-side-right.svg` | `motif/motif-side-right.png` |
| **C. Side, both edges** — mirrored, framing centered content | Hero sections with centered content, application forms, 1:1 social | `motif/motif-side-both.svg` | `motif/motif-side-both.png` |
| **D. Side, both edges on brand blue** — variant C tuned for #003C7E | Pricing sections, feature callouts on lighter navy | `motif/motif-side-both-on-brand-blue.svg` | `motif/motif-side-both-on-brand-blue.png` |

Full URLs prefix each with `https://brand.easypaydirect.com/assets/`. See real site sections using each variant in `assets/examples/`.

**Logos, palette, typography, examples**

| Asset | URL |
|---|---|
| EPD logo (white, for dark backgrounds) | `https://brand.easypaydirect.com/assets/logo/epd-logo-white.png` |
| EPD logo (navy, for light backgrounds) | `https://brand.easypaydirect.com/assets/logo/epd-logo-dark.png` |
| Color palette (labeled swatch image) | `https://brand.easypaydirect.com/assets/palette/palette-swatch.png` |
| Typography specimen | `https://brand.easypaydirect.com/assets/typography/typography-specimen.png` |
| Example hero (positive style reference) | `https://brand.easypaydirect.com/assets/examples/example-hero.png` |
| Real site section: hero with phone | `https://brand.easypaydirect.com/assets/examples/example-section-hero-with-phone.png` |
| Real site section: testimonials | `https://brand.easypaydirect.com/assets/examples/example-section-testimonials.png` |
| Real site section: pricing (on brand blue) | `https://brand.easypaydirect.com/assets/examples/example-section-pricing.png` |
| Real site section: application form | `https://brand.easypaydirect.com/assets/examples/example-section-application-form.png` |
| Example social graphic, wide banner | `https://brand.easypaydirect.com/assets/examples/example-social-graphic.png` |
| Example social graphics, two 1:1 squares | `https://brand.easypaydirect.com/assets/examples/example-social-squares.png` |
| Example social graphic, 1:1 finished ad | `https://brand.easypaydirect.com/assets/examples/example-social-square.png` |
| Motif do / do not sheet | `https://brand.easypaydirect.com/assets/dos-and-donts/motif-dos-and-donts.png` |
| **Full brand guidelines PDF (for humans)** | `https://brand.easypaydirect.com/docs/easy-pay-direct-brand-guidelines.pdf` |
| Machine manifest | `https://brand.easypaydirect.com/.well-known/brand-assets.json` |

## Full brand guidelines

The full written brand system (color rules, type scale, layout, voice, copy) is in [`docs/easy-pay-direct-brand-guidelines.pdf`](./docs/easy-pay-direct-brand-guidelines.pdf). Anyone can read it directly from the repo.

Agents: the PDF is a secondary reference. It is a human document translated into words. It cannot replace attaching the actual PNG references (motif, palette, example hero) to your image generation call. See `AGENTS.md` for the exact reference-attachment workflow.

## Contact

For asset requests, corrections, or questions, contact `directorofmarketing@easypaydirect.com`.

## License

These assets are copyright Easy Pay Direct. Free for use in EPD-affiliated marketing, ads, and content. Not licensed for use by unaffiliated parties.
