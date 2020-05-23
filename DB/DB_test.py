import sqlite3

conn = sqlite3.connect('test.db')

cur = conn.cursor()

cur.execute('CREATE TABLE abc(fruit text PRIMARY KEY, price text, number text)')

conn.commit()

conn.close()