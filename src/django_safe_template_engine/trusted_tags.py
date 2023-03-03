from django.template.defaulttags import autoescape, do_for, do_if, firstof
from django.template.library import Library

register = Library()

register.tag(autoescape)
register.tag(firstof)
register.tag('for', do_for)
register.tag('if', do_if)
