import sqlite3


def database_setup():
    connection = sqlite3.connect('products.db')
    currsor = connection.cursor()

    currsor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            title text,
            category text,
            subcategory text,
            subtitle text,
            product_number text PRIMARY KEY,
            price decimal(10,2)
        )"""
    )

    connection.commit()
    connection.close()
