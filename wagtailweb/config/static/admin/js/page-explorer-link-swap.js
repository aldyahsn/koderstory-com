(() => {
  const rowSelector = ".c-page-explorer__item";
  const titleLinkSelector = ".c-page-explorer__item__link";
  const actionLinkSelector = ".c-page-explorer__item__action--small";

  const getPageUrls = (row) => {
    const titleLink = row.querySelector(titleLinkSelector);
    const actionLink = row.querySelector(actionLinkSelector);

    if (!titleLink || !actionLink) {
      return null;
    }

    const pageUrl =
      row.dataset.ksPageExplorerUrl ||
      actionLink.href.replace(/edit\/(?:\?.*)?$/, "");

    if (!row.dataset.ksPageExplorerUrl && pageUrl === actionLink.href) {
      return null;
    }

    row.dataset.ksPageExplorerUrl = pageUrl;

    return {
      titleLink,
      actionLink,
      pageUrl,
      editUrl: `${pageUrl}edit/`,
    };
  };

  const updateRow = (row) => {
    const urls = getPageUrls(row);
    if (!urls) {
      return;
    }

    urls.titleLink.href = urls.editUrl;
    urls.actionLink.href = urls.pageUrl;

    const icon = urls.actionLink.querySelector("svg use");
    if (icon) {
      icon.setAttribute("href", "#icon-arrow-right");
      icon.setAttribute("xlink:href", "#icon-arrow-right");
    }

    const title = urls.actionLink.querySelector("svg title");
    if (title) {
      title.textContent = "View child pages";
    }
  };

  const updateRows = (root) => {
    root.querySelectorAll(rowSelector).forEach(updateRow);
  };

  document.addEventListener(
    "click",
    (event) => {
      const target = event.target instanceof Element ? event.target : null;
      const link = target?.closest(`${titleLinkSelector}, ${actionLinkSelector}`);
      const row = link?.closest(rowSelector);
      const urls = row && getPageUrls(row);

      if (!link || !urls) {
        return;
      }

      const destination = link === urls.titleLink ? urls.editUrl : urls.pageUrl;
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
