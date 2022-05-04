# argument image instead of build**?
# https://docs.docker.com/compose/compose-file/#image
# -- Author: Christopher Ek and Lukas Eklund -- #
# -- Version: 1.12.1 ---------------------------#
# -- Date: 2022-04-27 --------------------------#
# -- License: MIT ------------------------------#
# -- Description: RESTAPI ------------------- #


FROM python:3.10-slim


WORKDIR /app/

COPY ./server.py ./

COPY ./index.html ./

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

CMD python server.py