"""Blog index plus long-form articles. These target informational queries and
exist to earn links and rankings that the service pages can then benefit from
through internal linking."""

from build import SITE, icon, render_faq, BUILD_DATE
from partials import sidebar, article_schema, page_hero, TEL, PHONE

ARTICLE_TEMPLATE = """<section class="page-hero">
  <div class="wrap">
    <div class="meta-row" style="justify-content:center">
      <span class="tag">%(category)s</span>
      <span class="date">Published %(date_display)s</span>
    </div>
    <h1>%(h1)s</h1>
    <p>%(standfirst)s</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="article-layout">
      <article class="prose">
%(body)s
        <div class="callout">
          <p><strong>Need this applied to your own situation?</strong> General guidance only goes so
          far. <a href="tel:%(tel)s">Call %(phone)s</a> or
          <a href="/contact/">book a consultation</a> and we will look at your actual numbers.</p>
        </div>
%(faq)s
      </article>
      %(sidebar)s
    </div>
  </div>
</section>
"""


def article(url, title, description, h1, standfirst, category, body, faqs=None,
            og_title=None, date_display="11 August 2026", published=BUILD_DATE):
    faqs = faqs or []
    html = ARTICLE_TEMPLATE % {
        "category": category, "date_display": date_display, "h1": h1,
        "standfirst": standfirst, "body": body,
        "faq": render_faq(faqs) if faqs else "",
        "sidebar": sidebar(), "tel": TEL, "phone": PHONE,
    }
    page = {
        "url": url, "nav": "blog", "priority": "0.7", "og_type": "article",
        "title": title, "og_title": og_title or h1, "description": description,
        "crumbs": [("Home", "/"), ("Blog", "/blog/"), (h1, url)],
        "schema": [article_schema(h1, description, url, published, published, category)],
        "body": html,
        "lastmod": published,
        # kept for the index listing
        "_card": {"title": h1, "url": url, "category": category, "date": date_display,
                  "excerpt": description},
    }
    if faqs:
        page["faqs"] = faqs
    return page


