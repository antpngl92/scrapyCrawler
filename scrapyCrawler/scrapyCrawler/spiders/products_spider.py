from urllib.parse import urljoin

import scrapy

from ..constants import DOMAIN, PRODUCTS_FILTERS
from ..database_setup import database_setup
from ..items import ProductItem


class ProductsSpider(scrapy.Spider):
    name = 'products'

    start_urls = [
        DOMAIN
    ]

    def parse(self, response):
        database_setup()
        pheriperal_path = response.css('a[title="Периферия"]::attr(href)').get()
        hardware_path = response.css('a[title="Хардуер"]::attr(href)').get()

        for path in [pheriperal_path, hardware_path]:
            yield response.follow(path, callback=self.sub_categories_parse)


    def sub_categories_parse(self, response):
        sub_categories_paths = response.css('div.categories-grid-item a::attr(href)').extract()

        for path in sub_categories_paths:
            path += PRODUCTS_FILTERS

            yield response.follow(path, callback=self.products_parse)


    def products_parse(self, response):
        products = response.css('a.product-image::attr(href)').extract()
        for product in products:
            yield response.follow(product, callback=self.product_scrape)


    def product_scrape(self, response):
        products = ProductItem()

        title = response.css('h1.large-title::text').extract()[0].strip('\n')
        breadcrum_paths = response.css('div.path a::attr(href)').extract()
        category = breadcrum_paths[1].strip(DOMAIN + '/')
        sub_category = breadcrum_paths[2].strip(DOMAIN + '/')
        subtitle = response.css('.product-subtitle::text').get().strip('\n')
        product_number = response.css('div.product-ref-number strong::text').extract()[0]
        price_element = response.css('div.normal-price price').extract()[0]
        price = round(float(price_element.split("\"")[1]),2)

        products['title'] = title
        products['category'] = category
        products['sub_category']= sub_category
        products['subtitle'] = subtitle
        products['product_number'] = product_number
        products['price'] = price

        yield products
