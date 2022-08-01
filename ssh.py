# Well this program is designed for Unix-based operating systems.
# i.e. Linux, macOS etc.
# Well anyhow
# This program is just used to execute OpenSSH built in to the parent OS.
# IT SHOULD NEVER BE USED TO RUN DIRECTLY.

import os
import sqlite3
from .sshpassinstall import installsshpass

    
def checksshpass():
    # Check if sshpass is installed
    # If not, ask the user to install it.
    # You will need sshpass in order to connect directly
    # But unfortunately most of the people don't have it.
    # So I'll let people decide it.
    print("Login via password directly will need 'sshpass', which is not installed by default.")
    print("Now checking if you have sshpass...")
    # Just use the dumb way.
    os.system("sshpass > keyfolder/sshpass.txt")
    with open("keyfolder/sshpass.txt", "r") as f:
        if "Usage" in f.read():
            # This guy do have sshpass
            return True
        else:
            # This asshole don't have sshpass
            print("It seems like you don't have sshpass installed.")
            print("Now dumping you to the automated installation.")
            installsshpass()
    
    # Hey you will need to delete the dumb file.
    os.remove("keyfolder/sshpass.txt")

def connectviakey(ip, port, username, keyid):
    # Connect to the server
    # Use the keyid to find the key
    # Use the key to connect to the server
    conn = sqlite3.connect('frSSH.db')
    c = conn.cursor()
    c.execute("SELECT key FROM keys WHERE id=?", (keyid,))
    key = c.fetchone()[0]
    # Get the ID of the key
    c.execute("SELECT id FROM keys WHERE key=?", (key,))
    keyid = c.fetchone()[0]
    keyid = str(keyid)
    conn.close()
    # Save the key to a file
    with open('keyfolder/' + str(keyid) + 'id.key', 'w') as f:
        f.write(key)
    filename = 'keyfolder/' + str(keyid) + 'id.key'
    # Execute the command
    while 1:
        # We are using a loop here just in case the end user has logged out accidentally.
        os.system("ssh -p " + str(port) + " -i " + filename + " " + username + "@" + ip)
        # Ask users if they want to logout entirely or login again.
        # Well sometimes some people want to logout and then login again.
        # I don't understand but I'm just a programmer.
        # That's none of my business XD
        opt = input("Do you really want to exit the session with the server? (y/n) ")
        if opt == 'y':
            break
        elif opt == 'n':
            continue
        else:
            print("Invalid input. Now logging out.")
            break

def connectviapassword(ip, port, username, password):
    # Connect to the server
    # Check if he/she has sshpass
    checksshpass()
    # Up until now, the sshpass should be installed.
    # Now we can use it to connect.
    os.system("sshpass -p '" + password + "' ssh -p " + str(port) + " " + username + "@" + ip)
    # Crap it sucks, I've spent an hour figuring out how to do this.
    # But whatever, it's done.
    return True