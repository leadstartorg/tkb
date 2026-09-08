# TKB Ventures site — change log

Every change since the first build, grouped by page. Five rounds so far:

| Round | What it covered |
|-------|-----------------|
| **R1** | Initial build from the sitemap brief |
| **R2** | Carolyn's first change list (Lilburn, PGA removal, service cuts) |
| **R3** | Real street address + first owner headshot |
| **R4** | Real phone number, rewritten bio, replacement headshot |
| **R5** | New logo, primary colour, Lora, Coverage Areas, ops photo |

---

## Site-wide

**R1**
- Built nine pages, one stylesheet, one JS file. No framework, no build step.
- Design tokens named to match `block-theme-boilerplate-1.0.0` so the WordPress conversion stays a 1:1 mapping.
- Navy / blue / grey palette, no green. Dark immersive hero, pill buttons with a leading ring, floating enquiry card — carried over from the Ventrix reference.
- Hero background built as an architectural floor-plan schematic (corridor, rooms, door swings, stair core) rather than stock photography.
- Accessibility pass: one `h1` per page, labelled form controls, `aria-expanded` accordions, arrow-key tabs, native `<dialog>` modals, skip link, `prefers-reduced-motion` respected.

**R2**
- Relocated the business from Norcross to **Lilburn, GA** everywhere.
- **PGA of America removed** entirely — footer strip, hero chip, and the trademark line in the footer legal row. `pga-of-america-logo.png` is still in `assets/img/` but is no longer referenced.
- "Jani-King standard" → "national standard" everywhere.
- Coverage narrowed from "roughly 100 miles" to "the Atlanta metro" following the removal of the outer-radius region.
- Curly apostrophes applied to body copy via a generator pass.

**R3**
- Street address set to **4045 Five Forks Trickum Road, Suite B9 #231, Lilburn, GA 30047**. Verified no horizontal overflow at 1440px or 390px.

**R4**
- Phone set to **(678) 600-0329** in 27 places, with every `tel:` link resolving to `tel:+16786000329` — including the hardcoded fallback in `main.js` shown when a form submission fails.

**R5**
- **Primary colour changed to `#1c69b3`.** It now carries every hero, the header, buttons, links and chips. `#0a1b33` stays in the scheme as a support tone for headings, the RFP and CTA bands, dark cards, table headers and the footer.
- **Primary font changed to Lora** (Google Fonts), replacing Archivo. Heading tracking loosened from `-0.035em` to `-0.015em` and body leading raised to 1.72, because a serif does not want grotesque-level negative tracking. IBM Plex Mono retained for small utility labels only — buttons, chips, breadcrumbs, table headers.
- **New TKB Ventures logo** replaces the drawn placeholder mark and wordmark in the header and footer.
- **"Home" added to the main menu** as the first item.
- **Floor-plan schematic lines recoloured** from light blue to white, which is what reads on the mid-blue hero.
- **Two-tone focus ring introduced.** No single colour clears 3:1 on both white and mid-blue, so a white inner ring now pairs with a navy outer ring.
- `--text-on-ink` raised from 78% to 90% white — 78% measured 4.10:1 on the new primary and failed AA.
- `--ice` lightened from `#a8c9f0` to `#dfeefc` for the same reason (4.30:1 → 4.78:1).
- **RFP band moved from blue to navy** so it reads as a distinct band beneath the now-blue hero.

---

## Home — `index.html`

**R2**
- Hero chip replaced: the PGA line became **"Serving Greater Atlanta since 2010."**
- Hero intro: Norcross → Lilburn, "franchise" → "franchisee", "plants" removed from the facility list.
- Commercial cleaning card: "Industrial and manufacturing" removed.
- Specialty card: **"Pressure washing" added.**
- ZIP card: "within about 100 miles of Norcross" → "across the Atlanta metro"; placeholder ZIP 30071 → 30047; a "See the coverage map" link added so all three scope cards share the same structure.
- Co-brand section: the Jani-King name removed from the body copy.
- Quality-control section rewritten to Carolyn's supplied wording, and the "Most cleaning contracts start well…" opener removed.
- Home FAQ subset re-indexed after a question was deleted from the master list.

**R5**
- Hero background is now the primary blue with a deepening gradient; RFP band beneath it is navy.

---

## About — `about.html`

**R2**
- First paragraph removed ("Facility managers in Atlanta have two bad options…"), and the dangling "close that gap" reference it left behind was repaired.
- "franchise" → "franchisee"; "the same metro" → "the same metro area as your building".
- "industrial plants" removed from the facility list; "within roughly 100 miles of Norcross" → "across the Atlanta metro".
- Step 3: trailing clause "— including your access and key-control procedures" removed.
- Step 4: "and any badging your site requires" → "and the needs of the customer".
- Step 5: rewritten to match the FAQ answer on quality inspections.
- **Team grid replaced with an owner bio** — the four-card layout and its three unnamed placeholder people are gone.

**R3**
- First owner headshot added, cropped 4:5 from the supplied 976×2048 original.

**R4**
- **Bio replaced with Carolyn's rewrite.** Grammar corrections only: "South Carolina" spelled out, comma before the final clause, "now bringing" → "are now bringing".
- Section retitled **"Meet the owner" → "Our story"**, since the new first paragraph is company history rather than personal. Name and title moved to a caption beneath the photo.
- Headshot replaced. The supplied `carolyn.png` was 704×1477 with **transparent letterbox bands**, not white — flattened onto white, cropped to the 701×876 photo region at 4:5, resized to 800×1000.

