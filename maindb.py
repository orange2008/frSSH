# This file is mainly used to manage the critical data in the database.
# It is used to add, remove, and update servers.
# It is used to add, remove, and update keys.

# IT SHOULD NEVER BE USED TO RUN DIRECTLY.


import sqlite3
from .dbinitalization import init_db

def initdb():
    # This should only be used on the first run.
    init_db()

def add_server(ip, port, username, password, keyid):
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("INSERT INTO servers (ip, port, username, password, keyid) VALUES (?, ?, ?, ?, ?)", (ip, port, username, password, keyid))
    conn.commit()
    conn.close()
    print("Server added.")

def remove_server(ip, port, username, password, keyid):
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("DELETE FROM servers WHERE ip=?", (ip,))
    conn.commit()
    conn.close()
    print("Server removed.")
    
def update_server(ip, port, username, password, keyid):
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("UPDATE servers SET ip=?, port=?, username=?, password=?, keyid=? WHERE ip=?", (ip, port, username, password, keyid, ip))
    conn.commit()
    conn.close()
    print("Server updated.")

def add_key(keyfile):
    # The private key is usually in a file so we need to read it in.
    with open(keyfile, 'r') as f:
        key = f.read()
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("INSERT INTO keys (key) VALUES (?)", (key,))
    # Read the ID
    keyid = c.lastrowid
    conn.commit()
    conn.close()
    print("Key added with key ID: " + str(keyid))

def remove_key(keyid):
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("DELETE FROM keys WHERE id=?", (keyid,))
    conn.commit()
    conn.close()
    print("Key removed.")

# Copyright (C) 2022 Frank Ruan w/ GitHub Copilot.
# Licensed under GPLv3.0.