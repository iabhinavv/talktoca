#!/usr/bin/env python3
"""
Static site builder for talktoca.in (CA Anil K. Verma & Associates).

Why a builder: the site needs ~17 crawlable URLs that all share one header,
footer, schema block and meta-tag pattern. Keeping that in one place means the
NAP (name/address/phone), canonical URLs and JSON-LD can never drift between
pages -- which is exactly what local SEO punishes.

Usage:
    python3 build.py

Writes index.html, the page directories, sitemap.xml and robots.txt in place.
Page content lives in pages_core.py, pages_services.py and pages_blog.py.
"""

import json
import os
import shutil
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Single source of truth for business details. Change it here, not in the HTML.
# --------------------------------------------------------------------------
SITE = {
    "domain": "https://talktoca.in",
    "name": "CA Anil K. Verma & Associates",
    "short": "Talk To CA",
    "legal": "CA Anil K. Verma & Associates",
    "street": "SCO 118-19, 2nd Floor, Madhya Marg, Sector 8C",
    "locality": "Chandigarh",
    "region": "Chandigarh",
    "postal": "160009",
    "country": "IN",
    "lat": 30.7372444,
    "lng": 76.7948811,
    "phone_display": "+91 94171 21061",
    "phone_tel": "+919417121061",
    "landline_display": "0172 5061061",
    "landline_tel": "+911725061061",
    "email": "ca.akvandassociates@gmail.com",
    "maps": "https://maps.google.com/?cid=15734563851373770143",
    "maps_embed": (
        "https://maps.google.com/maps?q=SCO%20118-19%2C%202nd%20Floor%2C%20Madhya%20Marg"
        "%2C%20Sector%208C%2C%20Chandigarh&t=&z=15&ie=UTF8&iwloc=&output=embed"
    ),
    "hours": "Mon – Sat, 9:30 AM – 6:30 PM",
    "founded": "1998",
}

BUILD_DATE = date.today().isoformat()

NAV = [
    ("Home", "/", "home"),
    ("About", "/about/", "about"),
    ("Services", "/services/", "services"),
    ("CA in Chandigarh", "/chartered-accountant-in-chandigarh/", "local"),
    ("Blog", "/blog/", "blog"),
    ("Careers", "/careers/", "careers"),
    ("Contact", "/contact/", "contact"),
]

