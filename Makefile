install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
