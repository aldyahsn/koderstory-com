(() => {
  const variants = window.KS_SECTION_VARIANTS || {};

  function closeHelpTooltips(except = null) {
    document
      .querySelectorAll(".ks-help-tooltip-field.is-help-open")
      .forEach((field) => {
        if (field === except) return;
        field.classList.remove("is-help-open");
        field
          .querySelector(".ks-help-tooltip__trigger")
          ?.setAttribute("aria-expanded", "false");
      });
  }

  function initHelpTooltips(root = document) {
    root.querySelectorAll("[data-field-wrapper]").forEach((fieldWrapper) => {
      if (fieldWrapper.dataset.ksHelpTooltipReady === "true") return;

      const help = fieldWrapper.querySelector("[data-field-help]");
      if (!help || !help.textContent.trim()) return;

      const panel = fieldWrapper.parentElement;
      const label = panel?.querySelector(":scope > .w-field__label");
      if (!panel || !label) return;

      fieldWrapper.dataset.ksHelpTooltipReady = "true";
      panel.classList.add("ks-help-tooltip-field");
      help.classList.add("ks-help-tooltip__content");
      help.setAttribute("role", "tooltip");

      const trigger = document.createElement("button");
      trigger.type = "button";
      trigger.className = "ks-help-tooltip__trigger";
      trigger.textContent = "i";
      trigger.setAttribute(
        "aria-label",
        `Help for ${label.textContent.trim() || "this field"}`,
      );
      trigger.setAttribute("aria-expanded", "false");

      if (help.id) {
        trigger.setAttribute("aria-controls", help.id);
        trigger.setAttribute("aria-describedby", help.id);
      }

      label.insertAdjacentElement("afterend", trigger);

      trigger.addEventListener("click", (event) => {
        event.stopPropagation();
        const willOpen = !panel.classList.contains("is-help-open");
        closeHelpTooltips(willOpen ? panel : null);
        panel.classList.toggle("is-help-open", willOpen);
        trigger.setAttribute("aria-expanded", String(willOpen));
      });

      trigger.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") return;
        panel.classList.remove("is-help-open");
        trigger.setAttribute("aria-expanded", "false");
        trigger.focus();
      });
    });
  }

  function initColorPreviews(root = document) {
    root
      .querySelectorAll('.ks-global-color-group input[type="text"]')
      .forEach((input) => {
        if (input.dataset.ksColorPreviewReady === "true") return;
        input.dataset.ksColorPreviewReady = "true";

        const refresh = () => {
          const value = input.value.trim();
          const isColor = CSS.supports("color", value);
          input.style.setProperty(
            "--ks-color-preview",
            isColor ? value : "transparent",
          );
        };

        input.addEventListener("input", refresh);
        refresh();
      });
  }

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
    initHelpTooltips();
    initColorPreviews();

    Object.keys(variants).forEach((section) => {
      const select = document.querySelector(`[name="${section}_layout"]`);
      if (!select) return;
      select.addEventListener("change", () => refreshSection(section));
      refreshSection(section);
    });
  }

  document.addEventListener("click", (event) => {
    if (!event.target.closest(".ks-help-tooltip-field")) {
      closeHelpTooltips();
    }
  });
  document.addEventListener("DOMContentLoaded", init);
  document.addEventListener("w-formset:ready", init);
})();
