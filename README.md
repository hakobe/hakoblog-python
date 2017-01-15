# hakoblog
A little simple blog for my python practice.

# Synopsis

```sh
# setup
$ pip install -r requirements.txt
$ mysqladmin -uroot create hakoblog
$ cat db/schema.sql| mysql -uroot hakoblog

# run
$ FLASK_APP=hakoblog/web.py flask run
```
