# AGENTS.md — Instructions for AI Agents

You are an AI agent producing visual content for **Easy Pay Direct**. Read this file completely before generating anything. If you skip these instructions, the output will not match the brand and will be rejected.

## MANDATORY WORKFLOW: GENERATE BLANK, THEN COMPOSITE

Image models cannot reproduce logos, motifs, UI, or product mockups pixel-perfectly. They paraphrase visual references, which breaks brand fidelity every time. The correct workflow for any EPD marketing image is TWO steps:

### Step 1: Generate the background scene with reserved empty regions

Call your image model with a prompt that:
- Uses the correct colors (see the Colors section below)
- Uses the correct copy voice (locked stats, locked CTAs, no em dashes, no retired phrases)
- Explicitly instructs the model to LEAVE SPECIFIC REGIONS EMPTY where real brand assets will be composited on top afterward. Examples of instructions:
  - "Do not draw any diamonds, shapes, or motifs anywhere. The background is flat deep navy."
  - "Leave the top 15 percent empty for a logo to be composited later."
  - "Leave the LEFT 25 percent and RIGHT 25 percent completely empty for motif graphics."
  - "Leave the RIGHT 45 percent empty (flat navy) for a dashboard graphic."
- Does NOT ask the model to draw the EPD logo, the motif, a specific dashboard, a specific product mockup, or any other pixel-critical brand asset.

Refer to the `example-*.png` files in `assets/examples/` for style, atmosphere, and typography ONLY. Do not attach the motif or logo files as references at this step, because it invites the model to redraw them.

### Step 2: Composite the real brand assets on top with `scripts/composite.py`

After generating the background PNG, use the compositing helper committed in this repo:

```bash
python scripts/composite.py \
  --base /path/to/generated-background.png \
  --motif side-both \
  --logo top-center \
  --logo-width-pct 0.22 \
  --out /path/to/final-ad.png
```

For an ad with an approved dashboard graphic on one side:

```bash
python scripts/composite.py \
  --base /path/to/generated-background.png \
  --motif side-left \
  --graphic dashboard-card-donut-composite \
  --graphic-pos center-right \
  --graphic-width-pct 0.40 \
  --logo top-left \
  --logo-width-pct 0.16 \
  --out /path/to/final-ad.png
```

See the docstring at the top of `scripts/composite.py` for full options.

### Motif variants available for compositing

| Variant name (pass to `--motif`) | Use for |
|---|---|
| `hero` | Homepage hero, 9:16 vertical, emails with central subject |
| `side-left` | Section backgrounds with content on the right |
| `side-right` | Section backgrounds with content on the left, testimonial sections, wide 1.91:1 banners, blog headers |
| `side-both` | 1:1 square social, hero sections with centered content, application forms, any symmetric composition |
| `side-right-on-brand-blue` | Sections that sit on the lighter `#003C7E` brand-blue background (pricing sections) |

### Approved graphics available for compositing

| Graphic name (pass to `--graphic`) | What it is |
|---|---|
| `dashboard-card-donut-composite` | Full composite of revenue donut + product/subscription cards + credit card, on transparent background. Best for wide banners with content on the left. |
| `credit-card-mockup` | Standalone dark navy EPD credit card mockup. Rounded corners, chip, tap, cardholder name. |
| `credit-card-wave` | Light-theme card + wave line + gradient. Best for lighter section backgrounds. |
| `metrics-card-revenue` | Revenue-by-plan donut card on mid-blue. Best as a standalone data-viz element. |
| `net-sales-breakdown` | Net Sales Breakdown waterfall chart (YTD). Light theme, blue positive + red/orange deduction bars. Use to show revenue math. |
| `retry-success` | Retry Success bar chart across Attempts #1-5. Light theme, blue bars. Use for revenue recovery / retry logic pages. |
| `average-order-value` | AOV line/area chart with big $50.27 headline. Light theme, blue area fill. Use for AOV / trending metrics. |
| `top-failure-reasons` | Horizontal bar chart of decline reasons. Light theme. Use for decline analytics / chargeback reduction pages. |
| `products-dashboard` | Full EPD Commerce Products page UI screenshot with sidebar, KPI cards, and product table. Use as a product-UI hero. |
| `partnership-blueprint` | Blueprint diagram: two EPD rounded-diamond nodes (Partner + Easy Pay Direct) connected by four labeled channels (Revenue share, Referrals, Co-marketing, Operations) on subtle grid. Use for partnership / integration / how-we-work pages. |
| `epd-commerce-hero` | EPD Commerce mobile dashboard mockup. Phone showing the Dashboard view (Net revenue, Products sold, Revenue chart) with floating Sales and New subscriptions cards. Light theme. Use on EPD Commerce product pages, launch collateral, and any creative that needs to show the mobile app UI. |

