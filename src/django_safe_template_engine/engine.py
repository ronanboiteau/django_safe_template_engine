from django.template.engine import Engine


class SafeTemplateEngine(Engine):

    def __init__(self, **kwargs):
        self.default_builtins = [
            "django_safe_template_engine.trusted_filters",
            "django_safe_template_engine.trusted_tags",
        ]

        super().__init__(**kwargs)

        self.dirs = []
        self.app_dirs = False
        self.loaders = []
