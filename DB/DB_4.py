import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()
try:
    cur.execute("INSERT INTO kakao VALUES('haemin', 'hello')")

    conn.commit()
except:
    print('not execute')

conn.close()