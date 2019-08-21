.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up

.PHONY: down
down:
	docker-compose down

.PHONY: test
test:
	docker-compose run --rm app pytest

.PHONY: prepare-db
prepare-db:
	docker-compose run --rm app ./prepare-db.sh
