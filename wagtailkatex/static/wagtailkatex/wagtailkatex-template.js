Array.from(
  document.querySelectorAll("[data-katex-embed]")
).map(
  (el) => Preview.renderToElement(el.dataset.katexEmbed, el)
);
