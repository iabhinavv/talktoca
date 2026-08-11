"""The six service pages. These are the commercial-intent landing pages -- each
targets a distinct keyword cluster and carries its own Service + FAQPage schema."""

from build import SITE, icon, render_faq
from partials import sidebar, service_schema, page_hero, TEL, PHONE, EMAIL

TEMPLATE = """%(hero)s
<section class="section">
  <div class="wrap">
    <div class="article-layout">
      <div class="prose">
%(body)s
        <div class="callout">
          <p><strong>%(cta_head)s</strong> %(cta_text)s
          <a href="tel:%(tel)s">Call %(phone)s</a> or
          <a href="mailto:%(email)s">email the office</a>.</p>
        </div>
%(faq)s
      </div>
      %(sidebar)s
    </div>
  </div>
</section>
"""


def service_page(url, title, description, h1, sub, body, faqs, schema_name, schema_type,
                 cta_head, cta_text, og_title=None):
    html = TEMPLATE % {
        "hero": page_hero(h1, sub),
        "body": body,
        "faq": render_faq(faqs),
        "sidebar": sidebar(),
        "tel": TEL, "phone": PHONE, "email": EMAIL,
        "cta_head": cta_head, "cta_text": cta_text,
    }
    return {
        "url": url, "nav": "services", "priority": "0.9",
        "title": title, "og_title": og_title or h1, "description": description,
        "crumbs": [("Home", "/"), ("Services", "/services/"), (h1, url)],
        "faqs": faqs,
        "schema": [service_schema(schema_name, description, url, schema_type)],
        "body": html,
    }


# ==========================================================================
# 1. Company & LLP registration
# ==========================================================================
INCORP_BODY = """
<p>Registering the business is the first decision with lasting tax consequences, and the one most
often made on the basis of what a friend did. We take founders through the structure that actually
fits their plans, then handle the filing end to end — name approval, incorporation, PAN, TAN, bank
account and the post-incorporation compliances that catch new companies out.</p>

<h2>Choosing between Private Limited, LLP, OPC and proprietorship</h2>
<p>There is no universally correct answer. The right structure depends on who is putting money in,
what liability you are exposed to, whether you intend to raise external capital, and how much annual
compliance you are willing to carry.</p>
<div class="table-scroll">
<table>
  <caption>Comparing the common Indian business structures</caption>
  <thead><tr><th>Structure</th><th>Best suited to</th><th>Liability</th><th>Annual compliance load</th></tr></thead>
  <tbody>
    <tr><td>Proprietorship</td><td>Single owner, low risk, testing an idea</td><td>Unlimited — personal assets exposed</td><td>Lightest: income tax return, GST if registered</td></tr>
    <tr><td>Partnership firm</td><td>Two or more owners, traditional trade</td><td>Unlimited and joint</td><td>Light: firm return, GST, partnership deed upkeep</td></tr>
    <tr><td>LLP</td><td>Professional services, family businesses, JVs</td><td>Limited to contribution</td><td>Moderate: LLP Form 8 and Form 11, income tax return</td></tr>
    <tr><td>One Person Company</td><td>Solo founder wanting corporate status</td><td>Limited</td><td>Moderate: ROC filings, audit, nominee requirement</td></tr>
    <tr><td>Private Limited</td><td>Startups raising capital, scaling businesses</td><td>Limited</td><td>Highest: statutory audit, AOC-4, MGT-7, board and general meetings</td></tr>
  </tbody>
</table>
</div>
<p>Two practical points founders underestimate. First, a private limited company must have its
accounts audited every year regardless of turnover — that cost is permanent from day one. Second,
converting later is not free: a proprietorship becoming a company means new registrations, transfer
of assets and potential tax on that transfer. It is worth an hour of thought now.</p>

<h2>What company registration involves</h2>
<p>Incorporation runs through the MCA portal on the SPICe+ form, which bundles several approvals
into one application:</p>
<ul>
  <li><strong>Digital Signature Certificates</strong> for each proposed director and subscriber.</li>
  <li><strong>SPICe+ Part A</strong> — name reservation. Two names can be proposed; we check them
  against existing companies and registered trademarks first, because a name that clashes with a
  live trademark gets rejected and costs you a resubmission.</li>
  <li><strong>SPICe+ Part B</strong> — the incorporation application itself, allotting DIN to
  directors who do not already hold one.</li>
  <li><strong>e-MoA (INC-33) and e-AoA (INC-34)</strong> — the memorandum and articles, with the
  objects clause drafted to cover what you actually intend to do, plus room to grow.</li>
  <li><strong>AGILE-PRO-S (INC-35)</strong> — linked application covering GSTIN, EPFO, ESIC,
  professional tax where applicable, and bank account opening.</li>
  <li><strong>PAN and TAN</strong>, issued along with the certificate of incorporation.</li>
</ul>

<h3>Documents you will need</h3>
<ul>
  <li>PAN and Aadhaar of every proposed director and subscriber</li>
  <li>Passport for any foreign national director, notarised or apostilled as required</li>
  <li>Recent bank statement, electricity bill or mobile bill as address proof for each director</li>
  <li>Passport-size photographs</li>
  <li>Proof of the registered office — a recent utility bill plus the owner's no-objection
  certificate, or the rent agreement where premises are leased</li>
</ul>

<h3>Typical timeline</h3>
<p>With complete documents, name approval usually comes through in one to three working days and
incorporation follows within roughly a week, subject to the Registrar's queries and current
processing volumes. The commonest cause of delay is not the department — it is address proof that
does not match, or a proposed name that was never checked against the trademark register.</p>

<div class="note">
  <p><strong>Do not miss INC-20A.</strong> A company with share capital must file the declaration of
  commencement of business within 180 days of incorporation, after the subscribers have actually
  paid in their subscription money. Missing it carries penalties and can lead to the company being
  struck off. It is the single most common first-year failure we are asked to fix.</p>
</div>

<h2>After incorporation: what year one actually requires</h2>
<ul>
  <li>Opening the bank account and bringing in subscription capital, then filing INC-20A</li>
  <li>Appointing the first auditor within 30 days of incorporation and filing Form ADT-1</li>
  <li>Issuing share certificates and paying stamp duty on them</li>
  <li>Maintaining statutory registers and minutes of board meetings from the first meeting onward</li>
  <li>GST registration where you cross the threshold or supply inter-state</li>
  <li>The first annual filings — AOC-4 and MGT-7 or MGT-7A — after the first AGM</li>
</ul>
<p>We fold these into an annual engagement so nothing depends on a founder remembering a form.
See <a href="/services/roc-annual-compliance/">ROC and annual compliance</a> for the full calendar.</p>

<h2>LLP registration</h2>
<p>An LLP is registered through the FiLLiP form after name reservation, and the LLP agreement must
be filed in Form 3 within 30 days of incorporation. It suits professional practices, family
businesses and joint ventures that want limited liability without the meeting and audit machinery of
a company. Note that an LLP still needs its accounts audited once turnover or contribution crosses
the prescribed limits, and files Form 11 and Form 8 annually.</p>

<h2>Startup India (DPIIT) recognition</h2>
<p>If your entity is a private limited company, LLP or registered partnership within the prescribed
age and turnover limits and is working on innovation or a scalable business model, DPIIT recognition
is worth obtaining. It opens access to government schemes, self-certification under certain labour
and environmental laws, and eligibility to apply for the income tax exemption available to eligible
startups. We prepare the application and the supporting write-up.</p>
"""

