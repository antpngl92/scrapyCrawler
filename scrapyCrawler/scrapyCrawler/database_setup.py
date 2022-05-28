import sqlite3

connection = sqlite3.connect('products.db')
currsor = connection.cursor()

currsor.execute("""create table products (
                    title text,
                    category text,
                    sub_category text,
                    subtitle text,
                    product_number text PRIMARY KEY,
                    price decimal(10,2)
                )""")


connection.commit()
connection.close()
