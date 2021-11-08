FROM python:3.8-alpine

ARG TEST_PYPI_USERNAME
ARG TEST_PYPI_PASSWORD

RUN mkdir /slots

WORKDIR /slots

RUN python3 -m pip install --upgrade build
RUN python3 -m build

RUN python3 -m pip install --upgrade twine
RUN python3 -m twine upload --repository testpypi dist/* 
RUN echo "username: $TEST_PYPI_USERNAME\n\tpassword: $TEST_PYPI_PASSWORD"