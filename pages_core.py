"""Core pages: home, about, services hub, Chandigarh local page, contact, careers."""

from build import SITE, icon
from partials import cta, page_hero, TEL, PHONE, EMAIL, WHATSAPP

D = SITE["domain"]

# --------------------------------------------------------------------------
# Shared blocks
# --------------------------------------------------------------------------
SERVICE_CARDS = [
    ("bulb", "Company &amp; LLP Registration",
     "Private Limited, LLP, OPC and partnership registration through SPICe+ and FiLLiP, "
     "including PAN, TAN, bank account and Startup India (DPIIT) recognition.",
     "/services/company-registration-chandigarh/"),
    ("calc", "GST Registration &amp; Return Filing",
     "GST registration, monthly and quarterly GSTR-1 and GSTR-3B filing, input tax credit "
     "reconciliation, annual returns and departmental notices.",
     "/services/gst-registration-return-filing/"),
    ("rupee", "Income Tax Return Filing",
     "ITR filing for companies, LLPs, firms, professionals and salaried individuals, with "
     "advance tax planning and regime comparison before you file.",
     "/services/income-tax-return-filing/"),
    ("file", "Audit &amp; Assurance",
     "Statutory audit under the Companies Act, tax audit, internal audit, stock and "
     "management audits — carried out so the report stands up to scrutiny.",
     "/services/audit-and-assurance/"),
    ("scale", "ROC &amp; Annual Compliance",
     "AOC-4, MGT-7, DIR-3 KYC, DPT-3, MSME-1 and event-based filings, plus statutory "
     "registers and minutes maintained through the year.",
     "/services/roc-annual-compliance/"),
    ("case", "Virtual CFO Services",
     "Monthly MIS, cash-flow forecasting, budgeting, payroll oversight and investor "
     "reporting — senior finance capability without a full-time hire.",
     "/services/virtual-cfo-services/"),
]


def service_grid():
    cards = []
    for ico, title, desc, url in SERVICE_CARDS:
        cards.append("""<article class="card">
      <div class="icon-box">%s</div>
      <h3><a href="%s">%s</a></h3>
      <p>%s</p>
      <a class="card-link" href="%s">Learn more %s</a>
    </article>""" % (icon(ico), url, title, desc, url, icon("arrow")))
    return "\n    ".join(cards)


# --------------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------------
HOME_FAQS = [
    ("What does a Chartered Accountant do for a small business in India?",
     "A CA takes responsibility for the parts of your business that the law tests: choosing the "
     "right entity, registering it, keeping books that stand up to scrutiny, filing GST, TDS and "
     "income tax returns on time, signing off audits where they are required, and representing you "
     "if the department raises a query. In practice most owners come to us for the compliance "
     "calendar first and stay for the tax planning and the numbers that help them make decisions."),
    ("How much does a CA charge in Chandigarh?",
     "Fees depend on the entity type, turnover, number of transactions and how many registrations "
     "you hold. A proprietor filing one income tax return sits at one end of the range; a private "
     "limited company needing monthly GST, TDS, payroll, statutory audit and ROC filings sits at "
     "the other. We quote a fixed annual fee after a short call so there is no meter running, and "
     "we tell you in advance which government fees are payable separately."),
    ("Do I need to visit your office in Sector 8C?",
     "Not usually. Registrations, return filing and audits are handled digitally — documents by "
     "email or WhatsApp, DSC and e-signing done remotely. Clients across India work with us "
     "without ever visiting. If you are in Chandigarh, Mohali or Panchkula and would rather sit "
     "down with us, our office on Madhya Marg is open Monday to Saturday."),
    ("Can you take over from my current accountant or CA?",
     "Yes, and it is a routine handover. We take the last two to three years of returns, financial "
     "statements, GST filings and ROC records, reconcile them against the portals, tell you plainly "
     "what is outstanding, and then take over the calendar. Where earlier filings are missing or "
     "wrong we will say so and give you the cost of putting it right before you commit."),
    ("Which businesses do you work with?",
     "Startups and founders incorporating for the first time, established SMEs and manufacturers, "
     "traders and e-commerce sellers, professionals and consultancies, and NRIs with Indian income "
     "or property. Our work spans Chandigarh, Mohali, Panchkula and Zirakpur, and clients across "
     "the rest of India who work with us entirely online."),
]

