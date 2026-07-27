# AGENTS.md — Instructions for AI Agents

You are an AI agent producing visual content for **Easy Pay Direct**. Read this file completely before generating anything. If you skip these instructions, the output will not match the brand and will be rejected.

## MANDATORY FIRST STEP FOR ANY IMAGE GENERATION

Before calling any image generation tool, you must first download the following reference images and attach them to the image generation call as visual reference inputs:

1. **Pick the right motif family and attach it as a reference.** EPD has TWO valid motif families, both canonical. Attach the URL for the family that matches the layout:

   **Hero family** (`motif-hero-*`): concentric rounded-diamond outlines fading up from the bottom. Use for hero graphics, vertical compositions, emails with a central subject, and 9:16 social where the copy sits above the motif.

   - Navy: `https://brand.easypaydirect.com/assets/motif/motif-hero-on-navy.png`
   - Light: `https://brand.easypaydirect.com/assets/motif/motif-hero-on-light.png`
   - Transparent tile: `https://brand.easypaydirect.com/assets/motif/motif-hero-tile.png`
   - SVG source: `https://brand.easypaydirect.com/assets/motif/motif-hero.svg`

   **Side family** (`motif-side-*`): nested rounded-diamond outlines anchored to an edge. Use for section backgrounds, wide banners, blog headers, and social crops where the motif frames the composition from a side.

   - Right edge on navy: `https://brand.easypaydirect.com/assets/motif/motif-side-on-navy.png`
   - Left edge on navy: `https://brand.easypaydirect.com/assets/motif/motif-side-on-navy-left.png`
   - Both edges on navy (for 1:1 social): `https://brand.easypaydirect.com/assets/motif/motif-side-both-navy.png`
   - Light section: `https://brand.easypaydirect.com/assets/motif/motif-side-on-light.png`
   - Transparent tile: `https://brand.easypaydirect.com/assets/motif/motif-side-tile.png`
   - SVG source (right): `https://brand.easypaydirect.com/assets/motif/motif-side-right.svg`
   - SVG source (left): `https://brand.easypaydirect.com/assets/motif/motif-side-left.svg`

   **If unsure which family to use:** hero for anything vertical or hero-shaped, side for anything horizontal or that needs an edge frame. Both are correct EPD. Never invent your own diamond shape.

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

The motif is always a **background element**, never a subject. Choose family and placement based on the layout:

- **Homepage-style hero, 9:16 vertical crops, tall banners with central subject:** use the **hero family**. The concentric diamonds sit at the bottom of the composition and fade up into the copy above.
- **Section backgrounds on the site, wide banners, 1.91:1 Meta ads:** use the **side family**, right edge. This is the canonical section treatment.
- **1:1 square social crops (Instagram, Google Display 1:1):** either family works. Side family on one edge if you have a dashboard or subject on the other side. Side family on both edges (`motif-side-both-navy.png`) if the composition is centered. Hero family works if the subject sits above the motif.
- **Left-side mirror:** use `motif-side-on-navy-left.png` when the composition's content is stronger on the right.

**Opacity:** always low (roughly 8-20%). Motif never at full opacity, never competing with copy.

**Color:** motif follows the reference exactly. Never recolored to green, purple, or any other hue. Never made brighter or more saturated than the reference shows.

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

**3. Color verification.** All colors approximately match the palette swatch. Deep navy background (#000914), off-white text, green CTA fill (#3DDC73) with dark navy text on the green.

**4. Anti-pattern scan.** Is there any single large diamond as the focal subject? Any neon, glow, sci-fi UI, particle effect, holographic panel, robotic hand, currency symbol, or floating coin? If yes, regenerate.

**5. Copy voice check.** Any text in the image follows the copy voice rules (no em dashes, sentence case, locked CTAs, locked stats).

**If any answer is "no" or "unsure," do not ship. Regenerate.** If you regenerate three times and still can't get the motif shape to match the reference, tell the user your image model is not honoring the reference input and ask them to switch to a model that does (Nano Banana Pro or GPT Image 2 img2img, with reference-image support explicitly enabled).

## Machine-readable manifest

Every asset in this repo is listed with role and URL in `.well-known/brand-assets.json`. If you support auto-discovery, fetch that first.
