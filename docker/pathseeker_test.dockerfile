FROM python:3.9-alpine

RUN mkdir /usr/pydiceweb
WORKDIR /usr/pydiceweb

RUN apk update
RUN apk add musl-dev mariadb-dev gcc build-base

COPY ../requirements.txt ./

RUN python -m pip install --upgrade --no-cache-dir setuptools
RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /application/pathseeker
COPY ../pyproject.toml ./

CMD python pathseeker/src/flask_app/new_db_setup.py & python -m pytest --black --isort --pylint --cov .
