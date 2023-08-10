![GitHub Actions build status](https://github.com/guestready/django_safe_template_engine/actions/workflows/build.yml/badge.svg?branch=main)

# Django Safe Template Engine

Django template engine to render untrusted template code

## Requirements

- Python 3.8 to 3.11
- Django 3.0

## Available tools

Template engine:

```py
from django.template import Template
from django_safe_template_engine.engine import SafeTemplateEngine

safe_engine = SafeTemplateEngine()
Template(source, engine=safe_engine)
```

Validator:

```py
from django_safe_template_engine.validators import validate_safe_engine_template_syntax

template_code = '{% include "hacked.html" %}'
validate_safe_engine_template_syntax(template_code)
```

## Trusted built-ins

The following filters and tags are allowed by this template engine.

### Trusted filters

<!-- TODO: Check for dead links -->
<!-- TODO: Re-order? -->
- [`addslashes`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#addslashes)
- [`capfirst`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#capfirst)
- [`escapejs`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#escapejs)
- [`json_script`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#json_script)
- [`floatformat`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)
- [`iriencode`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#iriencode)
- [`linenumbers`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#linenumbers)
- [`lower`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#lower)
- [`make_list`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#make_list)
- [`slugify`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#slugify)
- [`stringformat`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#stringformat)
- [`title`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#title)
- [`truncatechars`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatechars)
- [`truncatechars_html`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatechars_html)
- [`truncatewords`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatewords)
- [`truncatewords_html`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#truncatewords_html)
- [`upper`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#upper)
- [`urlencode`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#urlencode)
- [`urlize`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#urlize)
- [`urlizetrunc`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#urlizetrunc)
- [`wordcount`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#wordcount)
- [`wordwrap`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#wordwrap)
- [`ljust`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#ljust)
- [`rjust`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#rjust)
- [`center`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#center)
- [`cut`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#cut)
- [`escape`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#escape)
- [`force_escape`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#force_escape)
- [`linebreaks`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#linebreaks)
- [`linebreaksbr`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#linebreaksbr)
- [`safe`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safe)
- [`safeseq`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#safeseq)
- [`striptags`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#striptags)
- [`dictsort`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#dictsort)
- [`dictsortreversed`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#dictsortreversed)
- [`first`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#first)
- [`join`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#join)
- [`last`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#last)
- [`length`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#length)
- [`length_is`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#length_is)
- [`random`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#random)
- [`slice`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#slice)
- [`unordered_list`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#unordered_list)
- [`add`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#add)
- [`get_digit`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#get_digit)
- [`date`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date)
- [`time`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#time)
- [`timesince`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#timesince)
- [`timeuntil`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#timeuntil)
- [`default`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#default)
- [`default_if_none`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#default_if_none)
- [`divisibleby`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#divisibleby)
- [`yesno`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#yesno)
- [`filesizeformat`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#filesizeformat)
- [`pluralize`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#pluralize)
- [`phone2numeric`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#phone2numeric)

### Trusted tags

- [`autoescape`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#autoescape)
- [`comment`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#comment)
- [`cycle`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#cycle)
- [`filter`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#filter)
- [`firstof`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#firstof)
- [`for`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#for)
- [`for … empty`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#for-empty)
- [`if`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#if)
- [`ifchanged`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#ifchanged)
- [`lorem`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#lorem)
- [`now`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#now)
- [`regroup`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#regroup)
- [`resetcycle`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#resetcycle)
- [`spaceless`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#spaceless)
