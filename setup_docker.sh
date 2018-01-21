#!/bin/bash

mkdir -p tmp/
git clone --recursive git@github.com:mcgill-robotics/${ROBOT}.git tmp/${ROBOT}
docker build . --build-arg ROBOT=${ROBOT} --tag ${ROBOT}
rm -rf tmp/
