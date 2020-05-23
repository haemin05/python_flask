import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("select * from kakao")

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()