INCORP_FAQS = [
    ("How much does it cost to register a private limited company in Chandigarh?",
     "The total is made up of three separate things: government filing fees and stamp duty (which "
     "vary with the state of the registered office and the authorised capital), the cost of digital "
     "signature certificates for each director, and professional fees. We give a single all-inclusive "
     "figure before starting and show you which part is a government charge, so there are no "
     "additions later."),
    ("How long does company registration take?",
     "With complete and consistent documents, name approval typically takes one to three working "
     "days and incorporation about a week thereafter, subject to the Registrar's queries. Delays "
     "almost always come from mismatched address proof or a proposed name that conflicts with an "
     "existing company or trademark — both of which we check before filing."),
    ("Can I register a company at my home address in Chandigarh?",
     "Yes. A residential address can serve as the registered office provided you can produce a "
     "recent utility bill for the premises and a no-objection certificate from the owner. The "
     "registered office is where official correspondence is served, so it must be an address where "
     "you can reliably receive post."),
    ("Do I need GST registration immediately after incorporation?",
     "Not automatically. GST registration becomes mandatory when you cross the turnover threshold, "
     "make inter-state supplies of goods, sell through an e-commerce operator, or fall into one of "
     "the other categories requiring compulsory registration. Registering before you need to means "
     "filing returns every month from that point, including nil returns, so it is worth deciding "
     "deliberately rather than by default."),
    ("Should I choose an LLP or a private limited company?",
     "If you intend to raise external investment, a private limited company is effectively the only "
     "practical option — investors subscribe to shares, and LLPs cannot offer them. If you are a "
     "professional practice or a closely held family business with no plans to bring in outside "
     "capital, an LLP gives you limited liability with a lighter and cheaper annual compliance load."),
    ("Can NRIs or foreign nationals be directors in an Indian company?",
     "Yes, subject to the requirement that at least one director is resident in India, and to FEMA "
     "rules on foreign investment including the reporting that follows an infusion of foreign funds. "
     "Documents of foreign nationals need notarisation or apostille. We handle the incorporation and "
     "the subsequent FDI reporting together."),
]

