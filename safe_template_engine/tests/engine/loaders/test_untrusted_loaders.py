from django.template.base import Template
from django.template.context import Context
from django.template.exceptions import TemplateSyntaxError
from django.test import SimpleTestCase

from safe_template_engine.engine import SafeTemplateEngine


class UntrustedLoadersTestCase(SimpleTestCase):
    engine: SafeTemplateEngine

    @classmethod
    def setUpClass(cls):
        cls.engine = SafeTemplateEngine()

        return super().setUpClass()

    def _render(self, template_code, context={}):
        template = Template(template_code, engine=self.engine)
        return template.render(Context(context, autoescape=False))

    def test_do_not_trust_block(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError,
            "Invalid block tag on line 1: 'block'. Did you forget to register or load this tag?",
        ):
            self._render('{% block content %}{% endblockcontent %}')

    def test_do_not_trust_extends(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError,
            "Invalid block tag on line 1: 'extends'. Did you forget to register or load this tag?",
        ):
            self._render('{% extends "hacked.html" %}')

    def test_do_not_trust_include(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError,
            "Invalid block tag on line 1: 'include'. Did you forget to register or load this tag?",
        ):
            self._render('{% include "hacked.html" %}')

    def test_do_not_trust_load(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError,
            "Invalid block tag on line 1: 'load'. Did you forget to register or load this tag?",
        ):
            self._render('{% load i18n %}')

    def test_do_not_trust_static(self):
        with self.assertRaisesMessage(
            TemplateSyntaxError,
            "Invalid block tag on line 1: 'static'. Did you forget to register or load this tag?",
        ):
            self._render('{% static "hacked.css" %}')
