import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STRATA = '''<svg class="strata" viewBox="0 0 100 30" fill="none" aria-hidden="true"><path d="M2 28 Q50 -8 98 28" stroke="#B08D57" stroke-width="0.5" stroke-linecap="round"/></svg>'''
NAV = [('index.html', 'Home'), ('services.html', 'Services'), ('courses.html', 'Courses'), ('about.html', 'About')]

def page(fname, title, desc, body):
    links = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-src https://calendly.com; form-action 'self' mailto:; base-uri 'self'; object-src 'none'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://talusconsulting.net/{"" if fname=="index.html" else fname}">
<meta property="og:url" content="https://talusconsulting.net/{"" if fname=="index.html" else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-180.png">
<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="index.html" aria-label="Talus home"><img src="assets/img/talus-logo-navy.svg" alt="Talus"></a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <ul class="nav-links">{links}<li><a class="btn btn-primary btn-small" href="contact.html" style="color:var(--ivory)">Book a call</a></li></ul>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div class="foot-top">
      <div><img src="assets/img/talus-logo-ivory.svg" alt="Talus"><p style="margin:16px 0 0;max-width:300px">AI training for business. Built to carry what's next.</p></div>
      <ul class="foot-links"><li><a href="services.html">Services</a></li><li><a href="courses.html">Courses</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li></ul>
    </div>
    <div class="foot-bottom"><span>&copy; <span id="year">2026</span> Talus. All rights reserved.</span><a href="mailto:support@talusconsulting.net">support@talusconsulting.net</a></div>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
'''

CTA = '''<section class="dark cta-band"><div class="wrap reveal">
  <span class="eyebrow">Start here</span>
  <h2>Ready to take the first step?</h2>
  <p class="lead">Book a free discovery call and leave with a clear picture of where AI can help your business most.</p>
  <div class="actions"><a class="btn btn-primary" href="contact.html" style="background:var(--brass);border-color:var(--brass);color:var(--navy)">Book a discovery call <span class="arr">&rarr;</span></a></div>
</div></section>'''

home = f'''
<section class="hero">
  <canvas id="net" aria-hidden="true"></canvas>
  <div class="wrap">
    <span class="eyebrow reveal">AI training for business</span>
    <h1 class="reveal">Built to carry what's next.</h1>
    <p class="lead reveal">The talus is the ankle bone that carries the body's entire weight and keeps it moving forward. Talus does the same for your business, training your team to put AI to work with practical skills and real results instead of hype.</p>
    <div class="actions reveal">
      <a class="btn btn-primary" href="contact.html">Book a discovery call <span class="arr">&rarr;</span></a>
      <a class="btn btn-ghost" href="courses.html">Explore courses</a>
    </div>
    <div class="ask reveal">
      <label for="ask-input"><span class="dot"></span>Ask Talus &middot; What could AI do for my business?</label>
      <form id="ask-form" autocomplete="off">
        <input id="ask-input" placeholder="Type your industry, e.g. dental clinic" aria-label="Your industry">
        <button class="btn btn-primary" type="submit">Show me <span class="arr">&rarr;</span></button>
      </form>
      <div class="chips"><button class="chip" type="button">Retail</button><button class="chip" type="button">Healthcare</button><button class="chip" type="button">Real estate</button><button class="chip" type="button">Law</button><button class="chip" type="button">Construction</button><button class="chip" type="button">Finance</button></div>
      <div class="answer" id="ask-answer" aria-live="polite"><ol></ol><p class="note">Sample ideas from the Talus playbook, shown for illustration. Not a live AI model; real results depend on your business.</p><p class="cta">Want a plan built around your business? <a href="contact.html">Book a free discovery call &rarr;</a></p></div>
    </div>
  </div>
</section>

<section class="white"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Why Talus</span><h2>Practical AI, taught by people who use it.</h2></div>
  <div class="grid-3">
    <div class="card reveal"><span class="num">01</span><h3>Practical, not theoretical</h3><p>Every session ends with something your team can use on Monday.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>Built for your business</h3><p>We start from your workflows, tools and goals, not a generic syllabus.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>Responsible by default</h3><p>Data privacy, accuracy and governance are part of every program.</p></div>
  </div>
