import scrapy
from pcpartpicker.items import Product
import logging


class ProductSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        for line in open('conf/seed_urls.txt', encoding='utf-8').readlines():
            yield scrapy.Request(url=line.strip(), callback=self.parse_search_page)

    def parse_search_page(self, response):
        # self.logger.info(response.url)
        next_page = response.xpath('(//li[a[@class="pagination--current"]]/following-sibling::*)[1]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_search_page)
        for a in response.css('p.search_results--link a'):
            yield response.follow(a, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        # self.logger.info(response.url)
        url = response.url
        category = response.css('h3.pageTitle--categoryTitle a::text').get()
        # name = response.css('h1.pageTitle::text').get()
        name = response.css('title::text').get().replace(' - PCPartPicker', '')
        merchant = response.css('td.td__logo img::attr(alt)').get()
        base_price = response.css('td.td__base::text').get()
        total_price = response.css('td.td__finalPrice a::text').get()
        in_stock = 1 if total_price else 0

        yield Product(
            url=url,
            category=category,
            name=name,
            merchant=merchant,
            base_price=base_price,
            total_price=total_price,
            in_stock=in_stock
        )

    def parse(self, response):
        pass
