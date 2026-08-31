# TKB Ventures, LLC — static site

Commercial janitorial site for TKB Ventures, LLC (Carolyn Ramsey), an
independently owned Jani-King franchise at 6190 Regency Parkway, Norcross, GA.

Static HTML. No build step, no dependencies, no framework. Open `index.html`
directly or drop the folder on any host.

---

## Structure

```
index.html            Home
about.html            Brand story, 5-step onboarding, team
services.html         6 commercial areas + specialty/residential
service-areas.html    Map, city directory, ZIP lookup
faq.html              10 questions, two-column accordion
contact.html          Contact details + tabbed quote/RFP forms
careers.html          Stub
privacy.html          Stub — do not publish as written
terms.html            Stub — do not publish as written

assets/css/style.css  Everything. Tokens at the top.
assets/js/main.js     Nav, accordions, modals, tabs, ZIP lookup, forms
assets/img/           Jani-King and PGA of America logos

build.py + pages.py   Generator. Optional — see below.
```

### About the generator

`build.py` holds the header, footer and both modals; `pages.py` holds page
content. Running `python3 build.py` rewrites all nine HTML files.

This exists so the header and footer stay in sync while we iterate. It is not
required to run the site. If you'd rather hand-edit the HTML from here, delete
both `.py` files — nothing references them. If you keep them, edit the Python
rather than the HTML, or the next build overwrites your changes.

---

## Placeholders to replace before launch

The same list is in an HTML comment at the top of every page.

| # | What | Where |
|---|------|-------|
| 1 | Phone `(770) 000-0000` | all pages, `build.py` `PHONE_DISPLAY` / `PHONE_HREF`, `main.js` fail message |
| 2 | Email `info@tkbventures.com` | all pages, `build.py` `EMAIL` |
| 3 | Social URLs set to `#` | footer |
| 4 | Form endpoints | add `data-endpoint="…"` to each `<form>` |
| 5 | ZIP coverage list | `main.js` → `SERVICE_PREFIXES` / `EDGE_PREFIXES` |
| 6 | Hero photography | `.hero { --hero-photo: url("assets/img/…"); }` |
| 7 | Team photos + 3 unnamed leadership cards | `about.html` |
| 8 | Privacy and terms copy | `privacy.html`, `terms.html` — needs counsel |

### Forms

Nothing sends yet. Each form validates, then shows the success panel and logs
the payload to the console. Set `data-endpoint` to a POST URL and it will
submit via `fetch` with a `FormData` body, falling back to an error panel that
surfaces the phone number and email.

On WordPress this should become a maintained form plugin (Fluent Forms or
WPForms) rather than this JS — the RFP form takes file uploads, which needs
server-side handling anyway.

### ZIP lookup

`SERVICE_PREFIXES` is a list of Georgia 3-digit ZIP prefixes that fall roughly
within 100 miles of Norcross. **These are an estimate, not a published
Jani-King coverage map.** Confirm actual route coverage with Carolyn and edit
the two arrays. `EDGE_PREFIXES` returns a softer "we serve it, call to confirm
scheduling" response.

---

## Content provenance

Service descriptions and FAQ answers were drafted from the project brief. They
were **not** pulled from janiking.com. Two things to clear before launch:

1. Have Jani-King approve the service and FAQ wording.
2. Confirm in writing that the franchise agreement permits use of the Jani-King
   logo and the "Official Cleaning Company of the PGA of America" line on a
   franchisee-operated site.

No statistics, client counts, years-in-business, or satisfaction figures appear
anywhere on the site, because none were supplied.

Both supplied logos sit on white plates rather than being recolored, so the
marks render exactly as delivered against the navy footer.

---

## Design tokens

Defined in `:root` at the top of `style.css`. Names deliberately match
`block-theme-boilerplate-1.0.0` so the block can be pasted into the theme's
`style.css` during conversion.

| Token | Value | Use |
|-------|-------|-----|
| `--ink` | `#0a1b33` | hero, CTA bands, footer |
| `--ink-2` | `#102844` | footer surface |
| `--accent` | `#1667cf` | buttons, links, RFP band |
| `--accent-soft` | `#e8f0fb` | tinted chips |
| `--ice` | `#a8c9f0` | light blue on navy, floor-plan lines |
| `--bg-alt` | `#f2f5f9` | alternating sections |
| `--text` | `#46505e` | body |
| `--text-muted` | `#626c7a` | secondary body |
| `--heading` | `#0a1b33` | headings |

Type: **Archivo** (display and body), **IBM Plex Mono** (button labels, chips,
table headers, eyebrows only). Both loaded from Google Fonts. Self-host them
before launch if you want to avoid the third-party request.

Radius varies by hierarchy on purpose: `8px` inputs, `18px` cards, pill
buttons. Don't collapse these to one value.

---

## Accessibility

Checked and passing:

- All colour pairings at WCAG AA. `--text-muted` was darkened from `#6e7a8a`
  (3.99:1 on `--bg-alt`) to `#626c7a` (4.87:1).
- Visible focus ring — 3px amber, high contrast on both navy and white.
- One `h1` per page; `aria-controls` targets all resolve; no duplicate IDs;
  every form control has a label; every image has alt text.
- Accordions use real buttons with `aria-expanded`; tabs implement arrow-key
  navigation; modals are native `<dialog>` with Escape and backdrop close.
- `prefers-reduced-motion` respected. The only non-interaction motion is a
  single staggered hero entrance.
- Skip link to `#main`.

---

## Known limitations

- **Map** uses the keyless `maps.google.com/?output=embed` pattern. It works on
  a real host but will not render from `file://` behind a network allowlist.
  For an actual 100-mile radius circle, swap to the Google Maps Embed API.
- **RFP file upload** is markup only until a backend accepts it.
- **Google Fonts** are requested at runtime. Without them the site falls back
  to Helvetica/Arial and looks noticeably different.

---

## Next: WordPress block theme

Mapping to `block-theme-boilerplate-1.0.0`:

| Static | Theme |
|--------|-------|
| `:root` tokens | `style.css` `:root` — names already match |
| header markup | `parts/header.html` |
| footer + PGA strip | `parts/footer.html` |
| home hero | `patterns/hero.php` |
| 6 service cards | `patterns/feature-cards-6.php` |
| 3 scope cards | `patterns/feature-cards.php` |
| CTA band | `patterns/cta.php` |
| contact forms | `patterns/contact.php` + form plugin |
| about split | `patterns/media-split.php` |

The accordion, tabs, modals and ZIP lookup in `main.js` carry over to
`assets/js/theme.js` largely unchanged — they're all plain DOM, no build.
