from django.template.base import Template
from django.template.context import Context

from django_safe_template_engine.engine import SafeTemplateEngine


class TestTrustedFilters:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context, autoescape=False))

    def test_trust_addslashes(self):
        expected = '\\\\test'
        result = self._render('{{ "\\test"|addslashes }}')
        assert result == expected

    def test_trust_capfist(self):
        expected = 'Hello world'
        result = self._render('{{ "hello world"|capfirst }}')
        assert result == expected

    def test_trust_escapejs(self):
        expected = '\\u003Ctest\\u0026test\\u003E'
        result = self._render('{{ "<test&test>"|escapejs }}')
        assert result == expected

    def test_trust_json_script(self):
        expected = '<script id="test-id" type="application/json">"{\\"id\\": 1}"</script>'
        result = self._render(
            '{{ json_string|json_script:"test-id" }}',
            context={'json_string': '{"id": 1}'}
        )
        assert result == expected

    def test_trust_floatformat(self):
        expected = '42'
        result = self._render('{{ 42.0000|floatformat }}')
        assert result == expected

    def test_trust_title(self):
        expected = 'Hello World'
        result = self._render('{{ "hello world"|title }}')
        assert result == expected
