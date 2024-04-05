import sqlite3

db = sqlite3.connect('users.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id integer,
    text_id text,
    user_name text,
    balance integer
)""")

db.commit()

db.close()