# ==========================================================================
# Article 1 — pillar
# ==========================================================================
A1_BODY = """
<p>Ask ten Indian business owners what their Chartered Accountant does and most will say some version
of "he files my returns". That is accurate and it undersells the role considerably. The filing is the
output. The work that determines what goes into it — and what it costs you — happens months earlier.</p>
<p>This article sets out what a CA actually does across the life of an Indian business, in the order
you are likely to need it.</p>

<h2>Before you start: choosing the structure</h2>
<p>The first decision is the entity. A proprietorship is cheap and simple, taxed in the owner's hands
at slab rates, with unlimited personal liability. A partnership adds partners and keeps the
unlimited liability. An LLP limits liability with a lighter compliance load than a company. A private
limited company is the most expensive to maintain — statutory audit every year regardless of
turnover — and the only structure institutional investors will realistically fund.</p>
<p>What makes this a CA question rather than a registration-agent question is that each option has
different tax consequences, different exit consequences, and different implications for how you can
take money out of the business. Converting later is possible but never free.</p>
<p>We have written a fuller comparison in
<a href="/blog/private-limited-company-vs-llp-in-india/">Private Limited vs LLP</a>.</p>

<h2>Getting registered — and not over-registered</h2>
<p>Beyond incorporation there is PAN and TAN, GST where you cross the threshold or supply
inter-state, Udyam registration for MSME benefits, IEC for imports and exports, professional tax in
some states, and DPIIT recognition if you qualify as a startup.</p>
<p>The instinct is to get everything. That is a mistake. A GST registration you did not need obliges
you to file returns every month for as long as it stays active — including nil returns, with late
fees if you miss them. Registrations should be taken deliberately, when they are needed or when the
benefit outweighs the ongoing obligation.</p>

<h2>Books that survive an assessment</h2>
<p>Book-keeping and accounting are not the same thing. Data entry produces a trial balance;
accounting produces records that can be defended. The test is whether any number can be traced back
to a document that an assessing officer would accept.</p>
<p>In practice that means: invoices in a proper series, input tax credit matched against GSTR-2B
rather than assumed, expenses supported by evidence and routed through the banking channel where the
law requires it, related-party transactions identified and disclosed, and cash transactions kept
within the limits the Income Tax Act prescribes. Businesses that treat this as clerical work pay for
it later in disallowed expenses and reversed credit.</p>

<h2>The compliance calendar</h2>
<p>This is the most visible part of the relationship, and the part most easily judged. A typical
private limited company's year includes:</p>
<div class="table-scroll">
<table>
  <caption>What a compliant Indian company files in a year</caption>
  <thead><tr><th>Frequency</th><th>Obligations</th></tr></thead>
  <tbody>
    <tr><td>Monthly</td><td>GSTR-1 and GSTR-3B, TDS deposit, payroll processing, book-keeping close</td></tr>
    <tr><td>Quarterly</td><td>TDS returns (24Q / 26Q / 27Q), advance tax instalments in June, September, December and March</td></tr>
    <tr><td>Annually</td><td>Statutory audit, tax audit where applicable, income tax return, GST annual return, AOC-4 and MGT-7 after the AGM, DIR-3 KYC, DPT-3</td></tr>
    <tr><td>Event-based</td><td>Director changes, share allotments, charge creation, registered office changes, INC-20A within 180 days of incorporation</td></tr>
  </tbody>
</table>
</div>
<p>None of this is intellectually difficult. All of it carries per-day consequences. The value a CA
adds here is not expertise so much as reliability — a calendar that runs without the founder holding
it in their head.</p>

<h2>Tax planning, properly understood</h2>
<p>Legitimate tax planning is unglamorous. It looks like this: comparing the old and new income tax
regimes on your actual figures rather than by rule of thumb; structuring director remuneration
sensibly between salary, interest and dividend; claiming depreciation and allowances you are
entitled to; timing capital expenditure to fall in the right year; deciding whether a presumptive
scheme genuinely suits your margins; and characterising each receipt under the correct head of
income.</p>
<p>What it does not look like is a scheme whose viability depends on the department not examining it.
The distinction matters most three years later, when an assessment is opened and the person who
recommended the position has to defend it.</p>

<h2>Audit — the underrated part</h2>
<p>Companies are audited annually regardless of turnover. Other entities cross into tax audit at
prescribed turnover thresholds. Most owners experience this as a cost and a deadline.</p>
<p>It is also the one occasion each year when somebody independent examines how cash, stock and
credit actually move through the business. A well-run audit produces a management letter identifying
where controls are weak. Reading that letter is optional. It is also where most of the money is.</p>

<h2>When the department writes to you</h2>
<p>Notices are routine, not catastrophic. The common ones: a mismatch between GSTR-1 and GSTR-3B; a
difference between credit claimed and credit available in GSTR-2B; an income tax query where the
return does not reconcile with Form 26AS or the Annual Information Statement; a TDS default flagged
on TRACES.</p>
<p>Nearly all are answerable with a clean reconciliation and a reply filed inside the window.
Proceedings are largely faceless, which means the written submission carries the case. What you want
from a CA at this point is a reply drafted properly and filed on time — and an honest read on whether
the position is worth defending or worth settling.</p>

<h2>Numbers that drive decisions</h2>
<p>Once compliance is stable, the same data answers better questions. Which product line makes money
after overheads are allocated honestly? How many days of cash remain at the current burn? Why has
the working capital cycle stretched by eleven days? Should the next expansion be funded by debt, by
equity, or by collecting receivables faster?</p>
<p>This is <a href="/services/virtual-cfo-services/">virtual CFO</a> territory — monthly MIS,
forecasting and unit economics. It is the point at which the relationship stops being a cost centre.</p>

<h2>Funding, valuation and diligence</h2>
<p>When you raise capital, your finance function is what gets examined. Investors run financial and
tax due diligence. Valuation reports are needed for pricing and for regulatory filings. Every
historic shortcut surfaces in the data room.</p>
<p>Companies with clean books close faster and on better terms. Not because the numbers are larger —
because nothing in them requires explaining.</p>

<h2>So what should you actually expect?</h2>
<p>A reasonable standard for the relationship:</p>
<ul>
  <li>You are told what is due <em>before</em> it is due, and asked for documents with time to spare.</li>
  <li>Filings are confirmed with acknowledgements you can keep.</li>
  <li>Fees are fixed and agreed up front, with government charges shown separately.</li>
  <li>A qualified professional — not only support staff — reviews your file.</li>
  <li>You are told when a position is weak, and when a past filing was wrong.</li>
  <li>Somebody picks up the phone when a notice arrives.</li>
</ul>
<p>If your current arrangement clears that bar, you are well served. If it does not, the cost of
changing is lower than the cost of staying — and it is almost always lower than the accumulated late
fees of a calendar nobody is running.</p>
"""

A1_FAQS = [
    ("Do I need a CA if my business is small?",
     "Not necessarily for everything — a small proprietorship with simple affairs can manage a lot "
     "itself. But even small businesses benefit from a professional at the decision points: choosing "
     "the structure, deciding whether to register for GST, choosing between presumptive and regular "
     "taxation, and responding to any notice. Those decisions have consequences that outlast the "
     "saving on fees."),
    ("What is the difference between a CA, a tax consultant and an accountant?",
     "A Chartered Accountant holds a statutory qualification from the Institute of Chartered "
     "Accountants of India and is the only one of the three who can sign a statutory audit report or "
     "a tax audit report. An accountant or book-keeper maintains records; a tax consultant may "
     "prepare and file returns. For anything requiring attestation, certification or representation "
     "at a technical level, the qualification matters."),
    ("How often should I speak to my CA?",
     "Monthly at minimum if you are GST-registered, because that cycle needs data from you anyway. "
     "Beyond routine filing, speak to them before decisions rather than after: taking a new premises "
     "in another state, hiring across a threshold, taking a loan, bringing in a partner, or making a "
     "large capital purchase. Advice sought before the transaction is worth several times the same "
     "advice sought after it."),
]

