#!/bin/sh

docker build -t mindmap-app -f ./Dockerfile .
docker run -p 5000:5000 mindmap-app
