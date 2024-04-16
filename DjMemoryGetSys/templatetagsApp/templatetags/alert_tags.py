from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('alert.html')
def render_alert(messages):
    return {'messages': messages}
