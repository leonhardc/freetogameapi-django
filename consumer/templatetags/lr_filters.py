from django import template
from utils.filters import formata_data

register = template.Library()

@register.filter(name="format_date")
def format_date(date):
    return formata_data(date)
