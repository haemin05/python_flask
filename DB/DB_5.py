import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE kakao(id text PRIMARY KEY , PW text)")

conn.commit()

conn.close()