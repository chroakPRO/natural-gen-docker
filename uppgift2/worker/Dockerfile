FROM python:3.10-slim


ENV START_NUMBER=1

ARG MAINTAINER="LE"

ARG LE=worker.py


ENV LE=$LE

WORKDIR /app/

COPY ./worker.py ./

COPY ./requirements.txt ./

RUN pip install -r requirements.txt 

CMD python $LE $START_NUMBER=1