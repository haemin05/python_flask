import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()
try:
    cur.execute("INSERT INTO abc VALUES('banana', '200', '1')")
    cur.execute("INSERT INTO abc VALUES('apple', '1000', '2')")

    conn.commit()
except:
    print('not execute')

conn.close()