(() => {
  const variants = window.KS_SECTION_VARIANTS || {};

  function refreshSection(section) {
    const select = document.querySelector(`[name="${section}_layout"]`);
    if (!select || !variants[section]) return;

    const enabled = new Set(variants[section][select.value] || []);
    document
      .querySelectorAll(
        `.ks-component-group[data-section="${section}"][data-component]`,
      )
      .forEach((panel) => {
        panel.hidden = !enabled.has(panel.dataset.component);
      });
  }

  function init() {
    Object.keys(variants).forEach((section) => {
      const select = document.querySelector(`[name="${section}_layout"]`);
      if (!select) return;
      select.addEventListener("change", () => refreshSection(section));
      refreshSection(section);
    });
  }

  document.addEventListener("DOMContentLoaded", init);
  document.addEventListener("w-formset:ready", init);
})();
