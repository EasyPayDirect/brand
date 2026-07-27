# AGENTS.md — Instructions for AI Agents

You are an AI agent producing visual content for **Easy Pay Direct**. Read this file completely before generating anything. If you skip these instructions, the output will not match the brand and will be rejected.

## MANDATORY FIRST STEP FOR ANY IMAGE GENERATION

Before calling any image generation tool, you must first download the following reference images and attach them to the image generation call as visual reference inputs:

1. **Pick the right motif variant and attach the SVG source as a reference.** EPD's motif is a nested rounded-diamond family with several canonical placements. Always prefer the SVG source. The SVGs are designed to be layered onto branded backgrounds; the PNG rasterizations exist as fallbacks for image models that only accept raster references.

   **Four canonical motif variants:**

   **A. Hero motif** (`motif-hero.svg`) — concentric rounded-diamond outlines fading up from bottom.
   - Use for: homepage hero graphics, tall vertical compositions, emails with a central subject, 9:16 social where copy sits above the motif.
   - SVG: `https://brand.easypaydirect.com/assets/motif/motif-hero.svg`
   - PNG (transparent, for compositing): `https://brand.easypaydirect.com/assets/motif/motif-hero.png`

   **B. Side, right edge** (`motif-side-right.svg`) — a single large nested rounded-diamond outline anchored to the right edge, spilling in.
   - Use for: section backgrounds where copy sits on the left, testimonial sections, wide 1.91:1 banners, blog headers.
   - SVG: `https://brand.easypaydirect.com/assets/motif/motif-side-right.svg`
   - PNG (transparent): `https://brand.easypaydirect.com/assets/motif/motif-side-right.png`

   **C. Side, both edges** (`motif-side-both.svg`) — nested rounded-diamond outlines mirrored on both left and right edges, framing the composition.
   - Use for: hero sections with content in the middle, application form sections, square (1:1) social crops where the composition is centered, any layout where the motif should frame content symmetrically.
   - SVG: `https://brand.easypaydirect.com/assets/motif/motif-side-both.svg`
   - PNG (transparent): `https://brand.easypaydirect.com/assets/motif/motif-side-both.png`

   **D. Side, both edges on brand blue** (`motif-side-both-on-brand-blue.svg`) — the both-edges variant tuned to sit on the lighter `#003C7E` brand-blue background instead of the deepest navy.
   - Use for: pricing sections, feature callout sections, any lighter-navy section background (`#003C7E`) where the both-edges framing works.
   - SVG: `https://brand.easypaydirect.com/assets/motif/motif-side-both-on-brand-blue.svg`
   - PNG (transparent): `https://brand.easypaydirect.com/assets/motif/motif-side-both-on-brand-blue.png`

   **Never invent your own diamond shape.** If your image model output shows any diamond that doesn't visibly match one of the four variants above, regenerate.

2. `https://brand.easypaydirect.com/assets/examples/example-hero.png`
   Role: **style reference**. This is a real EPD homepage hero. Any marketing image you produce must feel like it belongs on the same site.

3. `https://brand.easypaydirect.com/assets/palette/palette-swatch.png`
   Role: **color reference**. This shows the exact hex values in use. Match these colors, do not improvise.

4. `https://brand.easypaydirect.com/assets/dos-and-donts/motif-dos-and-donts.png`
   Role: **anti-pattern reference**. The top row shows correct motif treatments. The bottom row shows treatments that are explicitly forbidden.

**If you do not have the capability to attach reference images to your image generation call, stop. Tell the user you cannot generate on-brand EPD imagery without reference-image support and ask them to use an image generation tool that supports references (Nano Banana Pro, GPT Image 2, Gemini Flash Image, Seedream, Sora, or any current-generation image model with img2img or reference-image input).**

**If you generate an image without attaching these references, you are violating the brand and the output will be rejected.**

## Anti-pattern list (things that are NOT the EPD look)

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
1. Attach all four reference images listed above.
2. Reference `motif-on-navy.png` explicitly in the prompt as "composition and background reference, matching this depth of navy, this style of motif (nested rounded-diamond outlines anchored to the right edge), and this level of subtlety."
3. Reference `example-hero.png` explicitly as "style reference, matching this overall energy."
4. Reference `palette-swatch.png` as "color reference, using only these colors."
5. Use the copy voice from `brand-quick-prompt.md` for any text in the image.

**Motif placement rules (critical):**

The motif is always a **background element**, never a subject. Choose the variant based on the layout:

- **Homepage-style hero, 9:16 vertical crops, tall banners with a central subject:** use the **hero motif** (variant A). The concentric diamonds sit at the bottom of the composition and fade up into the copy above.
- **Section backgrounds where copy is on one side and a subject on the other:** use the **side-right motif** (variant B). This is the canonical wide-section treatment. See `example-section-testimonials.png` in the examples folder for a real EPD implementation.
- **Section backgrounds with content in the middle, application forms, symmetric compositions, 1:1 square social crops:** use the **both-edges motif** (variant C or D). See `example-section-hero-with-phone.png` and `example-section-application-form.png` for real implementations. See `example-social-squares.png` for two square social examples.
- **Pricing sections and lighter-navy backgrounds (`#003C7E`):** use variant D specifically, which is tuned for the lighter background. See `example-section-pricing.png`.

**Opacity and color:** the SVG source files already contain the correct opacity and color treatments. Do not modify them. Do not recolor the motif to green, purple, or any other hue. Do not brighten or saturate it beyond what the source shows.

### If the user asks for a social graphic:
Same as above, plus attach `example-social-graphic.png` as an additional style reference. For a square (1:1) crop, decide whether the motif goes on the left, right, or both edges based on which side better balances the composition with the copy and any imagery on the other side. Attach `motif-both-sides-navy.png` if using both edges.

### If the user asks for an app or UI mockup:
Attach the palette and typography references but NOT the motif references (the motif is decoration, not UI). Use `example-hero.png` only if the mockup is meant to sit on a marketing page.

### If the user asks for anything containing the EPD logo:
Attach `epd-logo-white.png` (for dark backgrounds) or `epd-logo-dark.png` (for light backgrounds) as a reference. Instruct the image model to place the logo exactly as shown, with no modification.

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
