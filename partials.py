"""Reusable HTML blocks shared by the page modules."""

from build import SITE, icon

TEL = SITE["phone_tel"]
PHONE = SITE["phone_display"]
EMAIL = SITE["email"]
WHATSAPP = "https://wa.me/" + SITE["phone_tel"].lstrip("+")


def cta(heading, text, dark=False):
    return """<section class="section">
  <div class="wrap">
    <div class="cta-band%(dark)s">
      <h2>%(heading)s</h2>
      <p>%(text)s</p>
      <div class="btn-row center">
        <a class="btn btn-primary" href="tel:%(tel)s">%(pico)s Call %(phone)s</a>
        <a class="btn %(alt)s" href="/contact/">Book a consultation</a>
      </div>
    </div>
  </div>
</section>""" % {
        "dark": " dark" if dark else "",
        "heading": heading,
        "text": text,
        "tel": TEL,
        "phone": PHONE,
        "pico": icon("phone"),
        "alt": "btn-ghost" if dark else "btn-outline",
    }


def sidebar(extra=""):
    """Right-hand rail used on service and blog pages: contact card plus
    internal links, so every deep page passes authority back to the money pages."""
    return """<aside class="sidebar">
  <div class="side-card dark">
    <h3>Talk to a Chartered Accountant</h3>
    <p>Straight answers on your GST, income tax or company compliance question — no obligation.</p>
    <p><a class="btn btn-primary" href="tel:%(tel)s">%(pico)s %(phone)s</a></p>
    <p><a class="btn btn-ghost" href="%(wa)s" rel="noopener">WhatsApp us</a></p>
  </div>
  <div class="side-card">
    <h3>Popular services</h3>
    <ul>
      <li><a href="/services/company-registration-chandigarh/">Company &amp; LLP registration</a></li>
      <li><a href="/services/gst-registration-return-filing/">GST registration &amp; returns</a></li>
      <li><a href="/services/income-tax-return-filing/">Income tax return filing</a></li>
      <li><a href="/services/audit-and-assurance/">Audit &amp; assurance</a></li>
      <li><a href="/services/roc-annual-compliance/">ROC annual compliance</a></li>
      <li><a href="/services/virtual-cfo-services/">Virtual CFO</a></li>
    </ul>
  </div>
  <div class="side-card">
    <h3>Visit the office</h3>
    <p>%(street)s,<br>%(city)s %(pin)s</p>
    <p>%(hours)s</p>
    <p><a href="%(maps)s" rel="noopener">Get directions &rarr;</a></p>
  </div>
  %(extra)s
</aside>""" % {
        "tel": TEL, "phone": PHONE, "pico": icon("phone"), "wa": WHATSAPP,
        "street": SITE["street"], "city": SITE["locality"], "pin": SITE["postal"],
        "hours": SITE["hours"], "maps": SITE["maps"], "extra": extra,
    }


def service_schema(name, description, url, service_type):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": description,
        "serviceType": service_type,
        "url": SITE["domain"] + url,
        "provider": {"@id": SITE["domain"] + "/#organization"},
        "areaServed": [
            {"@type": "City", "name": "Chandigarh"},
            {"@type": "City", "name": "Mohali"},
            {"@type": "City", "name": "Panchkula"},
            {"@type": "Country", "name": "India"},
        ],
        "audience": {"@type": "BusinessAudience", "name": "Startups, SMEs and established businesses in India"},
    }


def article_schema(headline, description, url, published, modified, section):
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "url": SITE["domain"] + url,
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE["domain"] + url},
        "datePublished": published,
        "dateModified": modified,
        "articleSection": section,
        "inLanguage": "en-IN",
        "image": SITE["domain"] + "/assets/img/og-image.png",
        "author": {"@id": SITE["domain"] + "/#organization"},
        "publisher": {"@id": SITE["domain"] + "/#organization"},
    }


def page_hero(title, sub):
    return """<section class="page-hero">
  <div class="wrap">
    <h1>%s</h1>
    <p>%s</p>
  </div>
</section>""" % (title, sub)
