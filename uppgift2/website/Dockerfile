FROM python:3.10-slim


WORKDIR /app/

COPY ./server.py ./

COPY ./index.html ./

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

CMD python server.py