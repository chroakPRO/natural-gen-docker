# argument image instead of build**?
# https://docs.docker.com/compose/compose-file/#image
# -- Author: Christopher Ek and Lukas Eklund -- #
# -- Version: 1.12.1 ---------------------------#
# -- Date: 2022-04-27 --------------------------#
# -- License: MIT ------------------------------#
# -- Description: py worker ------------------- #


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