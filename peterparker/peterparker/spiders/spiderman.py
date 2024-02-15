import scrapy
from scrapy.exceptions import CloseSpider
from peterparker.items import UrlStatuses
from datetime import datetime
import time
from settings import CRAWL_TIME_LIMIT

class SpidermanSpider(scrapy.Spider):
    name = "spiderman"
    allowed_domains = ["example.com"] # Note - Set your own url here!
    start_urls = ["https://example.com"] # Note - Set your own  url here.
    visited_urls = set()
    crawl_start_time = time.time()
    CRAWL_TIME_LIMIT
    

    def parse(self, response):
        urls = response.css('a::attr(href)').extract()
        for url in urls:
            if url not in self.visited_urls:
                self.visited_urls.add(url)
                yield response.follow(url, callback=self.parse)
        status = response.status
        url = response.url
        timestamp = datetime.now().strftime("%Y%m%d.%H%M%S")
        

        page_hits = UrlStatuses()
        page_hits['timestamp'] = timestamp
        page_hits['url'] = url
        page_hits['status'] = status
        yield page_hits

        if time.time() - self.crawl_start_time > CRAWL_TIME_LIMIT:
            self.log("Time limit reached")
            raise CloseSpider(reason="Time Limit Reached")