HOME_BODY = """<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <p class="eyebrow-pill"><span class="dot"></span> Chartered Accountants &middot; Chandigarh</p>
        <h1>Chartered Accountants in Chandigarh <em>for growing Indian businesses</em></h1>
        <p class="lede">GST, income tax, company incorporation, audit and ROC compliance — handled
        end to end by a practising CA firm on Madhya Marg, Sector 8C. Serving Chandigarh, Mohali,
        Panchkula and clients across India.</p>
        <ul class="hero-points">
          <li>%(check)s <span>One firm for registration, filing, audit and advisory</span></li>
          <li>%(check)s <span>Fixed annual fees agreed before we start</span></li>
          <li>%(check)s <span>Deadlines tracked for you, not reminded to you</span></li>
        </ul>
        <div class="btn-row">
          <a class="btn btn-primary" href="tel:%(tel)s">%(phone_i)s Talk To CA</a>
          <a class="btn btn-ghost" href="/services/">Explore services</a>
        </div>
      </div>
      <div>
        <div class="stat-card">
          <div class="card-head">
            <div>
              <h2>Your compliance year</h2>
              <p class="muted">Recurring deadlines we track for clients</p>
            </div>
            <span class="badge-up">%(clock)s Always on</span>
          </div>
          <ul class="checklist">
            <li>%(check)s <span><strong>Monthly</strong> — GSTR-1 and GSTR-3B, TDS payment,
              payroll and book-keeping close</span></li>
            <li>%(check)s <span><strong>Quarterly</strong> — TDS returns (24Q / 26Q / 27Q) and
              advance tax instalments in June, September, December and March</span></li>
            <li>%(check)s <span><strong>Annually</strong> — income tax return, tax audit where
              applicable, GST annual return and ROC filings after the AGM</span></li>
            <li>%(check)s <span><strong>As they arise</strong> — notices, assessments, director
              changes, capital raises and registrations</span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Practice areas</p>
      <h2>Everything a compliant Indian business needs</h2>
      <p>Six core services covering the full life of a business — from the day you register it to
      the year you raise capital against it.</p>
    </div>
    <div class="grid g3">
    %(services)s
    </div>
    <p class="center" style="margin-top:2.5rem"><a class="btn btn-outline" href="/services/">See all services in detail %(arrow)s</a></p>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap">
    <div class="prose">
      <h2>How a Chartered Accountant helps an Indian business grow</h2>
      <p>Most Indian business owners meet a Chartered Accountant for the first time because
      something is due. A GST return, a notice, an audit, a bank asking for financials. That is a
      narrow use of a professional whose real value shows up earlier — in the decisions that set
      how much tax you will pay and how much scrutiny you will attract for years afterwards.</p>

      <h3>1. Choosing the right structure before you start trading</h3>
      <p>A sole proprietorship is cheap to run and taxed at slab rates in the owner's hands. An LLP
      limits liability with lighter annual compliance than a company. A private limited company
      costs more to maintain but is the only structure that institutional investors, and most
      large customers, will contract with comfortably. Getting this wrong is expensive to undo —
      converting later means fresh registrations, transfer of assets and, sometimes, tax on the
      transfer itself. This is a one-hour conversation that saves years of friction.</p>

      <h3>2. Getting the registrations right the first time</h3>
      <p>Beyond incorporation there is PAN and TAN, GST where you cross the threshold or sell
      inter-state, Udyam registration for MSME benefits, an Importer Exporter Code if you trade
      across borders, professional tax and shops-and-establishment registration in some states, and
      DPIIT recognition if you qualify as a startup. Each carries its own consequences: a GST
      registration you did not need still obliges you to file nil returns every month, and an
      unfiled nil return still attracts late fees.</p>

      <h3>3. Books that survive an assessment</h3>
      <p>Book-keeping is not data entry. The test of a set of books is whether an assessing officer,
      a GST officer or a lender can trace any number back to a document. That means invoices in the
      correct series, input tax credit matched against GSTR-2B rather than assumed, expenses backed
      by evidence and paid through the banking channel where the law requires it, and related-party
      transactions disclosed. Businesses that treat this as an afterthought pay for it later in
      disallowed expenses and blocked credit.</p>

      <h3>4. A compliance calendar that runs without you chasing it</h3>
      <p>GST returns are monthly or quarterly. TDS is deducted and deposited monthly, then reported
      quarterly. Advance tax falls due four times a year. Companies file AOC-4 and MGT-7 after the
      AGM, directors complete DIR-3 KYC annually, and specific events — allotting shares, changing
      directors, altering the registered office — carry their own forms and their own clocks. Late
      fees and interest here are entirely avoidable, which is why they are the most irritating
      money a business can spend.</p>

      <h3>5. Tax planning that is planning, not aggression</h3>
      <p>Legitimate planning is mostly unglamorous: choosing between the old and new income tax
      regime with the actual numbers in front of you, structuring director remuneration sensibly,
      claiming depreciation and allowances you are entitled to, timing capital expenditure,
      deciding whether a presumptive scheme genuinely suits you, and using the right head of income
      for each receipt. Done properly it is defensible in an assessment. Schemes that depend on
      the department not looking closely are not planning; they are deferred trouble.</p>

      <h3>6. Audit and independent assurance</h3>
      <p>Statutory audit under the Companies Act, tax audit where turnover crosses the prescribed
      limit, internal audits for larger operations and stock or process audits where inventory
      drives the business. Beyond the signature, a well-run audit is the one time each year someone
      independent examines your controls and tells you where cash, stock or credit is leaking.</p>

      <h3>7. Standing between you and the department</h3>
      <p>Notices arrive: mismatches between GSTR-3B and GSTR-2B, income tax queries under scrutiny
      or reassessment, TDS defaults, demands raised by the CPC. Most are answerable with the right
      reconciliation and a clear reply within the deadline. A CA drafts that reply, files it,
      appears where representation is needed, and escalates to appeal only when it is worth it.</p>

      <h3>8. The numbers that drive decisions</h3>
      <p>Once compliance is under control, the same data answers better questions. Which product
      line actually makes money after overheads? How many days of cash are left at the current burn?
      What does the working capital cycle look like against the industry? Should the next expansion
      be funded by debt, by equity or by fixing collections? This is the virtual CFO work — monthly
      MIS, forecasting, unit economics and board-ready reporting — and it is where a CA stops being
      a cost and starts being leverage.</p>

      <h3>9. Funding, valuation and diligence</h3>
      <p>When capital arrives, so does scrutiny. Investors run financial and tax due diligence,
      valuation reports are required for pricing and for regulatory filings, term sheets carry
      accounting implications, and every historic shortcut surfaces in the data room. Businesses
      that kept clean books close rounds faster and at better terms — not because the numbers are
      bigger, but because nothing in them needs explaining.</p>

      <div class="callout">
        <p><strong>The practical takeaway.</strong> Compliance is the floor, not the ceiling. If
        your CA only appears at filing season, you are paying for the least valuable half of the
        relationship. <a href="tel:%(tel)s">Call us on %(phone)s</a> and we will tell you plainly
        which of the above your business actually needs this year.</p>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap">
    <div class="split">
      <div>
        <h2>Why businesses across the tricity work with us</h2>
        <p>We combine the discipline of traditional practice with processes built for how
        businesses actually operate now — documents shared digitally, portals reconciled monthly
        rather than in March, and one point of contact who knows your file.</p>
        <ul class="checklist">
          <li>%(check)s <span>Client data handled confidentially, with access limited to the team on your file</span></li>
          <li>%(check)s <span>Proactive alerts before a deadline, not after a late fee</span></li>
          <li>%(check)s <span>A dedicated relationship manager for every engagement</span></li>
          <li>%(check)s <span>Transparent fees quoted up front, with government charges shown separately</span></li>
          <li>%(check)s <span>Direct access to a qualified CA, not only to support staff</span></li>
        </ul>
        <p style="margin-top:2rem"><a class="btn btn-blue" href="/about/">More about the firm %(arrow)s</a></p>
      </div>
      <div class="stats">
        <div class="stat"><div class="num">500+</div><div class="lbl">Clients served</div></div>
        <div class="stat"><div class="num">25+</div><div class="lbl">Years in practice</div></div>
        <div class="stat"><div class="num">6</div><div class="lbl">Core service lines</div></div>
        <div class="stat filled"><div class="num">Mon–Sat</div><div class="lbl">9:30 AM – 6:30 PM</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Who we work with</p>
      <h2>Built for the way Indian businesses are actually structured</h2>
    </div>
    <div class="grid g4">
      <article class="card">
        <div class="icon-box">%(bulb)s</div>
        <h3>Startups &amp; founders</h3>
        <p>Incorporation, founders' agreements, DPIIT recognition, ESOP accounting, cap-table
        support and the compliance base investors expect to see at diligence.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(bank)s</div>
        <h3>SMEs &amp; manufacturers</h3>
        <p>Monthly GST and TDS, payroll, stock and cost controls, statutory and tax audit, working
        capital documentation for bank limits and Udyam-linked benefits.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(case)s</div>
        <h3>Traders &amp; e-commerce</h3>
        <p>Multi-state GST positions, marketplace TCS reconciliation, input credit matching,
        e-way bill discipline and inventory accounting across warehouses.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(users)s</div>
        <h3>Professionals &amp; NRIs</h3>
        <p>Presumptive taxation for professionals, capital gains on property and securities,
        repatriation, DTAA relief, Form 15CA/CB and residential status planning.</p>
      </article>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Local presence</p>
      <h2>A CA firm in Sector 8C, serving the whole tricity</h2>
      <p>Our office sits on Madhya Marg in Sector 8C, Chandigarh — within easy reach of Sector 17,
      Industrial Area, Mohali and Panchkula.</p>
    </div>
    <ul class="link-grid">
      <li><a href="/chartered-accountant-in-chandigarh/">%(pin)s Chartered Accountant in Chandigarh</a></li>
      <li><a href="/services/gst-registration-return-filing/">%(calc)s GST consultant in Chandigarh</a></li>
      <li><a href="/services/company-registration-chandigarh/">%(bulb)s Company registration in Chandigarh</a></li>
      <li><a href="/services/income-tax-return-filing/">%(rupee)s Income tax filing in Chandigarh</a></li>
      <li><a href="/services/audit-and-assurance/">%(file)s Auditors in Chandigarh</a></li>
      <li><a href="/contact/">%(phone_i)s Visit or call the office</a></li>
    </ul>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Testimonials</p>
      <h2>What our clients say</h2>
    </div>
    <div class="grid g4">
      <div class="quote-card">
        <p>"CA Anil K. Verma &amp; Associates made our incorporation and first-year compliance
        completely hassle-free."</p>
        <div class="quote-who">Rahul Sharma</div>
        <div class="quote-role">Founder, technology startup</div>
      </div>
      <div class="quote-card">
        <p>"Their GST advice saved us a significant amount in avoidable penalties. Professional and
        responsive throughout."</p>
        <div class="quote-who">Priya Desai</div>
        <div class="quote-role">Director, e-commerce firm</div>
      </div>
      <div class="quote-card">
        <p>"Having them as our virtual CFO has changed how we manage cash flow month to month."</p>
        <div class="quote-who">Amit Patel</div>
        <div class="quote-role">CEO, manufacturing unit</div>
      </div>
      <div class="quote-card">
        <p>"They understand the modern Indian business landscape and explain things in plain
        language."</p>
        <div class="quote-who">Sneha Gupta</div>
        <div class="quote-role">Managing partner</div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap narrow">
    <div class="prose">
      %(faq)s
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# ABOUT
# --------------------------------------------------------------------------
ABOUT_BODY = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="prose">
        <h2>A practice built around answering, not deflecting</h2>
        <p>CA Anil K. Verma &amp; Associates is a Chartered Accountancy firm based on Madhya Marg in
        Sector 8C, Chandigarh. We advise startups, SMEs, professionals and established companies on
        taxation, audit, incorporation and corporate compliance — across Chandigarh, Mohali,
        Panchkula and, increasingly, wherever in India our clients happen to be.</p>
        <p>The firm was built on a straightforward observation: most business owners do not need
        more information about tax law. They need someone who will read their specific situation,
        say what it means in plain language, and then take responsibility for the filing. That is
        the standard we hold ourselves to on every engagement, whether it is a first-time
        proprietor's return or a group audit.</p>
        <p>Our team brings together Chartered Accountants, tax practitioners and compliance staff so
        that a client's GST position, income tax exposure and corporate filings are looked at as one
        picture rather than three separate jobs handed to three separate people.</p>
      </div>
      <div class="stats">
        <div class="stat"><div class="num">25+</div><div class="lbl">Years in practice</div></div>
        <div class="stat"><div class="num">500+</div><div class="lbl">Clients served</div></div>
        <div class="stat"><div class="num">Tricity</div><div class="lbl">Chandigarh · Mohali · Panchkula</div></div>
        <div class="stat filled"><div class="num">Pan-India</div><div class="lbl">Remote engagements</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">How we work</p>
      <h2>Four things we do differently</h2>
    </div>
    <div class="grid g4">
      <article class="card">
        <div class="icon-box">%(shield)s</div>
        <h3>We tell you the downside</h3>
        <p>If a position is aggressive, if a past filing is wrong, or if a plan will not survive
        scrutiny, you hear it from us before you commit — not after a notice arrives.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(clock)s</div>
        <h3>We own the calendar</h3>
        <p>Deadlines are tracked on our side. You get a document request ahead of time and a
        confirmation once the return is filed, with the acknowledgement on record.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(rupee)s</div>
        <h3>Fees are fixed and stated</h3>
        <p>An annual engagement fee agreed at the start, with statutory and government charges
        itemised separately so you always know what is professional fee and what is not.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(users)s</div>
        <h3>One person knows your file</h3>
        <p>A named relationship manager backed by a qualified CA. You do not re-explain your
        business every time you call, and nothing falls between desks.</p>
      </article>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">Core values</p>
      <h2>What the firm is built on</h2>
    </div>
    <div class="grid g3">
      <article class="card">
        <div class="icon-box">%(scale)s</div>
        <h3>Integrity</h3>
        <p>Independence and ethical standards are not negotiable in this profession. We decline
        work where we cannot act independently, and we say so.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(trend)s</div>
        <h3>Rigour</h3>
        <p>Accurate, timely and evidenced work. Every position we take is one we are prepared to
        defend in front of the department.</p>
      </article>
      <article class="card">
        <div class="icon-box">%(users)s</div>
        <h3>Clarity</h3>
        <p>Advice in language a business owner can act on, with the reasoning shown rather than
        hidden behind section numbers.</p>
      </article>
    </div>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap narrow">
    <div class="prose">
      <h2>Disciplines under one roof</h2>
      <p>Businesses rarely have a problem that is purely a tax problem. A funding round is a
      valuation question, a company law question and a tax question at the same time. A departmental
      notice about input credit is a GST question that begins in the purchase ledger. We staff
      engagements so those threads are handled together:</p>
      <ul>
        <li><strong>Direct taxation</strong> — corporate and personal income tax, TDS, advance tax,
        capital gains, assessments and appeals.</li>
        <li><strong>Indirect taxation</strong> — GST registration, returns, input credit
        reconciliation, refunds, audits and departmental representation.</li>
        <li><strong>Audit and assurance</strong> — statutory, tax, internal, stock and management
        audits.</li>
        <li><strong>Corporate law and secretarial</strong> — incorporation, ROC filings, registers,
        minutes, charges and event-based compliance.</li>
        <li><strong>Advisory</strong> — virtual CFO, business valuation, due diligence, restructuring
        and funding support.</li>
      </ul>
      <p>If you are weighing up whether to move your work to us, the fastest way to judge the fit is
      a short call about a live problem. <a href="/contact/">Get in touch</a> — there is no charge
      for the first conversation.</p>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# SERVICES HUB
# --------------------------------------------------------------------------
SERVICES_BODY = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="prose" style="max-width:none">
      <p>We work across the full compliance and advisory cycle of an Indian business: registering
      the entity, keeping it filed and audited, defending it when the department asks questions,
      and giving the owners numbers they can plan with. Each service below has its own page with
      scope, documents required, timelines and answers to the questions clients ask most.</p>
    </div>
    <div class="grid g3" style="margin-top:2.5rem">
    %(services)s
    </div>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap narrow">
    <div class="prose">
      <h2>Also handled by the firm</h2>
      <p>Alongside the six core service lines, our team regularly takes on the following work.
      If what you need is not listed, ask — it is usually adjacent to something we already do.</p>
      <div class="table-scroll">
      <table>
        <caption>Additional engagements</caption>
        <thead><tr><th>Area</th><th>What it covers</th></tr></thead>
        <tbody>
          <tr><td>TDS &amp; TCS compliance</td><td>Monthly deposits, quarterly 24Q / 26Q / 27Q returns, Form 16 and 16A issuance, correction statements and default resolution on TRACES.</td></tr>
          <tr><td>Payroll &amp; labour compliance</td><td>Salary processing, TDS on salary, PF and ESI computation and returns, professional tax where applicable.</td></tr>
          <tr><td>Trademark &amp; IP registration</td><td>Trademark search, class selection, filing, objection replies and renewal tracking; copyright registration support.</td></tr>
          <tr><td>FEMA, RBI &amp; NRI matters</td><td>FDI reporting, Form FC-GPR, Form 15CA/CB certification for foreign remittances, repatriation and DTAA positions.</td></tr>
          <tr><td>Business valuation</td><td>Valuation reports for funding rounds, share transfers, regulatory filings and internal decision-making.</td></tr>
          <tr><td>Due diligence</td><td>Financial and tax due diligence for acquirers, investors and lenders, and sell-side readiness reviews.</td></tr>
          <tr><td>Project reports &amp; bank finance</td><td>CMA data, projections and documentation for working capital limits, term loans and government scheme applications.</td></tr>
          <tr><td>Notices, assessments &amp; appeals</td><td>Drafting replies, e-proceedings, representation before income tax and GST authorities, and appeals where warranted.</td></tr>
        </tbody>
      </table>
      </div>
    </div>
  </div>
</section>

<section class="section bg-light">
  <div class="wrap narrow">
    <div class="prose">
      %(faq)s
    </div>
  </div>
</section>
"""

