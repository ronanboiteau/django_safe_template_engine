# Django Safe Template Engine

Django template engine to render untrusted template code

## Available tools

Template engine:

```py
from django.template import Template
from django_safe_template_engine.engine import SafeTemplateEngine

safe_engine = SafeTemplateEngine
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

- [`addslashes`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#addslashes)
- [`capfirst`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#capfirst)
- [`floatformat`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#floatformat)
- [`title`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#title)

### Trusted tags

- [`autoescape`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#autoescape)
- [`firstof`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#firstof)
- [`for`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#for)
- [`if`](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#if)
