import sqlite3
def create_db():
    con = sqlite3.connect(database='bs.db')
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        pr_id INTEGER PRIMARY KEY,
        pr_name TEXT,
        stocks INTEGER,
        cost_price REAL,
        sell_price REAL,
        gst REAL,
        ven_name TEXT,
        ven_num TEXT
    );
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        admin TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        location TEXT NOT NULL,
        pass TEXT NOT NULL
    );
    """)
    con.commit()

create_db()