#!/bin/bash

echo "Stopping any containers on port 8089"
docker ps -q --filter "publish=8089" | xargs -r docker stop

echo "Creating reports folder if it doesn't exist"
mkdir -p reports

echo "Building locust-docker-image"
docker build -t locust-docker-image .

echo "Starting docker container in browser mode"
docker run -p 8089:8089 -v $(pwd)/reports:/app/reports locust-docker-image --host=https://jsonplaceholder.typicode.com

echo "Open the locust dashboard in http://localhost:8089 in your browser"