</div></section>

<section class="dark"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">How it works</span><h2>Four steps to move forward with confidence.</h2></div>
  <div class="steps">
    <div class="step"><span class="n">01</span><div><h3>Discover</h3><p>A free 30-minute call to understand your goals and where AI fits.</p></div></div>
    <div class="step"><span class="n">02</span><div><h3>Assess</h3><p>We map your processes and find the highest-value opportunities.</p></div></div>
    <div class="step"><span class="n">03</span><div><h3>Train</h3><p>Hands-on workshops and courses tailored to each team.</p></div></div>
    <div class="step"><span class="n">04</span><div><h3>Implement</h3><p>We help you launch, measure and scale what works.</p></div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="split">
    <div class="reveal"><span class="eyebrow">Courses</span><h2>Learn AI the practical way.</h2><p class="lead">Self-paced courses and live workshops that turn curiosity into everyday skill.</p><div class="actions" style="margin-top:28px"><a class="btn btn-ghost" href="courses.html">See all courses <span class="arr">&rarr;</span></a></div></div>
    <div class="reveal"><p class="quote">&ldquo;The talus carries the body's full weight with every step. We help your business carry what comes next.&rdquo;</p></div>
  </div>
</div></section>
{CTA}'''

def svc(name, text, price):
    return f'<div class="service reveal"><h3>{name}</h3><p>{text}</p><span class="price">{price}</span></div>'

services = f'''
<section class="page-hero">{STRATA}<div class="wrap">
  <span class="eyebrow reveal">Services</span>
  <h1 class="reveal">AI adoption, from first question to full rollout.</h1>
  <p class="lead reveal">Whether you're just curious or ready to scale, Talus meets your team where it is.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap">
  {svc("Discovery call", "A 30-minute conversation about your goals, your team and your current tools. You leave with two or three concrete ideas, whether or not we work together.", "Free")}
  {svc("AI readiness assessment", "We review your workflows, data and skills, then deliver a prioritized roadmap of where AI will save time or create value first.", "From $X")}
  {svc("Team workshops", "Half-day or full-day hands-on sessions, in person or remote, tailored to a department such as sales, operations, HR or leadership.", "From $X")}
  {svc("Implementation coaching", "Ongoing support while your team puts AI into daily work: choosing tools, writing policies, building workflows and measuring results.", "$X / month")}
</div></section>
{CTA}'''

def course(meta, name, who, price, action):
    return f'<div class="course reveal"><span class="meta">{meta}</span><h3>{name}</h3><p>{who}</p><div class="foot"><strong>{price}</strong><a class="btn btn-ghost btn-small" href="contact.html">{action}</a></div></div>'

courses = f'''
<section class="page-hero">{STRATA}<div class="wrap">
  <span class="eyebrow reveal">Courses &amp; workshops</span>
  <h1 class="reveal">Learn AI the practical way.</h1>
  <p class="lead reveal">Self-paced courses and live workshops that turn curiosity into everyday skill.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap"><div class="grid-3">
  {course("Self-paced &middot; ~2 hours", "AI Foundations for Business", "For anyone new to AI. What it can and can't do, and where it fits in your work.", "$X", "Enroll now")}
  {course("Self-paced &middot; ~3 hours", "Prompting That Works", "For everyday users of ChatGPT, Claude or Copilot who want better results, faster.", "$X", "Enroll now")}
  {course("Live &middot; Half day", "AI for Leaders", "For owners and executives setting AI strategy, budgets and expectations.", "$X", "Reserve a seat")}
  {course("Live &middot; 2 hours", "Responsible AI &amp; Policy", "For leadership, HR and compliance teams writing the rules for safe AI use.", "$X", "Reserve a seat")}
  {course("Live &middot; Full day", "Team Bootcamp", "A custom, hands-on day for a whole department, built around its real work.", "Quote", "Get a quote")}
