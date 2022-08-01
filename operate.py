# This is the main Operating Library.
# One of the most important library of this program.
# But hey I'm not saying that others are not important
# Oh whatever
# Bullshit aside, let's do the main stuff.

# Database is always the most critical thing to do.
import sqlite3

def addserverviapwd(ip, username, password, port):
    # Connect database
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    # Add server
    c.execute("INSERT INTO servers (ip, username, password, port) VALUES ('?', '?', '?', ?)", (ip, username, password, port))
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    return True

def addserverviakey(ip, username, port, keyid):
    # Connect database
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    # Add server
    c.execute("INSERT INTO servers (ip, username, keyid, port) VALUES ('?', '?', ?, ?)", (ip, username, keyid, port))
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()
    return True