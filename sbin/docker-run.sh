#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
docker run -it -v ${SCRIPTPATH}/..:/app scrapy_pcpartpicker bash /app/run.sh "$@"