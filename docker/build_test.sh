#! /bin/bash
SALMON_VERSION=0.13.0
docker build -t combinelab/salmon:${SALMON_VERSION} -t combinelab/salmon:latest .