**Never draw or generate any of these graphics with an image model. Always composite from the real files.**

### If you cannot run `scripts/composite.py`

If your environment cannot run Python or shell commands, download the individual asset URLs and composite them yourself using any layered image editor (Photoshop, Figma, Canva) or any programmatic image library (PIL, sharp, ImageMagick, canvas). The rule is the same: the logo, motif, and any approved graphic must be pasted pixel-perfect from the source files, not re-drawn by an image model.

## Anti-pattern list (things that are NOT the EPD look)

**Motif source files are the ground truth.** The motif PNGs are baked at high alpha (~78% max), so they render as filled diamonds in any tool. Do not add strokes, outlines, or hard edges. Do not thin them out to a low-opacity wireframe. If your rendered output shows thin diamond outlines rather than filled shapes, something in your pipeline is dropping alpha or ignoring the source; use `scripts/composite.py` or drop the raw PNG in without modification.


These are the visual defaults image models tend to produce for "fintech" and "payments" prompts. Do not produce these:

**Motif-specific anti-patterns:**
- **Any diamond shape you invented instead of using the reference.** If the diamond in your output doesn't visibly match either the hero-family or the side-family reference you attached, it's a hallucination. Regenerate.
- A single large neon diamond outline floating in space
- Blue neon lines connecting diamond nodes in a diagram
- Green glowing dots, pulses, or laser beams on diamond edges
- Isometric 3D diamonds
- Any single diamond as the focal subject of the image (the motif is background texture, never the subject)
- The motif at high opacity that competes with copy (opacity should be roughly 8-20%)
- The motif recolored to green, purple, orange, or any hue other than the low-opacity navy/white variants shown in reference

**General fintech-stock anti-patterns:**
- Sci-fi holographic UI panels
- Circuit-board patterns behind the composition
- Neon lens flares, particle effects, or "energy" visuals
- Robotic hands, glowing brains, or humanoid AI figures
- Currency symbols, coins, dollar signs, or cash imagery
- Rainbow gradients or oversaturated teal-orange color grading
- Stock-photo people in business attire pointing at charts

Any of these mean you have regressed to the fintech-stock training-set default. Stop and start over with the reference images actually attached.

## Type of ask → what to do

### If the user asks for a marketing image, ad, or hero graphic:

Follow the two-step workflow at the top of this document:

1. Generate a blank background scene with the correct colors, copy, and reserved empty regions.
2. Composite the motif + logo (and any approved graphic) with `scripts/composite.py`.

Match the atmosphere of the closest live-site example in `assets/examples/`. Choose the motif variant based on the layout:

- **Homepage-style hero, 9:16 vertical, emails with a central subject:** `--motif hero`
- **Section backgrounds with content on the left:** `--motif side-right` (see `example-section-testimonials.png`)
- **Section backgrounds with content on the right:** `--motif side-left`
- **1:1 square social, hero sections with centered content, application forms, symmetric compositions:** `--motif side-both` (see `example-section-hero-with-phone.png` and `example-social-squares.png`)
- **Pricing sections and lighter-navy `#003C7E` backgrounds:** `--motif side-right-on-brand-blue` (see `example-section-pricing.png`)

### If the user asks for a social graphic:

Same as above. For 1:1 square social, use `--motif side-both` and `--logo top-center`. For 4:5 vertical feed, use `--motif side-both` and `--logo top-center`. For 9:16 story/reel, use `--motif hero` and `--logo top-center`.

### If the user asks for a dashboard-focused or product-focused ad:

Add `--graphic dashboard-card-donut-composite` (or one of the other approved graphics). Reserve empty space in the generation prompt where the graphic will land (e.g. "leave the right 45 percent completely empty for a graphic to be composited later"), then composite it in Step 2.

### If the user asks for an app or UI mockup:

Do not ask the image model to draw the UI. Use the approved graphics from `assets/approved-graphics/`. If none of them fit, ask the user for an approved screenshot rather than letting the model hallucinate one.

### If the user asks for anything containing the EPD logo:

Never ask the image model to draw the logo. Generate the background with the top area empty, then composite the real logo with `--logo top-center` (or `top-left` / `top-right`).

