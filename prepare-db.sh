#!/bin/bash

set -xe

mysqladmin -uroot -hdb create hakoblog || :
cat db/schema.sql | mysql -uroot -hdb hakoblog

mysqladmin -uroot -hdb create hakoblog_test || :
cat db/schema.sql | mysql -uroot -hdb hakoblog_test
