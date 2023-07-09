start:
	flask --app app --debug run

lint:
	poetry run flake8 app.py
	poetry run flake8 tools.py
	poetry run flake8 templates

test:
	poetry run pytest -vv --cov -s

test-coverage:
	poetry run pytest --cov=course_tests --cov-report xml
