#!/bin/bash

# Remove images, uneccessary in production
docker rm $(docker ps -a -q) --force
docker rmi $(docker images -q) --force

# Run docker compose
docker-compose -f docker-compose.yml up -d

