from django.conf import settings
from django.contrib.staticfiles import finders
from django.templatetags.static import static

DEFAULT_CONF = {
    'js': 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js',
    'css': 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
}


def get_conf(key):
    try:
        conf = settings.WAGTAIL_KATEX
        value = conf[key]
    except:
        url = DEFAULT_CONF[key]
    else:
        url = value

    if finders.find(url):
        return static(url)
    else:
        return url
