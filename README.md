# pcpartpicker

## Installation

Install docker. Build image by running the following command:

`docker build -t scrapy_pcpartpicker`

## Usage

Start new job:

`sbin/docker-run.sh job_name`

Find scraped data (CSV file) in the `data` directory, same name as `job_name`

### Jobs: pausing and resuming crawls

You can stop the spider safely at any time (by pressing Ctrl-C or sending a signal), and resume it later by issuing the above command with same `job_name`

Start new job by using new `job_name` or delete the directory corresponding with paused job's `job_name` in the `crawls` directory

## Settings

- `/conf/proxies` - a list of proxies to choose from.
- `/conf/seed_urls` - start urls to scrape
