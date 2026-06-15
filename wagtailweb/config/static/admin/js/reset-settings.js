(function () {
  var match = window.location.pathname.match(
    /^\/admin\/settings\/home\/designsystemsettings\/(\d+)\//
  );
  if (!match) return;

  var sitePk = match[1];

  var observer = new MutationObserver(function () {
    var nav = document.querySelector("nav.actions--primary.footer__container");
    if (!nav) return;
    if (nav.querySelector(".ks-reset-btn")) return;

    var themeBtn = document.createElement("a");
    themeBtn.className = "button button-secondary button--icon text-icon";
    themeBtn.href = "/admin/snippets/home/colortheme/";
    themeBtn.innerHTML =
      '<svg class="icon icon-cogs icon" aria-hidden="true"><use href="#icon-cogs"></use></svg>Manage color themes';

    var resetBtn = document.createElement("a");
    resetBtn.className = "button button-secondary button--icon text-icon ks-reset-btn";
    resetBtn.href = "#";
    resetBtn.innerHTML =
      '<svg class="icon icon-rotate icon" aria-hidden="true"><use href="#icon-rotate"></use></svg>Reset to defaults';
    resetBtn.addEventListener("click", function (e) {
      e.preventDefault();
      if (!confirm("Reset all global settings to their default values? This cannot be undone.")) return;
      window.location.href = "/admin/settings/home/designsystemsettings/reset/" + sitePk + "/";
    });

    nav.appendChild(themeBtn);
    nav.appendChild(resetBtn);
    observer.disconnect();
  });

  observer.observe(document.body, { childList: true, subtree: true });
})();
