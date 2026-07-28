# Obadah Aldweiri — CV Website

A static, single-page CV/portfolio site. No build step, no dependencies — plain HTML/CSS/JS.

## Structure

```
index.html    → content & structure
styles.css    → design tokens + layout (edit CSS variables at the top to re-theme)
script.js     → typing effect, scroll-reveal, active nav highlighting
assets/       → put your CV PDF and any images here
```

## Languages

The site ships with EN / AR / NO buttons in the side nav (`i18n.js`). Arabic
switches the whole page to RTL. To edit translated text, edit the matching
key in the `I18N` object in `i18n.js` — the English, Norwegian and Arabic
copies are separate blocks in that same file. Anything with a `data-i18n="…"`
attribute in `index.html` is translated; anything without one (proper nouns
like company names, tool names) stays the same in every language.

## Download CV button

"Download CV" no longer points at a static file. Clicking it:

1. Shows a small terminal-style overlay with a typed "build log".
2. Switches `#main` into a clean, single-column print layout (`body.pdf-mode` in `styles.css`) — the side nav and hero terminal are hidden for this snapshot only.
3. Uses [html2pdf.js](https://github.com/eKoopmans/html2pdf.js) (loaded from cdnjs) to render `#main` into a PDF and trigger a download, named after whichever language is currently active (e.g. `Obadah_Aldweiri_CV_EN.pdf`).
4. Restores the normal layout once done.

All of this lives in `script.js` (search for `downloadCvBtn`) and the `.pdf-mode` rules in `styles.css`. If you'd rather ship a hand-made PDF instead, put it at `assets/Obadah_Aldweiri_CV.pdf` and swap the button back to a plain `<a href="assets/..." download>` link.

## Edit your content

Everything lives in `index.html` in plain, readable sections:

- `#intro` — name, tagline, terminal intro text (also edit `TYPE_TEXT` in `script.js`)
- `#about` — bio paragraphs
- `#experience` / `#education` — timeline items (copy/paste an `<li class="timeline__item">` block to add more)
- `#skills` — tag lists
- `#contact` — email / phone / links

To swap the "Download CV" button target, add your PDF at `assets/Obadah_Aldweiri_CV.pdf` (or change the `href` in `index.html`).

## Run locally

Just open `index.html` in a browser, or serve it:

```bash
npx serve .
```

## Deploy — GitHub Pages (free, recommended)

1. Push this folder to a GitHub repo (e.g. `obada19/cv`).
2. Repo → **Settings → Pages**.
3. Under "Build and deployment", set **Source: Deploy from a branch**.
4. Branch: `main`, folder: `/ (root)` → **Save**.
5. Your site will be live at `https://obada19.github.io/cv/` within a minute or two.

## Deploy — Vercel (alternative, since you're already using it)

1. `vercel` CLI or import the repo at vercel.com/new.
2. Framework preset: **Other** (static site) — no build command needed.
3. Deploy.

## Notes

- Fonts load from Google Fonts (Fraunces, Inter, IBM Plex Mono) — remove the `<link>` tags in `<head>` if you want a fully offline/self-hosted version.
- Respects `prefers-reduced-motion` and is keyboard-navigable.
- Mobile layout collapses the side nav into a top bar under 760px.
