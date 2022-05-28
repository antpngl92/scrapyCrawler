import sqlite3


class ProductPipeline(object):
    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = sqlite3.connect('products.db')
        self.curr = self.conn.cursor()


    def store_to_db(self, item):
        self.curr.execute("""
            INSERT INTO products
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(product_number) DO UPDATE
            SET title = ?, subtitle = ?, price = ?
                            """,(
                                    item['title'],
                                    item['category'],
                                    item['sub_category'],
                                    item['subtitle'],
                                    item['product_number'],
                                    item['price'],
                                    # The values bellow are used for update
                                    item['title'],
                                    item['subtitle'],
                                    item['price'],
                                )
        )
        self.conn.commit()


    def process_item(self, item, spider):
        self.store_to_db(item)
        return item
