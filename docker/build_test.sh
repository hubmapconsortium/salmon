#! /bin/bash
SALMON_VERSION=1.3.0-hbm
docker build --no-cache -t combinelab/salmon:${SALMON_VERSION} -t combinelab/salmon:latest .