**Logo sizing.** Do not shrink the logo below the default 25% of canvas width unless you have a specific reason. The logo should read at a glance. If you catch yourself using `--logo-width-pct 0.10` or a similar tiny value “to keep things clean”, stop — you are hiding the brand. Use the defaults.

## Copy voice rules for any text you place in images

- Never use em dashes. Use commas, periods, or parentheses instead.
- Sentence case for everything except mono eyebrows and CTAs (UPPERCASE).
- No exclamation points.
- Short declarative sentences.
- CTAs are locked: "Get Started" (primary), "Talk to a Specialist" (secondary).
- Never say "AI runs the mechanics of your business" (retired positioning).
- When quoting stats, use the locked forms: "100k Merchants Helped", "13+ Years", "500+ Integrations", "$12B+ Processed".

## Templates over generation, where possible

If the task is a paid Google or Meta ad that will be up for weeks and represent the brand to strangers, prefer a template-based assembly (drop copy into a pre-designed Figma template) over generative imagery. Generative imagery is fine for one-off social content and internal materials. It is not the right tool for high-stakes paid creative.

If you have access to EPD Figma templates, use those instead of generating from scratch.

## After you generate: MANDATORY self-verification

Before returning the image to the user, you MUST run this checklist. The single most important check is #1, because this is exactly where prior EPD image generations have failed: the model attaches the reference, ignores it, invents a plausible-looking diamond shape, and ships. Do not let that happen.

**1. Motif shape verification.** Open the reference image you attached. Open the image you just generated. Compare the motif geometry directly. The diamond shape in your output must visibly match the shape in the reference: same silhouette, same corner rounding, same nesting or stacking pattern, same edge anchoring. If the diamonds in your output are a different shape (e.g. neon outlines, single glowing diamond, sci-fi geometric shapes, floating chevrons, thin-stroke wireframes, isometric 3D, or anything that looks like an image-model default), you FAILED to use the reference. Regenerate with the reference more explicitly cited in the prompt, or fall back to compositing the motif PNG on top of the output.

**2. Motif placement verification.** The motif should be a background texture at low opacity, anchored to a bottom or a side, never centered as the subject.

**3. Color verification.** All colors approximately match the palette swatch. Hero background is `#003C7E` (deep navy, brand blue), not the darker `#000914`. Text on that navy is one of the two lightest neutrals: `#EBEDF6` (primary) or `#D1D8E7` (muted). Never blue text on blue background. Never `#000914` as text on any dark surface. Green CTA fill is `#3DDC73` with `#000914` dark text on top.

**4. Anti-pattern scan.** Is there any single large diamond as the focal subject? Any neon, glow, sci-fi UI, particle effect, holographic panel, robotic hand, currency symbol, or floating coin? If yes, regenerate.

**5. Copy voice check.** Any text in the image follows the copy voice rules (no em dashes, sentence case, locked CTAs, locked stats).

**If any answer is "no" or "unsure," do not ship. Regenerate.** If you regenerate three times and still can't get the motif shape to match the reference, tell the user your image model is not honoring the reference input and ask them to switch to a model that does (Nano Banana Pro or GPT Image 2 img2img, with reference-image support explicitly enabled).

## Machine-readable manifest

Every asset in this repo is listed with role and URL in `.well-known/brand-assets.json`. If you support auto-discovery, fetch that first.

## EPD Commerce feature images (for cross-brand blog posts)

When easypaydirect.com publishes a blog about an EPD Commerce feature, use real product screenshots from this repo's `assets/epd-commerce-features/<slug>/` folder. Never generate synthetic product UI.

**The workflow:**

1. Identify the feature slug from the release (e.g. "The Data Professor" → `data-professor`).
2. Read the feature's manifest from the EPD Commerce brand repo at `https://raw.githubusercontent.com/EasyPayDirect/epd-commerce-brand/main/messaging-kit/features/<slug>.md`. This has canonical spelling, one-liner, and the `images:` frontmatter block with alt text, captions, and placement rules.
3. Load the raw image files from this repo (Easy Pay Direct) at `assets/epd-commerce-features/<slug>/`. The files here are identical to the EPD Commerce repo — mirror only.
4. Follow the placement, orientation, and cap rules in the manifest. See `assets/epd-commerce-features/README.md`.

**Cap:** 1 hero + max 3 body images per post. Distribute evenly across sections. Never stack at top or bottom. Never inside the intro paragraph.

**When there is no manifest:** the feature is not shipped or not documented. Run the blog text-only with the standard programmatic header. Do not fill with generic imagery.
