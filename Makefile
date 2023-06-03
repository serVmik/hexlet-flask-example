start-lesson:
	flask --app lesson_15 --debug run

start-example:
	flask --app example --debug run

start-solution:
	flask --app solution_13 --debug run

start-app:
	flask --app app --debug run

lint:
	poetry run flake8 app.py
	poetry run flake8 validate.py
	poetry run flake8 templates