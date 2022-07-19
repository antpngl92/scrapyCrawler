# scrapyCrawler
Spider bot for scraping web content and storing it into sqlite database

## Setup

### Prerequisites
1. Python >= 3.8

### Setup virtualenv (`conda` example)
```
conda create scrapyCrawler
conda activate scrapyCrawler
conda install pip
``` 

### Install project's requirements
```
conda activate scrapyCrawler
pip install -r requiremnets.txt
```


### Run spider
```scrapy crawl products```

## Overview
1) Database setup
* Once the spider is initiated it will automatically create sqlite3 database if it doesn't already exist. This is done by the 
`database_setup()` function located in `scrapyCrawler/database_setup.py`
2) JSON Schema validation
* The project uses scrapy-jsonschema package for validating an `Item`. The schema is located at `scrapyCrawler/items.py`
