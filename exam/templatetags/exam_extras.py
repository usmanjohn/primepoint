from html import unescape

from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.filter
def get_item(d, key):
    if isinstance(d, dict):
        return d.get(key)
    return None


@register.filter
def plain_text(value):
    """Strip HTML tags, unescape entities, and normalise non-breaking spaces."""
    return unescape(strip_tags(value or '')).replace('\xa0', ' ').strip()
