install:
	poetry install

lint:
	poetry run flake8
	poetry run pytest
