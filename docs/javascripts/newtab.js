// Open external links in a new tab so the venue map stays open.
// Material for MkDocs re-renders pages on instant navigation, hence document$.
(function () {
  function externalize() {
    var host = window.location.host;
    document.querySelectorAll("a[href]").forEach(function (anchor) {
      var url;
      try {
        url = new URL(anchor.href, window.location.href);
      } catch (err) {
        return;
      }
      if (url.protocol.indexOf("http") !== 0 || url.host === host) {
        return;
      }
      anchor.target = "_blank";
      anchor.rel = "noopener noreferrer";
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(externalize);
  } else {
    document.addEventListener("DOMContentLoaded", externalize);
  }
})();