</div>
<p class="fine reveal" style="margin-top:28px;font-size:14px;color:var(--slate)">Self-paced courses are digital and non-refundable. Live workshops are fully refundable up to 7 days before the start date. <a href="terms.html#refunds">Refund policy</a></p>
</div></section>
{CTA}'''

about = f'''
<section class="page-hero">{STRATA}<div class="wrap">
  <span class="eyebrow reveal">About</span>
  <h1 class="reveal">Why Talus?</h1>
</div></section>
<section style="padding-top:10px"><div class="wrap"><div class="split">
  <div class="reveal"><p class="quote">The talus is a small bone in the ankle that carries the full weight of the body with every step.</p></div>
  <div class="reveal"><p class="lead">It connects the leg to the foot and turns that weight into forward motion. That is our role: the strength your business stands on as AI reshapes how work gets done.</p><h3 style="margin-top:36px">Our mission</h3><p style="color:var(--slate)">Help every business use AI with confidence, through clear teaching, honest advice and results you can measure.</p></div>
</div></div></section>
<section class="white"><div class="wrap"><div class="split">
  <div class="reveal"><span class="eyebrow">Founder</span><h2>James E. Lewis</h2></div>
  <div class="reveal"><p class="lead">James founded Talus to help companies stay competitive as AI reshapes the global economy. He builds with AI hands-on, including designing and launching websites with AI from first sketch to live site, and brings that same build-first approach to every team he trains.</p></div>
</div></div></section>
{CTA}'''

contact = f'''
<section class="page-hero">{STRATA}<div class="wrap">
  <span class="eyebrow reveal">Contact</span>
  <h1 class="reveal">Let's talk.</h1>
  <p class="lead reveal">Pick a time for a free 30-minute discovery call, or send a message and we'll reply within one business day.</p>
</div></section>
<section style="padding-top:10px"><div class="wrap"><div class="contact-grid">
  <div class="booking reveal"><div><h3>Booking calendar</h3><p>Your Calendly scheduler appears here once it's connected.</p></div></div>
  <form class="contact reveal" id="contact-form" action="mailto:support@talusconsulting.net" method="post" enctype="text/plain">
    <label for="n">Name</label><input id="n" name="name" required>
    <label for="c">Company</label><input id="c" name="company">
    <label for="e">Email</label><input id="e" name="email" type="email" required>
    <label for="m">What would you like AI to help with?</label><textarea id="m" name="message"></textarea>
    <button class="btn btn-primary" type="submit">Send message <span class="arr">&rarr;</span></button>
    <p class="form-note">This opens your email app with your message ready to send. We use your details only to reply to you. See our <a href="privacy.html">Privacy Policy</a>.</p>
  </form>