SERVICES_FAQS = [
    ("Can I engage you for a single filing rather than an annual retainer?",
     "Yes. One-off work is common — a single income tax return, a company incorporation, a GST "
     "registration or a reply to a notice. We quote it as a standalone job. Most clients who start "
     "with one-off work move to an annual engagement once they see how much of the calendar they "
     "were carrying themselves."),
    ("How quickly can you start?",
     "For registrations and one-off filings, usually within a day or two of receiving documents. "
     "For a full handover from another accountant we ask for a week to reconcile the portals and "
     "tell you where things actually stand before we take responsibility for them."),
    ("Do you work with clients outside Chandigarh?",
     "Regularly. Filings, registrations and audits are handled through government portals and "
     "digital signatures, so physical location rarely matters. We have clients across Punjab, "
     "Haryana, Himachal Pradesh, Delhi NCR and further afield who work with us entirely remotely."),
    ("What documents will you need from me to begin?",
     "It depends on the service, and each service page lists its own requirements. As a baseline we "
     "ask for PAN and Aadhaar of the proprietor, partners or directors, proof of business address, "
     "bank statements for the period, and access to any existing GST, income tax or MCA logins."),
]


# --------------------------------------------------------------------------
# LOCAL PAGE — Chandigarh
# --------------------------------------------------------------------------
LOCAL_FAQS = [
    ("Where is your CA office in Chandigarh?",
     "Our office is at SCO 118-19, 2nd Floor, Madhya Marg, Sector 8C, Chandigarh. Madhya Marg is "
     "the main arterial road through the city, so the office is straightforward to reach from "
     "Sector 17, the Industrial Area, Mohali and Panchkula. We are open Monday to Saturday, "
     "9:30 AM to 6:30 PM."),
    ("What is the GST state code for Chandigarh?",
     "Chandigarh's GST state code is 04, so every GSTIN registered in the Union Territory begins "
     "with those digits. Neighbouring codes matter for tricity businesses: Punjab is 03 and Haryana "
     "is 06. A supply from Chandigarh to Mohali is therefore an inter-state supply attracting IGST, "
     "even though the two are a short drive apart — a point that catches out a lot of new "
     "businesses operating across the tricity."),
    ("Which Registrar of Companies covers Chandigarh?",
     "Companies incorporated in Chandigarh and Punjab fall under the Registrar of Companies, "
     "Chandigarh. Incorporation and annual filings are made through the MCA portal, so the process "
     "is the same wherever you sit, but jurisdiction matters when there is correspondence, "
     "adjudication or a physical hearing."),
    ("Do you serve Mohali, Panchkula and Zirakpur as well?",
     "Yes. The tricity functions as one economy even though it spans three GST jurisdictions, and a "
     "large share of our work is for businesses in Mohali's IT City and industrial phases, "
     "Panchkula's industrial area, and Zirakpur. We handle the multi-state GST positions that come "
     "with operating across that boundary."),
    ("Can you handle a scrutiny notice or GST audit locally?",
     "Yes. We draft and file replies, handle e-proceedings, and appear before the income tax and GST "
     "authorities where representation is required. Being in Chandigarh means we can attend in "
     "person when a hearing calls for it rather than relying entirely on written submissions."),
]

