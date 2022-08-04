# This is the main UI
# It shouldn't be executed by users
# But whatever, this is the main interface.

# This file is written in Aug. 4, 2022
# It's really hard to catch up by the way...

from .operate import addserverviakey, addserverviapwd
from .maindb import list_keys, add_key, list_servers
from .ver import version
import sys

def ui_addkey():
    keyfile = input("Please input your key file path: ")
    keyfile = str(keyfile)
    return add_key(keyfile)

def ui_addserverviaprivkey(ip, port, username):
    print("Now listing your all keys...")
    keylist = list_keys()
    for current_tuple in keylist:
        current_pair = "ID: " + str(current_tuple[0]) + ", Description: " + str(current_tuple[1])
        print(current_pair)
    print("\n")
    alreadyhave = input("Do you have your ideal key? (y/n): ")
    alreadyhave = str(alreadyhave)
    if "y" in alreadyhave:
        keyid = input("Please input your key ID: ")
        keyid = int(keyid)
        addserverviakey(ip, port, username, keyid)
        return True
    else:
        print("Okay, let's add your key.")
        keyid = ui_addkey()
        addserverviakey(ip, port, username, keyid)
        return True


def ui_addserverviapassword(ip, port, username):
    # Ask users to type in their config.
    password = input("Please input your password (The password will be display as normal, so be careful and not screenshot or screen record anything on this page): ")
    password = str(password)
    addserverviapwd(ip, username, password, port)
    return True

def ui_addserver():
    ip = input("Okay, Please input your server's IP/Domain(i.e. 10.20.0.1 / server.example.com): ")
    port = input("Please input your server's port(i.e. 22), leave blank to use '22': ")
    if port == "":
        port = 22
    username = input("Please input your server's username(i.e. root): ")
    # Convert everything into 'String', just in case some losers will make their username full of numbers, which sucks.
    username = str(username)
    ip = str(ip) # Usually this is not needed.
    port = int(port)
    # Ask user if they would like to login via Key/Password
    loginmethod = input("How do you login? (key/password), leave blank to use password login: ")
    # Some bitches would type some random numbers here.
    # So we are going to convert them to usable string
    loginmethod = str(loginmethod)
    if "key" in loginmethod:
        print("Seems like you are going to use Private Key login.")
        print("Now dumping you to subfunction to do further configuration.")
        ui_addserverviaprivkey(ip, port, username)
        print("\nCongrats! You have added your server!")
        return True
    else:
        print("Seems like you are going to use password login.")
        print("Now dumping you to subfunction to do further configuration.")
        ui_addserverviapassword(ip, port, username)
        print("\nCongrats! You have added your server!")
        return True

def ui_listserver():
    print("Now listing your all servers...")
    serverlist = list_servers()
    for current_tuple in serverlist:
        current_pair = "ID: " + str(current_tuple[0]) + ", Description: " + str(current_tuple[1])
        print(current_pair)
    print("\n")
    return True

def main():
    print("*-" * 5 + " Welcome to frSSH " + "-*" * 5)
    print("Version: " + version())
    print("\n")
    print("What would you like to do?")
    print("1. Add a server")
    print("2. Update a server")
    print("3. Delete a server")
    print("4. Connect to a server")
    print("5. List all servers")
    print("6. Add a key")
    print("7. Delete a key")
    print("8. List all keys")
    print("*-" * 5 + "" + "-*" * 5)
    print("9. Flush the database (DANGEROUS)")
    print("10. Quit")
    opt = input("Please input your option: ")
    try:
        opt = int(opt)
    except:
        print("Invalid option.")
        main() # This is really poor designed.
    if opt == 1:
        ui_addserver()
        main()
    elif opt == 2:
        print("Not implemented yet.")
        main()
    elif opt == 3:
        print("Not implemented yet.")
        main()
    elif opt == 4:
        print("Not implemented yet.")
        main()
    elif opt == 5:
        ui_listserver()
        main()
    elif opt == 6:
        ui_addkey()
        main()
    elif opt == 7:
        print("Not implemented yet.")
        main()
    elif opt == 8:
        print("Not implemented yet.")
        main()
    elif opt == 9:
        print("Not implemented yet.")
        main()
    elif opt == 10:
        print("Bye!")
        sys.exit(0)


def guide():
    print("You are now in the Beginners' Guide.")
    print("Now we are going to add your first server.")
    ui_addserver()
    # LOLOLOL The so called "Beginners' Guide" is just a joke.
    # Threw you to the main program.
    main()