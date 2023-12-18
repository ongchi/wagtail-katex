![PyPI Package Version](https://img.shields.io/pypi/v/wagtail-katex)
![Python Version](https://img.shields.io/pypi/pyversions/wagtail-cjkcms)
![Wagtail Version](https://img.shields.io/pypi/frameworkversions/wagtail/wagtail-katex)
![License](https://img.shields.io/github/license/ongchi/wagtail-katex)

Math typesetting for [Wagtail CMS](https://wagtail.org/) powered by **[KaTeX](https://katex.org)**.

> This package is forked from [gatensj/wagtail-draftail-katex](https://github.com/gatensj/wagtail-draftail-katex).  
> This package contains svg icon from [Font Awesome](http://fontawesome.io), which is licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0).

![KaTeX Editor Screenshot](https://raw.githubusercontent.com/ongchi/wagtail-katex/master/screenshots/screenshot_katex_editor.png)

## Quick Start

### Installation

Install the package using the following command:

```sh
pip install wagtail-katex
```

Add `wagtailkatex` to the `INSTALLED_APPS` section in your `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    "wagtailkatex",
    ...
]
```

Add `RichTextField` to your page model, then you should find the math typesetting
icon in the toolbar of rich-text editor in Wagtail admin views.

### Template rendering

Add required assets to your page template:

```html
{% load wagtailkatex %}

<link rel="stylesheet" href="{% wagtailkatex_media 'css' %}" />
<script src="{% wagtailkatex_media 'js' %}"></script>
<script src="{% static 'wagtailkatex/wagtailkatex-template.js' %}"></script>
```

The page content contains `KaTeX` embed should render properly.

### Config

The `KaTeX` library is linked directly to a CDN distribution by default.
If you want to change to the nearby server,
the path could be specified in the `settings.py` file:

```python
WAGTAIL_KATEX = {
    "js": "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"
    "css": "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css"
}
```

Alternatively, you can make your own copy in the static folder and serve it as Django static files:

```python
WAGTAIL_KATEX = {
    "js": "my_app/katex.min.js"
    "css": "my_app/katex.min.css"
}
```
