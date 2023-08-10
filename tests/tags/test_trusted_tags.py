import pytest
from django.template.base import Template
from django.template.context import Context
from django.template.exceptions import TemplateSyntaxError

from django_safe_template_engine.engine import SafeTemplateEngine


class TestTrustedTags:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context))

    def test_trust_autoescape(self):
        expected = '<script></script>'
        result = self._render(
            '{% autoescape off %}'
            '<script></script>'
            '{% endautoescape %}',
        )
        assert result == expected

    def test_trust_comment(self):
        expected = 'Displayed'
        result = self._render(
            'Displayed'
            '{% comment %}'
            'Hidden'
            '{% endcomment %}',
        )
        assert result == expected

    def test_trust_cycle(self):
        expected = (
            '<span class="text1">First text</span>'
            '<span class="text2">Second text</span>'

        )
        result = self._render(
            '{% for item in items %}'
            '<span class="{% cycle "text1" "text2" "text3" %}">{{ item }}</span>'
            '{% endfor %}',
            context={'items': ['First text', 'Second text']}
        )
        assert result == expected

    def test_trust_filter(self):
        expected = '1. ONE\n2. TWO\n3. THREE'
        result = self._render(
            '{% filter linenumbers|upper %}'
            'one\ntwo\nthree'
            '{% endfilter %}',
            context={'value': 'one\ntwo\nthree'},
        )
        assert result == expected

    def test_filter_with_untrusted_filter(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=r"^Invalid filter: 'pprint'",
        ):
            self._render(
                '{% filter pprint %}'
                'Unreachable due to usage of pprint filter'
                '{% endfilter %}',
            )

    def test_trust_firstof(self):
        expected = 'OK'
        result = self._render(
            '{% firstof empty "OK" %}',
            context={'empty': ''},
        )
        assert result == expected

    def test_trust_for(self):
        expected = '123'
        result = self._render(
            '{% for item in items %}'
            '{{ item }}'
            '{% endfor %}',
            context={'items': [1, 2, 3]},
        )
        assert result == expected

    def test_trust_for_empty(self):
        expected = 'No items'
        result = self._render(
            '{% for item in items %}'
            '{{ item }}'
            '{% empty %}'
            'No items'
            '{% endfor %}',
            context={'items': []},
        )
        assert result == expected

    def test_trust_if(self):
        expected = 'New messages'
        result = self._render(
            '{% if messages %}'
            'New messages'
            '{% else %}'
            'No new messages'
            '{% endif %}',
            context={'messages': ['message1', 'message2']}
        )
        assert result == expected

    def test_trust_if_with_trusted_filter(self):
        expected = 'New messages'
        result = self._render(
            '{% if messages|length > 0 %}'
            'New messages'
            '{% else %}'
            'No new messages'
            '{% endif %}',
            context={'messages': ['message1', 'message2']}
        )
        assert result == expected

    def test_if_with_untrusted_filter(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=r"^Invalid filter: 'pprint'",
        ):
            self._render(
                '{% if messages|pprint %}'
                'Unreachable due to usage of pprint filter'
                '{% endif %}',
            )

    def test_trust_ifchanged(self):
        expected = '123'
        result = self._render(
            '{% for number in numbers %}'
            '{% ifchanged number %}{{ number }}{% endifchanged %}'
            '{% endfor %}',
            context={'numbers': [1, 1, 2, 3, 3]}
        )
        assert result == expected
