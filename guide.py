# This is the beginners' guide
# The main frame will decide if this needs to be run.

from .maindb import *
# Well this is the "Beginners' Guide", they shouldn't delete anything from the database.
# Wait why would they have database at this time lol.
from .ui import main as ui
from .ui import guide as uiguide

def main():
    print("*" + "-" * 10 + "*")
    print("Welcome to frSSH's setup guide!")
    print("*" + "-" * 10 + "*")
    print("Now initializing the database...")
    initdb()
    print("Database initialized.")
    print("*" + "-" * 10 + "*")
    opt = input("Would you like to add your first server? (y/n)")
    if opt == 'y':
        pass
    else:
        print("Okay, then I think you are a really confident guy.")
        print("Dumping you to the main UI...")
        ui()
    # I think we might just dump this guy to the main UI, but with some magic arguments.
    print("Okay, to ensure the ease of programming, I'm now dumping you to the main UI but with some special data.")
    print("Hang on a sec please.")
    uiguide()
    print("Now you are back to the Beginners' Guide.")
    print("But I think it's unnecessary for you to walk through this.")
    print("Transferring you to the main UI.")
    ui()
    