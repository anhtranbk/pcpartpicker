# pcpartpicker

## Installation

Install docker. Build image by running the following command:

`docker build -t scrapy_pcpartpicker` .

## Usage

Start new job:

`sbin/docker-run.sh job_name`

`job_name`: name of job will be started

Find scraped data (CSV file) in the `data` directory, same name as `job_name`

### Jobs: pausing and resuming crawls

You can stop the job safely at any time (by pressing Ctrl-C or sending a signal), and resume it later by issuing the above command with same `job_name`

Start new job by using new `job_name` or delete the directory corresponding with pausing job in the `crawls` directory

> Scraped data always append to the file same name as `job_name` even if you start a new job. Make sure delete old data before starting new job that has `job_name` same as a stopped job.

## Settings

- `/conf/proxies` - a list of proxies to choose from.
- `/conf/seed_urls` - start urls to scrape
