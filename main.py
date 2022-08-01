# This is the main frame
# User should only run this program in this directory.

# Check if this is the first run.

from .guide import main as guide
import sys
from .ui import main as ui

# All modules are independent from each other because it will be easier for me to fix and this is good for the open-source community.
# Below are function modules.

def checkfirstrun():
    try:
        # Just try to open the database.
        # If this is not exist then this should be the first run LOL.
        # If some motherfuckers delete the database then that's none of my business LOL.
        open("frSSH.db")
    except FileNotFoundError:
        print("First run detected, now going to the Beginners' Guide.")
        # This is the first run so we need to run the guide.
        guide()
        # Don't want to bother anything else, just let them go.
        sys.exit(0)

# Below are the main program.
# Check if this is the first run.
checkfirstrun()

# HAHA, BEING CHEATED
# This is not the main program actually.
# Well technically it is.
# But everything we will be done will be in the so called "UI" module.
# So I'm transferring you to the main UI.
ui()
print("*" + "-" * 10 + "*")
print("Thanks for using frSSH, see ya later!")