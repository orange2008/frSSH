# This file is used to initialize the database.
# This should be run once before running the application.

import sqlite3

def init_db():
    # Create a database with the name "frSSH.db"
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    try:
        # Create a table with the name "servers"
        c.execute("""CREATE TABLE servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            ip TEXT NOT NULL,
            port INTEGER,
            username TEXT NOT NULL,
            password TEXT,
            keyid INTEGER
        )""")
    except sqlite3.OperationalError:
        # Table already exists
        pass
    try:
        # Create a table with the name "keys" with an ID
        c.execute("""CREATE TABLE keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            key TEXT NOT NULL
            )""")
    except sqlite3.OperationalError:
        # Table already exists
        pass
    conn.commit()
    conn.close()
    

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
