// Talus — site interactions
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header border on scroll + mobile menu
  const header = document.querySelector('.site-header');
  const onScroll = () => header && header.classList.toggle('scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const btn = document.querySelector('.menu-btn'), links = document.querySelector('.nav-links');
  if (btn && links) btn.addEventListener('click', () => {
    const open = links.classList.toggle('open'); btn.setAttribute('aria-expanded', open);
  });

  // Reveal on scroll
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.15 });
  document.querySelectorAll('.reveal, .step').forEach(el => io.observe(el));

  // Hero: a living network of nodes that settles into strata (the Talus mark) near the edge
  const canvas = document.getElementById('net');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let W, H, dpr, nodes = [], mouse = { x: -9999, y: -9999 };
    const BRASS = [176, 141, 87], NAVY = [20, 33, 61];
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = W * dpr; canvas.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const count = Math.round(Math.min(90, Math.max(36, W * H / 16000)));
      nodes = Array.from({ length: count }, () => ({
        x: Math.random() * W, y: Math.random() * H,
        vx: (Math.random() - .5) * .25, vy: (Math.random() - .5) * .25,
        r: Math.random() * 1.6 + 1, b: Math.random() < .28
      }));
    }
    let t = 0;
    function frame() {
      t++;
      ctx.clearRect(0, 0, W, H);
      for (const n of nodes) {
        if (!reduce) { n.x += n.vx; n.y += n.vy; }
        if (n.x < -20) n.x = W + 20; if (n.x > W + 20) n.x = -20;
        if (n.y < -20) n.y = H + 20; if (n.y > H + 20) n.y = -20;
        const dx = n.x - mouse.x, dy = n.y - mouse.y, d = Math.hypot(dx, dy);
        if (d < 140 && d > 0) { n.x += dx / d * .6; n.y += dy / d * .6; }
      }
      const max = Math.min(160, W / 7);
      for (let i = 0; i < nodes.length; i++) for (let j = i + 1; j < nodes.length; j++) {
        const a = nodes[i], b = nodes[j], d = Math.hypot(a.x - b.x, a.y - b.y);
        if (d < max) {
          const o = (1 - d / max) * .22, c = a.b && b.b ? BRASS : NAVY;
          ctx.strokeStyle = `rgba(${c},${o})`; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
        }
      }
      for (const n of nodes) {
        const pulse = n.b ? .55 + .35 * Math.sin(t / 40 + n.x) : .28;
        ctx.fillStyle = `rgba(${n.b ? BRASS : NAVY},${pulse})`;
        ctx.beginPath(); ctx.arc(n.x, n.y, n.b ? n.r + .8 : n.r, 0, Math.PI * 2); ctx.fill();
      }
      if (!reduce) requestAnimationFrame(frame);
    }
    size(); frame();
    window.addEventListener('resize', () => { size(); if (reduce) frame(); });
    canvas.parentElement.addEventListener('pointermove', e => {
      const r = canvas.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top;
    });
    canvas.parentElement.addEventListener('pointerleave', () => { mouse.x = mouse.y = -9999; });
  }

  // "Ask Talus" demo — curated ideas by industry, typed out live
  const ask = document.getElementById('ask-form');
  if (ask) {
    const IDEAS = {
      retail: ['<b>Demand forecasting</b> that predicts which products to reorder, and when.', '<b>Product descriptions</b> written in your brand voice in seconds, for every SKU.', '<b>A customer chat assistant</b> that answers sizing, stock and returns questions 24/7.'],
      healthcare: ['<b>Visit notes drafted automatically</b>, so clinicians spend time with patients, not paperwork.', '<b>Smarter scheduling</b> that predicts no-shows and fills gaps.', '<b>Plain-language patient instructions</b> generated from care plans.'],
      'real estate': ['<b>Listing descriptions and social posts</b> drafted from a few photos and notes.', '<b>Lead follow-up</b> that responds instantly and books showings.', '<b>Market summaries</b> for clients, built from comps in minutes.'],
      law: ['<b>First-pass contract review</b> that flags unusual clauses for a lawyer to check.', '<b>Research summaries</b> that cut hours from case prep.', '<b>Client intake</b> that gathers facts before the first meeting.'],
      manufacturing: ['<b>Predictive maintenance</b> that spots equipment trouble before it stops the line.', '<b>Visual quality inspection</b> that catches defects people miss.', '<b>Instant answers from manuals and SOPs</b> for every operator on the floor.'],
      restaurant: ['<b>Inventory and prep forecasting</b> that cuts food waste.', '<b>Review replies and social posts</b> written in your voice.', '<b>Staff scheduling</b> matched to predicted traffic.'],
      construction: ['<b>Bid and estimate drafting</b> from plans and past jobs.', '<b>Daily site reports</b> generated from photos and voice notes.', '<b>Safety and compliance checks</b> summarized for every project.'],
      finance: ['<b>Automated bookkeeping</b> that categorizes transactions and flags anomalies.', '<b>Client reports</b> drafted in plain language from the numbers.', '<b>Document processing</b> that reads invoices, statements and forms for you.'],
      marketing: ['<b>Campaign drafts</b> across email, social and ads from a single brief.', '<b>Audience insights</b> pulled from your customer data in minutes.', '<b>Content repurposing</b>: one webinar becomes ten posts.'],
      education: ['<b>Lesson and quiz drafting</b> aligned to your curriculum.', '<b>Personalized feedback</b> on student work, at scale.', '<b>Admin automation</b> for scheduling, reminders and reports.']
    };
    const ALIAS = { store: 'retail', ecommerce: 'retail', shop: 'retail', medical: 'healthcare', clinic: 'healthcare', dental: 'healthcare', health: 'healthcare', realtor: 'real estate', property: 'real estate', legal: 'law', attorney: 'law', factory: 'manufacturing', food: 'restaurant', cafe: 'restaurant', bar: 'restaurant', contractor: 'construction', builder: 'construction', accounting: 'finance', bank: 'finance', insurance: 'finance', agency: 'marketing', school: 'education', training: 'education' };
    const esc = t => t.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    const generic = raw => { const x = esc(raw.slice(0, 60)); return [`<b>A knowledge assistant</b> that answers your team's questions about ${x} processes instantly.`, `<b>Automated first drafts</b> of the emails, proposals and reports your ${x} team writes every week.`, `<b>Data-driven insights</b> that surface trends in your ${x} numbers before you'd spot them.`]; };
    const input = document.getElementById('ask-input'), out = document.getElementById('ask-answer');
    const askBtn = document.getElementById('ask-btn'), chips = document.querySelectorAll('.chip');
    const list = out.querySelector('ol'), cta = out.querySelector('.cta');
    let busy = false;
    function pick(q) {
      const s = q.toLowerCase();
      for (const k of Object.keys(IDEAS)) if (s.includes(k)) return IDEAS[k];
      for (const [a, k] of Object.entries(ALIAS)) if (s.includes(a)) return IDEAS[k];
      return generic(q.trim().toLowerCase() || 'business');
    }
    async function type(li, html) {
      const tmp = document.createElement('div'); tmp.innerHTML = html;
      const text = tmp.textContent, caret = '<span class="caret"></span>';
      if (reduce) { li.innerHTML = html; return; }
      for (let i = 1; i <= text.length; i += 2) {
        li.textContent = text.slice(0, i); li.insertAdjacentHTML('beforeend', caret);
        await new Promise(r => setTimeout(r, 12));
      }
      li.innerHTML = html;
    }
    const wait = ms => new Promise(r => setTimeout(r, ms));
    async function run(q, chip) {
      if (busy || !q.trim()) return; busy = true;
      chips.forEach(c => c.setAttribute('aria-pressed', c === chip));
      if (askBtn) { askBtn.disabled = true; askBtn.setAttribute('aria-busy', 'true'); }
      out.classList.add('show'); cta.classList.remove('show');
      // Loading state: a short "thinking" row before the ideas type out
      list.innerHTML = '<li class="thinking" aria-label="Finding ideas"><span class="dots"><i></i><i></i><i></i></span>Finding ideas for your business&hellip;</li>';
      if (!reduce) await wait(650);
      list.innerHTML = '';
      const ideas = pick(q);
      for (const idea of ideas) { const li = document.createElement('li'); list.appendChild(li); await type(li, idea); }
      cta.classList.add('show'); busy = false;
      if (askBtn) { askBtn.disabled = false; askBtn.removeAttribute('aria-busy'); }
    }
    ask.addEventListener('submit', e => { e.preventDefault(); run(input.value); });
    chips.forEach(c => { c.setAttribute('aria-pressed', 'false'); c.addEventListener('click', () => { input.value = c.textContent; run(c.textContent, c); }); });
  }

  // Calendly embed: show a loading state until the calendar arrives, and point to the fallback link if it's slow
  const booking = document.querySelector('.booking');
  if (booking) {
    const frame = booking.querySelector('iframe');
    const done = () => booking.classList.add('loaded');
    if (frame) frame.addEventListener('load', done);
    setTimeout(() => { if (!booking.classList.contains('loaded')) booking.classList.add('slow'); }, 10000);
  }

  // Contact form: confirm the click did something (it hands off to the visitor's email app)
  const form = document.getElementById('contact-form');
  if (form) form.addEventListener('submit', () => {
    const b = form.querySelector('button[type=submit]'); if (!b) return;
    const html = b.innerHTML;
    b.innerHTML = '<span class="check" aria-hidden="true"></span> Opening your email app';
    setTimeout(() => { b.innerHTML = html; }, 4000);
  });

  const y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
