# Changelog

## 1.5.1 - 2025-12-11

- Update tests to use Django 6.0 instead of 6.0rc1
- Fix a broken link on PyPi

## 1.5.0 - 2025-11-24

- Add support for Django 6's `partial` and `partialdef` template tags
- Add official support for Django 6.0
- Add official support for Python 3.14
- Add missing documentation about support for Django 5.1's `querystring` template tag
- Improve mypy type checking coverage
- Fix a few broken links in the documentation + Use Django 6 links by default when linking Django documentation

## 1.4.0 - 2025-08-13

- Add official support for Django 5.1 and 5.2
- Add official support for Python 3.13
- Add support for Django 5.1's `querystring` template tag
- Drop official support for deprecated Python 3.7

## 1.3.2 - 2024-06-05

- Update dependencies to make it clear that version 1.3 is not compatible with Django 5.1

## 1.3.1 - 2024-04-18

- Small fixes in changelog and README

## 1.3.0 - 2024-04-18

- Lower Django version requirement to 3.0
- Lower Python version requirement to 3.7
- Add official support for Django 3.0 to 5.0 with:
    - Addition of automated test coverage
    - Review of all the built-in template tags and filters
- Add support for Django 5's `escapeseq` template filter
- Use [tox](https://tox.wiki/) to manage test suite environment

## 1.2.0 - 2024-04-18

- Add official support for Python 3.12
- Reformat source code with with [black](https://pypi.org/project/black/)
- Set up project for PyPi release
    - Update `pyproject.toml` with build system and other details for PyPi
    - Add contributing guidelines to `README.md`
- Add `.git-blame-ignore-revs` with revisions to ignore in `git blame`
- Sort filters by alphabetical order in the documentation and source code

## 1.1.0 - 2024-02-04

- Add official support for Django 3.2:
    - Use Django 3.2 in automated tests
    - Review all the Django 3.2 built-in template tags and filters (no changes needed)
- Drop official support for Django 3.0 (still unofficially supported in this version as there are no breaking changes)
- Remove Python 3.7 from supported versions in `pyproject.toml` (never officially supported)
- Start keeping a changelog in `CHANGELOG.md`

## 1.0.0 - 2023-08-10

- Review all the Django 3.0 built-in template tags and filters:
    - Allow the ones considered safe
    - Make sure the rest is forbidden with technical test coverage
- Add official support for Python 3.8 to Python 3.11 (covered by automated tests)
- Add official support for Django 3.0 (covered by automated tests)
