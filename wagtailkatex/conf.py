from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static

DEFAULT_ENGINE = "katex"

DEFAULT_MATHJAX_SETTINGS = {
    "js": [
        "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-MML-AM_CHTML",
    ],
    "preview": [
        "wagtailkatex/mathjax_preview.js",
    ],
}

DEFAULT_KATEX_SETTINGS = {
    "css": ["https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.css"],
    "js": [
        "https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/katex.min.js",
        "https://cdn.jsdelivr.net/npm/katex@0.16.10/dist/contrib/auto-render.min.js",
    ],
    "preview": ["wagtailkatex/katex_preview.js"],
}

WAGTAILKATEX_ENGINE = getattr(settings, "WAGTAILPOLYMATH_ENGINE", DEFAULT_ENGINE)
WAGTAILKATEX_SETTINGS = globals()[f"DEFAULT_{WAGTAILKATEX_ENGINE.upper()}_SETTINGS"]
WAGTAILKATEX_SETTINGS.update(getattr(settings, "WAGTAILPOLYMATH_SETTINGS", {}))


def get_conf(key):
    urls = WAGTAILKATEX_SETTINGS.get(key, [])

    return [static(_url) if finders.find(_url) else _url for _url in urls]
