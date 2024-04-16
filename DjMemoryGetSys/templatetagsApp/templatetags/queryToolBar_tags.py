from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('queryToolbar.html')
def render_queryToolbar(Form, formUrl, formAddUrl):
    return {'Form': Form, "formUrl": formUrl, "formAddUrl": formAddUrl}
