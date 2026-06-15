(function () {
  // Only run on the DesignSystemSettings edit page
  var match = window.location.pathname.match(
    /^\/admin\/settings\/home\/designsystemsettings\/(\d+)\//
  );
  if (!match) return;

  var sitePk = match[1];

  var observer = new MutationObserver(function () {
    var nav = document.querySelector("nav.actions--primary.footer__container");
    if (!nav) return;
    if (nav.querySelector(".ks-reset-btn")) return;

    var btn = document.createElement("a");
    btn.className = "button button-secondary button--icon text-icon ks-reset-btn";
    btn.href = "#";
    btn.innerHTML =
      '<svg class="icon icon-rotate icon" aria-hidden="true"><use href="#icon-rotate"></use></svg>Reset to defaults';
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      if (
        !confirm(
          "Reset all global settings to their default values? This cannot be undone."
        )
      )
        return;
      window.location.href =
        "/admin/settings/home/designsystemsettings/reset/" + sitePk + "/";
    });

    nav.appendChild(btn);
    observer.disconnect();
  });

  observer.observe(document.body, { childList: true, subtree: true });
})();