LOCAL_BODY = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="article-layout">
      <div class="prose">
        <p>If you are looking for a <strong>Chartered Accountant in Chandigarh</strong>, the
        practical questions are usually the same: can they handle my GST and income tax filings
        without me chasing them, will they pick up the phone when a notice arrives, and do they
        understand the way business actually works in this city. This page sets out what our firm
        does, where we are, and who we typically work with in the tricity.</p>

        <h2>Our office on Madhya Marg</h2>
        <p>We practise from <strong>SCO 118-19, 2nd Floor, Madhya Marg, Sector 8C, Chandigarh</strong>.
        Madhya Marg runs through the centre of the city, which makes the office easy to reach from
        Sector 17, the Industrial Area in Phases I and II, and from the Mohali and Panchkula sides
        of the tricity. Chandigarh Junction railway station and ISBT-17 are both a short drive away,
        and Chandigarh International Airport is roughly half an hour out depending on traffic.</p>
        <p>Office hours are Monday to Saturday, 9:30 AM to 6:30 PM. Most work does not require a
        visit — documents move by email or WhatsApp and filings happen on the portals — but clients
        who prefer to sit across a table are welcome to.</p>

        <h2>Services we provide in Chandigarh</h2>
        <ul>
          <li><a href="/services/gst-registration-return-filing/">GST registration and return
            filing</a> — new registrations, monthly and quarterly returns, input credit
            reconciliation, annual returns and departmental notices.</li>
          <li><a href="/services/income-tax-return-filing/">Income tax return filing</a> — for
            companies, LLPs, firms, professionals, salaried individuals and NRIs, with advance tax
            planning through the year.</li>
          <li><a href="/services/company-registration-chandigarh/">Company and LLP registration</a>
            — Private Limited, LLP, OPC and partnership formation, including PAN, TAN and bank
            account opening.</li>
          <li><a href="/services/audit-and-assurance/">Audit and assurance</a> — statutory audit
            under the Companies Act, tax audit, internal and stock audits.</li>
          <li><a href="/services/roc-annual-compliance/">ROC and annual compliance</a> — AOC-4,
            MGT-7, DIR-3 KYC, DPT-3, MSME-1 and event-based filings.</li>
          <li><a href="/services/virtual-cfo-services/">Virtual CFO services</a> — monthly MIS,
            cash-flow forecasting, budgeting and investor reporting.</li>
        </ul>

        <h2>Why tricity businesses need multi-state GST advice</h2>
        <p>Chandigarh, Mohali and Panchkula operate as a single economy across three separate GST
        jurisdictions. Chandigarh carries state code 04, Punjab 03 and Haryana 06. A firm with its
        office in Sector 8C and a warehouse in Zirakpur is dealing with two registrations, and a
        supply between them is an inter-state supply attracting IGST rather than CGST and SGST.</p>
        <p>This trips up new businesses constantly. It affects where you need to register, which
        head of tax you charge, how e-way bills are generated for movements that take twenty
        minutes, and how input credit flows between locations. It is one of the more common reasons
        tricity businesses end up with a mismatch notice, and it is entirely avoidable with the
        structure set up correctly at the start.</p>

        <div class="callout">
          <p><strong>Working across the tricity?</strong> Before you take a second premises in
          another state, get the GST structure reviewed. Restructuring registrations after the fact
          is far more painful than planning them.
          <a href="tel:%(tel)s">Call %(phone)s</a>.</p>
        </div>

        <h2>The businesses we work with here</h2>
        <p>Chandigarh's business base is unusually mixed for a city its size, and the compliance
        profile differs sharply between them:</p>
        <ul>
          <li><strong>IT and services firms</strong> in the Chandigarh IT Park and Mohali's IT City —
          export of services, LUT filings for zero-rated supply, foreign inward remittance
          documentation, and TDS on contractor and consultant payments.</li>
          <li><strong>Manufacturers and traders</strong> in the Industrial Area Phases I and II and
          the Panchkula industrial belt — inventory accounting, input credit on capital goods,
          e-way bills, stock audits and working capital documentation for bank limits.</li>
          <li><strong>Professionals and consultancies</strong> — doctors, architects, lawyers and
          consultants weighing presumptive taxation against maintaining full books.</li>
          <li><strong>Retail and hospitality</strong> across the sectors and Zirakpur — composition
          scheme decisions, cash-handling discipline and turnover-linked audit thresholds.</li>
          <li><strong>NRIs with property or income in the region</strong> — residential status,
          capital gains on sale of property, TDS under section 195, repatriation and Form 15CA/CB.</li>
        </ul>

        <h2>Choosing a CA in Chandigarh: what to actually check</h2>
        <p>Fee quotes are the least useful basis for comparison, because they rarely cover the same
        scope. More telling questions:</p>
        <ul>
          <li><strong>Who signs and who does the work?</strong> Ask whether a qualified CA reviews
          your file or only signs at the end.</li>
          <li><strong>What is inside the annual fee?</strong> Nail down whether GST returns, TDS
          returns, ROC filings, notices and audit are included or billed separately.</li>
          <li><strong>How are deadlines tracked?</strong> A practice that relies on you to remember
          is one that will cost you late fees.</li>
          <li><strong>What happens when a notice arrives?</strong> Response drafting and
          representation are the moments the relationship is actually tested.</li>
          <li><strong>Will they tell you when you are wrong?</strong> The value of the professional
          is in the position they refuse to sign, not the one they will.</li>
        </ul>
        <p>We are happy to be asked all five. If the answers suit you, the next step is a short call
        about your live situation.</p>

        %(faq)s
      </div>
      %(sidebar)s
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------------
CONTACT_BODY = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Let's discuss your business</h2>
      <p>Whether you are incorporating a new company, dealing with a notice, or looking to move your
      compliance work to a firm that will actually run it — call, email or message us. The first
      conversation is free and we will tell you honestly whether we are the right fit.</p>
    </div>
    <div class="grid g3">
      <div class="contact-card">
        <div class="icon-round">%(pin)s</div>
        <h2>Office address</h2>
        <p>%(name)s<br>%(street)s<br>%(city)s %(postal)s<br>India</p>
        <p><a href="%(maps)s" rel="noopener">Get directions &rarr;</a></p>
      </div>
      <a class="contact-card" href="tel:%(tel)s">
        <div class="icon-round teal">%(phone_i)s</div>
        <h2>Call us</h2>
        <p><strong>%(phone)s</strong><br>%(landline)s<br>%(hours)s</p>
      </a>
      <a class="contact-card" href="mailto:%(email)s">
        <div class="icon-round">%(mail)s</div>
        <h2>Email us</h2>
        <p>%(email)s<br>We reply to enquiries within one working day.</p>
      </a>
    </div>
    <div class="btn-row center" style="margin-top:2.5rem">
      <a class="btn btn-primary" href="%(wa)s" rel="noopener">Message us on WhatsApp</a>
      <a class="btn btn-outline" href="mailto:%(email)s?subject=Consultation%%20request">Request a consultation</a>
    </div>
  </div>
