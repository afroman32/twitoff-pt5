# twitoff-pt5


# installation

```sh
git clone __________
cd twitoff-pt5
```


# Setup

```sh
pipenv install
```

Migrate the database:

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```


# Usage

```sh
FLAS_APP=web_app.py flask run
```