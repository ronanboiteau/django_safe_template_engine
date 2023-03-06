# Django Safe Template Engine

Django template engine to render untrusted template code

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
