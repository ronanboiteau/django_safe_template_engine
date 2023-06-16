import pytest
from django.template.base import Template
from django.template.context import Context
from django.template.exceptions import TemplateSyntaxError

from django_safe_template_engine.engine import SafeTemplateEngine


class TestUntrustedTags:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context))

    def _msg_regex(self, tag_name):
        return rf"^Invalid block tag on line .+: '{tag_name}'"

    def test_do_not_trust_load(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex('load'),
        ):
            self._render('{% load i18n %}')