# ==========================================================================
# Article 2 — GST threshold
# ==========================================================================
A2_BODY = """
<p>"Do I need to register for GST?" is the single most common question we are asked by new
businesses, and the answer is more layered than the headline threshold suggests. Turnover is only one
of the triggers — several situations require registration from the first rupee.</p>

<h2>The turnover thresholds</h2>
<p>For businesses in normal category states, registration becomes compulsory once aggregate turnover
in a financial year exceeds broadly ₹40 lakh for suppliers of goods and ₹20 lakh for suppliers of
services. Special category states apply lower limits. Chandigarh is a normal category Union
Territory.</p>
<p>Two details in that sentence do most of the damage:</p>
<ul>
  <li><strong>"Aggregate turnover" is computed on the PAN, across India.</strong> If you run two
  businesses under the same PAN, their turnovers are added together. Exempt supplies, exports and
  inter-state supplies all count towards the aggregate, even though they may not attract tax
  themselves.</li>
  <li><strong>Goods and services are treated differently.</strong> A business supplying both is
  generally tested against the lower services limit — a point that catches out businesses that think
  of themselves as traders but bill a service component.</li>
</ul>

<h2>When registration is compulsory regardless of turnover</h2>
<p>The threshold is irrelevant if any of these apply:</p>
<ul>
  <li>You make <strong>inter-state taxable supplies of goods</strong>. One consignment across a state
  border can trigger registration.</li>
  <li>You sell through an <strong>e-commerce operator</strong> that is required to collect tax at
  source.</li>
  <li>You are liable to pay tax under <strong>reverse charge</strong>.</li>
  <li>You are a <strong>casual taxable person</strong> — for example exhibiting at a trade fair in
  another state — or a <strong>non-resident taxable person</strong>.</li>
  <li>You act as an <strong>agent</strong> supplying on behalf of another, or as an
  <strong>input service distributor</strong>.</li>
</ul>

<div class="callout">
  <p><strong>The tricity version of this problem.</strong> Chandigarh's GST state code is 04, Punjab's
  is 03, Haryana's is 06. A business in Sector 8C supplying goods to a customer in Mohali or Panchkula
  is making an inter-state supply — IGST, not CGST plus SGST — and if it holds stock across that
  border it may need a second registration. The distance is twenty minutes; the compliance position
  is entirely different.</p>
</div>

<h2>Should you register voluntarily?</h2>
<p>Voluntary registration below the threshold is allowed, and sometimes sensible. It makes sense if
your customers are businesses who want to claim credit on your invoices, if you buy substantial
inputs on which you would otherwise absorb the tax, or if you are about to cross the threshold
anyway.</p>
<p>It is a poor idea if you sell mainly to end consumers and have few input costs. Registration is a
permanent monthly obligation: returns are due whether or not you traded, and late fees apply to nil
returns exactly as they do to any other. Businesses register in optimism and then pay late fees for
years on a dormant GSTIN.</p>

<h2>What happens if you cross the threshold and do not register</h2>
<p>Liability does not wait for registration. Tax becomes payable from the date you were required to
be registered, with interest, and penalties apply for the failure. You also cannot claim input tax
credit for the unregistered period against that liability, so the cost lands entirely on your margin.
Monitoring turnover as it approaches the limit is far cheaper than reconstructing the position later.</p>

<h2>Documents you will need</h2>
<ul>
  <li>PAN of the business and of the proprietor, partners or directors</li>
  <li>Aadhaar of the authorised signatory, for e-KYC authentication</li>
  <li>Certificate of incorporation or partnership deed, as applicable</li>
  <li>Proof of the principal place of business — utility bill, rent agreement, owner's NOC</li>
  <li>Bank details: cancelled cheque or first page of a statement</li>
  <li>Photographs and the authorisation for the signatory</li>
</ul>
<p>Completing Aadhaar authentication materially speeds up approval. Without it, applications usually
go to physical verification of the premises.</p>

<h2>After registration: what you have signed up for</h2>
<p>Registration is the start of a monthly rhythm — GSTR-1 and GSTR-3B, or the quarterly QRMP route if
you are eligible, plus the annual return where applicable. Input tax credit has to be reconciled
against GSTR-2B every month, because credit that does not appear there is not available to you no
matter how genuine the invoice.</p>
<p>Full detail on the cycle is on our
<a href="/services/gst-registration-return-filing/">GST registration and return filing</a> page.</p>
"""

