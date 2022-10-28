# Use in order to access different app features
# Opens main app container
console:
	sudo docker exec -it app /bin/bash
# Create and start container
up:
	sudo docker-compose up
# Build or rebuild services (force-recreate, no-cache and others omitted)
build:
	sudo docker-compose up --build
# Django migrations
# May be problematic and might require sudo (Currently developed on ubuntu with only sudo prems #TODO)
migrations:
	poetry run python manage.py makemigrations app
	poetry run python manage.py migrate app
# Main FEATURES from recruitment task
# Get data from specified url (check scripts/client.py)
url:
	poetry run python -m scripts.client
# Get data from specified Json file (check scripts/file_client.py)
json:
	poetry run python -m scripts.file_client
# Run unittests
test:
	poetry run python -m unittest tests.test_scripts.test_client
	poetry run python -m unittest tests.test_scripts.test_file_client