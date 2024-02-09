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

    def test_do_not_trust_block(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("block"),
        ):
            self._render("{% block main %}")

    def test_do_not_trust_csrf_token(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("csrf_token"),
        ):
            self._render("{% csrf_token %}")

    def test_do_not_trust_debug(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("debug"),
        ):
            self._render("{% debug %}")

    def test_do_not_trust_extends(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("extends"),
        ):
            self._render('{% extends "hacked.html" %}')

    def test_do_not_trust_include(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("include"),
        ):
            self._render('{% include "hacked.html" %}')

    def test_do_not_trust_load(self):
        with pytest.raises(
            TemplateSyntaxError,
            match=self._msg_regex("load"),
        ):
            self._render("{% load i18n %}")