</div></div></section>'''


def legal_page(title, updated, html):
    return f"""
<section class="page-hero">{STRATA}<div class="wrap">
  <span class="eyebrow">Legal</span>
  <h1>{title}</h1>
  <p class="lead">Last updated {updated}</p>
</div></section>
<section style="padding-top:10px"><div class="wrap legal">
{html}
</div></section>"""

privacy = legal_page("Privacy Policy", "November 7, 2026", """
<p>This policy explains what information Talus (&ldquo;we&rdquo;, &ldquo;us&rdquo;) collects through talusconsulting.net and how we use it. If you have questions, email <a href="mailto:support@talusconsulting.net">support@talusconsulting.net</a>.</p>
<h2>Information we collect</h2>
<ul>
<li><strong>Information you send us.</strong> When you email us or use the contact form, we receive your name, company, email address and anything you choose to write.</li>
<li><strong>Bookings.</strong> If you book a call through our scheduling tool, the scheduling provider collects your name, email and chosen time and shares them with us.</li>
<li><strong>Payments.</strong> Course and workshop payments are processed by our payment provider. We do not receive or store your full card number.</li>
<li><strong>Technical data.</strong> Our website host and domain provider may automatically log basic technical data, such as your IP address and browser type, for security and reliability. We do not use advertising cookies, analytics trackers or third-party fonts.</li>
</ul>
<h2>How we use it</h2>
<p>We use your information to reply to you, schedule and deliver our services, process payments, keep records required by law, and protect our website. We do not sell your personal information, and we do not share it for advertising.</p>
<h2>Who we share it with</h2>
<p>We share information only with service providers that help us run the business (for example our email, scheduling, payment and website hosting providers), when required by law, or to protect our rights. These providers may only use it to provide their services to us.</p>
<h2>How long we keep it</h2>
<p>We keep your information only as long as we need it for the purposes above or as required for tax and legal records, then delete it.</p>
<h2>Security</h2>
<p>We use reasonable safeguards, including encrypted connections and limited access to your information. No method of transmission or storage is completely secure. If a breach affects your personal information, we will notify you as required by law.</p>
<h2>Your choices and rights</h2>
<p>You can ask us to tell you what personal information we hold about you, correct it, or delete it, by emailing <a href="mailto:support@talusconsulting.net">support@talusconsulting.net</a>. You can unsubscribe from any marketing email at any time using the link in that email. We will respond within 45 days.</p>
<h2>Children</h2>
<p>Our services are for businesses and are not directed to children under 13. We do not knowingly collect information from children.</p>
<h2>Changes</h2>
<p>We may update this policy. The date at the top shows when it last changed.</p>
""")

terms = legal_page("Terms of Use", "November 7, 2026", """
<p>These terms apply to your use of talusconsulting.net. By using the site you agree to them. Separate written agreements govern paid consulting, workshops and courses.</p>
<h2>Information on this site</h2>
<p>Content on this site, including the &ldquo;Ask Talus&rdquo; sample ideas, is general information for educational purposes. It is not legal, financial, tax or other professional advice, and it is not a promise of any particular result. AI tools can produce inaccurate output, so review any AI-generated work before relying on it.</p>
<h2>Courses and workshops</h2>
<p>Prices, schedules and what is included are described at the time of purchase. </p>
<h3 id="refunds">Refunds</h3>
<ul>
<li><strong>Self-paced courses</strong> give you immediate access to digital content, so all sales are final and they are not refundable. Please review the course description before you buy.</li>
<li><strong>Live workshops</strong> can be cancelled for a full refund up to 7 days before the start date. Within 7 days, we can move your seat to a later session instead. If Talus cancels or reschedules a workshop, you may choose a full refund.</li>
<li><strong>Consulting and custom bootcamps</strong> follow the payment and cancellation terms in your written agreement.</li>
</ul>
<p>Nothing in these terms limits any rights you have under applicable law.</p>
<h2>Intellectual property</h2>
<p>The Talus name, logo, website design, course materials and content are owned by Talus and may not be copied, resold or redistributed without written permission. Course purchases give you a personal, non-transferable license for your own or your team&rsquo;s internal use, as stated at purchase.</p>
<h2>Acceptable use</h2>
<p>Do not misuse the site, attempt to access it without authorization, or use it to send spam or harmful content.</p>
<h2>Disclaimer and limitation of liability</h2>
<p>The site is provided &ldquo;as is&rdquo; without warranties of any kind. To the fullest extent permitted by law, Talus is not liable for indirect, incidental or consequential damages arising from your use of the site, and our total liability for any claim related to the site will not exceed $100.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Texas. Any dispute will be handled in the state or federal courts located in Brewster County, Texas.</p>
<h2>Contact</h2>
<p>Questions about these terms: <a href="mailto:support@talusconsulting.net">support@talusconsulting.net</a>.</p>
""")

P = [
 ('index.html', 'Talus · AI training for business', 'Talus trains companies to adopt AI with practical workshops, courses and implementation support.', home),
 ('services.html', 'Services · Talus', 'AI readiness assessments, team workshops and implementation coaching for businesses.', services),
 ('courses.html', 'Courses · Talus', 'Self-paced and live AI courses for teams and leaders.', courses),
 ('about.html', 'About · Talus', "Why Talus exists and who's behind it.", about),
 ('contact.html', 'Book a call · Talus', 'Book a free 30-minute AI discovery call.', contact),
 ('privacy.html', 'Privacy Policy · Talus', 'How Talus collects, uses and protects your information.', privacy),
 ('terms.html', 'Terms of Use · Talus', 'Terms for using the Talus website.', terms),
]
for f, t, d, b in P:
    open(f'{OUT}/{f}', 'w').write(page(f, t, d, b))
print('ok')