# --------------------------------------------------------------------------
# Inline SVG sprite. Beats an icon-font CDN: no extra request, no FOIT, and the
# icons stay crisp. Hand-drawn primitives, so there is no third-party licence.
# --------------------------------------------------------------------------
ICONS = {
    "check": '<polyline points="20 6 9 17 4 12"/>',
    "arrow": '<line x1="4" y1="12" x2="19" y2="12"/><polyline points="13 6 19 12 13 18"/>',
    "chev": '<polyline points="9 5 16 12 9 19"/>',
    "phone": '<path d="M6 3h4l2 5-2.5 1.5a12 12 0 0 0 5 5L16 12l5 2v4a2 2 0 0 1-2.2 2A17 17 0 0 1 4 5.2 2 2 0 0 1 6 3z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><polyline points="3 7 12 13 21 7"/>',
    "pin": '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "bulb": '<path d="M9.5 18h5"/><path d="M10.5 21h3"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5.9 1.2.9 1.9v.2h5.2v-.2c0-.7.3-1.4.9-1.9A6 6 0 0 0 12 3z"/>',
    "calc": ('<rect x="4" y="3" width="16" height="18" rx="2"/><line x1="7.5" y1="7" x2="16.5" y2="7"/>'
             '<line x1="8" y1="12" x2="8" y2="12"/><line x1="12" y1="12" x2="12" y2="12"/>'
             '<line x1="16" y1="12" x2="16" y2="12"/><line x1="8" y1="16" x2="8" y2="16"/>'
             '<line x1="12" y1="16" x2="12" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/>'),
    "scale": ('<line x1="12" y1="4" x2="12" y2="20"/><line x1="6.5" y1="20" x2="17.5" y2="20"/>'
              '<line x1="4.5" y1="8" x2="19.5" y2="8"/><path d="M4.5 8l-2.5 5.5h5z"/><path d="M19.5 8l-2.5 5.5h5z"/>'),
    "file": ('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/>'
             '<polyline points="14 3 14 8 19 8"/><line x1="9" y1="13.5" x2="15" y2="13.5"/>'
             '<line x1="9" y1="17" x2="15" y2="17"/>'),
    "case": ('<rect x="3" y="7" width="18" height="13" rx="2"/>'
             '<path d="M9 7V5.5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2V7"/><line x1="3" y1="12" x2="21" y2="12"/>'),
    "bank": ('<line x1="3" y1="21" x2="21" y2="21"/><polyline points="3 10 12 4 21 10"/>'
             '<line x1="6.5" y1="10" x2="6.5" y2="18"/><line x1="10" y1="10" x2="10" y2="18"/>'
             '<line x1="14" y1="10" x2="14" y2="18"/><line x1="17.5" y1="10" x2="17.5" y2="18"/>'),
    "shield": '<path d="M12 3l7.5 3v6c0 4.6-3.2 8-7.5 9-4.3-1-7.5-4.4-7.5-9V6z"/><polyline points="9 12 11.2 14.2 15.3 10"/>',
    "users": ('<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/>'
              '<path d="M16 5.4a3.2 3.2 0 0 1 0 5.9"/><path d="M17.4 14.3A6 6 0 0 1 21 20"/>'),
    "trend": '<polyline points="3 17 9 11 13 15 21 7"/><polyline points="15.5 7 21 7 21 12.5"/>',
    "award": '<circle cx="12" cy="9" r="5.5"/><polyline points="8.5 13.5 7 21 12 18.4 17 21 15.5 13.5"/>',
    "clock": '<circle cx="12" cy="12" r="8.5"/><polyline points="12 7 12 12 15.5 14"/>',
    "rupee": '<path d="M7 5h10"/><path d="M7 9.2h10"/><path d="M13.5 5a4.2 4.2 0 0 1 0 8.4H7L14.5 21"/>',
    "menu": '<line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/>',
    "close": '<line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/>',
    "quote": '<path d="M9 6C6 7 4.5 9.5 4.5 13V18h6v-6H7.5c0-2.4.6-3.9 3-4.6z" fill="currentColor" stroke="none"/><path d="M18 6c-3 1-4.5 3.5-4.5 7V18h6v-6h-3c0-2.4.6-3.9 3-4.6z" fill="currentColor" stroke="none"/>',
}


def sprite():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" class="sr-only" aria-hidden="true" focusable="false"><defs>']
    for key, body in ICONS.items():
        parts.append('<symbol id="i-%s" viewBox="0 0 24 24">%s</symbol>' % (key, body))
    parts.append("</defs></svg>")
    return "".join(parts)


