from django import template
from django.utils.html import format_html

register = template.Library()


@register.inclusion_tag('dbSelectDialog.html')
def render_dbSelectDialog(dbSelectTable, url):
    return {'dbSelectTable': dbSelectTable, "dbSelectUrl": url}
