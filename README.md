# hh_scraping
my crawler for top russian recruiting website https://hh.ru/

Crawler based on scrapy framework https://scrapy.org/



In scrapy parsers calling 'spiders' , so spider is HH_crawler/spiders/HH_spider.py

This spider crawl pages and scraping data from every vacancy to file by command : 

    $scrapy crawl hh_spider -o filename.csv

Selectors in spider tuned to scrape main skill tags and salary from every vacancy

Then scraped data calculating and analysing in HH_crawler/statistics.py :

    $python3 statistics.py