</section>

<section class="section-sm">
  <div class="wrap">
    <div class="map-frame">
      <iframe src="%(embed)s" title="Map showing the office of %(name)s in Sector 8C, Chandigarh"
        loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

<section class="section bg-white bordered-y">
  <div class="wrap narrow">
    <div class="prose">
      <h2>Getting here</h2>
      <p>The office is on <strong>Madhya Marg in Sector 8C</strong>, the main arterial road running
      east to west through Chandigarh. Coming from Sector 17 or the ISBT, head north along Madhya
      Marg; from the Mohali side, Madhya Marg is reached via the Sector 8/9 stretch. Parking is
      available in the SCO block.</p>
      <h2>What to bring to a first meeting</h2>
      <p>Nothing is mandatory for an initial conversation. If you want the meeting to be productive
      rather than exploratory, bringing the following helps us give you specifics instead of
      generalities:</p>
      <ul>
        <li>PAN of the business and of the proprietor, partners or directors</li>
        <li>Last filed income tax return and financial statements, if any</li>
        <li>GST registration certificate and the last three months of returns, if registered</li>
        <li>Any notice or communication you have received from the department</li>
        <li>Bank statements for the current financial year</li>
      </ul>
      <h2>Office hours</h2>
      <p>%(hours)s. We are closed on Sundays and on public holidays. During peak filing periods —
      the weeks before the income tax and GST annual deadlines — we recommend calling ahead to fix
      a time rather than dropping in.</p>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# CAREERS
