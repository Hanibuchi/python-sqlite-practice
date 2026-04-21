import sqlite3

conn = sqlite3.connect("sample.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Taro", 20))
conn.commit()

cur.execute("SELECT id, name, age FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()