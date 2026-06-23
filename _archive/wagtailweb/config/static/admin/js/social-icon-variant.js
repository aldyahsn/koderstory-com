(function () {
  // Platforms that have a filled variant in Tabler Icons.
  // Derived from home/templatetags/social_icons.py — platforms whose
  // "filled" key is not None.
  var PLATFORMS_WITH_FILLED = {
    facebook: true,
    linkedin: true,
    x: true,
    instagram: true,
    youtube: true,
    tiktok: true,
    whatsapp: true,
    pinterest: true,
    tumblr: true,
    github: true,
  };

  function prefixFromId(id) {
    // id like "id_links-0-platform" → prefix "links-0-"
    var m = id.match(/^id_(.+)-platform$/);
    return m ? m[1] + "-" : null;
  }

  function getIconVariantSelect(prefix) {
    return document.getElementById("id_" + prefix + "icon_variant");
  }

  function updateIconVariant(platformSelect) {
    var prefix = prefixFromId(platformSelect.id);
    if (!prefix) return;

    var variantSelect = getIconVariantSelect(prefix);
    if (!variantSelect) return;

    var platform = platformSelect.value;
    var hasFilled = PLATFORMS_WITH_FILLED[platform] === true;

    // Remember current selection, default to "outline" when missing.
    var currentVal = variantSelect.value;
    var currentHtml = "";

    if (hasFilled) {
      currentHtml = '<option value="filled">Filled</option><option value="outline">Outline</option>';
    } else {
      currentHtml = '<option value="outline">Outline</option>';
    }

    variantSelect.innerHTML = currentHtml;

    // If the previously selected variant is still valid, restore it.
    if ((hasFilled && currentVal === "filled") || currentVal === "outline") {
      variantSelect.value = currentVal;
    }
  }

  function initPlatformSelect(select) {
    if (select.dataset.ksIconVariantInit) return;
    select.dataset.ksIconVariantInit = "1";
    select.addEventListener("change", function () {
      updateIconVariant(this);
    });
    // Apply immediately so the initial state is correct.
    updateIconVariant(select);
  }

  function scanForPlatformSelects(root) {
    var selects = root.querySelectorAll("select[id$=-platform]");
    for (var i = 0; i < selects.length; i++) {
      initPlatformSelect(selects[i]);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    scanForPlatformSelects(document);

    // Watch for new InlinePanel forms added dynamically.
    var observer = new MutationObserver(function (mutations) {
      for (var i = 0; i < mutations.length; i++) {
        for (var j = 0; j < mutations[i].addedNodes.length; j++) {
          var node = mutations[i].addedNodes[j];
          if (node.nodeType === 1) {
            scanForPlatformSelects(node);
          }
        }
      }
    });

    observer.observe(document.body, { childList: true, subtree: true });
  });
})();
