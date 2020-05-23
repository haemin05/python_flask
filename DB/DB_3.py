import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("INSERT INTO kakao VALUES('haemin', 'hello')")

conn.commit()

conn.close()