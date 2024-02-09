![GitHub Actions build status](https://github.com/ronanboiteau/django_safe_template_engine/actions/workflows/build.yml/badge.svg?branch=main)

# Django Safe Template Engine

Django template engine to render untrusted template code

## Table of contents

* __[Requirements](#requirements)__
* __[Available tools](#available-tools)__
* __[Trusted built-ins](#trusted-built-ins)__
  * [Trusted tags](#trusted-tags)
  * [Trusted filters](#trusted-filters)
* __[Contribute](#contribute)__
  * [How to contribute](#how-to-contribute)
  * [Code formatting and tests](#code-formatting-and-tests)
  * [Ignore code formatting revisions from git blame](#ignore-code-formatting-revisions-from-git-blame)

## Requirements

- Python 3.8 to 3.11
- Django 3.2 (officially supported in automated tests, all built-in template tags and filters reviewed)

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

The following tags and filters are allowed by this template engine.

### Trusted tags

- [`autoescape`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#autoescape)
- [`comment`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#comment)
- [`cycle`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#cycle)
- [`filter`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#filter)
- [`firstof`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#firstof)
- [`for`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for)
- [`for … empty`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for-empty)
- [`if`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#if)
- [`ifchanged`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ifchanged)
- [`lorem`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#lorem)
- [`now`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#now)
- [`regroup`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#regroup)
- [`resetcycle`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#resetcycle)
- [`spaceless`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#spaceless)
- [`templatetag`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#templatetag)
- [`url`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#url)
- [`verbatim`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#verbatim)
- [`widthratio`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#widthratio)
- [`with`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#with)

### Trusted filters

<!-- TODO: Check for dead links -->
<!-- TODO: Re-order? -->
- [`addslashes`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#addslashes)
- [`capfirst`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#capfirst)
- [`escapejs`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#escapejs)
- [`json_script`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#json_script)
- [`floatformat`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#floatformat)
- [`iriencode`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#iriencode)
- [`linenumbers`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#linenumbers)
- [`lower`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#lower)
- [`make_list`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#make_list)
- [`slugify`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#slugify)
- [`stringformat`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#stringformat)
- [`title`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#title)
- [`truncatechars`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#truncatechars)
- [`truncatechars_html`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#truncatechars_html)
- [`truncatewords`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#truncatewords)
- [`truncatewords_html`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#truncatewords_html)
- [`upper`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#upper)
- [`urlencode`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#urlencode)
- [`urlize`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#urlize)
- [`urlizetrunc`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#urlizetrunc)
- [`wordcount`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#wordcount)
- [`wordwrap`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#wordwrap)
- [`ljust`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ljust)
- [`rjust`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#rjust)
- [`center`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#center)
- [`cut`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#cut)
- [`escape`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#escape)
- [`force_escape`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#force_escape)
- [`linebreaks`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#linebreaks)
- [`linebreaksbr`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#linebreaksbr)
- [`safe`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#safe)
- [`safeseq`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#safeseq)
- [`striptags`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#striptags)
- [`dictsort`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#dictsort)
- [`dictsortreversed`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#dictsortreversed)
- [`first`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#first)
- [`join`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#join)
- [`last`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#last)
- [`length`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#length)
- [`length_is`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#length_is)
- [`random`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#random)
- [`slice`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#slice)
- [`unordered_list`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#unordered_list)
- [`add`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#add)
- [`get_digit`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#get_digit)
- [`date`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date)
- [`time`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#time)
- [`timesince`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#timesince)
- [`timeuntil`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#timeuntil)
- [`default`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#default)
- [`default_if_none`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#default_if_none)
- [`divisibleby`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#divisibleby)
- [`yesno`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#yesno)
- [`filesizeformat`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#filesizeformat)
- [`pluralize`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#pluralize)
- [`phone2numeric`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#phone2numeric)

## Contribute


### How to contribute

You want to add awesome features to Django Safe Template Engine? Here's how!

1. [Fork](https://github.com/ronanboiteau/django_safe_template_engine/fork) this repository
2. Commit and push to your forked repository
3. Open a [pull request](https://github.com/ronanboiteau/django_safe_template_engine/pulls) to merge your work into this repository

### Code formatting and tests

Here is how to run the code formatting / type checking tools, and run the test suite.

1. [Recommended] Create a Python venv for this repository:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install the dependencies:

    ```sh
    cd tests/ && pip install -r requirements.txt && cd ..
    ```

3. Run the code formatting tools:

    [`black`](https://pypi.org/project/black/) code formatter:

    ```sh
    black src tests
    ```

    [`isort`](https://pypi.org/project/isort/) import sorter:

    ```sh
    isort --settings-path isort.cfg src tests
    ```

    [`flake8`](https://pypi.org/project/flake8/) coding style checker:

    ```sh
    flake8 --config .flake8 src tests
    ```

    [`mypy`](https://pypi.org/project/mypy/) type checker:

    ```sh
    mypy --config-file mypy.ini src tests
    ```

4. Run the test suite:

    ```sh
    python run_tests.py
    ```

### Ignore code formatting revisions from git blame

For a more relevant git blame you can set up your git to use the file [`.git-blame-ignore-revs`](.git-blame-ignore-revs) in [`blame.ignoreRevsFile`](https://www.git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-fileltfilegt):

```sh
git config blame.ignoreRevsFile .git-blame-ignore-revs
```
