#!/usr/bin/env python3
"""
Page bodies for the TKB Ventures static site.

COPY SOURCE NOTE
----------------
Service descriptions and FAQ answers below are drafted from the project
brief supplied by the client, not scraped from janiking.com. Have Jani-King
corporate approve the wording (and the co-branding / PGA line) before launch.
No statistics, counts, or performance claims are asserted anywhere on the
site, because none were supplied.
"""

# --- small line icons for the service grid ---------------------------------

def icon(paths):
    return ('<svg class="service__icon" width="30" height="30" viewBox="0 0 30 30" fill="none" '
            'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">' + paths + "</svg>")


ICONS = {
    "office": icon('<path d="M4 26h22M7 26V6h10v20M17 26V12h6v14"/>'
                   '<path d="M10 10h1.5M13.5 10H15M10 14h1.5M13.5 14H15M10 18h1.5M13.5 18H15M20 16h1M20 20h1"/>'),
    "medical": icon('<rect x="5" y="6" width="20" height="19" rx="2"/>'
                    '<path d="M15 11v8M11 15h8M5 10h20"/>'),
    "education": icon('<path d="M3 10 15 5l12 5-12 5L3 10Z"/>'
                      '<path d="M8 12.5V19c0 1.7 3.1 3 7 3s7-1.3 7-3v-6.5M25 11v6"/>'),
    "retail": icon('<path d="M4 10h22l-1.5 15H5.5L4 10Z"/>'
                   '<path d="M10.5 13V8a4.5 4.5 0 0 1 9 0v5"/>'),
    "industrial": icon('<path d="M4 26V13l7 4.5V13l7 4.5V8h4l1 18H4Z"/>'
                       '<path d="M8 21h2M15 21h2M21 21h2"/>'),
    "hospitality": icon('<path d="M6 20h18a9 9 0 0 0-18 0Z"/>'
                        '<path d="M4 24h22M15 7v4M13.5 5.5a1.5 1.5 0 1 1 3 0"/>'),
}


# --- reusable blocks -------------------------------------------------------

def accordion(items, ident, ink=False):
    """items: list of (question, answer)"""
    cls = "accordion accordion--ink" if ink else "accordion"
    rows = []
    for i, (q, a) in enumerate(items, start=1):
        bid = f"{ident}-btn-{i}"
        pid = f"{ident}-panel-{i}"
        rows.append(f"""        <div class="accordion__item">
          <h3>
            <button class="accordion__btn" type="button" id="{bid}"
                    aria-expanded="false" aria-controls="{pid}">
              <span>{q}</span>
              <span class="accordion__icon" aria-hidden="true"></span>
            </button>
          </h3>
          <div class="accordion__panel" id="{pid}" role="region" aria-labelledby="{bid}" data-open="false">
            <div><p>{a}</p></div>
          </div>
        </div>""")
    return f'      <div class="{cls}">\n' + "\n".join(rows) + "\n      </div>"


ZIP_CARD_DARK = """        <div class="scope-card scope-card--tool">
          <h3>Are you in our radius?</h3>
          <p>We run routes within about 100 miles of Norcross. Check your ZIP code.</p>
          <form class="zip-form" data-zip-form novalidate>
            <label class="visually-hidden" for="zip-home">ZIP code</label>
            <input id="zip-home" name="zip" type="text" inputmode="numeric" maxlength="5"
                   pattern="[0-9]{5}" placeholder="30071" autocomplete="postal-code">
            <button type="submit">Check</button>
          </form>
          <p class="zip-result" data-zip-result role="status"></p>
          <a class="link-plain" href="service-areas.html">See the coverage map</a>
        </div>"""


# --- FAQ content (10 questions, from the client brief) ---------------------