A2_FAQS = [
    ("What is the GST registration limit for services in India?",
     "Broadly ₹20 lakh of aggregate turnover in normal category states, with a lower limit in special "
     "category states. This is half the limit that applies to suppliers of goods, and a business "
     "supplying both goods and services is generally tested against the lower services limit."),
    ("Is GST registration compulsory for online sellers?",
     "If you sell through an e-commerce operator that is required to collect tax at source, "
     "registration is compulsory regardless of turnover. If you sell through your own website "
     "directly to customers, the ordinary threshold rules apply — but the moment you ship goods "
     "across a state border, the inter-state supply trigger comes into play."),
    ("Can I cancel a GST registration I no longer need?",
     "Yes. Apply for cancellation through the portal, file the final return, and settle any liability "
     "including reversal of credit on stock held. Simply stopping filing is not cancellation — late "
     "fees keep accruing on an active GSTIN, and the registration can be cancelled by the department "
     "in a way that causes problems if you later want to register again."),
    ("How long does GST registration take in Chandigarh?",
     "Where Aadhaar authentication is completed, registration is typically granted within a few "
     "working days. Where it is not completed, the application usually goes for physical verification "
     "of the premises, which extends the timeline. Unclear address proof is the most common reason "
     "for a query."),
]

# ==========================================================================
# Article 3 — Pvt Ltd vs LLP
# ==========================================================================
A3_BODY = """
<p>This decision gets made badly more often than any other in Indian business formation, usually on
the basis of what a friend did or what a registration website recommended. The two structures are
genuinely different, and the right answer depends almost entirely on one question: are you going to
raise outside capital?</p>

<h2>The short version</h2>
<div class="table-scroll">
<table>
  <caption>Private Limited company vs LLP at a glance</caption>
  <thead><tr><th></th><th>Private Limited Company</th><th>LLP</th></tr></thead>
  <tbody>
    <tr><td>Governing law</td><td>Companies Act, 2013</td><td>Limited Liability Partnership Act, 2008</td></tr>
    <tr><td>Owners are called</td><td>Shareholders; managed by directors</td><td>Partners; managed by designated partners</td></tr>
    <tr><td>Liability</td><td>Limited to unpaid share capital</td><td>Limited to agreed contribution</td></tr>
    <tr><td>External investment</td><td>Straightforward — investors subscribe to shares</td><td>Impractical — VCs do not invest in LLPs</td></tr>
    <tr><td>ESOPs</td><td>Possible</td><td>Not in the conventional sense</td></tr>
    <tr><td>Statutory audit</td><td>Every year, regardless of turnover</td><td>Only above prescribed turnover or contribution limits</td></tr>
    <tr><td>Annual ROC filings</td><td>AOC-4, MGT-7 / MGT-7A, ADT-1, DIR-3 KYC, DPT-3</td><td>Form 11 and Form 8</td></tr>
    <tr><td>Meetings</td><td>Board meetings and an AGM, with minutes</td><td>No statutory meeting requirement</td></tr>
    <tr><td>Ongoing cost</td><td>Higher</td><td>Lower</td></tr>
    <tr><td>Perception with large customers</td><td>Generally preferred</td><td>Accepted, occasionally questioned</td></tr>
  </tbody>
</table>
</div>

<h2>Choose a private limited company if…</h2>
<ul>
  <li><strong>You intend to raise external funding.</strong> This is close to decisive. Venture
  investors and most angels subscribe to equity shares; the instruments they use assume a company.
  Converting an LLP to a company mid-raise is possible but adds months at exactly the wrong time.</li>
  <li><strong>You want to give employees equity.</strong> ESOPs work in a company structure.</li>
  <li><strong>Your customers are large corporates or government bodies.</strong> Procurement teams
  are more comfortable with companies, and some tenders effectively require one.</li>
  <li><strong>There will be multiple founders with differing shareholdings that may change.</strong>
  Share transfers are cleaner than amending an LLP agreement each time.</li>
</ul>

<h2>Choose an LLP if…</h2>
<ul>
  <li><strong>It is a professional practice or a services firm</strong> with no plans for outside
  capital. This is what the structure was designed for.</li>
  <li><strong>It is a family business or a closely held venture</strong> where the partners are stable
  and the priority is limited liability without administrative overhead.</li>
  <li><strong>You want to hold assets or run a joint venture</strong> with limited compliance.</li>
  <li><strong>Annual running cost genuinely matters.</strong> No mandatory audit below the prescribed
  limits and two annual filings instead of a full secretarial calendar is a meaningful saving,
  year after year.</li>
</ul>

<div class="callout">
  <p><strong>The cost people forget.</strong> A private limited company must be audited every single
  year even if it did no business at all. Founders who incorporate a company "to look serious" and
  then trade at ₹5 lakh of revenue are paying a permanent fixed cost for an option they may never
  exercise. If funding is genuinely not on the roadmap, that money is better spent elsewhere.</p>
</div>

<h2>What about a One Person Company?</h2>
<p>An OPC gives a single founder corporate status and limited liability, with a nominee who steps in
on death or incapacity. It carries most of a company's compliance obligations, including audit. It
suits a solo founder who wants the corporate form and does not want a partner. If external funding is
in view, a private limited company with a co-founder or a nominal second shareholder is usually the
better starting point.</p>

<h2>Can you convert later?</h2>
<p>Yes — an LLP can be converted into a private limited company and vice versa, subject to
conditions. But conversion means fresh approvals, transfer of assets and contracts, new registrations
under GST and other laws, and potential tax consequences on the transfer itself. It is a project, not
a form. Choosing correctly at the start is materially cheaper.</p>

<h2>How we would decide it with you</h2>
<p>The conversation takes about half an hour and covers four things: whether outside capital is
realistically on the horizon in the next three years, who your customers will be, what liability the
business is genuinely exposed to, and what ongoing compliance cost you are prepared to carry. The
answer usually falls out of those four.</p>
<p>See <a href="/services/company-registration-chandigarh/">company and LLP registration</a> for
what each process involves, or <a href="/contact/">get in touch</a> to talk it through.</p>
"""

