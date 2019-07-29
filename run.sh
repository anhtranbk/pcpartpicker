#!/usr/bin/env bash

current_date=$(date +"%Y-%m-%d")
scrapy crawl products -o data/products.csv -s JOBDIR='crawls/products' 2>&1 \
  | tee -a "logs/products_${current_date}.log"