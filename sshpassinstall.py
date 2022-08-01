# This script is just used to install sshpass for those who don't have it.
# Fucking Windows users will download my pre-compiled sshpass here.
# I'm not sure if this is the best way to do it but it works.
# Linux & macOS users will be compiled here.

import os
from urllib.request import urlretrieve
from .checkos import getos
import sys

def installsshpass():
    print("To ensure the transparency, we are displaying the verbose log of installation.")
    print("Now checking your OS platform")
    osplat = getos()
    if osplat == 1:
        # Microsoft Windows platform detected
        print("Microsoft Windows detected")
        windows()
    elif osplat == 2:
        # Linux platform detected
        print("Linux detected")
        linux()
    elif osplat == 3:
        # macOS platform detected
        print("macOS detected")
        macos()
    else:
        # What the fuck is this.
        print("This is not a supported operating system.")
        print("Please contact the author of this program.")
        print("Contact the author on https://frank-ruan.com/about")
        # Just exit the program.
        # I'm done.
        sys.exit(1)



def windows():
    print("Now downloading pre-compiled SSHPass")
    # Download the pre-compiled sshpass from my CDN
    urlretrieve("https://cdn.frank-ruan.com/frSSH/sshpass/sshpass.exe", "sshpass.exe")
    urlretrieve("https://cdn.frank-ruan.com/frSSH/sshpass/cygwin1.dll", "cygwin1.dll")
    print("Note: This sshpass was compiled using Cygwin on Windows Server 2022.")
    print("      It may not work on your system.")
    print("      If it doesn't work, please contact the author of this program.")
    print("      Contact the author on https://frank-ruan.com/about")
    print("Installation completed.")
    return True
def linux():
    # NEVER PUT THIS PROGRAM INTO ANY FOLDER WITH SPACES
    # SOME BITCHES WOULD PUT THIS EVEN I HAVE SAID THAT EXPLICTLY IN THE DOCUMENT
    print("Now downloading SSHPass's source code")
    # Download the source code of sshpass from my CDN
    urlretrieve("https://cdn.frank-ruan.com/frSSH/sshpass/sshpass-1.09.tar.gz", "sshpass.tar.gz")
    print("Now extracting the source code")
    # Extract the source code
    os.system("tar -xzvf sshpass.tar.gz")
    print("Now compiling the source code")
    # Compile the source code
    os.system("cd sshpass-1.09 && ./configure && make && sudo make install")
    print("Now cleaning up")
    # Clean up
    os.system("rm -rf sshpass-1.09 sshpass.tar.gz")
    print("Installation completed.")
    return True
def macos():
    # Usually Darwin is the same as Linux
    # So I'm dumping those to linux()
    linux()
    return True