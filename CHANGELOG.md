# Changelog

## 1.1.0 - Unreleased

- Add official support for Django 3.2:
    - Use Django 3.2 in technical tests
    - Review all the Django 3.2 built-in template tags and filters (no changes needed)
- Drop official support for Django 3.0 (still unofficially supported in this version as there are no breaking changes)
- Start keeping a changelog in `CHANGELOG.md`

## 1.0.0 - 2023-08-10

- Review all the Django 3.0 built-in template tags and filters:
    - Allow the ones considered safe
    - Make sure the rest is forbidden with technical test coverage
- Add official support for Python 3.8 to Python 3.11 (covered by technical tests)
- Add official support for Django 3.0 (covered by technical tests)
