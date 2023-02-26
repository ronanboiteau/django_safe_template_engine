from django.template.engine import Engine


class SafeTemplateEngine(Engine):

    def __init__(self, **kwargs):
        self.default_builtins = [
            'safe_template_engine.trusted_filters',
            'safe_template_engine.trusted_tags',
        ]

        super().__init__(self, **kwargs)

        self.dirs = []
        self.app_dirs = False
        self.loaders = []
