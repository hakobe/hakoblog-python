.PHONY: setupdb
setupdb:
	- mysqladmin -uroot create hakoblog
	cat db/schema.sql | mysql -uroot hakoblog
	- mysqladmin -uroot create hakoblog_test
	cat db/schema.sql | mysql -uroot hakoblog_test
