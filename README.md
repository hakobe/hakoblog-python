# hakoblog
[![Build Status](https://travis-ci.org/hakobe/hakoblog-python.svg?branch=master)](https://travis-ci.org/hakobe/hakoblog-python)

A little simple blog for my python practice.

# Synopsis

```sh
# setup
$ pip install -r requirements.txt
$ mysqladmin -uroot create hakoblog
$ cat db/schema.sql| mysql -uroot hakoblog

# test
$ pytest tests

# run
$ FLASK_APP=hakoblog/web.py flask run
```

# Usage
See hakoblog/web.py please :relaxed:

# Lisense
[MIT](./LICENSE)

## Author
[hakobe](http://github.com/hakobe)
