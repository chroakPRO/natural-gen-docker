#!/usr/bin/env sh

docker build -t web1 . -f website/Dockerfile
docker build -t wor1 . -f worker/Dockerfile
docker build -t data1 . -f database/Dockerfile