# ==========================================================================
# 2. GST
# ==========================================================================
GST_BODY = """
<p>GST is where most Indian businesses meet the tax system every month, and where most avoidable
money is lost — to late fees, to input tax credit that was claimed without matching, and to notices
that a clean reconciliation would have prevented. We handle registration, the monthly and quarterly
cycle, annual returns and departmental correspondence.</p>

<h2>Who has to register for GST</h2>
<p>Registration becomes compulsory once aggregate turnover crosses the threshold — broadly ₹40 lakh
for suppliers of goods and ₹20 lakh for suppliers of services in normal category states, with lower
limits for special category states. Aggregate turnover is computed across all your registrations on
the same PAN, all India, which surprises businesses running more than one vertical.</p>
<p>Threshold aside, registration is required regardless of turnover in several situations:</p>
<ul>
  <li>Making inter-state taxable supplies of goods</li>
  <li>Selling through an e-commerce operator that collects tax at source</li>
  <li>Being liable to pay tax under reverse charge</li>
  <li>Acting as an agent, input service distributor, or casual or non-resident taxable person</li>
</ul>
<div class="callout">
  <p><strong>A tricity trap worth knowing.</strong> Chandigarh's GST state code is 04, Punjab's is 03
  and Haryana's is 06. A supply from your Chandigarh office to your Zirakpur or Panchkula premises is
  an inter-state supply attracting IGST, and may require a separate registration — despite being a
  twenty-minute drive. Structure this before you take the second premises, not after.</p>
</div>

<h3>Documents for GST registration</h3>
<ul>
  <li>PAN of the business and of the proprietor, partners or directors</li>
  <li>Aadhaar of the authorised signatory, for e-KYC authentication</li>
  <li>Certificate of incorporation or partnership deed, as applicable</li>
  <li>Proof of the principal place of business — utility bill, rent agreement and owner's NOC</li>
  <li>Bank account details: a cancelled cheque or the first page of a statement</li>
  <li>Photographs and board resolution or authorisation letter for the signatory</li>
</ul>
<p>Aadhaar authentication speeds things up substantially. Where it is not completed, the application
usually goes to physical verification of premises, which adds time.</p>

<h2>The monthly and quarterly filing cycle</h2>
<div class="table-scroll">
<table>
  <caption>Principal GST returns and their due dates</caption>
  <thead><tr><th>Return</th><th>Who files it</th><th>Due date</th></tr></thead>
  <tbody>
    <tr><td>GSTR-1</td><td>Regular taxpayers filing monthly</td><td>11th of the following month</td></tr>
    <tr><td>IFF (optional)</td><td>QRMP taxpayers, for B2B invoices in months 1 and 2</td><td>13th of the following month</td></tr>
    <tr><td>GSTR-3B</td><td>Regular taxpayers filing monthly</td><td>20th of the following month</td></tr>
    <tr><td>GSTR-3B (QRMP)</td><td>Quarterly filers with turnover up to ₹5 crore</td><td>22nd or 24th after quarter end, by state group — Chandigarh falls in the 24th group</td></tr>
    <tr><td>CMP-08</td><td>Composition dealers</td><td>18th after each quarter</td></tr>
    <tr><td>GSTR-9</td><td>Annual return (optional below the prescribed turnover)</td><td>31 December following the financial year</td></tr>
    <tr><td>GSTR-9C</td><td>Reconciliation statement, above the prescribed turnover</td><td>31 December following the financial year</td></tr>
  </tbody>
</table>
</div>
<p>Late fees and interest accrue per return, per day. Nil returns are not optional — a dormant
registration with no transactions still has to file, and the late fee applies just the same.</p>

<h2>Input tax credit: where the real money is</h2>
<p>Credit is the part of GST that rewards discipline and punishes assumption. A few rules govern most
of the disputes we see:</p>
<ul>
  <li>Credit is available only where the invoice appears in your auto-populated <strong>GSTR-2B</strong>.
  If your supplier has not filed, you do not have the credit — however valid your invoice looks.</li>
  <li>Payment to the supplier must be made within the prescribed period, or the credit is reversed
  with interest.</li>
  <li>Certain credits are blocked outright — motor vehicles in most cases, works contract for
  immovable property, personal consumption and goods lost or written off.</li>
  <li>There is a hard cut-off for claiming credit for a financial year, after which it lapses
  permanently. Reconciling in March, when the year is nearly closed, is far too late.</li>
</ul>
<p>We reconcile purchase registers against GSTR-2B every month, flag suppliers who are not filing so
you can chase them while the invoice is still current, and keep the running difference visible
instead of discovering it at year end.</p>

<h2>E-invoicing and e-way bills</h2>
<p>Businesses above the prescribed aggregate turnover must generate e-invoices with an Invoice
Reference Number for B2B supplies; an invoice without a valid IRN is not a valid tax invoice, and
your customer's credit depends on it. Separately, movement of goods above the prescribed consignment
value requires an e-way bill. Both are areas where the compliance is mechanical but the consequence
of getting it wrong lands on the customer's credit and, eventually, on your relationship with them.</p>

<h2>Notices, mismatches and departmental representation</h2>
<p>The commonest GST notices follow a predictable pattern: a difference between GSTR-1 and GSTR-3B,
a difference between credit claimed in GSTR-3B and credit available in GSTR-2B, or a mismatch
between GST turnover and the turnover declared in your income tax return. Most are answerable with a
clean reconciliation and a reply filed within the deadline. We prepare the working, draft the reply,
file it, and appear before the authority where a hearing is called.</p>
"""

GST_FAQS = [
    ("What is the GST registration limit in India?",
     "Broadly, ₹40 lakh of aggregate turnover for suppliers of goods and ₹20 lakh for suppliers of "
     "services in normal category states, with lower limits in special category states. Aggregate "
     "turnover is calculated on the PAN across all registrations in India, so multiple businesses "
     "under the same PAN are added together. Registration is compulsory regardless of turnover for "
     "inter-state supply of goods, supplies through e-commerce operators, and certain other "
     "categories."),
    ("How long does GST registration take?",
     "Where Aadhaar authentication is completed successfully, registration is typically granted "
     "within a few working days. Where it is not, the application usually goes for physical "
     "verification of the business premises, which extends the timeline. Incomplete address proof is "
     "the most common reason an application is queried."),
    ("What happens if I file GST returns late?",
     "Late fees accrue for each day of delay for each return, and interest runs on any tax paid late. "
     "Beyond the money, a pattern of late filing blocks your customers from claiming credit on your "
     "invoices, which is usually the more expensive consequence. Prolonged non-filing can lead to "
     "cancellation of the registration."),
    ("Do I have to file GST returns if I had no sales?",
     "Yes. A nil return is still a return. An active GSTIN with no transactions in the period must "
     "file, and the late fee applies for nil returns too. If a registration is genuinely no longer "
     "needed, the correct course is to apply for cancellation rather than to stop filing."),
    ("Can I claim input tax credit if my supplier has not filed their return?",
     "In practice, no. Credit is restricted to invoices appearing in your auto-populated GSTR-2B. If "
     "the supplier has not filed their GSTR-1, the invoice does not appear and the credit is not "
     "available to you, however genuine the purchase. This is why we reconcile monthly — so you can "
     "chase the supplier while it can still be fixed."),
    ("Should I opt for the composition scheme?",
     "It depends on who your customers are. The composition scheme reduces your compliance and your "
     "rate, but you cannot charge GST on your invoices and your customers cannot claim credit from "
     "you. That is fine if you sell to end consumers and fatal if you sell to businesses. You also "
     "cannot claim input credit on your own purchases. We run the comparison on your actual numbers "
     "before you elect."),
]

