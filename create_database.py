import os
import sqlite3


def create_table():
    connection = sqlite3.connect("goods.db")
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE goods'
                   '(id INTEGER PRIMARY KEY,'
                   'name VARCHAR(20),'
                   'type VARCHAR(20),'
                   'image VARCHAR(100),'
                   'price VARCHAR(20))')

    connection.close()


def create_test_data():
    connection = sqlite3.connect("goods.db")
    cursor = connection.cursor()

    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(1, \'iPhone 7\', \'smartphone\', \'./images/smartphone/apple.jpg\', \'800 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(2, \'Samsung S8\', \'smartphone\', \'./images/smartphone/samsung.jpg\', \'750 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(3, \'Google Pixel\', \'smartphone\', \'./images/smartphone/google.jpg\', \'700 AED\')')

    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(4, \'Adidas\', \'bag\', \'./images/bag/adidas.jpg\', \'250 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(5, \'Nike\', \'bag\', \'./images/bag/nike.jpg\', \'200 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(6, \'Puma\', \'bag\', \'./images/bag/puma.jpg\', \'150 AED\')')

    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(7, \'iWatch\', \'spectacles\', \'./images/spectacles/apple.jpg\', \'250 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(8, \'Samsung Gear\', \'spectacles\', \'./images/spectacles/samsung.jpg\', \'650 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(9, \'Google Glass\', \'spectacles\', \'./images/spectacles/google.jpg\', \'1200 AED\')')

    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(10, \'Apple Watch\', \'watch\', \'./images/watch/apple.jpg\', \'500 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(11, \'Samsung Watch\', \'watch\', \'./images/watch/samsung.jpg\', \'350 AED\')')
    cursor.execute('INSERT INTO goods (id, name, type, image, price)'
                   'VALUES(12, \'Google Watch\', \'watch\', \'./images/watch/google.jpg\', \'400 AED\')')

    connection.commit()
    connection.close()


def get_data():
    connection = sqlite3.connect("goods.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM goods')
    for i in cursor.fetchall():
        print(i)

    connection.close()

create_table()
create_test_data()
get_data()
