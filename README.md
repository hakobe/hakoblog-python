[![Build Status](https://travis-ci.org/hakobe/hakoblog-python.svg?branch=master)](https://travis-ci.org/hakobe/hakoblog-python)

# hakoblog
A little simple blog for my python practice.

# Synopsis

```sh
# setup
$ pip install -r requirements.txt
$ mysqladmin -uroot create hakoblog
$ cat db/schema.sql| mysql -uroot hakoblog

# test
$ nosetest tests

# run
$ FLASK_APP=hakoblog/web.py flask run
```
