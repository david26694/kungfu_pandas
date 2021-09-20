dist:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

test:
	pytest

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

install-test:
	pip install -e ".[test]"

install-docs:
	pip install -e ".[docs]"

docs-deploy:
	mkdocs gh-deploy

docs-serve:
	mkdocs serve
