import sqlite3


class ProductPipeline(object):
    def open_spider(self, spider):
        self.create_connection()
        self.items = []


    def create_connection(self):
        self.conn = sqlite3.connect('products.db')
        self.curr = self.conn.cursor()


    def store_to_db(self):
        sql = """
        INSERT INTO products (title, category, subcategory, subtitle, product_number, price)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(product_number) DO UPDATE
         SET title = EXCLUDED.title, subtitle = EXCLUDED.subtitle, price = EXCLUDED.price
        """
        data = [list(item.values()) for item in self.items]

        self.curr.executemany(sql, data)
        self.conn.commit()


    def process_item(self, item, spider):
        self.items.append(item)
        if len(self.items) == 100:
            self.store_to_db()
            self.items = []

        return item


    def close_spider(self,spider):
        if self.items:
            self.store_to_db()

        self.conn.close()
