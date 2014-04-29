# -*- coding: utf-8 -*-

"""
implement my own 'markdown' template tag
requires 'python-markdown' (pip install markdown)
"""
# ref: http://www.dominicrodger.com/django-markdown.html

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def my_markdown(value):
    extensions = ["nl2br", ]

    return mark_safe(markdown.markdown(force_unicode(value),
                                       extensions,
                                       safe_mode=True,
                                       enable_attributes=False))