# ==========================================================================
# 3. Income tax
# ==========================================================================
ITR_BODY = """
<p>Filing the return is the visible part. The work that determines what the return says happens
through the year — deciding the regime, paying advance tax on time, deducting TDS correctly, and
keeping the documentation that supports each claim. We file for companies, LLPs, firms,
professionals, salaried individuals and NRIs, and we do the planning that makes the filing
straightforward.</p>

<h2>Who we file for</h2>
<ul>
  <li><strong>Companies and LLPs</strong> — with the tax audit where applicable, and reconciliation
  between books, GST turnover and the return.</li>
  <li><strong>Partnership firms and proprietorships</strong> — including presumptive taxation where
  it genuinely suits the business.</li>
  <li><strong>Professionals and consultants</strong> — doctors, architects, lawyers, freelancers and
  agencies, weighing presumptive schemes against maintaining books.</li>
  <li><strong>Salaried individuals</strong> — with capital gains, house property, foreign assets or
  multiple Form 16s.</li>
  <li><strong>NRIs</strong> — residential status, income taxable in India, DTAA relief, TDS on
  property sales under section 195 and repatriation certificates.</li>
</ul>

<h2>The dates that matter</h2>
<div class="table-scroll">
<table>
  <caption>Recurring income tax deadlines in a financial year</caption>
  <thead><tr><th>Obligation</th><th>Ordinarily due</th></tr></thead>
  <tbody>
    <tr><td>Advance tax — first instalment (15%)</td><td>15 June</td></tr>
    <tr><td>Advance tax — second instalment (45% cumulative)</td><td>15 September</td></tr>
    <tr><td>Advance tax — third instalment (75% cumulative)</td><td>15 December</td></tr>
    <tr><td>Advance tax — fourth instalment (100%)</td><td>15 March</td></tr>
    <tr><td>Tax audit report, where applicable</td><td>30 September</td></tr>
    <tr><td>Income tax return — non-audit cases</td><td>31 July</td></tr>
    <tr><td>Income tax return — audit cases</td><td>31 October</td></tr>
    <tr><td>Income tax return — transfer pricing cases</td><td>30 November</td></tr>
    <tr><td>Belated or revised return</td><td>31 December of the assessment year</td></tr>
    <tr><td>TDS returns (24Q / 26Q / 27Q)</td><td>31 July, 31 October, 31 January, 31 May</td></tr>
  </tbody>
</table>
<p style="font-size:.86rem;color:#64748b">Dates are the ordinary statutory positions and are
occasionally extended by the department. We confirm the operative date for your case before filing.</p>
</div>

<h2>Old regime or new regime?</h2>
<p>The new regime under section 115BAC is now the default; the old regime must be opted into. The
comparison is not a matter of principle — it is arithmetic, and it changes as your deductions change.
For someone with a home loan, substantial 80C investments, HRA and a health insurance premium, the
old regime can still come out ahead. For someone with few deductions, the new regime usually wins.
We run both on your actual numbers before filing rather than assuming.</p>
<p>Note that businesses and professionals face restrictions on switching back and forth between
regimes in later years, so the first choice carries more weight for them than for salaried taxpayers.</p>

<h2>Presumptive taxation: useful, but not for everyone</h2>
<p>Sections 44AD and 44ADA let eligible small businesses and professionals declare income at a
prescribed percentage of turnover or gross receipts, with relief from maintaining detailed books.
The turnover limits are higher where cash receipts stay within the prescribed small proportion of
total receipts — which is a deliberate nudge towards banking channels.</p>
<p>It is genuinely simpler. But if your actual margin is lower than the deemed rate, you pay tax on
profit you never earned; and once you opt out, you are locked out for a period. It suits high-margin
professional practices far better than thin-margin trading businesses. We compare the presumptive
outcome against actual results before recommending it.</p>

<h2>Tax audit under section 44AB</h2>
<p>A tax audit is triggered when business turnover exceeds the prescribed limit — with a
substantially higher limit available where both cash receipts and cash payments stay within the
prescribed small proportion of the total — or where professional gross receipts exceed the
prescribed limit. It also applies in certain cases where a taxpayer declares income below the
presumptive rate. The report is filed before the return, and missing it carries a penalty linked to
turnover. See <a href="/services/audit-and-assurance/">audit and assurance</a> for how we run it.</p>

<h2>Notices, assessments and appeals</h2>
<p>Most communications from the department are routine and answerable: intimation of an arithmetic
difference, a mismatch between the return and Form 26AS or the Annual Information Statement, a query
under limited scrutiny, or a TDS default flagged on TRACES. Proceedings are largely faceless now,
which means the quality of the written submission carries the case. We prepare the reconciliation,
draft the response, file it within the window, and take the matter to appeal where the position is
worth defending.</p>

<div class="note">
  <p><strong>Check your AIS before you file, not after.</strong> The Annual Information Statement
  aggregates what third parties have reported about you — interest, dividends, securities
  transactions, property dealings, large cash deposits. A return that does not reconcile with it is
  the single most common trigger for a query. We reconcile it as a matter of course.</p>
</div>
"""

ITR_FAQS = [
    ("What is the last date for filing an income tax return?",
     "For taxpayers not subject to audit, the ordinary due date is 31 July following the end of the "
     "financial year. Where a tax audit applies, it is 31 October, and 30 November where transfer "
     "pricing provisions apply. A belated or revised return can ordinarily be filed up to 31 "
     "December of the assessment year. The department occasionally extends these dates, so we "
     "confirm the operative deadline for your case."),
    ("What happens if I miss the ITR deadline?",
     "You can still file a belated return, but a late filing fee applies and interest runs on unpaid "
     "tax. More importantly, filing late restricts your ability to carry forward certain losses, "
     "which can be far more expensive than the fee itself for a business that had a loss year."),
    ("Which income tax regime should I choose?",
     "The new regime is the default and generally favours taxpayers with few deductions. The old "
     "regime can still be better where you have significant deductions — a home loan, 80C "
     "investments, HRA, health insurance. It is a calculation, not a principle, and we run both on "
     "your figures before filing. Business and professional taxpayers should note the restrictions "
     "on switching between regimes in later years."),
    ("Do I need to file a return if my income is below the taxable limit?",
     "Often yes. Filing is required in a number of situations irrespective of income level — for "
     "example where you hold foreign assets, where prescribed high-value transactions or deposits "
     "have occurred, or where TDS has been deducted and you want the refund. Filing also creates the "
     "income record that banks and visa authorities ask for."),
    ("How is a Chartered Accountant different from a filing website?",
     "A portal validates arithmetic. A CA decides the positions — which regime, which head of "
     "income, whether a receipt is capital or revenue, whether presumptive taxation genuinely suits "
     "you, and what documentation you need to hold if the claim is questioned three years later. "
     "The filing is the easy part; standing behind the position is the work."),
    ("Can you handle a scrutiny notice I have already received?",
     "Yes, and it is common for clients to come to us at that point. Bring the notice, the return it "
     "relates to and the supporting records. We will tell you what the department is actually asking, "
     "what the realistic outcome is, and what it will cost to respond properly — before you commit."),
]

