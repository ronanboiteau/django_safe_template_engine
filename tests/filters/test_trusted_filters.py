from django.template.base import Template
from django.template.context import Context

from django_safe_template_engine.engine import SafeTemplateEngine


class TestTrustedFilters:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context))

    def test_trust_addslashes(self):
        expected = '\\\\test'
        result = self._render('{{ "\\test"|addslashes }}')
        assert result == expected

    def test_trust_capfist(self):
        expected = 'Hello world'
        result = self._render('{{ "hello world"|capfirst }}')
        assert result == expected

    def test_trust_floatformat(self):
        expected = '42'
        result = self._render('{{ 42.0000|floatformat }}')
        assert result == expected

    def test_trust_title(self):
        expected = 'Hello World'
        result = self._render('{{ "hello world"|title }}')
        assert result == expected