def icon(name, cls=""):
    c = ("ico " + cls).strip()
    return '<svg class="%s" aria-hidden="true"><use href="#i-%s"/></svg>' % (c, name)


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------
def organisation_schema():
    """AccountingService is the LocalBusiness subtype Google understands for a
    CA/accounting practice. Deliberately no aggregateRating/Review: rating
    markup must come from real, verifiable, on-page reviews or it risks a
    manual action."""
    return {
        "@context": "https://schema.org",
        "@type": ["AccountingService", "ProfessionalService"],
        "@id": SITE["domain"] + "/#organization",
        "name": SITE["name"],
        "alternateName": SITE["short"],
        "description": (
            "Chartered Accountant firm in Sector 8C, Chandigarh offering GST registration and "
            "return filing, income tax return filing, company and LLP incorporation, statutory "
            "and tax audit, ROC compliance and virtual CFO services across Chandigarh, Mohali "
            "and Panchkula."
        ),
        "url": SITE["domain"] + "/",
        "logo": {
            "@type": "ImageObject",
            "url": SITE["domain"] + "/assets/caakvlogo.png",
            "width": 500,
            "height": 500,
        },
        "image": SITE["domain"] + "/assets/img/og-image.png",
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "priceRange": "₹₹",
        "currenciesAccepted": "INR",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["locality"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["postal"],
            "addressCountry": "IN",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "hasMap": SITE["maps"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:30",
            "closes": "18:30",
        }],
        "areaServed": [
            {"@type": "City", "name": "Chandigarh"},
            {"@type": "City", "name": "Mohali"},
            {"@type": "City", "name": "Panchkula"},
            {"@type": "City", "name": "Zirakpur"},
            {"@type": "State", "name": "Punjab"},
            {"@type": "State", "name": "Haryana"},
            {"@type": "Country", "name": "India"},
        ],
        "knowsAbout": [
            "Goods and Services Tax", "Income Tax", "Statutory Audit", "Tax Audit",
            "Company Incorporation", "ROC Compliance", "TDS", "Virtual CFO", "Business Valuation",
        ],
        "sameAs": [SITE["maps"]],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Chartered Accountancy Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n,
                 "url": SITE["domain"] + u}}
                for n, u in [
                    ("Company & LLP Registration", "/services/company-registration-chandigarh/"),
                    ("GST Registration & Return Filing", "/services/gst-registration-return-filing/"),
                    ("Income Tax Return Filing", "/services/income-tax-return-filing/"),
                    ("Statutory, Tax & Internal Audit", "/services/audit-and-assurance/"),
                    ("ROC & Annual Company Compliance", "/services/roc-annual-compliance/"),
                    ("Virtual CFO Services", "/services/virtual-cfo-services/"),
                ]
            ],
        },
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITE["domain"] + "/#website",
        "url": SITE["domain"] + "/",
        "name": SITE["name"],
        "inLanguage": "en-IN",
        "publisher": {"@id": SITE["domain"] + "/#organization"},
    }


def breadcrumb_schema(crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": SITE["domain"] + url}
            for i, (name, url) in enumerate(crumbs)
        ],
    }


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


# --------------------------------------------------------------------------
# HTML fragments
# --------------------------------------------------------------------------
def render_faq(faqs):
    """Renders the visible FAQ. Answers here must match faq_schema() exactly --
    structured data has to reflect what a user can actually see on the page."""
    items = []
    for q, a in faqs:
        items.append(
            '<details><summary>%s</summary><div><p>%s</p></div></details>' % (q, a)
        )
    return ('<h2>Frequently asked questions</h2><div class="faq">%s</div>' % "".join(items))


def header_html(active):
    desktop = []
    mobile = []
    for label, url, key in NAV:
        cls = ' class="active" aria-current="page"' if key == active else ""
        desktop.append('<a href="%s"%s>%s</a>' % (url, cls, label))
        mobile.append('<a href="%s"%s>%s</a>' % (url, cls, label))
    return """<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="/">
      <img src="/assets/caakvlogo.png" width="52" height="52" alt="%(name)s logo" fetchpriority="high">
      <span class="brand-name">CA Anil K. Verma<span>&amp; Associates</span></span>
    </a>
    <nav class="nav" aria-label="Primary">
      %(desktop)s
      <a class="nav-cta" href="tel:%(tel)s">Talk To CA</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">%(menu)s</button>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
    <div class="wrap">
      %(mobile)s
      <a href="tel:%(tel)s">Call %(phone)s</a>
    </div>
  </nav>
</header>""" % {
        "name": SITE["name"],
        "desktop": "\n      ".join(desktop),
        "mobile": "\n      ".join(mobile),
        "tel": SITE["phone_tel"],
        "phone": SITE["phone_display"],
        "menu": icon("menu"),
    }


