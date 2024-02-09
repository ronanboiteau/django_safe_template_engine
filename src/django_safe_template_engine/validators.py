from django.core.exceptions import ValidationError
from django.template import Template, TemplateSyntaxError

from django_safe_template_engine.engine import SafeTemplateEngine


def validate_safe_engine_template_syntax(source):
    try:
        Template(source, engine=SafeTemplateEngine())
    except TemplateSyntaxError as err:
        raise ValidationError(str(err))
