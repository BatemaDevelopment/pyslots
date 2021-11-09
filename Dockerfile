FROM python:3.8-alpine

RUN apk add --no-cache musl-dev libffi-dev gcc

ARG TEST_PYPI_USERNAME
ARG TEST_PYPI_PASSWORD

RUN mkdir /slots

WORKDIR /slots

COPY . .

RUN python3 -m pip install --upgrade build
RUN python3 -m build

RUN python3 -m pip install --upgrade twine
RUN python3 -m twine upload -u $TEST_PYPI_USERNAME -p $TEST_PYPI_PASSWORD --repository testpypi dist/*