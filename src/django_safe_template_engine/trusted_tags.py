from django.template.defaulttags import (
    autoescape, comment, cycle, do_filter, do_for, do_if, firstof, ifchanged,
    lorem, now, regroup,
)
from django.template.library import Library

register = Library()

register.tag(autoescape)
register.tag(comment)
register.tag(cycle)
register.tag('filter', do_filter)
register.tag(firstof)
register.tag('for', do_for)
register.tag('if', do_if)
register.tag(ifchanged)
register.tag(lorem)
register.tag(now)
register.tag(regroup)
