import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_product(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)
database = r'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0.0
);
'''
connection = create_connection(database)
if connection is not None:
    print('Connected successfully!')

create_table(connection, sql_create_products_table)
def add_products():
    create_product(connection, ("Мыло для бобра", 1199.53, 122))
    create_product(connection, ("Мыло для всего, кроме бобра", 1198.52, 12))
    create_product(connection, ("Рыба с вонью", 15.99, 22))
    create_product(connection, ("рыба без вони", 15.53, 122))
    create_product(connection, ("Полотенце для веток", 129.58, 322))
    create_product(connection, ("Полотенце бобра", 90000.99, 122))
    create_product(connection, ("Обезьяна без ноги и руки", 1199.00, 1))
    create_product(connection, ("Обезьяна без проблем", 2000.00, 2))
    create_product(connection, ("Обезьяна не без изьяна", 199.00, 7))
    create_product(connection, ("Мыло не без бобра", 1199.53, 122))
    create_product(connection, ("Мыло для всего и бобра", 1198.52, 12))
    create_product(connection, ("Рыба", 15.99, 22))
    create_product(connection, ("Повелитель вони", 15.53, 122))
def update_product_quantity(conn, id, quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (quantity, id))
        conn.commit()
    except Error as e:
        print(e)

def update_productd_price(conn, id, price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price, id))
        conn.commit()
    except Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)
def select_students_by_price_and_quantity(conn):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products WHERE price < 100 and products WHERE quantity < 5?'''
        cursor = conn.cursor()
        cursor.execute(sql, (100, 5))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)

def select_students_by_mark_limit(conn, product_title1):
    try:
        sql = '''SELECT id, product_title, price, quantity FROM products WHERE product_title1 in product_title '''
        cursor = conn.cursor()
        cursor.execute(sql, (product_title1,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)



