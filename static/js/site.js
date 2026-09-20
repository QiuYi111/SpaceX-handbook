(() => {
  const bar = document.getElementById("reading-progress-bar");
  if (bar) {
    const updateProgress = () => {
      const root = document.documentElement;
      const max = root.scrollHeight - root.clientHeight;
      const pct = max > 0 ? Math.min(100, Math.max(0, (root.scrollTop / max) * 100)) : 0;
      bar.style.width = pct + "%";
    };
    updateProgress();
    document.addEventListener("scroll", updateProgress, { passive: true });
    window.addEventListener("resize", updateProgress);
  }

  const search = document.getElementById("source-search");
  const tier = document.getElementById("source-tier");
  const list = document.getElementById("source-list");
  const count = document.getElementById("source-count");

  if (search && tier && list && count) {
    const rows = Array.from(list.querySelectorAll(".source-row"));
    const applySourceFilter = () => {
      const query = search.value.trim().toLocaleLowerCase();
      const tierPrefix = tier.value;
      let visible = 0;

      for (const row of rows) {
        const haystack = (row.dataset.search || "").toLocaleLowerCase();
        const rowTier = row.dataset.tier || "";
        const matchesText = !query || haystack.includes(query);
        const matchesTier = !tierPrefix || rowTier.startsWith(tierPrefix);
        row.hidden = !(matchesText && matchesTier);
        if (!row.hidden) visible += 1;
      }

      count.textContent = `${visible} / ${rows.length}`;
    };

    search.addEventListener("input", applySourceFilter);
    tier.addEventListener("change", applySourceFilter);
    applySourceFilter();
  }
})();
