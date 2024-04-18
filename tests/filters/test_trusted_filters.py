from django import VERSION
from django.template.base import Template
from django.template.context import Context

from django_safe_template_engine.engine import SafeTemplateEngine


class TestTrustedFilters:
    engine = SafeTemplateEngine()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context))

    # TODO: Write test for add

    def test_trust_addslashes(self):
        expected = "\\\\test"
        result = self._render('{{ "\\test"|addslashes }}')
        assert result == expected

    def test_trust_capfist(self):
        expected = "Hello world"
        result = self._render('{{ "hello world"|capfirst }}')
        assert result == expected

    # TODO: Write test for center
    # TODO: Write test for cut
    # TODO: Write test for date

    def test_trust_default_if_none(self):
        expected = "OK"
        result = self._render(
            '{{ value|default_if_none:"OK" }}',
            context={"value": None},
        )
        assert result == expected

    def test_trust_default(self):
        expected = "OK"
        result = self._render(
            '{{ value|default:"OK" }}',
            context={"value": False},
        )
        assert result == expected

    # TODO: Write test for dictsort
    # TODO: Write test for dictsortreversed
    # TODO: Write test for divisibleby

    def test_trust_escape(self):
        expected = "&lt;b&gt;T&amp;Cs&lt;/b&gt;"
        result = self._render("{{ value|escape }}", context={"value": "<b>T&Cs</b>"})
        assert result == expected

    def test_trust_escapejs(self):
        expected = "\\u003Ctest\\u0026test\\u003E"
        result = self._render('{{ "<test&test>"|escapejs }}')
        assert result == expected

    if VERSION[0] == 5:

        def test_trust_escapeseq(self):
            expected = "T&amp;Cs, &#x27;Test&#x27;"
            result = self._render(
                '{{ value|escapeseq|join:", " }}',
                context={"value": ["T&Cs", "'Test'"]},
            )
            assert result == expected

    # FIXME
    # def test_trust_filesizeformat(self):
    #     expected = '117.7 MB'
    #     result = self._render('{{ "123456789"|filesizeformat }}')
    #     assert result == expected

    def test_trust_first(self):
        expected = "test1"
        result = self._render(
            "{{ value|first }}",
            context={"value": ["test1", "test2"]},
        )
        assert result == expected

    def test_trust_floatformat(self):
        expected = "42"
        result = self._render("{{ 42.0000|floatformat }}")
        assert result == expected

    # TODO: Write test for force_escape
    # TODO: Write test for get_digit
    # TODO: Write test for iriencode
    # TODO: Write test for join

    def test_trust_json_script(self):
        expected = (
            '<script id="test-id" type="application/json">"{\\"id\\": 1}"</script>'
        )
        result = self._render(
            '{{ json_string|json_script:"test-id" }}',
            context={"json_string": '{"id": 1}'},
        )
        assert result == expected

    # TODO: Write test for last
    # TODO: Write test for length_is
    # TODO: Write test for length
    # TODO: Write test for linebreaks
    # TODO: Write test for linebreaksbr

    def test_trust_linenumbers(self):
        expected = "1. one\n2. two\n3. three"
        result = self._render(
            "{{ value|linenumbers }}",
            context={"value": "one\ntwo\nthree"},
        )
        assert result == expected

    # TODO: Write test for ljust

    def test_trust_lower(self):
        expected = "hello"
        result = self._render('{{ "HeLlO"|lower }}')
        assert result == expected

    def test_trust_make_list(self):
        expected = "[&#x27;1&#x27;, &#x27;2&#x27;, &#x27;3&#x27;]"
        result = self._render(
            "{{ value|make_list }}",
            context={"value": "123"},
        )
        assert result == expected

    def test_trust_phone2numeric(self):
        expected = "800-2655328"
        result = self._render('{{ "800-COLLECT"|phone2numeric }}')
        assert result == expected

    def test_trust_pluralize(self):
        expected = "tests"
        result = self._render(
            "test{{ value|pluralize }}",
            context={"value": 2},
        )
        assert result == expected

    # TODO: Write test for random
    # TODO: Write test for rjust
    # TODO: Write test for safe
    # TODO: Write test for safeseq
    # TODO: Write test for slice

    def test_trust_slugify(self):
        expected = "hello-world"
        result = self._render('{{ "hello world"|slugify }}')
        assert result == expected

    # TODO: Write test for stringformat
    # TODO: Write test for striptags
    # TODO: Write test for time
    # TODO: Write test for timesince
    # TODO: Write test for timeuntil

    def test_trust_title(self):
        expected = "Hello World"
        result = self._render('{{ "hello world"|title }}')
        assert result == expected

    # TODO: Write test for truncatechars_html
    # TODO: Write test for truncatechars
    # TODO: Write test for truncatewords_html
    # TODO: Write test for truncatewords
    # TODO: Write test for unordered_list

    def test_trust_upper(self):
        expected = "HELLO"
        result = self._render('{{ "HeLlO"|upper }}')
        assert result == expected

    # TODO: Write test for urlencode
    # TODO: Write test for urlize
    # TODO: Write test for urlizetrunc
    # TODO: Write test for wordcount
    # TODO: Write test for wordwrap

    def test_trust_yesno(self):
        expected = "No"
        result = self._render(
            '{{ value|yesno:"Yes,No" }}',
            context={"value": False},
        )
        assert result == expected
