(() => {
  const bar = document.getElementById("reading-progress-bar");
  if (!bar) return;
  const update = () => {
    const root = document.documentElement;
    const max = root.scrollHeight - root.clientHeight;
    const pct = max > 0 ? Math.min(100, Math.max(0, (root.scrollTop / max) * 100)) : 0;
    bar.style.width = pct + "%";
  };
  update();
  document.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
})();
