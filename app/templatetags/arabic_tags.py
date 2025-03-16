from django import template
from django.utils.dateformat import format as date_format
from django.utils.timezone import template_localtime
import re

register = template.Library()

# Define Arabic month names
ARABIC_MONTHS = {
    'January': 'يناير',
    'February': 'فبراير',
    'March': 'مارس',
    'April': 'أبريل',
    'May': 'مايو',
    'June': 'يونيو',
    'July': 'يوليو',
    'August': 'أغسطس',
    'September': 'سبتمبر',
    'October': 'أكتوبر',
    'November': 'نوفمبر',
    'December': 'ديسمبر',
}

# Define Arabic numerals
ARABIC_NUMERALS = {
    '0': '٠',
    '1': '١',
    '2': '٢',
    '3': '٣',
    '4': '٤',
    '5': '٥',
    '6': '٦',
    '7': '٧',
    '8': '٨',
    '9': '٩',
}

@register.filter
def arabic_date(date, format_string="j F Y"):
    """
    Formats a date in Arabic with Arabic numerals and month names.
    Example: 15 محرم 1445
    """
    if not date:
        return ''
    
    # Format the date using Django's date formatter
    formatted_date = date_format(template_localtime(date), format_string)
    
    # Replace month names with Arabic equivalents
    for eng, ar in ARABIC_MONTHS.items():
        formatted_date = formatted_date.replace(eng, ar)
    
    # Replace numerals with Arabic equivalents if requested
    return formatted_date

@register.filter
def arabic_numbers(value):
    """
    Converts Western Arabic numerals (0-9) to Eastern Arabic numerals (٠-٩)
    """
    if value is None:
        return ''
    
    value = str(value)
    for western, eastern in ARABIC_NUMERALS.items():
        value = value.replace(western, eastern)
    
    return value 