def footer_html():
    services = [
        ("Company &amp; LLP Registration", "/services/company-registration-chandigarh/"),
        ("GST Registration &amp; Returns", "/services/gst-registration-return-filing/"),
        ("Income Tax Return Filing", "/services/income-tax-return-filing/"),
        ("Audit &amp; Assurance", "/services/audit-and-assurance/"),
        ("ROC Annual Compliance", "/services/roc-annual-compliance/"),
        ("Virtual CFO Services", "/services/virtual-cfo-services/"),
    ]
    quick = [
        ("About the firm", "/about/"),
        ("All services", "/services/"),
        ("CA in Chandigarh", "/chartered-accountant-in-chandigarh/"),
        ("Blog &amp; updates", "/blog/"),
        ("Careers", "/careers/"),
        ("Contact us", "/contact/"),
    ]
    li = lambda items: "".join(
        '<li>%s<a href="%s">%s</a></li>' % (icon("chev"), u, t) for t, u in items
    )
    return """<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <div class="footer-brand">
        <img src="/assets/caakvlogo.png" width="44" height="44" alt="" loading="lazy">
        <span class="brand-name">CA Anil K. Verma<span>&amp; Associates</span></span>
      </div>
      <p>A Chandigarh-based Chartered Accountancy firm providing taxation, audit, incorporation
      and compliance services to startups, SMEs and established businesses across the tricity
      and the rest of India.</p>
      <p><a class="btn btn-primary" href="tel:%(tel)s">%(pico)s Talk To CA</a></p>
    </div>
    <div>
      <h2>Quick links</h2>
      <ul>%(quick)s</ul>
    </div>
    <div>
      <h2>Services</h2>
      <ul>%(services)s</ul>
    </div>
    <div>
      <h2>Contact</h2>
      <ul>
        <li>%(pin)s<span>%(name)s,<br>%(street)s,<br>%(city)s %(pin_code)s</span></li>
        <li>%(phone_i)s<span><a href="tel:%(tel)s">%(phone)s</a><br><a href="tel:%(ltel)s">%(landline)s</a></span></li>
        <li>%(mail)s<span><a href="mailto:%(email)s">%(email)s</a></span></li>
        <li>%(clock)s<span>%(hours)s</span></li>
      </ul>
    </div>
  </div>
  <div class="wrap">
    <div class="footer-bottom">
      <p>&copy; %(year)s %(name)s. All rights reserved.</p>
      <p>The content on this website is provided for general information only and does not
      constitute professional advice or a solicitation of work. Statutory positions change;
      please <a href="/contact/">speak to us</a> before acting on anything you read here.</p>
    </div>
  </div>
</footer>
<a class="call-fab" href="tel:%(tel)s">%(pico)s Call now</a>""" % {
        "quick": li(quick),
        "services": li(services),
        "name": SITE["name"],
        "street": SITE["street"],
        "city": SITE["locality"],
        "pin_code": SITE["postal"],
        "tel": SITE["phone_tel"],
        "ltel": SITE["landline_tel"],
        "phone": SITE["phone_display"],
        "landline": SITE["landline_display"],
        "email": SITE["email"],
        "hours": SITE["hours"],
        "year": date.today().year,
        "pin": icon("pin"),
        "phone_i": icon("phone"),
        "pico": icon("phone"),
        "mail": icon("mail"),
        "clock": icon("clock"),
    }


def crumbs_html(crumbs):
    if not crumbs or len(crumbs) < 2:
        return ""
    items = []
    for i, (name, url) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append('<li><span aria-current="page">%s</span></li>' % name)
        else:
            items.append('<li><a href="%s">%s</a></li>' % (url, name))
    return ('<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>%s</ol></div></nav>'
            % "".join(items))