A3_FAQS = [
    ("Is an LLP cheaper to run than a private limited company?",
     "Yes, materially. An LLP has no mandatory audit below the prescribed turnover and contribution "
     "limits, files two annual returns rather than a full secretarial calendar, and has no statutory "
     "meeting requirements. Across several years the difference is significant for a small business."),
    ("Can an LLP raise venture capital funding?",
     "In practice, no. Venture investors subscribe to equity shares and use instruments that assume a "
     "company structure. If you expect to raise institutional capital, incorporate as a private "
     "limited company from the start rather than planning to convert mid-raise."),
    ("Can a private limited company be converted into an LLP?",
     "Conversion is possible in either direction subject to conditions, but it involves fresh "
     "approvals, transfer of assets and contracts, new registrations and potential tax consequences. "
     "Treat it as a last resort rather than a plan."),
    ("How many people are needed to start each?",
     "A private limited company needs at least two shareholders and two directors, with at least one "
     "director resident in India. An LLP needs at least two partners, of whom at least two are "
     "designated partners with at least one resident in India. A single founder who wants corporate "
     "form can consider a One Person Company."),
]

# ==========================================================================
# Article 4 — annual compliance checklist
# ==========================================================================
A4_BODY = """
<p>If you have incorporated a private limited company, this is the list of things that have to happen
every year whether or not the business trades. Almost all of the penalties companies pay are for
items on this list, and almost all of them are avoidable.</p>

<h2>Immediately after incorporation (first year only)</h2>
<ul>
  <li><strong>Open the bank account</strong> and have subscribers actually pay in their subscription
  money.</li>
  <li><strong>File INC-20A</strong> — the declaration of commencement of business — within 180 days
  of incorporation. This is the most commonly missed first-year filing, and the consequences include
  penalties and the risk of the company being struck off.</li>
  <li><strong>Appoint the first auditor</strong> within 30 days of incorporation and file Form
  ADT-1.</li>
  <li><strong>Issue share certificates</strong> and pay stamp duty on them within the prescribed
  period.</li>
  <li><strong>Hold the first board meeting</strong> within 30 days of incorporation.</li>
</ul>

<h2>Through the year</h2>
<ul>
  <li><strong>Board meetings</strong> — the minimum prescribed number, with the prescribed maximum
  gap between them, properly noticed and minuted.</li>
  <li><strong>Monthly and quarterly tax filings</strong> — GST returns, TDS deposit and quarterly TDS
  returns, advance tax in June, September, December and March.</li>
  <li><strong>Statutory registers</strong> maintained contemporaneously — members, directors,
  charges, related party contracts.</li>
</ul>

<h2>The annual cycle</h2>
<div class="table-scroll">
<table>
  <caption>Annual company compliance and ordinary due dates</caption>
  <thead><tr><th>Step</th><th>Ordinarily due</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Finalise books and prepare financial statements</td><td>After year end</td><td>Reconcile with GST returns and Form 26AS before closing</td></tr>
    <tr><td>Statutory audit</td><td>Before the AGM</td><td>Mandatory for every company regardless of turnover</td></tr>
    <tr><td>Tax audit, where applicable</td><td>Report ordinarily by 30 September</td><td>Triggered by turnover thresholds under section 44AB</td></tr>
    <tr><td>Annual General Meeting</td><td>Within six months of the year end</td><td>First AGM has a longer window</td></tr>
    <tr><td>Income tax return</td><td>31 October for audit cases</td><td>31 July where no audit applies</td></tr>
    <tr><td>AOC-4</td><td>Within 30 days of the AGM</td><td>Filing of the audited financial statements</td></tr>
    <tr><td>MGT-7 / MGT-7A</td><td>Within 60 days of the AGM</td><td>MGT-7A applies to small companies and OPCs</td></tr>
    <tr><td>ADT-1</td><td>Within 15 days of the AGM</td><td>Auditor appointment or reappointment</td></tr>
    <tr><td>DIR-3 KYC</td><td>30 September</td><td>Every individual holding a DIN, every year</td></tr>
    <tr><td>DPT-3</td><td>30 June</td><td>Return of deposits and exempted deposits</td></tr>
    <tr><td>MSME-1</td><td>30 April and 31 October</td><td>Where amounts are outstanding to MSME suppliers beyond the prescribed period</td></tr>
    <tr><td>GST annual return</td><td>31 December</td><td>With the reconciliation statement above the prescribed turnover</td></tr>
  </tbody>
</table>
</div>

<h2>Event-based filings</h2>
<p>These are not annual, but they are where companies most often fall behind, because the clock
starts on an event nobody logs:</p>
<ul>
  <li>Director appointment, resignation or change — DIR-12</li>
  <li>Allotment of shares — PAS-3</li>
  <li>Change of registered office — INC-22, and INC-23 where jurisdiction changes</li>
  <li>Increase in authorised capital — SH-7</li>
  <li>Creation, modification or satisfaction of a charge — CHG-1, CHG-4</li>
  <li>Alteration of the name, objects or articles</li>
</ul>

<div class="note">
  <p><strong>Why the dates in this table say "ordinarily".</strong> Statutory due dates are extended
  by the MCA and the CBDT with some regularity, and the applicable date can also depend on your
  company's specific circumstances. Treat this as a planning checklist and confirm the operative date
  before you rely on it.</p>
</div>

<h2>What non-compliance actually costs</h2>
<p>Additional fees for late ROC filings increase with the length of the delay, and several
underlying defaults carry penalties on the company and on its officers personally. Sustained failure
to file allows the Registrar to strike the company off, and directors of a company that has failed to
file for a continuous period can be disqualified — which affects every other directorship they
hold.</p>
<p>Restoration and condonation routes exist, but they cost multiples of what the filings would have.
The economics here are unusually clear.</p>

<h2>A simple way to stay ahead</h2>
<p>Keep a single calendar with every date above, work backwards two weeks from each, and assign an
owner to each item. If that owner is you, and you are also running the business, expect to miss
some. This is precisely the work we take on as an annual engagement — see
<a href="/services/roc-annual-compliance/">ROC and annual compliance</a>.</p>
"""

