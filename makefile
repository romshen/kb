.ONESHELL:

.PHONY: default up_db wait_for_db clean install_environment

default: up_db wait_for_db

up_db:
	@docker-compose up --build --remove-orphans -d database

wait_for_db:
	@until docker container exec -it database pg_isready;
	do
		>&2 echo "waiting for Postgres... 😴";
		sleep 5;
	done
	@echo "database has started"

install_environment:
	@pipenv install --dev
	@pipenv run pre-commit install
	@pre-commit --version

clean:
	@docker-compose down --volumes --remove-orphans