FAQ_ALL = [
    ("Is TKB Ventures / Jani-King fully insured and bonded?",
     "Yes. We carry comprehensive general liability, property damage, and workers' compensation "
     "coverage. Certificates of insurance are available on request and can be issued naming your "
     "organization before service begins."),

    ("How does the partnership between TKB Ventures and Jani-King work?",
     "TKB Ventures is an independently owned Jani-King franchise operator. You get local ownership "
     "and local management, backed by Jani-King's national training standards, systems, and "
     "purchasing."),

    ("Can we customize our commercial cleaning schedule?",
     "Yes. We provide daily, weekly, bi-weekly, or customized after-hours cleaning built around how "
     "your building actually runs — including overnight, early-morning, and weekend windows."),

    ("What is included in a standard commercial walk-through?",
     "We assess square footage, high-traffic zones, floor types, restroom counts, and any specific "
     "sanitation requirements, then build a written scope and quote from what we find on site."),

    ("How is cleaning quality monitored and maintained?",
     "TKB Ventures performs routine, scheduled quality assurance inspections against the Jani-King "
     "standard. Findings go to your point of contact so nothing is corrected quietly or repeated."),

    ("Do you offer eco-friendly or green cleaning options?",
     "Yes. We use eco-friendly, non-toxic products and micro-fiber protocols that meet LEED "
     "standards. If your facility has its own approved-chemical list, we work from it."),

    ("What safety and security protocols do your crews follow?",
     "All staff undergo background checks, wear uniform badges, and follow your keycard and access "
     "rules. Alarm codes, key control, and after-hours entry procedures are documented before the "
     "first shift."),

    ("How quickly can service start after a site walk-through?",
     "Service can typically begin within 24 to 48 hours of proposal approval and walk-through "
     "completion, depending on crew scheduling and any badging your site requires."),

    ("Do you handle emergency or one-time deep cleanings?",
     "Yes. We offer rapid-response disinfection, post-construction cleanup, and event cleaning, "
     "whether or not you hold a recurring contract with us."),

    ("What specialized floor care services do you offer?",
     "Carpet extraction, hard-floor stripping and waxing, tile and grout restoration, and polishing "
     "— scheduled as periodic work alongside nightly janitorial, or booked on its own."),
]

FAQ_HOME = [FAQ_ALL[0], FAQ_ALL[2], FAQ_ALL[8], FAQ_ALL[4]]


# --- service content -------------------------------------------------------

SERVICES = [
    ("office", "Office buildings &amp; corporate suites",
     "Nightly or scheduled janitorial for workspaces, lobbies, conference rooms, break rooms, and "
     "restrooms. Day porter coverage available for buildings that need someone on site during hours.",
     ["Nightly service", "Day porter", "Restroom sanitation", "Break rooms"]),

    ("medical", "Healthcare &amp; medical facilities",
     "Exam rooms, waiting areas, labs, and restrooms cleaned to healthcare protocols, with "
     "touch-point disinfection and coordination around your regulated waste handling.",
     ["Touch-point disinfection", "Exam rooms", "Waiting areas", "Protocol-driven"]),

    ("education", "Educational &amp; childcare facilities",
     "Classrooms, cafeterias, gyms, and restrooms on a schedule that works around instruction hours, "
     "with disinfection frequency stepped up during illness season.",
     ["Classrooms", "Cafeterias", "Gyms", "Around the bell schedule"]),

    ("retail", "Retail &amp; shopping centers",
     "Sales floors, entrances, fitting rooms, and public restrooms handled before opening or after "
     "close, so the store is customer-ready at the start of every trading day.",
     ["Before open / after close", "Sales floors", "Entrances", "Public restrooms"]),

    ("industrial", "Industrial &amp; manufacturing plants",
     "Production floors, warehouses, locker rooms, and plant offices — including machine scrubbing "
     "of hard floors and cleaning that fits between shift changes.",
     ["Warehouse floors", "Machine scrubbing", "Locker rooms", "Shift-change timing"]),

    ("hospitality", "Hospitality &amp; event venues",
     "Lobbies, guest areas, banquet rooms, and restrooms, plus pre- and post-event turnaround when "
     "the room has to be reset quickly between bookings.",
     ["Event turnaround", "Lobbies", "Banquet rooms", "Same-day reset"]),
]

SPECIALTY = [
    "Carpet extraction and spot treatment",
    "Hard-floor stripping, waxing, and burnishing",
    "Tile and grout restoration",
    "Interior and exterior window washing",
    "Post-construction and post-renovation cleanup",
    "Multi-family and residential turnover cleaning",
    "Rapid-response disinfection",
]


