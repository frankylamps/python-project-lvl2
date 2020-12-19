install:
	poetry install

lint:
	poetry run flake8

tests:
	poetry run pytest --cov=gendiff --cov-report xml --per-file-ignores="__init__.py:F401"
