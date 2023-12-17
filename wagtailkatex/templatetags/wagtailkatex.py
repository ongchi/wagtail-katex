from django import template

from ..conf import get_conf

register = template.Library()


@register.simple_tag
def wagtailkatex_media(key):
    return get_conf(key)
