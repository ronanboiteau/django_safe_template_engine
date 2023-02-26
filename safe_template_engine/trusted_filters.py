from django.template.defaultfilters import (
    addslashes, capfirst, floatformat, title,
)
from django.template.library import Library

register = Library()

register.filter(addslashes, is_safe=True)
register.filter(floatformat, is_safe=True)
register.filter(capfirst, is_safe=True)
register.filter(title, is_safe=True)
