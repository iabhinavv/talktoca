# talktoca.in — SEO setup and ranking guide

Everything below is specific to this site as it now stands. Work through Part 2 in
order; the steps build on each other.

---

## Part 0 — Verify before you publish

Nothing here is a blocker for the site working, but a CA's own website is held to a
higher standard than most. Please have someone in the firm confirm these:

| # | Item | Where | Why |
|---|------|-------|-----|
| 1 | **Postal code `160009`** | every page — footer and the JSON-LD `postalCode` | Used in the address schema Google reads. I inferred it for Sector 8C; confirm it matches your letterhead and Google Business Profile exactly. |
| 2 | **Testimonials** | — | Done: removed 29 Sep 2026 (ICAI does not permit testimonials). No `Review`/`AggregateRating` schema. |
| 3 | **"500+ clients", "25+ years"** | — | Done: removed 29 Sep 2026 along with the other superlatives and success claims. |
| 4 | **Statutory figures and dates** | service pages + blog | Listed individually in Part 5 below. |
| 5 | **Firm details** | footer, `/about/`, JSON-LD `sameAs` | FRN 019748N is in every footer; membership no. 097020 only on `/about/`. Add LinkedIn/Facebook URLs to `sameAs` when you have them. |

---

## Part 1 — What changed and why

**The old site could not rank.** It was a single `index.html` running React + Babel
compiled in the browser. Every "page" (About, Services, Blog, Contact) was the same
URL, `https://talktoca.in/`. That meant:

- One URL to index, so one page could rank, for one thing.
- Nothing to put in a sitemap.
- No meta description, no canonical, no Open Graph, no structured data.
- The word "Chandigarh" appeared nowhere in the title tag.
- All content rendered by JavaScript after a ~500 KB download of React, Babel,
  Tailwind and Font Awesome from three CDNs.

**Now:** 18 static HTML pages, each with its own URL, title, meta description,
canonical and structured data. No frameworks, no CDN calls — one hand-written 12 KB
stylesheet and 0.5 KB of JavaScript for the nav. All content is in the raw HTML, so
crawlers see it without executing anything.

### The URLs

| URL | Targets |
|---|---|
| `/` | chartered accountant in chandigarh, CA firm chandigarh |
| `/chartered-accountant-in-chandigarh/` | CA in chandigarh, CA near me, tricity |
| `/services/` | CA services chandigarh |
| `/services/company-registration-chandigarh/` | company registration chandigarh, pvt ltd registration |
| `/services/gst-registration-return-filing/` | GST consultant chandigarh, GST return filing |
| `/services/income-tax-return-filing/` | ITR filing chandigarh, income tax consultant |
| `/services/audit-and-assurance/` | auditors in chandigarh, tax audit, statutory audit |
| `/services/roc-annual-compliance/` | ROC filing, AOC-4, MGT-7, annual compliance |
| `/services/virtual-cfo-services/` | virtual CFO india, outsourced CFO |
| `/about/`, `/contact/`, `/careers/` | brand + local + recruitment |
| `/blog/` + 5 articles | informational queries — GST limit, Pvt Ltd vs LLP, compliance checklist, choosing a CA, what a CA does |

~17,700 words of content total, from ~600 before.

### Metadata on every page

Unique `<title>` (≤64 chars) and `meta description` (137–158 chars), canonical URL,
`robots` with `max-image-preview:large`, Open Graph + Twitter card with a 1200×630
share image, `geo.position` / `geo.placename` for local, and `theme-color`.

### Structured data (JSON-LD)

- **`AccountingService`** (a LocalBusiness subtype) on every page — name, address,
  phone, email, geo coordinates `30.7372444, 76.7948811`, opening hours, `areaServed`
  for Chandigarh/Mohali/Panchkula/Zirakpur, and a service catalogue.
- **`WebSite`**, **`BreadcrumbList`** on every inner page.
- **`Service`** on each service page, **`BlogPosting`** on each article,
  **`FAQPage`** on the 9 pages that carry FAQs.

Test it after deploying: <https://search.google.com/test/rich-results>

### Editing the site later

The site is plain HTML — no build step. Each page is a folder with an `index.html`
(`/about/` is `about/index.html`). Edit the file, commit, push; GitHub Pages serves it.

The header, footer and structured-data block are **copied into every page**, so some
changes have to be made in every file. Use your editor's "find in folder" / "replace
in folder" for these:

