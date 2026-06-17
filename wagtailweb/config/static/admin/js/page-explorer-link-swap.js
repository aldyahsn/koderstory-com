(() => {
  const rowSelector = ".c-page-explorer__item";
  const titleLinkSelector = ".c-page-explorer__item__link";
  const editActionSelector = ".c-page-explorer__item__action--small";
  const exploreActionSelector =
    '.c-page-explorer__item__action[data-ks-page-explorer-action="explore"]';
  const childActionSelector =
    ".c-page-explorer__item__action:not(.c-page-explorer__item__action--small)";

  const setIcon = (link, iconName, titleText) => {
    const icon = link.querySelector("svg use");
    if (icon) {
      icon.setAttribute("href", `#icon-${iconName}`);
      icon.setAttribute("xlink:href", `#icon-${iconName}`);
    }

    const title = link.querySelector("svg title");
    if (title) {
      title.textContent = titleText;
    }
  };

  const ensureExploreAction = (row, editAction) => {
    const existingAction =
      row.querySelector(exploreActionSelector) ||
      row.querySelector(childActionSelector);

    if (existingAction) {
      existingAction.dataset.ksPageExplorerAction = "explore";
      return existingAction;
    }

    const exploreAction = editAction.cloneNode(true);
    exploreAction.classList.remove("c-page-explorer__item__action--small");
    exploreAction.dataset.ksPageExplorerAction = "explore";
    editAction.insertAdjacentElement("afterend", exploreAction);

    return exploreAction;
  };

  const getPageUrls = (row) => {
    const titleLink = row.querySelector(titleLinkSelector);
    const editAction = row.querySelector(editActionSelector);

    if (!titleLink || !editAction) {
      return null;
    }

    const pageUrl =
      row.dataset.ksPageExplorerUrl ||
      editAction.href.replace(/edit\/(?:\?.*)?$/, "");

    if (!row.dataset.ksPageExplorerUrl && pageUrl === editAction.href) {
      return null;
    }

    row.dataset.ksPageExplorerUrl = pageUrl;
    const editUrl = `${pageUrl}edit/`;

    return {
      titleLink,
      editAction,
      exploreAction: ensureExploreAction(row, editAction),
      pageUrl,
      editUrl,
    };
  };

  const updateRow = (row) => {
    const urls = getPageUrls(row);
    if (!urls) {
      return;
    }

    urls.titleLink.href = urls.editUrl;
    urls.editAction.href = urls.editUrl;
    urls.exploreAction.href = urls.pageUrl;

    setIcon(urls.editAction, "edit", "Edit this page");
    setIcon(urls.exploreAction, "arrow-right", "View child pages");
  };

  const updateRows = (root) => {
    root.querySelectorAll(rowSelector).forEach(updateRow);
  };

  document.addEventListener(
    "click",
    (event) => {
      const target = event.target instanceof Element ? event.target : null;
      const link = target?.closest(
        `${titleLinkSelector}, ${editActionSelector}, ${exploreActionSelector}, ${childActionSelector}`,
      );
      const row = link?.closest(rowSelector);
      const urls = row && getPageUrls(row);

      if (!link || !urls) {
        return;
      }

      const destination =
        link === urls.titleLink || link === urls.editAction
          ? urls.editUrl
          : urls.pageUrl;
      link.href = destination;

      if (
        event.ctrlKey ||
        event.shiftKey ||
        event.metaKey ||
        event.altKey ||
        event.button !== 0
      ) {
        return;
      }

      event.preventDefault();
      event.stopImmediatePropagation();
      window.location.assign(destination);
    },
    true,
  );

  document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.querySelector("#wagtail-sidebar");
    if (!sidebar) {
      return;
    }

    new MutationObserver((mutations) => {
      for (const mutation of mutations) {
        for (const node of mutation.addedNodes) {
          if (!(node instanceof Element)) {
            continue;
          }

          if (node.matches(rowSelector)) {
            updateRow(node);
          } else {
            updateRows(node);
          }
        }
      }
    }).observe(sidebar, { childList: true, subtree: true });

    updateRows(sidebar);
  });
})();
