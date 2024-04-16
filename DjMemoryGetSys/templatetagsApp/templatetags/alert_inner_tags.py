from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('alert_inner.html')
def render_alert_inner(messages):
    return {'messages': messages}
