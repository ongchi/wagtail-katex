Array.from(
  document.querySelectorAll("[data-katex-embed]")
).map(
  (el) => window.katex.render(el.dataset.katexEmbed, el)
);