| Change | Where it appears |
|---|---|
| Phone, email, address, hours | Every page: header (`tel:` links), footer, and the `<script type="application/ld+json">` block near the top |
| Menu item | Every page: two `<nav>` blocks in the header (desktop and mobile) |
| Footer links or text | Every page: `<footer class="site-footer">` |
| FRN | Every page footer |
| Membership number | `about/index.html` only |
| Styling | `assets/css/style.css` only |

**Adding a new blog article** (quickest: copy an existing article folder):

1. Copy `blog/gst-notice-reply-guide/` to `blog/<new-slug>/`.
2. In the new `index.html`, change: `<title>`, `meta description`, `canonical`,
   `og:title`, `og:description`, `og:url`, `twitter:title`, `twitter:description`,
   the breadcrumb last item, the `<h1>`, the date, the body, and the FAQ.
3. In its JSON-LD block, update the `BlogPosting` (headline, description, url,
   dates), the last `BreadcrumbList` item, and the `FAQPage` questions — they must
   match the visible FAQ word for word. Remove `FAQPage` if the page has no FAQ.
4. Add a card for it to `blog/index.html` (copy an existing `<article class="card">`)
   and add it to the `blogPost` list in that page's JSON-LD.
5. Add a `<url>` entry to `sitemap.xml` with today's date in `<lastmod>`.

**When you edit an existing page,** update its `<lastmod>` in `sitemap.xml` (and
`dateModified` in the JSON-LD for articles) so Google knows it changed.

**Every January,** update the © year in the footer (find-and-replace `&copy; 2026` in every file).

Check a page's structured data after any JSON-LD edit:
<https://search.google.com/test/rich-results>

---

## Part 2 — Getting it live and listed on Google

### Step 1 — Deploy

The site is served by **GitHub Pages** (confirmed from the live response headers).
Push the contents of this folder to the repository that serves `talktoca.in`.

> **Do not delete the `CNAME` file** in that repo — it is what maps the custom domain.
> It isn't in this folder because this folder wasn't the git checkout.

`.nojekyll` is included so GitHub Pages serves the files as-is.

Confirm after deploy:

```bash
curl -sI https://talktoca.in/services/gst-registration-return-filing/ | head -1
curl -s https://talktoca.in/robots.txt
curl -s https://talktoca.in/sitemap.xml | head -5
```

### Step 2 — Google Search Console

1. Go to <https://search.google.com/search-console> and sign in.
2. **Add property → Domain** and enter `talktoca.in`. The Domain property covers
   `www`, non-`www`, http and https in one place — better than the URL-prefix option.
3. Google gives you a **TXT record**. Add it in your domain registrar's DNS panel
   (wherever `talktoca.in` is registered), then click Verify. DNS can take 15 minutes
   to a few hours.
   - If you can't reach DNS, use **URL prefix** with `https://talktoca.in/` instead
     and verify by HTML file upload — put the file they give you in this folder,
     redeploy, then verify.
4. **Sitemaps** (left menu) → enter `sitemap.xml` → Submit. It should read "Success"
   with 18 discovered URLs within a day.
5. **URL Inspection** (top bar) → paste `https://talktoca.in/` → **Request Indexing**.
   Repeat for your five most important pages:
   - `/chartered-accountant-in-chandigarh/`
   - `/services/gst-registration-return-filing/`
   - `/services/income-tax-return-filing/`
   - `/services/company-registration-chandigarh/`
   - `/services/`

   There's a daily quota, so spread the rest over the following days. The sitemap will
   pick up the remainder on its own.

**Expect 2–6 weeks before rankings move.** Indexing happens in days; ranking doesn't.

### Step 3 — Bing Webmaster Tools

<https://www.bing.com/webmasters> → Import from Google Search Console (one click,
carries the verification over) → submit the same sitemap. Bing also feeds ChatGPT
search and DuckDuckGo, so it's worth the five minutes.

### Step 4 — Google Business Profile (the biggest single win)

**Your listing already exists.** I found it while resolving the map link on your site:
"Anil K. Verma & Associates" at <https://maps.google.com/?cid=15734563851373770143>.

For "CA near me" and "chartered accountant in Chandigarh" searches, the map pack sits
above the organic results. Owning that listing matters more than anything else on this
list.

1. Search for the business on Google Maps → **Claim this business** → verify (usually
   postcard, sometimes phone or video).
2. Once verified, complete it fully:
   - **Category:** primary = *Chartered accountant*. Secondaries = *Tax consultant*,
     *Auditor*, *Business management consultant*, *Certified public accountant*.
   - **NAP must match this website character for character:** `SCO 118-19, 2nd Floor,
     Madhya Marg, Sector 8C, Chandigarh` and `+91 94171 21061`. Inconsistent NAP is
     the most common reason local listings underperform.
   - Hours: Mon–Sat 9:30 AM – 6:30 PM.
   - Website: `https://talktoca.in/`
   - **Services:** add each one and link it to the matching page URL.
   - Photos: office exterior with signage, reception, the team. Real photos, ~10+.
