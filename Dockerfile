FROM python:3.8-alpine

RUN apk add --no-cache musl-dev libffi-dev gcc

ARG TEST_PYPI_USERNAME
ARG TEST_PYPI_PASSWORD

RUN mkdir /slots

WORKDIR /slots

RUN python3 -m pip install --upgrade build
RUN python3 -m build

RUN python3 -m pip install --upgrade twine
RUN python3 -m twine upload --repository testpypi dist/* $TEST_PYPI_USERNAME $TEST_PYPI_PASSWORD