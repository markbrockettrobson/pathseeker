FROM python:3.9-alpine

RUN mkdir /usr/pathseeker_web
WORKDIR /usr/pathseeker_web

RUN apk update
RUN apk add musl-dev mariadb-dev gcc build-base

COPY requirements.txt ./

RUN python -m pip install --upgrade --no-cache-dir setuptools
RUN python -m pip install --no-cache-dir -r requirements.txt

WORKDIR /application/pathseeker
ENV PYTHONPATH "${PYTHONPATH}:/application/pathseeker_web"

COPY pyproject.toml ./
COPY pathseeker ./pathseeker

RUN ls & python -m pytest --black --isort --pylint pathseeker

CMD exec gunicorn --bind :$PORT --workers 1 pathseeker.src.app:APP