3. **Reviews.** This is the single strongest local ranking factor after proximity. Ask
   satisfied clients directly, with the short review link from your GBP dashboard.
   Reply to every review. Aim for a steady trickle, not 20 in one week.
4. **Google Posts** — a short update every couple of weeks (a deadline reminder, a new
   article). Low effort, keeps the listing active.

### Step 5 — Local citations

Consistent NAP across directories reinforces the local signal. Free and worth doing:

- JustDial, Sulekha, IndiaMART
- Yellow Pages India, TradeIndia
- ICAI member/firm listing
- Local Chandigarh business directories and the Chamber of Commerce
- Facebook Page and LinkedIn Company Page (also add them to `sameAs` in each page's JSON-LD once live)

Same name, same address format, same phone number, every time.

---

## Part 3 — What to do next to rank better

Ordered by return on effort.

### 1. Reviews on Google Business Profile
Highest impact, lowest cost. A firm with 40 reviews at 4.8 outranks a firm with 3
reviews at 5.0 in almost every tricity search. Build a habit: ask at the end of every
completed engagement.

### 2. Publish one article a month
The blog has five substantial articles; five is a start, not a moat. Topics with real
search demand that you can answer better than a content mill because you do the work:

- Documents required for GST registration in India
- How to reply to a GST notice (DRC-01A / ASMT-10)
- Presumptive taxation under 44AD and 44ADA: who should actually use it
- TDS rate chart and quarterly return due dates
- Section 8 company / NGO registration
- Trademark registration in Chandigarh: process and cost
- Advance tax calculation with a worked example
- ITR-U (updated return): when it's worth filing
- Company strike-off vs dormant status
- NRI selling property in India: TDS under section 195

Rule of thumb: 900+ words, answer the question in the first paragraph, one table, an
FAQ block, and internal links to the relevant service page.

### 3. Add real photographs
The site currently has one image — the logo. Photos of the office and team improve
conversion and let you fill `image` in the schema properly. The old site referenced an
`/img/` folder that **404s in production** (client logos and testimonial photos), which
is why those sections silently rendered empty. I removed the placeholder client-logo
strip; put real client logos back only with permission.

### 4. Earn a few genuine local links
Domain authority is what separates page 1 from page 3 for competitive terms:

- Chandigarh Chamber of Commerce & Industry membership listing
- Guest article or quote in a local business publication
- ICAI Chandigarh branch activities and event listings
- Sponsor or speak at a local startup / MSME event and get listed
- Alumni or association pages you're entitled to be on

Avoid paid link networks and directory blasts — they're the fastest way to a penalty.

### 5. Add a contact form
GitHub Pages can't process forms, but **Formspree** or **Web3Forms** give you a form
endpoint with a free tier and no backend. Phone and email work; a form captures the
people who won't call. Add it to `/contact/` and to the sidebar on service pages.

### 6. Consider a page per tricity city — carefully
`/chartered-accountant-in-mohali/` and `/chartered-accountant-in-panchkula/` can work,
**but only with genuinely different content** — different industrial areas, different
GST state codes, different ROC jurisdiction (Haryana companies register with RoC Delhi,
not Chandigarh). Near-duplicate city pages are classic doorway pages and Google
demotes them. If you can't write 800 genuinely different words, don't make the page —
the tricity section already on `/chartered-accountant-in-chandigarh/` does the job.

### 7. Track what's actually happening
- **Google Analytics 4** — paste the tag into the `<head>` of every page (replace-in-folder
  on `</head>` works).
- In Search Console, watch **Performance → Queries** monthly. The queries you're
  getting impressions for but few clicks tell you which titles to rewrite; the queries
  ranking 8–20 tell you which pages to expand.

### 8. Speed and Core Web Vitals
Already in good shape — no render-blocking third-party JS, one small CSS file, no
webfonts. Two remaining wins:
- Convert `caakvlogo.png` (84 KB for a 52px logo) to WebP or resize it to ~120px.
- The Google Maps iframe on `/contact/` is the heaviest thing on the site. It's
  `loading="lazy"` so it won't hurt LCP, but you could swap it for a static image that
  links to Maps if you want that page perfect.

Check yourself: <https://pagespeed.web.dev/> — run the mobile test, that's the one
Google uses.

### 9. Things NOT to do
- **Don't buy backlinks or directory packages.** Common pitch to Indian professional
  firms; it's the fastest route to a manual action.
- **Don't add review or rating schema** unless the reviews are real, verifiable and
  shown on the page.
- **Don't spin near-identical pages** for every keyword variation.
- **Don't use "best CA in Chandigarh" as a title tag.** Aside from ICAI's restrictions
  on claims of superiority, Google doesn't reward it.

---

## Part 4 — A note on ICAI advertising rules

ICAI amended its Code of Ethics and advertising guidelines at the 447th Council
meeting, with the relaxations effective from **1 April 2026** — CA firms may now
advertise and promote their services, including through websites, Google Business
Profile and social media, within the prescribed limits. So the work in this repo is on
the right side of the current position.

What remains restricted, and why I wrote the content the way I did:

- No claims of **superiority or comparison** with other firms ("best", "leading",
  "India's premier" — all removed).
- Claims of fact should be **substantiable** (hence the flag on the client and years
  figures).
- **Testimonials and endorsements** are still not permitted — the four on the homepage were
  removed on 29 Sep 2026 and replaced with a "common questions" block linking to articles.
- **Reviews and directories:** asking clients for reviews can read as solicitation, and
  reserved CA services (audit, tax audit) should not be listed on commercial aggregators
  such as JustDial or Sulekha. Confirm with the ICAI Ethical Standards Board before either.
- **"500+ clients" / "25+ years"** were removed. The ICAI FRN is in every page footer.

Since this is your profession and the guidance was recently revised, please confirm the
current position with the ICAI Ethical Standards Board or your branch before publishing.
I've kept the copy factual and descriptive so there is little to walk back either way.

---

## Part 5 — Statutory figures used in the content

Please have these verified by the firm before publishing. I kept specific numbers
deliberately sparse and used "the prescribed limit" wherever a threshold changes often,
but these appear explicitly:

| Figure / date | Where |
|---|---|
| GST threshold ₹40 lakh (goods) / ₹20 lakh (services), normal category states | GST service page, GST blog article |
| GST state codes — Chandigarh 04, Punjab 03, Haryana 06 | local page, GST service page, GST article |
| QRMP GSTR-3B due 22nd/24th by state group, Chandigarh in the 24th group | GST service page table |
| GSTR-1 11th, GSTR-3B 20th, IFF 13th, CMP-08 18th, GSTR-9/9C 31 December | GST service page table |
| Advance tax 15% / 45% / 75% / 100% on 15 Jun, 15 Sep, 15 Dec, 15 Mar | income tax page, blog |
| ITR due 31 July / 31 Oct / 30 Nov; belated 31 Dec; tax audit report 30 Sept | income tax page |
| TDS returns 31 Jul, 31 Oct, 31 Jan, 31 May | income tax page, blog |
| AOC-4 within 30 days of AGM; MGT-7 within 60; ADT-1 within 15 | ROC page, compliance checklist article |
| DIR-3 KYC once every three years by 30 June (from 31 Mar 2026); DPT-3 30 June; MSME-1 30 Apr and 31 Oct | ROC page, article |
| LLP Form 11 by 30 May; Form 8 by 30 October | ROC page, Pvt Ltd vs LLP article |
| INC-20A within 180 days of incorporation | incorporation page, checklist article |
| First auditor appointed within 30 days of incorporation | incorporation page, checklist |
| AGM within six months of financial year end | ROC page, checklist |
| Registrar of Companies, Chandigarh covers Punjab and Chandigarh | local page FAQ |
| Section 115BAC new regime is the default | income tax page |

Section 44AB, 44AD and 44ADA thresholds are referred to as "the prescribed limit"
throughout rather than quoted, given how often they move.

---

## Appendix — files

```
talktoca/
├── index.html             # homepage
├── about/ services/ blog/ careers/ contact/ chartered-accountant-in-chandigarh/
│                          # one index.html per page
├── assets/css/style.css   # the whole design system
├── assets/js/site.js      # mobile nav only, deferred
├── assets/img/            # og-image.png (1200×630), favicon.png (48×48)
├── assets/caakvlogo.png   # logo
├── sitemap.xml            # 24 URLs — update by hand when pages change
├── robots.txt
├── 404.html               # GitHub Pages serves this for missing URLs
└── .nojekyll              # tells GitHub Pages not to run Jekyll
```

The Python generator used to build these pages was removed on 29 Sep 2026; its last
committed version is in git history (commit 929c3f8) if ever needed.
