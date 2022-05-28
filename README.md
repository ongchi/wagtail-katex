# wagtail-katex ![Wagtail 2.x](https://img.shields.io/badge/wagtail-2.x-g.svg) ![Wagtail 3.x](https://img.shields.io/badge/wagtail-3.x-g.svg)

> This package is modified from [gatensj/wagtail-draftail-katex](https://github.com/gatensj/wagtail-draftail-katex)

**[KaTex](https://katex.org)** support for Wagtail RichTextField.

![Inserting an Images](https://raw.githubusercontent.com/gatensj/wagtail-draftail-katex/master/images/screenshot06152018-1.png)

![Image Editor](https://raw.githubusercontent.com/gatensj/wagtail-draftail-katex/master/images/screenshot06152018-2.png)

## Quick Start

Install the package with

```sh
pip install wagtail-katex
```

Add `wagtailkatex` to your `settings.py` in the `INSTALLED_APPS` section:

```python
INSTALLED_APPS = [
    ...
    "wagtailkatex",
    ...
]
```

Add `katex-embed` to `RichTextField` features:

```python
body = RichTextField(features=[..., "katex-embed"])
```
