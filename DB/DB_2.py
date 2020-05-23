import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute("CREATE TABLE kakao(ID text, PW text)")

conn.commit()

conn.close()