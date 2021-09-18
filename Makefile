dist:
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*

test:
	pytest

install:
	python -m pip install -e .

install-dev:
	python -m pip install -e ".[dev]"
	pre-commit install

install-test:
	python -m pip install -e ".[test]"
