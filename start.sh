echo 'Enter filename to store scrapped data:'
read filename
scrapy crawl hh_spider -o $filename
sudo python3 HH_crawler/statistics.py