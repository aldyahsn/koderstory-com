(function () {
  var navbar = document.querySelector('.ks-navbar');

  if (!navbar) return;

  var isTransparent = navbar.classList.contains('ks-navbar-transparent');
  var hasAnim = navbar.classList.contains('ks-navbar-anim-shrink') ||
                navbar.classList.contains('ks-navbar-anim-reveal');

  if (!isTransparent && !hasAnim) return;

  var lastScrollY = window.scrollY;
  var ticking = false;

  function onScroll() {
    var scrollY = window.scrollY;
    var scrolled = scrollY > 0;

    if (scrolled) {
      navbar.classList.add('ks-navbar-scrolled');
    } else {
      navbar.classList.remove('ks-navbar-scrolled');
    }

    if (navbar.classList.contains('ks-navbar-anim-reveal')) {
      if (scrollY > 50 && scrollY > lastScrollY) {
        navbar.classList.add('ks-navbar-hidden');
      } else {
        navbar.classList.remove('ks-navbar-hidden');
      }
    }

    lastScrollY = scrollY;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(function () {
        onScroll();
        ticking = false;
      });
      ticking = true;
    }
  });
})();
