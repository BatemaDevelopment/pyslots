FROM python:3.8-alpine

RUN apk add --no-cache musl-dev libffi-dev gcc

ARG PYPI_USERNAME
ARG PYPI_PASSWORD

RUN mkdir /slots

WORKDIR /slots

COPY . .

RUN python3 -m pip install --upgrade build
RUN python3 -m build

RUN python3 -m pip install --upgrade twine
RUN python3 -m twine upload -u $PYPI_USERNAME -p $PYPI_PASSWORD --repository pypi dist/*
