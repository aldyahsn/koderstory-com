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

  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function toHex(value) {
    return clamp(Math.round(value), 0, 255).toString(16).padStart(2, "0");
  }

  function alphaToHex(alpha) {
    return toHex((clamp(alpha, 0, 100) / 100) * 255);
  }

  function hexToAlpha(hex) {
    return Math.round((parseInt(hex, 16) / 255) * 100);
  }

  function parseHex(value) {
    const match = value
      .trim()
      .match(/^#([0-9a-f]{3}|[0-9a-f]{4}|[0-9a-f]{6}|[0-9a-f]{8})$/i);
    if (!match) return null;

    const raw = match[1];
    if (raw.length === 3 || raw.length === 4) {
      const chars = raw.split("");
      return {
        hex: `#${chars[0]}${chars[0]}${chars[1]}${chars[1]}${chars[2]}${chars[2]}`,
        alpha: raw.length === 4 ? hexToAlpha(`${chars[3]}${chars[3]}`) : 100,
      };
    }

    return {
      hex: `#${raw.slice(0, 6)}`,
      alpha: raw.length === 8 ? hexToAlpha(raw.slice(6, 8)) : 100,
    };
  }

  function parseRgb(value) {
    const match = value
      .trim()
      .match(/^rgba?\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)(?:\s*,\s*([0-9.]+))?\s*\)$/i);
    if (!match) return null;

    const alpha =
      match[4] === undefined ? 100 : clamp(Number(match[4]) * 100, 0, 100);

    return {
      hex: `#${toHex(Number(match[1]))}${toHex(Number(match[2]))}${toHex(Number(match[3]))}`,
      alpha,
    };
  }

  function colorState(value) {
    if (!value.trim()) {
      return { hex: "#ffffff", alpha: 100, preview: "transparent", blank: true };
    }

    const parsed = parseHex(value) || parseRgb(value);
    if (parsed) {
      return {
        ...parsed,
        preview: colorValue(parsed.hex, parsed.alpha),
        blank: false,
      };
    }

    return {
      hex: "#ffffff",
      alpha: 100,
      preview: CSS.supports("color", value) ? value : "transparent",
      blank: false,
    };
  }

  function colorValue(hex, alpha) {
    return alpha >= 100 ? hex : `${hex}${alphaToHex(alpha)}`;
  }

  function initColorInputs(root = document) {
    root
      .querySelectorAll("[data-ks-color-input]")
      .forEach((widget) => {
        if (widget.dataset.ksColorInputReady === "true") return;

        const input = widget.querySelector(".ks-color-input__value");
        const picker = widget.querySelector(".ks-color-input__picker");
        const alpha = widget.querySelector(".ks-color-input__alpha-range");
        const alphaOutput = widget.querySelector(".ks-color-input__alpha-output");

        if (!input || !picker || !alpha || !alphaOutput) return;
        widget.dataset.ksColorInputReady = "true";

        const refresh = (syncPicker = true) => {
          const state = colorState(input.value);
          if (syncPicker) picker.value = state.hex;
          alpha.value = String(Math.round(state.alpha));
          alphaOutput.value = `${Math.round(state.alpha)}%`;
          picker.style.background = state.preview;
        };

        input.addEventListener("input", refresh);
        picker.addEventListener("input", () => {
          input.value = colorValue(picker.value, Number(alpha.value));
          refresh(false);
        });
        alpha.addEventListener("input", () => {
          input.value = colorValue(picker.value, Number(alpha.value));
          refresh(false);
        });

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
    initColorInputs();

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
