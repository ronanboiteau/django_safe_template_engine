import pytest
from django.template.base import Template
from django.template.context import Context
from django.template.exceptions import TemplateSyntaxError

from django_safe_template_engine.engine import SafeTemplateEngine


class TestUntrustedFilters:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context))

    def _msg_regex(self, filter_name):
        return rf"^Invalid filter: '{filter_name}'"

    def test_do_not_trust_pprint(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("pprint"),
        ):
            self._render("{{ test_list|pprint }}", context={"test_list": []})
