FROM python:3.6

RUN \
  apt-get update -y --fix-missing && \
  apt-get install -y \
  vim

RUN \
  mkdir /work

WORKDIR \
  /work

ADD \
  requirements.txt /work

RUN \
  pip install -U pip && \
  pip install -U -r requirements.txt