# --------------------------------------------------------------------------
CAREERS_BODY = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="article-layout">
      <div class="prose">
        <h2>Why build your career here</h2>
        <p>A Chandigarh practice with a mixed client base gives you something a large-firm silo
        usually does not: exposure to the whole picture. In a single quarter you might work on a
        startup incorporation, a manufacturer's stock audit, a GST mismatch reply and a virtual CFO
        pack for a growing services business. That range is how professional judgement is built.</p>
        <p>Whether you are a qualified Chartered Accountant looking for portfolio ownership or an
        article assistant starting out, you will work directly with clients rather than only with
        files, and you will be expected to form a view rather than just process paperwork.</p>

        <h2>Current openings</h2>
        <div class="job">
          <div class="job-head">
            <h3>Senior Tax Consultant — Direct Tax</h3>
            <span class="pill">Full-time</span>
          </div>
          <p class="job-meta">Chandigarh &middot; 3–5 years post-qualification experience</p>
          <p>Owning a portfolio of corporate and individual direct tax clients: return filing,
          advance tax, TDS compliance, drafting replies to notices and representation in
          assessments. Suits a qualified CA who wants client ownership early.</p>
          <p><a class="btn btn-outline" href="mailto:%(email)s?subject=Application%%20-%%20Senior%%20Tax%%20Consultant">Apply for this role</a></p>
        </div>
        <div class="job">
          <div class="job-head">
            <h3>Article Assistant — CA Intermediate cleared</h3>
            <span class="pill teal">Articleship</span>
          </div>
          <p class="job-meta">Chandigarh &middot; Stipend as per industry standards</p>
          <p>Rotation across taxation, audit and corporate compliance rather than three years on a
          single desk. You will attend client meetings, work on live audits, and be given
          responsibility as fast as you can take it.</p>
          <p><a class="btn btn-outline" href="mailto:%(email)s?subject=Application%%20-%%20Article%%20Assistant">Apply for this role</a></p>
        </div>

        <div class="note">
          <p><strong>No suitable role listed?</strong> Send your CV to
          <a href="mailto:%(email)s">%(email)s</a> with a short note on the area you want to build
          in. We keep applications on file and we do hire outside advertised roles.</p>
        </div>

        <h2>How to apply</h2>
        <p>Email your CV to <a href="mailto:%(email)s">%(email)s</a> with the role in the subject
        line. Include your ICAI registration or membership number where applicable, your availability,
        and one short paragraph on the kind of work you want to do. We read every application and
        reply to shortlisted candidates within two weeks.</p>
      </div>
      %(sidebar)s
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# Page definitions
# --------------------------------------------------------------------------
def build():
    from build import render_faq
    from partials import sidebar

    ic = {
        "check": icon("check"), "arrow": icon("arrow"), "clock": icon("clock"),
        "phone_i": icon("phone"), "mail": icon("mail"), "pin": icon("pin"),
        "bulb": icon("bulb"), "bank": icon("bank"), "case": icon("case"),
        "users": icon("users"), "calc": icon("calc"), "rupee": icon("rupee"),
        "file": icon("file"), "scale": icon("scale"), "shield": icon("shield"),
        "trend": icon("trend"), "quote": icon("quote"),
    }
    base = dict(ic, tel=TEL, phone=PHONE, email=EMAIL, wa=WHATSAPP)

    home = HOME_BODY % dict(base, services=service_grid(), faq=render_faq(HOME_FAQS))

    about = ABOUT_BODY % dict(base, hero=page_hero(
        "About CA Anil K. Verma &amp; Associates",
        "A Chandigarh Chartered Accountancy firm advising Indian businesses on tax, audit and compliance."))

    services = SERVICES_BODY % dict(
        base,
        hero=page_hero("Our Services",
                       "Taxation, audit, incorporation, compliance and CFO support for Indian businesses."),
        services=service_grid(), faq=render_faq(SERVICES_FAQS))

    local = LOCAL_BODY % dict(
        base,
        hero=page_hero("Chartered Accountant in Chandigarh",
                       "GST, income tax, audit and company compliance from our office on Madhya Marg, Sector 8C."),
        faq=render_faq(LOCAL_FAQS), sidebar=sidebar())

    contact = CONTACT_BODY % dict(
        base,
        hero=page_hero("Contact Us", "Speak to a Chartered Accountant in Chandigarh — call, email or WhatsApp."),
        name=SITE["name"], street=SITE["street"], city=SITE["locality"], postal=SITE["postal"],
        maps=SITE["maps"], embed=SITE["maps_embed"], landline=SITE["landline_display"],
        hours=SITE["hours"])

    careers = CAREERS_BODY % dict(
        base,
        hero=page_hero("Build Your Career With Us",
                       "Openings for qualified Chartered Accountants and article assistants in Chandigarh."),
        sidebar=sidebar())

    return [
        {
            "url": "/", "nav": "home", "priority": "1.0", "changefreq": "weekly",
            "title": "Chartered Accountant in Chandigarh | CA Anil K. Verma",
            "og_title": "Chartered Accountants in Chandigarh — GST, Tax, Audit & Compliance",
            "description": ("Chandigarh CA firm for GST registration and returns, income tax filing, "
                            "company registration, audit and ROC compliance. Call +91 94171 21061."),
            "faqs": HOME_FAQS, "body": home,
        },
        {
            "url": "/about/", "nav": "about", "priority": "0.6",
            "crumbs": [("Home", "/"), ("About", "/about/")],
            "title": "About Our CA Firm in Chandigarh | Talk To CA",
            "description": ("CA Anil K. Verma & Associates is a Chartered Accountancy firm in Sector 8C, "
                            "Chandigarh advising startups, SMEs and companies on tax, audit and "
                            "compliance."),
            "body": about,
        },
        {
            "url": "/services/", "nav": "services", "priority": "0.9", "changefreq": "monthly",
            "crumbs": [("Home", "/"), ("Services", "/services/")],
            "title": "CA Services in Chandigarh — GST, Income Tax, Audit & ROC",
            "description": ("Chartered Accountancy services in Chandigarh: GST returns, income tax "
                            "filing, company registration, statutory and tax audit, ROC compliance and "
                            "virtual CFO."),
            "faqs": SERVICES_FAQS, "body": services,
        },
        {
            "url": "/chartered-accountant-in-chandigarh/", "nav": "local", "priority": "0.9",
            "crumbs": [("Home", "/"), ("Chartered Accountant in Chandigarh",
                                       "/chartered-accountant-in-chandigarh/")],
            "title": "Chartered Accountant in Chandigarh — CA Firm in Sector 8C",
            "description": ("CA firm at SCO 118-19, Madhya Marg, Sector 8C, Chandigarh. GST, income tax, "
                            "audit, company registration and ROC compliance across the tricity."),
            "faqs": LOCAL_FAQS, "body": local,
        },
        {
            "url": "/contact/", "nav": "contact", "priority": "0.8",
            "crumbs": [("Home", "/"), ("Contact", "/contact/")],
            "title": "Contact Our CA Office in Chandigarh | Talk To CA",
            "description": ("Contact CA Anil K. Verma & Associates, SCO 118-19, 2nd Floor, Madhya Marg, "
                            "Sector 8C, Chandigarh. Call +91 94171 21061, Mon–Sat 9:30 AM – 6:30 PM."),
            "body": contact,
        },
        {
            "url": "/careers/", "nav": "careers", "priority": "0.4",
            "crumbs": [("Home", "/"), ("Careers", "/careers/")],
            "title": "CA Jobs & Articleship in Chandigarh | Careers",
            "description": ("Careers at CA Anil K. Verma & Associates, Chandigarh. Openings for a Senior "
                            "Tax Consultant (Direct Tax) and CA article assistants. Apply by email."),
            "body": careers,
        },
    ]


PAGES = build()
