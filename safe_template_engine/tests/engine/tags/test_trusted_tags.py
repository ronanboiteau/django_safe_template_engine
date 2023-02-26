from django.template.base import Template
from django.template.context import Context
from django.test import SimpleTestCase

from safe_template_engine.engine import SafeTemplateEngine


class TrustedTagsTestCase(SimpleTestCase):
    engine: SafeTemplateEngine

    @classmethod
    def setUpClass(cls):
        cls.engine = SafeTemplateEngine()

        return super().setUpClass()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context, autoescape=False))

    def test_trust_autoescape(self):
        self.assertEqual(
            self._render('{% autoescape off %}<script></script>{% endautoescape %}'),
            '<script></script>',
        )

    def test_trust_firstof(self):
        self.assertEqual(
            self._render('{% firstof empty "OK" %}', context={'empty': ''}),
            'OK',
        )

    def test_trust_for(self):
        self.assertEqual(
            self._render(
                '{% for item in items %}{{ item }}||{% endfor %}',
                context={'items': [1, 2, 3]},
            ),
            '1||2||3||',
        )

    def test_trust_if(self):
        self.assertEqual(
            self._render('{% if True %}OK{% else %}KO{% endif %}'),
            'OK',
        )
