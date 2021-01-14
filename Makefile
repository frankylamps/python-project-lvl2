install:
	poetry install

lint:
	poetry run flake8

tests:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