A4_FAQS = [
    ("What is the penalty for late filing of AOC-4 or MGT-7?",
     "Late filing attracts additional fees that increase with the length of the delay, and the "
     "underlying default can carry penalties on the company and on its officers in default "
     "personally. Because these are computed with reference to the period of delay, a filing missed "
     "for a year typically costs many times the original fee."),
    ("Does a company with no business activity still need to file?",
     "Yes. Every company must hold its meetings, have its accounts audited and complete its annual "
     "filings regardless of whether it traded. If the company is not going to operate, applying for "
     "dormant status or striking it off voluntarily is cheaper than years of nil compliance."),
    ("What is INC-20A and why does it matter so much?",
     "It is the declaration of commencement of business, filed within 180 days of incorporation once "
     "subscribers have paid in their subscription money. Companies that never file it cannot lawfully "
     "commence business or borrow, face penalties, and risk being struck off. It is the single most "
     "common first-year omission we are asked to remedy."),
]

# ==========================================================================
# Article 5 — choosing a CA
# ==========================================================================
A5_BODY = """
<p>Most businesses choose their Chartered Accountant on price, a referral, or proximity — and then
stay for a decade regardless of how it turns out. Given that this is the professional who signs your
audit report and defends your tax positions, it is worth a slightly more deliberate process.</p>

<h2>Start with what you actually need</h2>
<p>The requirements differ sharply, and a firm that is excellent at one may be indifferent at
another:</p>
<ul>
  <li><strong>Compliance-only</strong> — returns filed accurately and on time. Most small businesses
  need this and nothing more.</li>
  <li><strong>Compliance plus advisory</strong> — someone who will tell you what a decision costs
  before you make it.</li>
  <li><strong>Specialist work</strong> — transfer pricing, international taxation, valuation, FEMA,
  insolvency, litigation before tribunals. These need genuine depth, not general practice.</li>
  <li><strong>Finance function support</strong> — MIS, forecasting, controls. A different skill again,
  closer to management than to compliance.</li>
</ul>
<p>Be honest about which of these you need this year. Paying for advisory you never use is as
wasteful as buying compliance-only service when you needed advice.</p>

<h2>Questions worth asking before you engage</h2>
<ol>
  <li><strong>Who will actually do my work, and who reviews it?</strong> In many practices the
  qualified professional signs and articled staff execute. That is normal and fine — but you should
  know whether a CA has actually reviewed your file or only signed it.</li>
  <li><strong>What exactly is inside the annual fee?</strong> Get it in writing. Does it include GST
  returns? TDS returns? ROC filings? Replies to notices? The audit? Quotes that look different are
  usually covering different scopes.</li>
  <li><strong>How are deadlines tracked?</strong> Ask what happens two weeks before a due date. A
  practice that relies on you to remember will cost you late fees eventually.</li>
  <li><strong>What happens when a notice arrives?</strong> Is drafting a reply included, or billed
  separately? Will they represent you? This is the moment the relationship is genuinely tested.</li>
  <li><strong>Can you give me an example of advice you gave a client that they did not want to
  hear?</strong> The value of a professional is in the position they refuse to sign. A CA who has
  never had that conversation is not being careful with you either.</li>
  <li><strong>How do you handle a handover from my current accountant?</strong> A good answer
  involves reconciling the portals and telling you what is outstanding <em>before</em> taking
  responsibility.</li>
</ol>

<h2>Signals that should give you pause</h2>
<ul>
  <li>A fee that is far below everyone else's. Something is out of scope, or the work is going to
  someone unqualified.</li>
  <li>Assurance that a refund or a saving is guaranteed before anyone has looked at your records.</li>
  <li>Reluctance to put scope and fees in writing.</li>
  <li>Casual suggestions about cash transactions or expenses "we can add".</li>
  <li>Being unreachable in the two weeks before a major deadline — that is precisely when you will
  need them.</li>
</ul>

<h2>Does location still matter?</h2>
<p>Less than it did. Registrations, returns and audits run through government portals with digital
signatures, so a firm in another city can serve you perfectly well. Location matters for two things:
physical hearings and inspections, where a locally present firm can attend; and the simple fact that
some owners work better face to face.</p>
<p>If you are in the tricity, the practical advantage of a Chandigarh firm is representation — being
able to appear before the local income tax and GST authorities when a matter calls for it.</p>

<h2>Switching is easier than people assume</h2>
<p>Businesses stay in unsatisfactory arrangements because they imagine the handover is painful. In
practice it is a document request: the last two to three years of returns, financial statements, GST
filings and ROC records, plus portal access. A competent incoming firm reconciles those against the
portals, tells you plainly what is outstanding, and prices the clean-up before you commit.</p>
<p>The only genuinely awkward part is the conversation with the outgoing firm, and professional
practice has well-established conventions for it. Where a statutory auditor is being changed, there
are specific procedures to follow — your incoming firm will handle them.</p>

<div class="callout">
  <p><strong>A reasonable bar.</strong> You should be told what is due before it is due, given
  acknowledgements for every filing, quoted a fixed fee with government charges shown separately, and
  told plainly when a position is weak. If your current arrangement clears that, stay. If it does
  not, <a href="/contact/">talk to us</a>.</p>
</div>
"""