def service_grid():
    cards = []
    for key, title, body, tags in SERVICES:
        tag_html = "".join(f"<li>{t}</li>" for t in tags)
        cards.append(f"""        <article class="service">
          {ICONS[key]}
          <h3>{title}</h3>
          <p>{body}</p>
          <ul>{tag_html}</ul>
        </article>""")
    return '      <div class="service-grid">\n' + "\n".join(cards) + "\n      </div>"


# --- service area data (from the client brief) -----------------------------

AREAS = [
    ("Greater Atlanta &amp; north metro",
     "Norcross, Duluth, Alpharetta, Johns Creek, Roswell, Sandy Springs, Dunwoody, Marietta, "
     "Smyrna, Kennesaw, Cumming, Suwanee, Buford, Lawrenceville"),
    ("East &amp; south metro",
     "Decatur, Stone Mountain, Conyers, Covington, Snellville, McDonough, Peachtree City, "
     "Newnan, Stockbridge"),
    ("Outer 100-mile radius",
     "Athens, Gainesville, Canton, Woodstock, Cartersville, Dalton, Rome, Griffin, Macon"),
]


# ===========================================================================
#  Page builders
# ===========================================================================

def build(render, page_hero, CTA_BAND, PLAN_SVG, PHONE, PHONE_HREF, EMAIL, ADDR1, ADDR2):

    # ---------------------------------------------------------------- HOME
    home = f"""  <section class="hero">
    <div class="hero__media" aria-hidden="true"></div>
    {PLAN_SVG.format(cls="hero__plan")}
    <div class="wrap wrap--wide">
      <div class="hero__grid">
        <div>
          <p class="chip hero__chip" data-enter="1">
            <span class="chip__dot" aria-hidden="true"></span>
            Official Cleaning Company of the PGA of America
          </p>
          <h1 data-enter="2">Locally owned. Cleaned to a national standard.</h1>
          <p class="hero__intro" data-enter="3">TKB Ventures is an independently owned Jani-King
            franchise in Norcross, Georgia, cleaning offices, clinics, schools, plants, and retail
            space across the Atlanta metro.</p>
          <div class="btn-row" data-enter="4">
            <a class="btn btn--light" href="#" data-open-modal="modal-walkthrough">Request walk-through</a>
            <a class="btn btn--ghost-light" href="#" data-open-modal="modal-rfp">Submit RFP</a>
          </div>
          <div class="hero__foot" data-enter="5">
            <p>Insured and bonded. Background-checked crews. Scheduled quality inspections on every
              account, not just the new ones.</p>
          </div>
        </div>

        <aside class="hero-card" data-enter="5" aria-labelledby="hero-card-title">
          <h2 id="hero-card-title">Start here</h2>
          <ul class="hero-card__list">
            <li>
              <button class="hero-card__row" type="button" data-open-modal="modal-walkthrough">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="2" y="3" width="12" height="11" rx="1.5"/><path d="M2 6.5h12M5.5 1.5v3M10.5 1.5v3"/></svg>
                Book a walk-through
              </button>
            </li>
            <li>
              <button class="hero-card__row" type="button" data-open-modal="modal-rfp">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M9 1.5H4.5A1.5 1.5 0 0 0 3 3v10a1.5 1.5 0 0 0 1.5 1.5h7A1.5 1.5 0 0 0 13 13V5.5L9 1.5Z"/><path d="M9 1.5V5.5H13"/></svg>
                Send a bid package
              </button>
            </li>
            <li>
              <a class="hero-card__row" href="tel:{PHONE_HREF}">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M5.2 2.5 6.6 5 5.3 6.6a8 8 0 0 0 4.1 4.1L11 9.4l2.5 1.4v2.2a1 1 0 0 1-1.1 1A11.5 11.5 0 0 1 2 3.6a1 1 0 0 1 1-1.1h2.2Z"/></svg>
                Call {PHONE}
              </a>
            </li>
          </ul>
          <p class="hero-card__note">{ADDR1}, {ADDR2}</p>
        </aside>
      </div>
    </div>
  </section>

  <section class="rfp">
    <div class="wrap wrap--wide rfp__inner">
      <div>
        <h2>Running a bid for multiple sites?</h2>
        <p>Send us the package. We price multi-site portfolios on one standardized scope, with a
          single point of contact for every location instead of a different vendor per building.</p>
      </div>
      <a class="btn btn--light" href="#" data-open-modal="modal-rfp">Submit RFP to TKB</a>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <h2>What do you need cleaned?</h2>
        <p>Two service tracks and one question we get asked before anything else.</p>
      </div>
      <div class="scope-grid">
        <div class="scope-card">
          <h3>Commercial cleaning</h3>
          <ul>
            <li>Offices and corporate suites</li>
            <li>Healthcare and medical facilities</li>
            <li>Schools and childcare</li>
            <li>Retail and shopping centers</li>
            <li>Industrial and manufacturing</li>
            <li>Hospitality and event venues</li>
          </ul>
          <a class="link-plain" href="services.html#commercial">See commercial services</a>
        </div>

        <div class="scope-card">
          <h3>Specialty &amp; residential</h3>
          <ul>
            <li>Floor stripping, waxing, burnishing</li>
            <li>Carpet extraction</li>
            <li>Tile and grout restoration</li>
            <li>Window washing</li>
            <li>Post-construction cleanup</li>
            <li>Multi-family turnover</li>
          </ul>
          <a class="link-plain" href="services.html#specialty">See specialty services</a>
        </div>

{ZIP_CARD_DARK}
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="cobrand">
        <div class="cobrand__marks">
          <span class="logo-plate">
            <img src="assets/img/jani-king-logo.webp" alt="Jani-King" width="180" height="105" loading="lazy">
          </span>
          <span class="chip chip--light">
            <span class="chip__dot" aria-hidden="true"></span>
            Independently owned franchise
          </span>
        </div>
        <div>
          <h2>A national brand standard, run by people who live here</h2>
          <p>Jani-King has been building commercial cleaning systems for decades — training programs,
            inspection procedures, safety protocols, and equipment standards that most independent
            janitorial companies never develop.</p>
          <p>TKB Ventures runs those systems in Greater Atlanta. Carolyn Ramsey and her team hire,
            train, schedule, and inspect locally, so the person accountable for your building is
            someone you can reach directly.</p>
          <a class="link-plain" href="about.html">More about TKB Ventures</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Questions we get first</h2>
{accordion(FAQ_HOME, "home-faq")}
          <p style="margin-top: var(--sp-5);">
            <a class="link-plain" href="faq.html">Read all frequently asked questions</a>
          </p>
        </div>
        <div>
          <h2>Quality control isn't a promise, it's a schedule</h2>
          <p>Most cleaning contracts start well. What separates a good vendor from a bad one is what
            the building looks like in month seven.</p>
          <p>We inspect on a set schedule rather than when a complaint comes in. Inspections follow
            the Jani-King standard, findings are written down, and your point of contact sees them.
            When something slips, you hear about it from us first.</p>
          <p>Crews are background-checked and badged, follow your access and key-control rules, and
            are trained before they're assigned — not after.</p>
          <div class="btn-row" style="margin-top: var(--sp-5);">
            <a class="btn btn--primary" href="#" data-open-modal="modal-walkthrough">Request walk-through</a>
          </div>
        </div>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("index.html",
           "TKB Ventures | Jani-King of Atlanta — Commercial Cleaning in Norcross, GA",
           "Commercial janitorial and facility maintenance across Greater Atlanta. "
           "TKB Ventures is an independently owned Jani-King franchise based in Norcross, Georgia.",
           home, "index.html", solid=False)

    # --------------------------------------------------------------- ABOUT
    about = page_hero(
        "Local ownership, national systems",
        "TKB Ventures, LLC is an independently owned Jani-King franchise operating out of Norcross, "
        "Georgia.", "About") + f"""

  <section class="section">
    <div class="wrap">
      <div class="split split--media">
        <div>
          <!-- TODO: replace with a photograph of the crew or a serviced facility -->
          <div class="person__photo" style="aspect-ratio: 4 / 3;">
            <span style="font-family: var(--font-mono); font-size: 0.75rem; letter-spacing: 0.08em;">
              OPERATIONS PHOTO
            </span>
          </div>
        </div>
        <div>
          <h2>Why TKB Ventures exists</h2>
          <p>Facility managers in Atlanta have two bad options. Hire a small independent cleaner and
            get responsiveness without systems. Hire a national account and get systems without
            anyone who answers the phone.</p>
          <p>TKB Ventures was built to close that gap. As a Jani-King franchise we run the training,
            inspection, and safety programs of a national brand. As a locally owned business, the
            owner is in the same metro as your building.</p>
          <p>We serve office buildings, medical practices, schools and childcare centers, retail
            centers, industrial plants, and event venues within roughly 100 miles of Norcross.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="split">
        <div class="section-head" style="margin-bottom: 0;">
          <h2>From first call to first shift</h2>
          <p>Five steps, in order. Most accounts move through all of them inside a week.</p>
        </div>
        <div class="steps">
          <div class="step">
            <div>
              <h3>Walk-through</h3>
              <p>We visit the site and measure it — square footage, floor types, restroom counts,
                traffic patterns, access restrictions, anything unusual.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3>Written scope and quote</h3>
              <p>Every task and its frequency, in writing, priced per location. You should be able to
                hand it to someone else and have them understand exactly what we do.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3>Crew assignment and training</h3>
              <p>We assign a specific crew, run background checks, and train them on your building
                before their first shift — including your access and key-control procedures.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3>Service begins</h3>
              <p>Typically within 24 to 48 hours of approval, depending on crew scheduling and any
                badging your site requires.</p>
            </div>
          </div>
          <div class="step">
            <div>
              <h3>Scheduled inspections</h3>
              <p>Quality assurance visits happen on a set schedule against the Jani-King standard.
                Findings are documented and shared with your point of contact.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <h2>Who you'll be working with</h2>
        <p>Accountability has a name on it. These are the people responsible for your account.</p>
      </div>
      <div class="team-grid">
        <!-- TODO: add headshots and confirm titles and bios with each person -->
        <article class="person">
          <div class="person__photo"><span style="font-family: var(--font-mono); font-size: 0.7rem;">PHOTO</span></div>
          <h3>Carolyn Ramsey</h3>
          <p class="person__role">Owner</p>
          <p>Owner of TKB Ventures, LLC and the Jani-King franchise for the Atlanta market.</p>
        </article>
        <article class="person">
          <div class="person__photo"><span style="font-family: var(--font-mono); font-size: 0.7rem;">PHOTO</span></div>
          <h3>Name</h3>
          <p class="person__role">Operations director</p>
          <p>Placeholder. Replace with a short line on what this person is responsible for.</p>
        </article>
        <article class="person">
          <div class="person__photo"><span style="font-family: var(--font-mono); font-size: 0.7rem;">PHOTO</span></div>
          <h3>Name</h3>
          <p class="person__role">Field manager</p>
          <p>Placeholder. Replace with a short line on what this person is responsible for.</p>
        </article>
        <article class="person">
          <div class="person__photo"><span style="font-family: var(--font-mono); font-size: 0.7rem;">PHOTO</span></div>
          <h3>Name</h3>
          <p class="person__role">Quality assurance</p>
          <p>Placeholder. Replace with a short line on what this person is responsible for.</p>
        </article>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("about.html",
           "About TKB Ventures | Jani-King of Atlanta",
           "TKB Ventures, LLC is an independently owned Jani-King franchise in Norcross, Georgia, "
           "serving commercial facilities across the Atlanta metro.",
           about, "about.html")

    # ------------------------------------------------------------ SERVICES
    specialty_items = "\n".join(f"            <li>{s}</li>" for s in SPECIALTY)

    services = page_hero(
        "Commercial cleaning, floor care, and specialty work",
        "Six core commercial service areas, plus periodic and one-time work that runs alongside "
        "your nightly janitorial contract.", "Services") + f"""

  <section class="section" id="commercial">
    <div class="wrap">
      <div class="section-head">
        <h2>Commercial services</h2>
        <p>Scope and frequency are set at the walk-through. Nothing below is a fixed package —
          it's what we typically cover for each facility type.</p>
      </div>
{service_grid()}
    </div>
  </section>

  <section class="section section--ink" id="specialty">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Specialty, periodic, and residential work</h2>
          <p class="lede">Some jobs don't belong on a nightly schedule. Floor restoration, window
            washing, and post-construction cleanup are quoted separately and scheduled around your
            operating hours.</p>
          <p>Available whether or not you hold a recurring contract with us.</p>
          <div class="btn-row" style="margin-top: var(--sp-5);">
            <a class="btn btn--light" href="#" data-open-modal="modal-walkthrough">Get it quoted</a>
          </div>
        </div>
        <div>
          <ul style="list-style: none; padding: 0; margin: 0; display: grid; gap: 0.75rem;">
{specialty_items}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split split--media">
        <div>
          <h2>Do we cover your address?</h2>
          <p>Routes run within roughly 100 miles of our Norcross office, covering the Atlanta metro
            and reaching Athens, Gainesville, Rome, and Macon at the edges.</p>
          <a class="link-plain" href="service-areas.html">See the full coverage map</a>
        </div>
        <div class="zip-panel">
          <h3>Check a ZIP code</h3>
          <form class="zip-form" data-zip-form novalidate>
            <label class="visually-hidden" for="zip-services">ZIP code</label>
            <input id="zip-services" name="zip" type="text" inputmode="numeric" maxlength="5"
                   pattern="[0-9]{{5}}" placeholder="30071" autocomplete="postal-code">
            <button type="submit">Check</button>
          </form>
          <p class="zip-result" data-zip-result role="status"></p>
        </div>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("services.html",
           "Commercial Cleaning Services | TKB Ventures — Jani-King of Atlanta",
           "Office, medical, education, retail, industrial, and hospitality cleaning, plus floor "
           "care, window washing, and post-construction cleanup across Greater Atlanta.",
           services, "services.html")

    # ------------------------------------------------------- SERVICE AREAS
    rows = "\n".join(
        f"          <tr>\n            <th scope=\"row\">{region}</th>\n"
        f"            <td>{cities}</td>\n          </tr>"
        for region, cities in AREAS
    )

    map_q = "6190+Regency+Parkway+Suite+300,+Norcross,+GA+30071"

    areas = page_hero(
        "Where we run routes",
        "Our office is at 6190 Regency Parkway in Norcross. We service facilities within roughly "
        "100 miles of it.", "Service areas") + f"""

  <section class="section">
    <div class="wrap">
      <div class="map-frame">
        <iframe
          title="Map showing TKB Ventures at 6190 Regency Parkway, Norcross, Georgia"
          src="https://maps.google.com/maps?q={map_q}&amp;z=8&amp;output=embed"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <p class="form-note">Map is centered on our Norcross office. For an exact radius overlay,
        swap this for the Google Maps Embed API with a drawn 100-mile circle.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="wrap">
      <div class="section-head">
        <h2>Cities we serve</h2>
        <p>Grouped by how far they sit from Norcross. If your city isn't listed, ask — we bid
          outside the radius for multi-site contracts.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th scope="col">Region</th>
              <th scope="col">Cities covered</th>
            </tr>
          </thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split split--media">
        <div>
          <h2>Check a specific ZIP code</h2>
          <p>Faster than scanning the list. Enter the ZIP of the facility you need cleaned and we'll
            tell you whether it's on an existing route.</p>
        </div>
        <div class="zip-panel">
          <h3>ZIP lookup</h3>
          <form class="zip-form" data-zip-form novalidate>
            <label class="visually-hidden" for="zip-areas">ZIP code</label>
            <input id="zip-areas" name="zip" type="text" inputmode="numeric" maxlength="5"
                   pattern="[0-9]{{5}}" placeholder="30071" autocomplete="postal-code">
            <button type="submit">Check</button>
          </form>
          <p class="zip-result" data-zip-result role="status"></p>
        </div>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("service-areas.html",
           "Service Areas | TKB Ventures — Commercial Cleaning near Norcross, GA",
           "TKB Ventures services commercial facilities within roughly 100 miles of Norcross, "
           "Georgia, across the Atlanta metro and out to Athens, Rome, and Macon.",
           areas, "service-areas.html")

    # -------------------------------------------------------------- FAQ
    left = accordion(FAQ_ALL[:5], "faq-left")
    right = accordion(FAQ_ALL[5:], "faq-right")

    faq = page_hero(
        "Frequently asked questions",
        "Insurance, scheduling, quality control, and how the Jani-King franchise relationship "
        "actually works.", "FAQ") + f"""

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
{left}
        </div>
        <div>
{right}
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt section--tight">
    <div class="wrap">
      <div class="split split--media">
        <div>
          <h2>Still unanswered?</h2>
          <p>Ask directly. Questions about a specific building are usually faster on the phone than
            over email.</p>
        </div>
        <div class="btn-row">
          <a class="btn btn--primary" href="contact.html">Contact us</a>
          <a class="btn btn--ghost" href="tel:{PHONE_HREF}">Call {PHONE}</a>
        </div>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("faq.html",
           "FAQ | TKB Ventures — Jani-King of Atlanta",
           "Answers on insurance and bonding, custom schedules, green cleaning, crew background "
           "checks, emergency cleaning, and floor care from TKB Ventures in Norcross, GA.",
           faq, "faq.html")

    # ---------------------------------------------------------- CONTACT
    contact = page_hero(
        "Talk to TKB Ventures",
        "Request a walk-through, send a bid package, or just ask a question about your building.",
        "Contact") + f"""

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Get in touch</h2>
          <dl class="contact-list">
            <div>
              <dt>Phone</dt>
              <dd><a href="tel:{PHONE_HREF}">{PHONE}</a></dd>
            </div>
            <div>
              <dt>Email</dt>
              <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
            </div>
            <div>
              <dt>Office</dt>
              <dd class="normal">{ADDR1}<br>{ADDR2}</dd>
            </div>
            <div>
              <dt>Office hours</dt>
              <dd class="normal">Monday to Friday, 8:00am to 5:00pm ET<br>
                After-hours messages returned the next business morning.</dd>
            </div>
            <div>
              <dt>Service hours</dt>
              <dd class="normal">Crews run days, nights, and weekends depending on your scope.</dd>
            </div>
          </dl>
        </div>

        <div class="form-card">
          <div class="tabs" data-tabs role="tablist" aria-label="Inquiry type">
            <button class="tab" type="button" role="tab" id="tab-quote"
                    aria-controls="panel-quote" aria-selected="true">Request a quote</button>
            <button class="tab" type="button" role="tab" id="tab-rfp"
                    aria-controls="panel-rfp" aria-selected="false" tabindex="-1">Submit an RFP</button>
          </div>

          <div class="tabpanel" id="panel-quote" role="tabpanel" aria-labelledby="tab-quote">
            <form data-form="quote" novalidate>
              <div class="form-status" data-form-status role="status"></div>
              <div class="field-row">
                <div class="field">
                  <label for="q-name">Your name</label>
                  <input id="q-name" name="name" type="text" autocomplete="name" required>
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="q-business">Business name</label>
                  <input id="q-business" name="business" type="text" autocomplete="organization" required>
                  <span class="field__error"></span>
                </div>
              </div>
              <div class="field-row">
                <div class="field">
                  <label for="q-phone">Phone</label>
                  <input id="q-phone" name="phone" type="tel" autocomplete="tel" required>
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="q-email">Email</label>
                  <input id="q-email" name="email" type="email" autocomplete="email" required>
                  <span class="field__error"></span>
                </div>
              </div>
              <div class="field-row">
                <div class="field">
                  <label for="q-type">Facility type</label>
                  <select id="q-type" name="facility_type">
                    <option value="">Select one</option>
                    <option>Office / corporate suite</option>
                    <option>Healthcare / medical</option>
                    <option>School / childcare</option>
                    <option>Retail / shopping center</option>
                    <option>Industrial / manufacturing</option>
                    <option>Hospitality / event venue</option>
                    <option>Multi-family / residential</option>
                    <option>Other</option>
                  </select>
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="q-sqft">Approx. square footage</label>
                  <input id="q-sqft" name="square_footage" type="text" inputmode="numeric">
                  <span class="field__error"></span>
                </div>
              </div>
              <div class="field">
                <label for="q-frequency">Cleaning frequency needed</label>
                <select id="q-frequency" name="frequency">
                  <option value="">Select one</option>
                  <option>Daily</option>
                  <option>5 nights a week</option>
                  <option>3 nights a week</option>
                  <option>Weekly</option>
                  <option>Bi-weekly</option>
                  <option>Monthly or periodic</option>
                  <option>One-time / project</option>
                  <option>Not sure yet</option>
                </select>
                <span class="field__error"></span>
              </div>
              <div class="field">
                <label for="q-notes">Anything else <span class="hint">— optional</span></label>
                <textarea id="q-notes" name="notes" rows="4"></textarea>
              </div>
              <button class="btn btn--primary" type="submit">Send request</button>
            </form>
          </div>

          <div class="tabpanel" id="panel-rfp" role="tabpanel" aria-labelledby="tab-rfp" hidden>
            <form data-form="rfp-page" novalidate>
              <div class="form-status" data-form-status role="status"></div>
              <div class="field-row">
                <div class="field">
                  <label for="r-name">Your name</label>
                  <input id="r-name" name="name" type="text" autocomplete="name" required>
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="r-org">Organization</label>
                  <input id="r-org" name="organization" type="text" autocomplete="organization" required>
                  <span class="field__error"></span>
                </div>
              </div>
              <div class="field-row">
                <div class="field">
                  <label for="r-email">Email</label>
                  <input id="r-email" name="email" type="email" autocomplete="email" required>
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="r-phone">Phone <span class="hint">— optional</span></label>
                  <input id="r-phone" name="phone" type="tel" autocomplete="tel">
                  <span class="field__error"></span>
                </div>
              </div>
              <div class="field-row">
                <div class="field">
                  <label for="r-locations">Number of locations</label>
                  <input id="r-locations" name="locations" type="number" min="1" inputmode="numeric">
                  <span class="field__error"></span>
                </div>
                <div class="field">
                  <label for="r-due">Bid due date <span class="hint">— optional</span></label>
                  <input id="r-due" name="due_date" type="date">
                </div>
              </div>
              <div class="field">
                <label for="r-file">Bid documents <span class="hint">— PDF, DOCX or XLSX</span></label>
                <input id="r-file" name="documents" type="file"
                       accept=".pdf,.doc,.docx,.xls,.xlsx" multiple>
              </div>
              <div class="field">
                <label for="r-scope">Scope summary <span class="hint">— optional</span></label>
                <textarea id="r-scope" name="scope" rows="4"></textarea>
              </div>
              <button class="btn btn--primary" type="submit">Submit RFP</button>
              <p class="form-note">Large packages can also go straight to
                <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>"""

    render("contact.html",
           "Contact TKB Ventures | Jani-King of Atlanta, Norcross GA",
           "Request a cleaning quote or submit an RFP to TKB Ventures, LLC — 6190 Regency Parkway, "
           "Norcross, Georgia.",
           contact, "contact.html")

    # ------------------------------------------------------------ CAREERS
    careers = page_hero(
        "Work with TKB Ventures",
        "We hire cleaners, floor technicians, and supervisors across the Atlanta metro.",
        "Careers") + f"""

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>Open roles</h2>
          <p>Placeholder. List current openings here, or link to the application system TKB Ventures
            uses. Include shift, location, and pay range for each role.</p>
          <p>Until roles are posted, interested applicants can email
            <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>
        <div>
          <h2>What the job involves</h2>
          <p>Placeholder. Cover background check requirements, training, uniform and badge policy,
            typical shift windows, and whether transport to sites is provided.</p>
        </div>
      </div>
    </div>
  </section>

{CTA_BAND}"""

    render("careers.html", "Careers | TKB Ventures",
           "Cleaning, floor care, and supervisory roles with TKB Ventures in the Atlanta metro.",
           careers, "careers.html")

    # -------------------------------------------------------------- LEGAL
    for slug, title, heading in [
        ("privacy.html", "Privacy Policy | TKB Ventures", "Privacy policy"),
        ("terms.html", "Terms of Service | TKB Ventures", "Terms of service"),
    ]:
        body = page_hero(
            heading,
            "This page is a placeholder. Replace it with text reviewed by TKB Ventures' attorney.",
            heading) + f"""

  <section class="section">
    <div class="wrap">
      <div style="max-width: 70ch;">
        <h2>Placeholder</h2>
        <p>Do not publish this page as written. {heading} content should be drafted or reviewed by
          counsel and should reflect how TKB Ventures actually collects and handles information
          submitted through the quote and RFP forms on this site.</p>
        <p>Questions in the meantime: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </div>
    </div>
  </section>"""
        render(slug, title, "Placeholder page for TKB Ventures, LLC.", body, slug)
