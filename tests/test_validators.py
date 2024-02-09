import pytest
from django.core.exceptions import ValidationError

from django_safe_template_engine.validators import validate_safe_engine_template_syntax


class TestValidateSafeEngineTemplateSyntax:

    def _validate(self, template_code):
        validate_safe_engine_template_syntax(template_code)

    def test_valid_template(self):
        self._validate(
            "{% autoescape off %}"
            '<script>{{ "i am a test"|title }}</script>'
            "{% endautoescape %}"
        )

    def test_generic_invalid_syntax(self):
        with pytest.raises(ValidationError):
            self._validate("{% i_do_not_exist %}")
        with pytest.raises(ValidationError):
            self._validate("{{ test|i_do_not_exist }}")
        with pytest.raises(ValidationError):
            self._validate("{% if %} Unclosed if")

    def test_invalid_template_untrusted_loader(self):
        with pytest.raises(ValidationError):
            self._validate("{% load i18n %}")

    def test_invalid_template_untrusted_tag(self):
        with pytest.raises(ValidationError):
            self._validate('{% extends "hacked.html" %}')

    def test_invalid_template_untrusted_filter(self):
        with pytest.raises(ValidationError):
            self._validate("{{ test_list|pprint }}")
