# Changelog

## Unreleased

- Reformat source code with with [black](https://pypi.org/project/black/)
- Add `.git-blame-ignore-revs` with revisions to ignore in `git blame`
- Set up project for PyPi release
    - Update `pyproject.toml`
    - Add contributing guidelines to `README.md`
- Sort filters by alphabetical order in the documentation and source code
- Add official support for Python 3.12

## 1.1.0 - 2024-02-04

- Add official support for Django 3.2:
    - Use Django 3.2 in technical tests
    - Review all the Django 3.2 built-in template tags and filters (no changes needed)
- Drop official support for Django 3.0 (still unofficially supported in this version as there are no breaking changes)
- Remove Python 3.7 from supported versions in `pyproject.toml` (never officially supported)
- Start keeping a changelog in `CHANGELOG.md`

## 1.0.0 - 2023-08-10

- Review all the Django 3.0 built-in template tags and filters:
    - Allow the ones considered safe
    - Make sure the rest is forbidden with technical test coverage
- Add official support for Python 3.8 to Python 3.11 (covered by technical tests)
- Add official support for Django 3.0 (covered by technical tests)