# ==========================================================================
# 4. Audit
# ==========================================================================
AUDIT_BODY = """
<p>An audit is worth more than the signature at the end of it. Done properly, it is the one time each
year that someone independent examines how money, stock and credit actually move through your
business — and tells you where they are leaking. We conduct statutory, tax, internal and stock audits
for companies, LLPs and firms across Chandigarh and beyond.</p>

<h2>Statutory audit under the Companies Act</h2>
<p>Every company incorporated in India must have its financial statements audited each year,
regardless of turnover or whether it traded at all. The auditor is appointed by the members, the
appointment is filed with the Registrar in Form ADT-1, and the audited statements go on to form part
of the AOC-4 filing.</p>
<p>Our statutory audit covers the recognition and measurement of revenue and expenses, verification
of assets and liabilities, related party transactions and their disclosure, compliance with the
applicable accounting standards, and the specific reporting the auditor's report requires.</p>

<h2>Tax audit under section 44AB</h2>
<p>A tax audit applies where business turnover exceeds the prescribed limit — with a substantially
higher limit where both cash receipts and cash payments remain within the prescribed small
proportion of the total — or where professional gross receipts exceed the prescribed limit. It also
applies in certain cases where income is declared below the presumptive rate.</p>
<p>The report is filed in the prescribed forms with the detailed annexure, ordinarily before the
return is filed, and failure to obtain it attracts a penalty linked to turnover. The annexure asks
searching questions about cash transactions, loans, disallowable payments and TDS compliance, which
is why a tax audit tends to surface issues that book-keeping alone did not.</p>

<h2>Internal audit</h2>
<p>Required for certain classes of companies and voluntarily adopted by many others once they reach
a size where the promoter cannot personally see every transaction. Internal audit is about controls
rather than opinion: whether purchase orders precede purchases, whether receipts are banked
promptly, whether credit limits are respected, whether stock records match the floor, and whether
the people approving payments are different from the people making them.</p>

<h2>Stock, fixed asset and process audits</h2>
<p>For manufacturers, distributors and retailers, inventory is usually the largest number on the
balance sheet and the least verified. We conduct physical stock verification, reconcile it to the
records, examine valuation and slow-moving or obsolete provisioning, and verify fixed asset
existence against the register. Lenders frequently require this independently.</p>

<h2>GST audit and departmental audit support</h2>
<p>Where turnover crosses the prescribed limit, the annual reconciliation statement in GSTR-9C must
be filed alongside the annual return. Separately, the department conducts its own audits and
inspections. We prepare the reconciliations, assemble the records the officer will ask for, and
represent you through the process.</p>

<h2>How we run an audit</h2>
<ol>
  <li><strong>Planning</strong> — understanding the business, the transaction cycles and where
  material misstatement is actually likely, rather than applying a generic checklist.</li>
  <li><strong>Control evaluation</strong> — testing whether the controls you believe exist are
  operating.</li>
  <li><strong>Substantive testing</strong> — verification of balances, third-party confirmations,
  physical verification and analytical review against prior periods and industry norms.</li>
  <li><strong>Reporting</strong> — the statutory report, plus a management letter setting out
  control weaknesses and what to do about them. That letter is where most of the practical value
  sits.</li>
  <li><strong>Follow-up</strong> — checking in the following cycle whether the points raised were
  acted on.</li>
</ol>

<div class="note">
  <p><strong>A note on independence.</strong> Professional standards restrict an auditor from also
  performing certain services for the same audit client. Where that applies, we will tell you plainly
  and help you arrange the other work elsewhere. It is not a technicality — it is what makes the
  opinion worth anything.</p>
</div>
"""

AUDIT_FAQS = [
    ("Does every company need a statutory audit?",
     "Yes. Every company registered in India must have its financial statements audited each year, "
     "regardless of turnover, and even if it had no transactions during the year. This is a "
     "significant difference from a proprietorship or partnership, where audit is triggered only by "
     "turnover thresholds, and it is a recurring cost founders should factor in before choosing the "
     "company structure."),
    ("When is a tax audit required?",
     "A tax audit under section 44AB is triggered where business turnover exceeds the prescribed "
     "limit — with a substantially higher limit where both cash receipts and cash payments stay "
     "within the prescribed small proportion of the total — or where professional gross receipts "
     "exceed the prescribed limit. It can also apply where income is declared below the presumptive "
     "rate. We assess applicability on your actual figures well before the deadline."),
    ("Is an LLP required to be audited?",
     "An LLP must have its accounts audited once turnover or partner contribution crosses the "
     "prescribed limits. Below those limits, audit is not mandatory under the LLP Act, although a "
     "tax audit may still apply separately under the Income Tax Act, and lenders or investors "
     "frequently ask for audited accounts regardless."),
    ("What is the penalty for not getting a tax audit done?",
     "A penalty linked to turnover, subject to a prescribed ceiling, unless there is reasonable "
     "cause. The practical consequence is usually broader: the return cannot be filed correctly "
     "without the report, which cascades into late filing and the loss of certain carry-forward "
     "benefits."),
    ("Can the same firm do our audit and our accounting?",
     "Not for a statutory audit client — professional standards restrict an auditor from providing "
     "certain other services to the same entity, precisely so the opinion stays independent. Where "
     "this applies to you we will say so up front and help you arrange the other work with a "
     "different firm."),
    ("What documents do you need to start an audit?",
     "Trial balance and ledgers for the year, bank statements and reconciliations, purchase and "
     "sales registers, GST returns filed, TDS returns and challans, fixed asset register, inventory "
     "records, loan agreements and sanction letters, statutory registers and minutes, and the prior "
     "year's audited financials. We send a tailored request list once we understand the business."),
]

