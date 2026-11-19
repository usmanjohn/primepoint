from django import template
from general.formatters import format_number

register = template.Library()

@register.filter
def format_currency(value):
    formatted = format_number(value)
    
    # If it's a string, replace commas with spaces for clean regional formatting
    if isinstance(formatted, str):
        return formatted.replace(",", " ")
        
    return formatted
@register.filter
def currency(value, currency_code="USD"):
    try:
        # Use locale for better formatting (optional but good practice)
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 
        value = locale.currency(value, symbol=currency_code + ' ', grouping=True)
        return value
    except:
        # Fallback if locale fails
        return f"{intcomma(value):.2f} {currency_code}"