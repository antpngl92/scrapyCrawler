from urllib.parse import urljoin

import scrapy

from ..constants import DOMAIN, PRODUCTS_FILTERS
from ..items import ProductItem


# TODO: add database setup (check if database does not exist - create)
class BaseProductsSpider(scrapy.Spider):
    def parse(self, response):
        sub_cat_links = response.css('div.categories-grid-item a::attr(href)').extract()

        for sub_cat_link in sub_cat_links:
            sub_cat_link += PRODUCTS_FILTERS

            next_url = urljoin(response.url, sub_cat_link)
            self.log("next URL: %s" % next_url)


            yield response.follow(sub_cat_link, callback=self.products_parse)

    def products_parse(self, response):
        products = response.css('a.product-image::attr(href)').extract()

        for product in products:
            product = urljoin(response.url, product)

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
