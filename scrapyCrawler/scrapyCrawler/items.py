from scrapy_jsonschema.item import JsonSchemaItem


class ProductItem(JsonSchemaItem):
    jsonschema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "$id": "https://gplay.bg/",
        "title": 'Hardware and Pheripheral Products from GPLAY',
        "type": "object",
        "properties": {
            "title": {
                "type": "string"
            },
            "category": {
                "type": "string"
            },
            "subcategory": {
                "type": "string"
            },
            "subtitle": {
                "type": "string",
                "description": "brief description of the product"
            },
            "product_number": {
                "type": "string",
                "description": "uniquely identifies the product"
            },
            "price": {
                "type": "number",
                "minimum": 0.00,
                "maximum": 199.99
            }
        },
        "required": [
            "category",
            "price",
            "product_number",
            "subcategory",
            "subtitle",
            "title"
        ],


    }