A5_FAQS = [
    ("How do I verify that someone is actually a Chartered Accountant?",
     "Ask for the ICAI membership number and the firm registration number, and verify them through "
     "the Institute of Chartered Accountants of India. Only a member in practice can sign a statutory "
     "audit report or a tax audit report, so if attestation is part of what you need, verification is "
     "worth the two minutes."),
    ("Can I change my CA in the middle of a financial year?",
     "Yes. Compliance work can be transferred at any point — the new firm takes over from the next "
     "due filing. Where a statutory auditor is being replaced mid-term there are specific procedures "
     "under the Companies Act, including intimation to the Registrar, which your incoming firm will "
     "handle."),
    ("What should a CA's fees include?",
     "Get the scope in writing. A typical annual engagement for a small company covers book-keeping "
     "review, GST returns, TDS returns, the income tax return, statutory audit and ROC filings. "
     "Notices, representation, registrations and special assignments are commonly billed separately — "
     "which is reasonable, provided it is stated up front rather than discovered later."),
]


ARTICLES = [
    article(
        url="/blog/what-does-a-chartered-accountant-do-for-a-business-in-india/",
        h1="What a Chartered Accountant actually does for an Indian business",
        title="What Does a CA Do for a Business in India? | Talk To CA",
        og_title="What a Chartered Accountant Does for an Indian Business",
        description=("A practical guide to how a Chartered Accountant helps an Indian business: "
                     "structure, registrations, the compliance calendar, tax planning, audit and MIS."),
        standfirst=("Beyond filing returns: the nine things a CA does across the life of an Indian "
                    "business, and the standard you should hold the relationship to."),
        category="Business advisory", body=A1_BODY, faqs=A1_FAQS),
    article(
        url="/blog/gst-registration-limit-in-india/",
        h1="GST registration limit in India: when you must register",
        title="GST Registration Limit in India — Thresholds Explained",
        og_title="GST Registration Limit in India Explained",
        description=("GST registration thresholds explained: turnover limits for goods and services, "
                     "when registration is compulsory regardless of turnover, and late registration."),
        standfirst=("Turnover is only one of the triggers. Several situations require GST "
                    "registration from the first rupee — including one that catches out almost every "
                    "tricity business."),
        category="GST", body=A2_BODY, faqs=A2_FAQS),
    article(
        url="/blog/private-limited-company-vs-llp-in-india/",
        h1="Private Limited company vs LLP: which should you register?",
        title="Private Limited vs LLP in India — Which to Choose | CA Guide",
        og_title="Private Limited Company vs LLP in India",
        description=("Private Limited company vs LLP in India compared: liability, audit requirements, "
                     "annual compliance cost and the ability to raise outside funding."),
        standfirst=("The structure decision hinges on one question more than any other — whether you "
                    "will raise outside capital. Here is how the rest of the comparison falls out."),
        category="Company law", body=A3_BODY, faqs=A3_FAQS),
    article(
        url="/blog/annual-compliance-checklist-private-limited-company/",
        h1="Annual compliance checklist for a Private Limited company",
        title="Private Limited Company Annual Compliance Checklist (India)",
        og_title="Annual Compliance Checklist — Private Limited Company",
        description=("Every annual filing a private limited company in India must complete: AOC-4, "
                     "MGT-7, ADT-1, DIR-3 KYC, DPT-3, MSME-1, INC-20A, audits and tax returns."),
        standfirst=("Everything a private limited company has to do each year, whether or not it "
                    "trades — and what the misses actually cost."),
        category="Company law", body=A4_BODY, faqs=A4_FAQS),
    article(
        url="/blog/how-to-choose-a-chartered-accountant-for-your-business/",
        h1="How to choose a Chartered Accountant for your business",
        title="How to Choose a CA for Your Business in India | Talk To CA",
        og_title="How to Choose a Chartered Accountant in India",
        description=("Six questions to ask before engaging a Chartered Accountant, the warning signs "
                     "worth walking away from, and how straightforward switching firms actually is."),
        standfirst=("This is the professional who signs your audit report and defends your tax "
                    "positions. Six questions worth asking before you engage one."),
        category="Business advisory", body=A5_BODY, faqs=A5_FAQS),
]


