(function () {
  var match = window.location.pathname.match(
    /^\/admin\/snippets\/home\/colortheme\/edit\/(\d+)\//
  );
  if (!match) return;

  var themePk = parseInt(match[1], 10);
  if (themePk === 1) return; // never show on "Default"

  var observer = new MutationObserver(function () {
    var nav = document.querySelector("nav.actions--primary.footer__container");
    if (!nav) return;
    if (nav.querySelector(".ks-set-default-btn")) return;

    var btn = document.createElement("a");
    btn.className =
      "button button-secondary button--icon text-icon ks-set-default-btn";
    btn.href = "#";
    btn.innerHTML =
      '<svg class="icon icon-resubmit icon" aria-hidden="true"><use href="#icon-resubmit"></use></svg>Set as site default';
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      if (
        !confirm(
          "Replace all sections using this theme with the Default theme? Sections using other themes will not be affected."
        )
      )
        return;
      window.location.href =
        "/admin/snippets/home/colortheme/" + themePk + "/set-default/";
    });

    nav.appendChild(btn);
    observer.disconnect();
  });

  observer.observe(document.body, { childList: true, subtree: true });
})();