# ==========================================================================
# 5. ROC compliance
# ==========================================================================
ROC_BODY = """
<p>Company law compliance is unforgiving in a specific way: the penalties are usually per day, they
attach to the company <em>and</em> to the officers personally, and there is no reasonable-cause
escape for simply having forgotten. Most of it is entirely mechanical. We run the calendar so it
never becomes a problem.</p>

<h2>The annual filing cycle for a private limited company</h2>
<div class="table-scroll">
<table>
  <caption>Recurring ROC and secretarial obligations</caption>
  <thead><tr><th>Filing</th><th>What it covers</th><th>Ordinarily due</th></tr></thead>
  <tbody>
    <tr><td>Board meetings</td><td>Minimum number of meetings per year with the prescribed gap between them</td><td>Through the year</td></tr>
    <tr><td>Annual General Meeting</td><td>Adoption of accounts, auditor and director matters</td><td>Within six months of the financial year end</td></tr>
    <tr><td>AOC-4</td><td>Filing of the audited financial statements</td><td>Within 30 days of the AGM</td></tr>
    <tr><td>MGT-7 / MGT-7A</td><td>Annual return (MGT-7A for small companies and OPCs)</td><td>Within 60 days of the AGM</td></tr>
    <tr><td>ADT-1</td><td>Intimation of auditor appointment</td><td>Within 15 days of the AGM</td></tr>
    <tr><td>DIR-3 KYC</td><td>Annual KYC for every person holding a DIN</td><td>30 September</td></tr>
    <tr><td>DPT-3</td><td>Return of deposits and exempted deposits</td><td>30 June</td></tr>
    <tr><td>MSME-1</td><td>Half-yearly return of dues outstanding to MSME suppliers beyond the prescribed period</td><td>30 April and 31 October</td></tr>
    <tr><td>LLP Form 11</td><td>LLP annual return</td><td>30 May</td></tr>
    <tr><td>LLP Form 8</td><td>Statement of account and solvency</td><td>30 October</td></tr>
  </tbody>
</table>
</div>

<h2>Event-based filings</h2>
<p>Beyond the annual cycle, specific corporate actions carry their own forms and their own clocks —
usually 15 to 30 days from the event. Missing them is how companies end up paying additional fees
that dwarf the original filing cost:</p>
<ul>
  <li>Appointment, resignation or change of directors (DIR-12)</li>
  <li>Allotment of shares and the return of allotment (PAS-3)</li>
  <li>Change of registered office, within or across jurisdictions (INC-22, INC-23)</li>
  <li>Increase in authorised share capital and alteration of the memorandum (SH-7)</li>
  <li>Creation, modification or satisfaction of charges over assets (CHG-1, CHG-4)</li>
  <li>Declaration of commencement of business (INC-20A) within 180 days of incorporation</li>
  <li>Changes to the objects clause, name or articles</li>
</ul>

<h2>Registers and minutes — the part everyone skips</h2>
<p>The Companies Act requires companies to maintain statutory registers — members, directors,
charges, related party contracts — and to record properly signed minutes of board and general
meetings. These are rarely inspected in an ordinary year and become critical the moment they matter:
at due diligence, in an adjudication, when a bank takes a charge, or in a dispute between
shareholders.</p>
<p>Reconstructing three years of minutes under time pressure during a funding round is a
characteristic and avoidable panic. We maintain them contemporaneously.</p>

<div class="callout">
  <p><strong>Struck-off or defaulting company?</strong> If filings have been missed for years, or the
  company has been struck off the register, there are routes back — additional fee filings, condonation
  applications, or restoration proceedings before the Tribunal. Bring us the MCA master data and we
  will tell you what the realistic path and cost look like. <a href="tel:%(tel)s">Call %(phone)s</a>.</p>
</div>

<h2>What our annual ROC engagement includes</h2>
<ul>
  <li>Maintaining the compliance calendar and requesting documents ahead of each due date</li>
  <li>Drafting notices, agendas, resolutions and minutes for board and general meetings</li>
  <li>Preparing and filing AOC-4, MGT-7 or MGT-7A, ADT-1, DIR-3 KYC, DPT-3 and MSME-1</li>
  <li>Handling event-based filings as corporate actions occur</li>
  <li>Maintaining statutory registers and the register of members</li>
  <li>Coordinating with the auditor so the accounts are ready ahead of the AGM, not after it</li>
</ul>
"""

