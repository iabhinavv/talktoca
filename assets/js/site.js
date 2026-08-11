/* talktoca.in — minimal progressive enhancement (nav only). */
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
})();
