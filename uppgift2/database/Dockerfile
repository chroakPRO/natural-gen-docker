# argument image instead of build**?
# https://docs.docker.com/compose/compose-file/#image
# -- Author: Christopher Ek and Lukas Eklund -- #
# -- Version: 1.12.1 ---------------------------#
# -- Date: 2022-04-27 --------------------------#
# -- License: MIT ------------------------------#
# -- Description: database -------------------- #


FROM postgres:latest

# env varaibles
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres 
ENV POSTGRES_DB postgres 

COPY init.sql /docker-entrypoint-initdb.d/