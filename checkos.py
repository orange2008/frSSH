# This is used to check the operating system that the end user is on.
from platform import platform

def getos():
    pf = platform()
    if 'Windows' in pf:
        return 1
    elif 'Linux' in pf:
        return 2
    elif 'Darwin' or 'macOS' in pf:
        return 3
    else:
        # What the fuck is this system
        return 0