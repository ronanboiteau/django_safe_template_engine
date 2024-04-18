from django import VERSION
from django.template.defaultfilters import (
    add,
    addslashes,
    capfirst,
    center,
    cut,
    date,
    default,
    default_if_none,
    dictsort,
    dictsortreversed,
    divisibleby,
    escape_filter,
    escapejs_filter,
    filesizeformat,
    first,
    floatformat,
    force_escape,
    get_digit,
    iriencode,
    join,
    json_script,
    last,
    length,
    length_is,
    linebreaks_filter,
    linebreaksbr,
    linenumbers,
    ljust,
    lower,
    make_list,
    phone2numeric_filter,
    pluralize,
    random,
    rjust,
    safe,
    safeseq,
    slice_filter,
    slugify,
    stringformat,
    striptags,
    time,
    timesince_filter,
    timeuntil_filter,
    title,
    truncatechars,
    truncatechars_html,
    truncatewords,
    truncatewords_html,
    unordered_list,
    upper,
    urlencode,
    urlize,
    urlizetrunc,
    wordcount,
    wordwrap,
    yesno,
)
from django.template.library import Library

register = Library()

register.filter(add, is_safe=False)
register.filter(addslashes, is_safe=True)
register.filter(capfirst, is_safe=True)
register.filter(center, is_safe=True)
register.filter(cut)
register.filter(date, expects_localtime=True, is_safe=False)
register.filter(default_if_none, is_safe=False)
register.filter(default, is_safe=False)
register.filter(dictsort, is_safe=False)
register.filter(dictsortreversed, is_safe=False)
register.filter(divisibleby, is_safe=False)
register.filter("escape", escape_filter, is_safe=True)
register.filter("escapejs", escapejs_filter)

if VERSION[0] == 5:
    from django.template.defaultfilters import escapeseq

    register.filter(escapeseq)

register.filter(filesizeformat, is_safe=True)
register.filter(first, is_safe=False)
register.filter(floatformat, is_safe=True)
register.filter(force_escape, is_safe=True)
register.filter(get_digit, is_safe=False)
register.filter(iriencode, is_safe=True)
register.filter(join, is_safe=True, needs_autoescape=True)
register.filter(json_script, is_safe=True)
register.filter(last, is_safe=True)
register.filter(length_is, is_safe=False)
register.filter(length, is_safe=False)
register.filter("linebreaks", linebreaks_filter, is_safe=True, needs_autoescape=True)
register.filter(linebreaksbr, is_safe=True, needs_autoescape=True)
register.filter(linenumbers, is_safe=True, needs_autoescape=True)
register.filter(ljust, is_safe=True)
register.filter(lower, is_safe=True)
register.filter(make_list, is_safe=False)
register.filter("phone2numeric", phone2numeric_filter, is_safe=True)
register.filter(pluralize, is_safe=False)
register.filter(random, is_safe=True)
register.filter(rjust, is_safe=True)
register.filter(safe, is_safe=True)
register.filter(safeseq, is_safe=True)
register.filter("slice", slice_filter, is_safe=True)
register.filter(slugify, is_safe=True)
register.filter(stringformat, is_safe=True)
register.filter(striptags, is_safe=True)
register.filter(time, expects_localtime=True, is_safe=False)
register.filter("timesince", timesince_filter, is_safe=False)
register.filter("timeuntil", timeuntil_filter, is_safe=False)
register.filter(title, is_safe=True)
register.filter(truncatechars_html, is_safe=True)
register.filter(truncatechars, is_safe=True)
register.filter(truncatewords_html, is_safe=True)
register.filter(truncatewords, is_safe=True)
register.filter(unordered_list, is_safe=True, needs_autoescape=True)
register.filter(upper, is_safe=False)
register.filter(urlencode, is_safe=False)
register.filter(urlize, is_safe=True, needs_autoescape=True)
register.filter(urlizetrunc, is_safe=True, needs_autoescape=True)
register.filter(wordcount, is_safe=False)
register.filter(wordwrap, is_safe=True)
register.filter(yesno, is_safe=False)