**R5**
- **Operations photo added** (`operations.jpg`), replacing the labelled placeholder box. Frame set to 16:9 to suit the supplied 1376×768 image rather than cropping a wide corridor shot down to 4:3.
- Sentence replaced with: *"TKB Ventures runs the training, inspection, and safety programs of national brands. As a locally owned business, our leadership operates right here in your metro area."*

---

## Services — `services.html`

**R2**
- **"Industrial & manufacturing plants" card removed** — six service areas down to five.
- Specialty list: **"Pressure washing" added.**
- "We are also available for one-time services if needed" added to the specialty section and to the floor-care FAQ answer.
- **ZIP coverage-check section removed** from this page.
- Subtitle: "Six core commercial service areas" → "Five".
- Service grid divider technique rebuilt: hairlines are now a 1px ring on each card instead of a gap over a coloured grid background, so the trailing empty cell left by the removed sixth card stays white instead of showing a grey block.

**R5**
- Subtitle replaced with: *"We list our five core commercial service areas, plus specialty, periodic, and residential services."* ("speciality" corrected to "specialty" to match the rest of the site; serial comma added.)
- **Specialty / periodic / residential band recoloured** off `#0a1b33` to a light blue tint, with the service list rendered as white chips and the button switched from white to primary blue. It sat directly above the navy CTA band and the two dark sections were losing their edge against each other.

---

## Coverage Areas — was `service-areas.html`, now `coverage-areas.html`

**R2**
- **Outer 100-mile region removed** from the table — Athens, Gainesville, Canton, Woodstock, Cartersville, Dalton, Rome, Griffin and Macon are no longer listed. Three regions down to two.
- **Lilburn added** to the north-metro city list; Norcross retained as a served city.
- Map recentred from the Norcross address to Lilburn; map note and page intro rewritten off the "100-mile radius" framing.
- Section subtitle: "Grouped by how far they sit from Lilburn" → "Grouped by area", since with two regions the grouping is no longer by distance.
- ZIP lookup narrowed to prefixes `300`–`303`. Athens (`305`/`306`), Macon (`310`–`312`) and Dalton (`307`) now return "not on a route yet" and point to the RFP form. The `EDGE_PREFIXES` second tier is retained but empty.

**R3**
- Map query set to the street address, without the "Suite B9 #231" line — that phrasing tends to defeat Google's geocoder, and at this zoom it makes no visual difference.

**R5**
- **Page renamed** from `service-areas.html` to `coverage-areas.html`; nav label, breadcrumb, page title, meta description and every inbound link updated.
- Intro changed to: *"Our office is in Lilburn, Georgia, but we service commercial facilities across the Atlanta metro."*

---

## FAQ — `faq.html`

**R2**
- **"How does the partnership between TKB Ventures and Jani-King work?" removed.** Ten questions down to nine.
- Q1 retitled "Is TKB Ventures / Jani-King fully insured and bonded?" → **"Is TKB Ventures fully insured and bonded?"**
- Scheduling answer: "— including overnight, early-morning, and weekend windows" removed.
- Quality answer replaced with Carolyn's wording.
- Green cleaning answer: "meet LEED standards" → "meet standards".
- Start-of-service answer: "and any badging your site requires" → "and the needs of the customer".
- Floor-care answer: one-time services sentence added.
- Meta description: Norcross → Lilburn.

**R5**
- Subtitle replaced with: *"Learn more about insurance, scheduling, quality control, and how TKB Ventures works."* (Dropped "the" from "how the TKB Ventures works".)

---

## Contact — `contact.html`

**R2**
- **"Service hours" row removed** from the contact details list.
- Facility-type dropdown: **"Industrial / manufacturing" option removed** to match the services actually offered.
- Page title and meta description: Norcross → Lilburn.

**R3**
- Office address updated to the Lilburn street address.

**R4**
- Phone updated in the details list and both form fallbacks.

---

## Footer — every page

**R2**
- **PGA of America strip removed**, along with the "PGA of America marks" trademark line.
- **"Pressure washing" added** to the services column.
- About column rewritten to draw from the About page copy, per request.

**R5**
- New logo replaces the drawn mark and wordmark; lockup rebuilt as a stacked arrangement in the footer column.
- "Service areas" link relabelled **"Coverage areas"** and repointed.
- About column: **"As a Jani-King franchisee" removed** — no Jani-King reference in this column now.

---

## Careers, Privacy, Terms

**R1** — created as short stubs so the footer has no dead links. Privacy and Terms carry an explicit "do not publish as written" note; both need counsel.

**R2–R5** — inherit all site-wide header, footer, palette, font and logo changes. No page-specific copy changes.

---

## Still open

1. **Email** `info@tkbventures.com` — placeholder.
2. **Social URLs** — all three set to `#`.
3. **Form endpoint** — forms validate and show success but send nothing until `data-endpoint` is set.
4. **ZIP coverage list** — `SERVICE_PREFIXES` in `main.js` is an estimate, not a published coverage map.
5. **Hero background photo** — optional; the hero currently uses the floor-plan schematic.
6. **Privacy and Terms copy** — needs counsel.
7. **Jani-King references still on the site** — the header and footer sub-label "Jani-King of Atlanta", the co-brand band and its logo on the home page, the hero and About intro lines "independently owned Jani-King franchisee", and the footer disclaimer. None of these were flagged for removal, so they remain.