# --------------------------------------------------------------------------
# Page renderer
# --------------------------------------------------------------------------
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="%(site_name)s">
<meta name="publisher" content="%(site_name)s">
<meta name="geo.region" content="IN-CH">
<meta name="geo.placename" content="Chandigarh">
<meta name="geo.position" content="%(lat)s;%(lng)s">
<meta name="ICBM" content="%(lat)s, %(lng)s">
<meta property="og:type" content="%(og_type)s">
<meta property="og:site_name" content="%(site_name)s">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="%(og_title)s">
<meta property="og:description" content="%(description)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(domain)s/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="%(site_name)s, Chartered Accountants, Chandigarh">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="%(og_title)s">
<meta name="twitter:description" content="%(description)s">
<meta name="twitter:image" content="%(domain)s/assets/img/og-image.png">
<meta name="theme-color" content="#003366">
<link rel="icon" href="/assets/img/favicon.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="/assets/caakvlogo.png">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">%(schema)s</script>
</head>
<body>
%(sprite)s
%(header)s
<main id="main">
%(crumbs)s
%(body)s
</main>
%(footer)s
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def render(page):
    url = SITE["domain"] + page["url"]
    schema = [organisation_schema(), website_schema()]
    if page.get("crumbs"):
        schema.append(breadcrumb_schema(page["crumbs"]))
    if page.get("faqs"):
        schema.append(faq_schema(page["faqs"]))
    schema.extend(page.get("schema", []))

    html = PAGE_TEMPLATE % {
        "title": page["title"],
        "description": page["description"].replace('"', "&quot;"),
        "og_title": page.get("og_title", page["title"]),
        "og_type": page.get("og_type", "website"),
        "url": url,
        "domain": SITE["domain"],
        "site_name": SITE["name"],
        "lat": SITE["lat"],
        "lng": SITE["lng"],
        "schema": json.dumps(schema, ensure_ascii=False, separators=(",", ":")),
        "sprite": sprite(),
        "header": header_html(page.get("nav", "")),
        "crumbs": crumbs_html(page.get("crumbs")),
        "body": page["body"],
        "footer": footer_html(),
    }

    out_dir = ROOT if page["url"] == "/" else os.path.join(ROOT, page["url"].strip("/"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    return len(html)


# --------------------------------------------------------------------------
# sitemap.xml / robots.txt
# --------------------------------------------------------------------------
def write_sitemap(pages):
    rows = []
    for p in pages:
        rows.append(
            "  <url>\n"
            "    <loc>%s%s</loc>\n"
            "    <lastmod>%s</lastmod>\n"
            "    <changefreq>%s</changefreq>\n"
            "    <priority>%s</priority>\n"
            "  </url>" % (
                SITE["domain"], p["url"], p.get("lastmod", BUILD_DATE),
                p.get("changefreq", "monthly"), p.get("priority", "0.7"),
            )
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)


def write_robots():
    txt = """# robots.txt for talktoca.in
User-agent: *
Allow: /

# Nothing on this site is private; the whole thing is meant to be indexed.
Disallow: /build.py
Disallow: /partials.py
Disallow: /pages_core.py
Disallow: /pages_services.py
Disallow: /pages_blog.py

Sitemap: %s/sitemap.xml
""" % SITE["domain"]
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)


def write_404():
    body = """<section class="page-hero">
  <div class="wrap">
    <h1>Page not found</h1>
    <p>The page you were looking for has moved or no longer exists.</p>
  </div>
</section>
<section class="section">
  <div class="wrap center">
    <p>Try one of these instead, or call us and we will point you to the right place.</p>
    <div class="btn-row center">
      <a class="btn btn-primary" href="/">Go to homepage</a>
      <a class="btn btn-outline" href="/services/">Browse services</a>
      <a class="btn btn-outline" href="tel:%s">Call %s</a>
    </div>
  </div>
</section>""" % (SITE["phone_tel"], SITE["phone_display"])
    page = {
        "url": "/404/", "title": "Page not found | " + SITE["name"],
        "description": ("The page you requested could not be found. Browse our Chartered Accountancy "
                        "services in Chandigarh or call the office on +91 94171 21061."),
        "body": body, "nav": "",
    }
    # 404 must sit at the web root as 404.html for GitHub Pages to serve it.
    render(page)
    shutil.move(os.path.join(ROOT, "404", "index.html"), os.path.join(ROOT, "404.html"))
    os.rmdir(os.path.join(ROOT, "404"))


def main():
    from pages_core import PAGES as core
    from pages_services import PAGES as services
    from pages_blog import PAGES as blog

    pages = core + services + blog
    seen = {}
    total = 0
    for p in pages:
        if p["url"] in seen:
            raise SystemExit("Duplicate URL: %s" % p["url"])
        seen[p["url"]] = True
        total += render(p)
        print("  %-58s %s" % (p["url"], p["title"][:60]))

    write_sitemap(pages)
    write_robots()
    write_404()

    # .nojekyll stops GitHub Pages running the files through Jekyll.
    open(os.path.join(ROOT, ".nojekyll"), "w").close()

    print("\n%d pages, %.0f KB of HTML, sitemap + robots.txt written." % (len(pages), total / 1024))


if __name__ == "__main__":
    main()
