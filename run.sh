#!/usr/bin/env bash

current_date=$(date +"%Y-%m-%d")
job_name=${1:-products}

scrapy crawl products -o "data/${job_name}.csv" -s JOBDIR="crawls/${job_name}" 2>&1 \
  | tee -a "logs/${job_name}_${current_date}.log"