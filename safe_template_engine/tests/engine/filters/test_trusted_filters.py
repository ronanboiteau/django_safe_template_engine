from django.template.base import Template
from django.template.context import Context
from django.test import SimpleTestCase

from safe_template_engine.engine import SafeTemplateEngine


class TrustedFiltersTestCase(SimpleTestCase):
    engine: SafeTemplateEngine

    @classmethod
    def setUpClass(cls):
        cls.engine = SafeTemplateEngine()

        return super().setUpClass()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context, autoescape=False))

    def test_trust_addslashes(self):
        self.assertEqual(
            self._render('{{ "\\test"|addslashes }}'),
            '\\\\test',
        )

    def test_trust_capfist(self):
        self.assertEqual(
            self._render('{{ "hello world"|capfirst }}'),
            'Hello world',
        )

    def test_trust_floatformat(self):
        self.assertEqual(
            self._render('{{ 42.0000|floatformat }}'),
            '42',
        )

    def test_trust_title(self):
        self.assertEqual(
            self._render('{{ "hello world"|title }}'),
            'Hello World',
        )
