![PyPI Package Version](https://img.shields.io/pypi/v/wagtail-katex)
![Python Version](https://img.shields.io/pypi/pyversions/wagtail-cjkcms)
![Wagtail Version](https://img.shields.io/pypi/frameworkversions/wagtail/wagtail-katex)
![License](https://img.shields.io/github/license/ongchi/wagtail-katex)

Math typesetting for [Wagtail CMS](https://wagtail.org/) powered by **[KaTeX](https://katex.org)**.

> This package is forked from [gatensj/wagtail-draftail-katex](https://github.com/gatensj/wagtail-draftail-katex).  
> This package contains svg icon from [Font Awesome](http://fontawesome.io), which is licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0).

![KaTeX Editor Screenshot](https://raw.githubusercontent.com/ongchi/wagtail-katex/master/screenshots/screenshot_katex_editor.png)

## Quick Start

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

Now you will see the math typesetting icon displayed in the toolbar of
rich text fields in Wagtail admin views.