# ==========================================================================
# Blog index
# ==========================================================================
def blog_index():
    cards = []
    for a in ARTICLES:
        c = a["_card"]
        cards.append("""<article class="card">
        <div class="meta-row">
          <span class="tag">%s</span><span class="date">%s</span>
        </div>
        <h3><a href="%s">%s</a></h3>
        <p>%s</p>
        <a class="card-link" href="%s">Read the article %s</a>
      </article>""" % (c["category"], c["date"], c["url"], c["title"], c["excerpt"],
                       c["url"], icon("arrow")))

    return """<section class="page-hero">
  <div class="wrap">
    <h1>Insights &amp; Updates</h1>
    <p>Practical guidance on Indian taxation, GST, company law and running a compliant business —
    written by our team for business owners rather than for other accountants.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="grid g2">
      %s
    </div>
  </div>
</section>
<section class="section bg-white bordered-y">
  <div class="wrap narrow">
    <div class="prose">
      <h2>Official portals worth bookmarking</h2>
      <p>We link to primary sources rather than paraphrasing them. If you want to check something
      yourself, start here:</p>
      <ul>
        <li><a href="https://www.incometax.gov.in/iec/foportal/" rel="noopener nofollow">Income Tax
        Department e-filing portal</a> — returns, Form 26AS, the Annual Information Statement and
        e-proceedings.</li>
        <li><a href="https://www.gst.gov.in/" rel="noopener nofollow">GST portal</a> — registration,
        returns, GSTR-2B and notices.</li>
        <li><a href="https://www.mca.gov.in/" rel="noopener nofollow">Ministry of Corporate
        Affairs</a> — incorporation, ROC filings and company master data.</li>
        <li><a href="https://www.startupindia.gov.in/" rel="noopener nofollow">Startup India</a> —
        DPIIT recognition and scheme details.</li>
        <li><a href="https://udyamregistration.gov.in/" rel="noopener nofollow">Udyam
        Registration</a> — MSME registration.</li>
        <li><a href="https://www.icai.org/" rel="noopener nofollow">ICAI</a> — verify a Chartered
        Accountant's membership.</li>
      </ul>
      <div class="note">
        <p>Articles on this site are general in nature and reflect the position as we understand it
        at the time of writing. Statutory positions, thresholds and due dates change, and several are
        extended by notification during the year. Please <a href="/contact/">speak to us</a> before
        acting on anything here.</p>
      </div>
    </div>
  </div>
</section>""" % "\n      ".join(cards)


BLOG_INDEX = {
    "url": "/blog/", "nav": "blog", "priority": "0.7", "changefreq": "weekly",
    "title": "CA Insights — GST, Income Tax & Company Law Updates | Talk To CA",
    "og_title": "Insights & Updates from our Chartered Accountants",
    "description": ("Practical articles on GST, income tax, company registration and annual "
                    "compliance for Indian businesses, written by CA Anil K. Verma & Associates, "
                    "Chandigarh."),
    "crumbs": [("Home", "/"), ("Blog", "/blog/")],
    "schema": [{
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": SITE["domain"] + "/blog/#blog",
        "name": "Insights & Updates",
        "url": SITE["domain"] + "/blog/",
        "inLanguage": "en-IN",
        "publisher": {"@id": SITE["domain"] + "/#organization"},
        "blogPost": [{"@type": "BlogPosting", "headline": a["_card"]["title"],
                      "url": SITE["domain"] + a["url"]} for a in ARTICLES],
    }],
    "body": blog_index(),
}

PAGES = [BLOG_INDEX] + [{k: v for k, v in a.items() if k != "_card"} for a in ARTICLES]
