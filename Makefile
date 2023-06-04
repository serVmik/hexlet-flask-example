start:
	flask --app app --debug run

lint:
	poetry run flake8 app.py
	poetry run flake8 tools.py
	poetry run flake8 templates