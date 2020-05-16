FROM python:3.7-alpine

RUN mkdir /usr/pydiceweb
WORKDIR /usr/pydiceweb

RUN apk update
RUN apk add musl-dev mariadb-dev gcc

COPY requirements.txt ./
COPY .coveragerc ./
COPY pylintrc ./

RUN python -m pip install --upgrade --no-cache-dir setuptools
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY pathseeker ./pathseeker

RUN python -m pytest --black --isort --pylint --cov pathseeker

CMD exec gunicorn --bind :$PORT --workers 1 pathseeker.src.app:APP