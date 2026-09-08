# TKB Ventures, LLC — static site

Commercial janitorial site for TKB Ventures, LLC (Carolyn Ramsey), an
independently owned Jani-King franchisee at 4045 Five Forks Trickum Road,
Suite B9 #231, Lilburn, GA 30047. Phone (678) 600-0329.

See `CHANGELOG.md` for the full per-page history of every revision round.

**Revision 2** applied Carolyn's first change list: relocated to Lilburn, PGA of
America removed, coverage narrowed to metro Atlanta, industrial/manufacturing
dropped, pressure washing added, team grid replaced with the owner bio.

Static HTML. No build step, no dependencies, no framework. Open `index.html`
directly or drop the folder on any host.

---

## Structure

```
index.html            Home
about.html            Brand story, 5-step onboarding, owner bio
coverage-areas.html   Map, city directory, ZIP lookup (was service-areas.html)
services.html         6 commercial areas + specialty/residential
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
| 1 | Email `info@tkbventures.com` | all pages, `build.py` `EMAIL` |
| 2 | Social URLs set to `#` | footer |
| 3 | Form endpoints | add `data-endpoint="…"` to each `<form>` |
| 4 | ZIP coverage list | `main.js` → `SERVICE_PREFIXES` |
| 5 | Hero background image (optional) | `.hero { --hero-photo: url("assets/img/…"); }` |
| 6 | Privacy and terms copy | `privacy.html`, `terms.html` — needs counsel |

### Images

Carolyn approved AI-generated imagery provided it reads as real photography.
The owner headshot is in place: `assets/img/carolyn-ramsey.jpg`. The supplied
`carolyn.png` was 704x1477 with transparent letterbox bands top and bottom; it
was flattened onto white, cropped to the 701x876 photo region at 4:5, and
resized to 800x1000 (154 KB).
The operations photo is in place at `assets/img/operations.jpg`, cropped to
16:9 from the supplied 1376x768 original — the frame was set to suit the image
rather than cropping a wide corridor shot down to 4:3.

The supplied logo (`TKB-Ventures-Logo_jpeg.png`) had **no transparency at all** —
every pixel was opaque and the transparency checkerboard was baked in as dark
grey. It was keyed out by luminance with the threshold set above the light
checker squares, trimmed, and written to `assets/img/tkb-ventures-logo.png` at
800x194 with real alpha. The art is white, so it only works on dark
backgrounds; both the header and footer qualify. **Ask Carolyn for the original
vector or a true-transparency export before launch** — a keyed raster is a
workaround, not a proper brand asset.

Only the hero background image remains optional and unstubbed.

### Forms

Nothing sends yet. Each form validates, then shows the success panel and logs
the payload to the console. Set `data-endpoint` to a POST URL and it will
submit via `fetch` with a `FormData` body, falling back to an error panel that
surfaces the phone number and email.

On WordPress this should become a maintained form plugin (Fluent Forms or
WPForms) rather than this JS — the RFP form takes file uploads, which needs
server-side handling anyway.

### ZIP lookup

`SERVICE_PREFIXES` covers metro Atlanta (`300`–`303`), keyed off the Lilburn
office. **These are an estimate, not a published coverage map.** Confirm actual
route coverage with Carolyn and edit the array.

Removing the outer 100-mile row from the Service Areas page narrowed coverage,
so Athens (`305`/`306`), Macon (`310`–`312`) and Dalton (`307`) now return
"not on a route yet" and point to the RFP form. `EDGE_PREFIXES` is the optional
second tier for ZIPs served with extra lead time — it's empty now, but add
prefixes to switch it back on.

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

The Jani-King logo sits on a white plate rather than being recolored, so the
mark renders exactly as delivered against the co-brand band.

**PGA of America was removed** from the footer in revision 2, along with the
hero chip that carried the "Official Cleaning Company" line and the trademark
line in the footer legal row. `assets/img/pga-of-america-logo.png` is still in
the folder but is no longer referenced anywhere — delete it, or restore the
footer strip from git history if that changes.

---

## Design tokens

Defined in `:root` at the top of `style.css`. Names deliberately match
`block-theme-boilerplate-1.0.0` so the block can be pasted into the theme's
`style.css` during conversion.

| Token | Value | Use |
|-------|-------|-----|
| `--primary` | `#1c69b3` | **PRIMARY** — heroes, header, buttons, links, chips |
| `--primary-hover` | `#15507f` | button hover, mobile drawer |
| `--primary-deep` | `#10416b` | gradient depth beneath the hero |
| `--primary-soft` | `#e9f1fa` | light tint bands and chips |
| `--primary-tint` | `#d3e4f6` | tint borders |
| `--ink` | `#0a1b33` | headings, RFP + CTA bands, dark cards, table headers |
| `--ink-2` | `#102844` | footer surface |
| `--ice` | `#dfeefc` | light blue text and rules on blue |
| `--bg-alt` | `#f2f5f9` | alternating sections |
| `--text` | `#46505e` | body |
| `--text-muted` | `#626c7a` | secondary body |
| `--heading` | `#0a1b33` | headings |

`--accent`, `--accent-hover` and `--accent-soft` remain as aliases of the
primary tokens, so the mapping into the boilerplate's `theme.json` stays 1:1.

Type: **Lora** (display and body — the primary face), **IBM Plex Mono** (button
labels, chips, breadcrumbs, table headers only). Both loaded from Google Fonts.
Self-host them before launch if you want to avoid the third-party request.

Heading tracking is deliberately loose (`-0.015em` on `h1`) and body leading is
1.72 — a serif does not want the tight negative tracking a grotesque can carry.

Radius varies by hierarchy on purpose: `8px` inputs, `18px` cards, pill
buttons. Don't collapse these to one value.

The service grid draws its hairline dividers as a 1px ring on each card, not as
a gap over a coloured grid background. Adjacent rings overlap into a single
line, and a trailing empty cell stays white — so the card count can change
(6 → 5 in revision 2) without leaving a grey hole in the last cell.

---

## Accessibility

Checked and passing:

- All colour pairings at WCAG AA, rechecked after the primary-colour change.
  `--text-muted` was darkened from `#6e7a8a` (3.99:1 on `--bg-alt`) to `#626c7a`
  (4.87:1). `--text-on-ink` was raised from 78% to 90% white and `--ice` from
  `#a8c9f0` to `#dfeefc`, both of which fell below 4.5:1 on the new primary.
- Two-tone focus ring — white inner, navy outer. No single colour clears 3:1
  on both white and the mid-blue primary, so the ring carries its own contrast.
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
| 5 service cards | `patterns/feature-cards-6.php` |
| 3 scope cards | `patterns/feature-cards.php` |
| CTA band | `patterns/cta.php` |
| contact forms | `patterns/contact.php` + form plugin |
| about split + owner bio | `patterns/media-split.php` |

The accordion, tabs, modals and ZIP lookup in `main.js` carry over to
`assets/js/theme.js` largely unchanged — they're all plain DOM, no build.
