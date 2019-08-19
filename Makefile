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

.PHONY: setupdb
prepare-db:
	- docker-compose run --rm app mysqladmin -uroot -hdb create hakoblog
	cat db/schema.sql | docker-compose run --rm db mysql -uroot -hdb hakoblog
	- docker-compose run --rm app mysqladmin -uroot -hdb create hakoblog_test
	cat db/schema.sql | docker-compose run --rm db mysql -uroot -hdb hakoblog_test
