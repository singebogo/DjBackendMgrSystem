from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('messages.html')
def render_messages(messages):
    return {'messages': messages}
