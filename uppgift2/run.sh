#!/usr/bin/env sh
docker run -d -p 5432:5432 -t data1
docker run -d -p 5000:5000 -t web1
docker run -d -t wor1