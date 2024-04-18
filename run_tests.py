import os

import pytest

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    import django

    django.setup()

    pytest.main()
