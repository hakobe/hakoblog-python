# hakoblog
[![Build Status](https://travis-ci.org/hakobe/hakoblog-python.svg?branch=master)](https://travis-ci.org/hakobe/hakoblog-python)

A little simple blog for my python practice.

# Synopsis

```sh
# setup
$ pip install -r requirements.txt
$ make setupdb

# test
$ pytest tests

# run
$ FLASK_APP=hakoblog/web.py flask run
```

# Usage
See hakoblog/web.py please :relaxed:

# Structure

- `hakoblog/web.py` Flask app (entry point)
- `hakoblog/config.py` Configuration object
- `hakoblog/db.py` Database instance wrapper
- `hakoblog/model/*.py` Plain model objects (not related to db directly)
- `hakoblog/loader/*.py` Loder services which fetch model objects from database (aka. repository)
- `hakoblog/actoin/*.py` Action services which affect model objects in database.

# Lisense
[MIT](./LICENSE)

## Author
[hakobe](http://github.com/hakobe)
