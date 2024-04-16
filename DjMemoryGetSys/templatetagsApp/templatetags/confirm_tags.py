from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('confirm.html')
def render_confirm():
    pass
