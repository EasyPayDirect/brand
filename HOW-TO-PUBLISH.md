# How to publish this repo

Step-by-step for the EPD team. Total time: about 15 minutes if your DNS is on Cloudflare.

There are two things to do:

1. **Push this folder to a new public GitHub repo** and turn on GitHub Pages.
2. **Point `brand.easypaydirect.com` at that GitHub Pages URL** via a CNAME record.

Both are one-time setup. After this, updating an asset is a `git commit` and `git push`.

---

## Part 1: Push to GitHub

### Prerequisites
- You have write access to a GitHub organization for EPD (e.g. `easypaydirect`, `epd-inc`, or your personal account if there's no org yet). If there is no org, create one at https://github.com/organizations/plan (free tier is fine).
- You have `git` installed locally, or you're comfortable dragging files into the GitHub web UI.

### Steps

**1. Create the repo on GitHub.**
- Go to https://github.com/organizations/YOUR-ORG/repositories/new (or https://github.com/new for a personal repo).
- Name: `brand`
- Description: `Easy Pay Direct brand assets and agent instructions`
- Visibility: **Public** (required for GitHub Pages on free tier, and required so agents can fetch the URLs)
- Do **NOT** initialize with a README, .gitignore, or license (this repo already contains those files)
- Click **Create repository**

**2. Upload the files.** Two ways to do this — pick one:

**Option A — Command line (fastest if you have git set up):**

```bash
# From the workspace where you downloaded the epd-brand-repo folder
cd path/to/epd-brand-repo

git init
git add .
git commit -m "Initial: EPD brand asset repo for agents"
git branch -M main
git remote add origin https://github.com/YOUR-ORG/brand.git
git push -u origin main
```

**Option B — GitHub web UI (no command line):**

- On the newly-created empty repo page, click "uploading an existing file"
- Drag the entire contents of the `epd-brand-repo` folder into the browser
- Commit message: `Initial: EPD brand asset repo for agents`
- Click **Commit changes**

**3. Turn on GitHub Pages.**
- On the repo page, go to **Settings** → **Pages** (left sidebar)
- Under "Build and deployment":
  - Source: **Deploy from a branch**
  - Branch: **main**, folder: **/ (root)**
- Click **Save**

Wait 60 seconds. Your assets are now live at:
`https://YOUR-ORG.github.io/brand/assets/motif/motif-on-navy.png`

Test it in a browser. If the image loads, you're good.

---

## Part 2: Point brand.easypaydirect.com at it

### Prerequisites
- DNS access for `easypaydirect.com`. If DNS is on Cloudflare (your background suggests it is), you already have this. Log in at https://dash.cloudflare.com.

### Steps

**1. Add the custom domain in GitHub.**
- Repo → **Settings** → **Pages**
- Under "Custom domain", type `brand.easypaydirect.com` and click **Save**
- GitHub will show a warning about DNS not being configured yet — that's expected. Do not tick "Enforce HTTPS" yet.

**2. Add the CNAME record in Cloudflare.**
- Cloudflare dashboard → `easypaydirect.com` → **DNS** → **Records** → **Add record**
- Type: **CNAME**
- Name: `brand`
- Target: `YOUR-ORG.github.io` (no https://, no trailing slash, no /brand)
- Proxy status: **DNS only** (the gray cloud, not the orange cloud). GitHub Pages will not work through Cloudflare's proxy for the initial certificate issuance. You can turn on the orange cloud later once HTTPS is enforced.
- TTL: **Auto**
- Click **Save**

**3. Wait for DNS to propagate (usually 1-5 minutes).**

Test from a terminal:
```bash
dig brand.easypaydirect.com CNAME +short
```
Should return `YOUR-ORG.github.io.`

**4. Come back to GitHub and enforce HTTPS.**
- Repo → **Settings** → **Pages**
- Wait until you see a green check next to your custom domain
- Tick **Enforce HTTPS**
- Wait another minute for the certificate to be issued.

**5. Test the final URL.**
Open in a browser: `https://brand.easypaydirect.com/assets/motif/motif-on-navy.png`

If the image loads, you're done.

---

## What to do after it's live

**1. Share the URL with your team.**
Anyone at EPD, any affiliate, any vendor, any AI agent can now pull assets from `brand.easypaydirect.com/...`

**2. Update the BRAND-QUICK-PROMPT.md in your workspace.**
The one in your `/home/user/workspace/BRAND-QUICK-PROMPT.md` should be replaced with the version from this repo (which has the mandatory-first-step block and the anti-pattern list at the top). Or just have your workspace fetch from `https://brand.easypaydirect.com/brand-quick-prompt.md`.

**3. Add the manifest URL to any AI tool that supports auto-discovery.**
Some MCP servers and agent frameworks look for `.well-known/brand-assets.json`. The manifest is served at `https://brand.easypaydirect.com/.well-known/brand-assets.json`.

**4. Package the EPD Commerce assets similarly.**
Once this is working, create a second repo at `brand.epd.com` (or `brand-commerce.easypaydirect.com`) with the EPD Commerce equivalents. Same structure, different assets.

---

## Updating an asset later

Anyone with commit access to the repo can update. Workflow:

1. Replace the file locally with the new version
2. `git commit -am "Update motif-on-navy.png"` and `git push`
3. Wait ~30 seconds for GitHub Pages to redeploy
4. New version is live at the same URL

The URL never changes even if you replace the file. This is the whole point of hosting assets at stable URLs.

---

## Troubleshooting

**Images don't load at brand.easypaydirect.com after 5 minutes:**
- Check the CNAME record actually points at `YOUR-ORG.github.io` and not `YOUR-ORG.github.io/brand` (the folder is not part of the CNAME target).
- If Cloudflare proxy is on (orange cloud), turn it off. GitHub Pages certificate issuance requires DNS-only for the first setup.

**HTTPS certificate not issuing:**
- Wait longer (up to 24 hours for the first cert). GitHub uses Let's Encrypt and it needs to complete an HTTP challenge, which requires DNS to be settled first.
- Confirm the CNAME resolves with `dig` (see step 3 above).

**404 on a specific asset URL:**
- Confirm the file exists in the repo at the exact path.
- Filenames are case-sensitive on GitHub Pages. `Motif-on-navy.png` won't match `motif-on-navy.png`.

**Any other issue:**
- The full step-by-step from GitHub is at https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site — worth reading if you get stuck.
