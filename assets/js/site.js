/* talktoca.in — progressive enhancement: sticky header, mobile nav, scroll reveals. */
(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.menu-btn');
  var mobileNav = document.getElementById('mobile-nav');

  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 20);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
  }

  // Fade sections in as they scroll into view. Anything already on screen at
  // load is left alone (no flash), and nothing happens for reduced-motion users.
  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      el.classList.add('in');
      io.unobserve(el);
      // Hand the element back to its own hover transitions once it has settled.
      setTimeout(function () { el.classList.remove('reveal', 'in'); }, 1300);
    });
  }, { rootMargin: '0px 0px -8% 0px' });

  var sel = '.section-head, .card, .folder, .stat, .quote-card, .job, .link-grid li, ' +
            '.cta-band, .table-scroll, .prose > h2, .split > div';
  Array.prototype.forEach.call(document.querySelectorAll(sel), function (el) {
    if (el.getBoundingClientRect().top < window.innerHeight) return;
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.setProperty('--d', (Math.min(i, 5) * 0.08) + 's');
    el.classList.add('reveal');
    io.observe(el);
  });
})();
