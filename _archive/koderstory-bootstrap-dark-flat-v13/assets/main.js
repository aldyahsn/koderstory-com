(function () {
  function updateNavbar() {
    var nav = document.querySelector(".ks-navbar");
    if (!nav) return;

    if (window.scrollY > 0) {
      nav.classList.add("ks-navbar-scrolled");
    } else {
      nav.classList.remove("ks-navbar-scrolled");
    }
  }

  document.addEventListener("DOMContentLoaded", updateNavbar);
  window.addEventListener("scroll", updateNavbar, { passive: true });
})();