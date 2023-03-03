from django.template.base import Template
from django.template.context import Context

from django_safe_template_engine.engine import SafeTemplateEngine


class TestTrustedTags:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context, autoescape=False))

    def test_trust_autoescape(self):
        expected = '<script></script>'
        result = self._render(
            '{% autoescape off %}'
            '<script></script>'
            '{% endautoescape %}'
        )
        assert result == expected

    def test_trust_firstof(self):
        expected = 'OK'
        result = self._render(
            '{% firstof empty "OK" %}',
            context={'empty': ''},
        )
        assert result == expected

    def test_trust_for(self):
        expected = '1||2||3||'
        result = self._render(
            '{% for item in items %}{{ item }}||{% endfor %}',
            context={'items': [1, 2, 3]},
        )
        assert result == expected

    def test_trust_if(self):
        expected = 'OK'
        result = self._render(
            '{% if True %}'
            'OK'
            '{% else %}'
            'KO'
            '{% endif %}'
        )
        assert result == expected