ROC_FAQS = [
    ("What are the annual compliance requirements for a private limited company?",
     "At minimum: holding the required board meetings and the AGM, getting the accounts audited, "
     "filing AOC-4 with the financial statements and MGT-7 or MGT-7A as the annual return, filing "
     "ADT-1 for the auditor's appointment, DIR-3 KYC for each director, DPT-3, and MSME-1 where "
     "amounts are outstanding to MSME suppliers. The income tax return and any GST and TDS filings "
     "run alongside these."),
    ("What is the penalty for late ROC filing?",
     "Late filings attract additional fees that increase with the length of the delay, and the "
     "underlying default can carry penalties on the company and on the officers in default "
     "personally. Because several of these are computed per day, a filing forgotten for a year "
     "typically costs many times the original fee."),
    ("What happens if a company does not file for several years?",
     "The Registrar can strike the company off the register, and directors of a company that has "
     "failed to file for a continuous period can be disqualified from holding directorships. Both "
     "are reversible in appropriate cases — through condonation or restoration proceedings — but "
     "the process is considerably more expensive than the filings would have been."),
    ("Does a dormant company with no transactions still have to file?",
     "Yes. A company with no business activity still has to hold its meetings, have its accounts "
     "audited and make its annual filings. If the company is genuinely not going to trade, the "
     "cleaner options are applying for dormant status or striking it off voluntarily — either is "
     "cheaper than years of nil compliance."),
    ("Is ROC compliance the same for an LLP?",
     "No, and it is lighter. An LLP files Form 11 as its annual return and Form 8 as its statement "
     "of account and solvency, and has no requirement to hold board meetings or an AGM. Audit is "
     "required only once turnover or contribution crosses the prescribed limits. This is one of the "
     "main practical reasons to prefer an LLP where outside investment is not planned."),
]

# ==========================================================================
# 6. Virtual CFO
# ==========================================================================
CFO_BODY = """
<p>There is a stage most growing businesses hit where the accountant is keeping up but nobody is
actually running the numbers. Revenue is growing, cash is tight, and no one can say confidently which
customer or product is funding the rest. That is the gap a virtual CFO fills — senior financial
judgement, applied monthly, without a full-time hire at a full-time salary.</p>

<h2>What a virtual CFO actually does</h2>
<ul>
  <li><strong>Monthly management accounts</strong> closed on a fixed date, with variance against
  budget and the prior period explained rather than just presented.</li>
  <li><strong>Cash-flow forecasting</strong> — a rolling view of what is coming in and going out, so
  a shortfall is visible weeks ahead instead of on the day.</li>
  <li><strong>Budgeting and planning</strong> — an annual budget the business is actually run
  against, with quarterly re-forecasts as reality diverges.</li>
  <li><strong>Unit economics</strong> — contribution by product, service line, customer or branch,
  after allocating overheads honestly.</li>
  <li><strong>Working capital management</strong> — debtor days, creditor days and inventory
  holding, and the specific interventions that move them.</li>
  <li><strong>Pricing and margin analysis</strong> — what a discount actually costs once volume
  effects are counted.</li>
  <li><strong>Investor and lender reporting</strong> — board packs and bank submissions that
  anticipate the questions rather than inviting them.</li>
  <li><strong>Controls and process</strong> — approval limits, segregation of duties, and the
  discipline that keeps a growing business from losing money quietly.</li>
</ul>

<h2>Who this is for</h2>
<p>Businesses roughly in the range where a full-time CFO is not yet justified but the founder is
already the bottleneck on financial decisions. In practice that means funded startups after their
first round, family businesses professionalising, manufacturers with complex working capital, and
services firms whose profitability varies sharply by client without anyone knowing exactly why.</p>

<div class="callout">
  <p><strong>A useful test.</strong> If you cannot answer, this month, which of your customers or
  products is unprofitable and by how much — you have a book-keeper, not a finance function. That is
  the gap this service closes.</p>
</div>

<h2>How the engagement runs</h2>
<ol>
  <li><strong>Diagnostic</strong> — two to three weeks reviewing the books, the reporting and the
  controls as they are, and setting out plainly what is missing.</li>
  <li><strong>Foundations</strong> — a chart of accounts that supports decisions, a monthly close
  calendar, and an MIS pack designed around the handful of numbers that actually drive your business.</li>
  <li><strong>Monthly cycle</strong> — close, MIS, a review meeting where the numbers are discussed
  and decisions are taken, and a rolling cash-flow update.</li>
  <li><strong>Quarterly</strong> — re-forecast, deeper margin and working capital review, and board
  or investor reporting.</li>
  <li><strong>As needed</strong> — funding support, valuation, due diligence readiness and lender
  negotiations.</li>
</ol>

<h2>Funding, valuation and due diligence support</h2>
<p>When you raise capital or take on debt, the finance function is what is being examined. We prepare
the financial model and projections, assemble the data room, run pre-diligence to find the problems
before the investor does, prepare valuation reports where they are required for pricing or regulatory
filings, and sit in on the diligence process. Businesses whose books are already clean close faster
and negotiate from a stronger position — the difference is rarely the numbers themselves, it is how
much of them needs explaining.</p>

<h2>How this differs from your accountant</h2>
<p>Your accountant records what happened and files what is due, and that work remains essential. A
virtual CFO uses the same data to answer forward-looking questions: whether to take the order, hire
the team, extend the credit, or raise the round. We are happy to work alongside your existing
accountant, or to take on the compliance work too — see
<a href="/services/">our full service list</a>.</p>
"""

CFO_FAQS = [
    ("What is a virtual CFO?",
     "A virtual CFO is an experienced finance professional engaged on a part-time or retained basis "
     "to do the work a full-time chief financial officer would do — monthly management reporting, "
     "cash-flow forecasting, budgeting, margin analysis, controls, and investor or lender reporting "
     "— without the cost of a full-time senior hire."),
    ("How is a virtual CFO different from an accountant or book-keeper?",
     "A book-keeper records transactions and an accountant prepares and files statutory returns. "
     "Both are backward-looking by nature and both are necessary. A virtual CFO uses that data to "
     "answer forward-looking questions: whether the business can fund a hire, which product line is "
     "subsidising the others, when cash will get tight, and what a lender or investor will make of "
     "the numbers."),
    ("What size of business needs a virtual CFO?",
     "Typically one where the founder is spending significant time on financial decisions without "
     "reliable numbers to base them on, but where a full-time CFO salary is not yet justified. Funded "
     "startups after a first round, family businesses professionalising, and manufacturers with "
     "complex working capital cycles are the most common profiles."),
    ("Can you work alongside our existing accountant?",
     "Yes, and it is a common arrangement. We take the data your accountant produces, add the "
     "reporting and analysis layer on top, and give your team clearer instructions on what we need "
     "and when. If you would rather consolidate compliance and CFO work with one firm, we can do "
     "that too."),
    ("Will you help us raise funding?",
     "We prepare the financial model and projections, build the data room, run a pre-diligence "
     "review to surface issues before an investor does, prepare valuation reports where required, "
     "and support you through the diligence process. We do not act as placement agents or introduce "
     "investors — our role is to make sure the numbers hold up when they look."),
]


