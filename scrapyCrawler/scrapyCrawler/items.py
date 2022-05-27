import scrapy


class ProductItem(scrapy.Item):
    title = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
    subtitle = scrapy.Field()
    product_number = scrapy.Field()
    price = scrapy.Field()
