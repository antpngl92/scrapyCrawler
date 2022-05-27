import scrapy

from ..items import ProductItem

DOMAIN = 'https://gplay.bg'


class ProductSpider(scrapy.Spider):
    name = 'products'

    start_urls = [
        'https://gplay.bg/hama-sonic-mobil-183'
    ]

    def parse(self, response):
        products = ProductItem()

        title = response.css('h1.large-title::text').extract()[0].strip('\n')
        __breadcrum_paths = response.css('div.path a::attr(href)').extract()
        category = __breadcrum_paths[1].strip(DOMAIN + '/')
        sub_category = __breadcrum_paths[2].strip(DOMAIN + '/')
        subtitle = response.css('h2.product-subtitle::text').extract()[0].strip('\n')
        product_number = response.css('div.product-ref-number strong::text').extract()[0]
        __price_element = response.css('div.normal-price price').extract()[0]
        price = __price_element.split("\"")[1]

        products['title'] = title
        products['category'] = category
        products['sub_category']= sub_category
        products['subtitle'] = subtitle
        products['product_number'] = product_number
        products['price'] = price

        yield products