PAGES = [
    service_page(
        url="/services/company-registration-chandigarh/",
        h1="Company &amp; LLP Registration",
        sub="Private Limited, LLP, OPC and partnership registration in Chandigarh, filed end to end.",
        title="Company Registration in Chandigarh — Pvt Ltd & LLP",
        og_title="Company & LLP Registration in Chandigarh",
        description=("Register a Private Limited company, LLP or OPC in Chandigarh. SPICe+ filing, "
                     "DSC, DIN, PAN, TAN and Startup India recognition handled by a CA firm."),
        body=INCORP_BODY, faqs=INCORP_FAQS,
        schema_name="Company and LLP Registration",
        schema_type="Business incorporation and startup registration",
        cta_head="Ready to register?",
        cta_text=("Tell us what the business will do and who is involved, and we will recommend the "
                  "structure and give you an all-inclusive quote."),
    ),
    service_page(
        url="/services/gst-registration-return-filing/",
        h1="GST Registration &amp; Return Filing",
        sub="Registration, monthly and quarterly returns, input credit reconciliation and notices.",
        title="GST Registration & Return Filing in Chandigarh | Talk To CA",
        og_title="GST Registration & Return Filing — Chandigarh",
        description=("GST consultants in Chandigarh for registration, GSTR-1 and GSTR-3B filing, input "
                     "tax credit reconciliation, annual returns and departmental notices."),
        body=GST_BODY, faqs=GST_FAQS,
        schema_name="GST Registration and Return Filing",
        schema_type="Goods and Services Tax compliance",
        cta_head="Behind on GST returns?",
        cta_text=("Send us your GSTIN and we will pull the filing status, quantify the late fees and "
                  "tell you what it takes to get current."),
    ),
    service_page(
        url="/services/income-tax-return-filing/",
        h1="Income Tax Return Filing",
        sub="ITR filing and year-round tax planning for companies, firms, professionals and individuals.",
        title="Income Tax Return Filing in Chandigarh — ITR for Business",
        og_title="Income Tax Return Filing — Chandigarh CA Firm",
        description=("ITR filing in Chandigarh for companies, LLPs, firms, professionals, salaried "
                     "individuals and NRIs. Advance tax planning, regime comparison and tax audit."),
        body=ITR_BODY, faqs=ITR_FAQS,
        schema_name="Income Tax Return Filing and Planning",
        schema_type="Direct tax compliance and advisory",
        cta_head="Not sure which regime or which form applies?",
        cta_text=("Send us last year's return and we will tell you what changes this year and what it "
                  "will cost."),
    ),
    service_page(
        url="/services/audit-and-assurance/",
        h1="Audit &amp; Assurance",
        sub="Statutory audit, tax audit, internal audit and stock audit conducted to withstand scrutiny.",
        title="Statutory & Tax Audit Services in Chandigarh | Auditors",
        og_title="Audit & Assurance Services — Chandigarh",
        description=("Chartered Accountants in Chandigarh for statutory audit under the Companies Act, "
                     "tax audit under section 44AB, internal audit and stock audit."),
        body=AUDIT_BODY, faqs=AUDIT_FAQS,
        schema_name="Audit and Assurance Services",
        schema_type="Statutory, tax and internal audit",
        cta_head="Need an auditor appointed?",
        cta_text=("Tell us your entity type, turnover and year end, and we will confirm which audits "
                  "apply to you and what the timeline looks like."),
    ),
    service_page(
        url="/services/roc-annual-compliance/",
        h1="ROC &amp; Annual Compliance",
        sub="AOC-4, MGT-7, DIR-3 KYC, DPT-3, MSME-1 and event-based filings, tracked and filed on time.",
        title="ROC Annual Filing & Company Compliance in Chandigarh",
        og_title="ROC & Annual Company Compliance — Chandigarh",
        description=("ROC compliance in Chandigarh: AOC-4 and MGT-7 annual filings, DIR-3 KYC, DPT-3, "
                     "MSME-1, event-based forms and statutory registers for companies and LLPs."),
        body=ROC_BODY % {"tel": TEL, "phone": PHONE}, faqs=ROC_FAQS,
        schema_name="ROC and Corporate Compliance",
        schema_type="Companies Act and secretarial compliance",
        cta_head="Filings overdue?",
        cta_text=("Send us the company CIN. We will pull the MCA master data, list exactly what is "
                  "outstanding and price the clean-up before you commit to anything."),
    ),
    service_page(
        url="/services/virtual-cfo-services/",
        h1="Virtual CFO Services",
        sub="Monthly MIS, cash-flow forecasting, budgeting and investor reporting for growing businesses.",
        title="Virtual CFO Services in India for Startups & SMEs",
        og_title="Virtual CFO Services for Indian Businesses",
        description=("Virtual CFO services for Indian startups and SMEs: monthly MIS, cash-flow "
                     "forecasting, budgeting, unit economics, funding support and investor reporting."),
        body=CFO_BODY, faqs=CFO_FAQS,
        schema_name="Virtual CFO Services",
        schema_type="Outsourced chief financial officer and management reporting",
        cta_head="Want to see what this would look like for your business?",
        cta_text=("We start with a short diagnostic of your current books and reporting, and tell you "
                  "honestly whether you need this yet."),
    ),
]
