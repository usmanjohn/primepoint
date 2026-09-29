"""Template access to `prime.seo` — the search-facing title and description.

    {% load seo_extras %}
    {% block title %}{{ tutorial|seo_title }}{% endblock %}
    {% block meta_description %}{% seo_description tutorial.summary tutorial.title %}{% endblock %}
"""
from django import template

from prime import seo

register = template.Library()


@register.filter(name='seo_title')
def seo_title(obj):
    """The <title>: topic first, subject after, brand if it fits."""
    return seo.title_for(obj)


@register.filter(name='seo_social_title')
def seo_social_title(obj):
    """The same without the brand — og:site_name already carries it, and a
    card reading "Powerty · Topic | Powerty" looks like a bug."""
    return seo.strip_brand(seo.title_for(obj))


@register.simple_tag(name='seo_description')
def seo_description(*candidates):
    """First candidate with words in it, as plain text inside 160 characters."""
    return seo.description(*candidates)
