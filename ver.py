# Get version and return it
# Just for lol
# If I don't modify this then it will be always the same.

# ONLY DEVELOPER CAN CHANGE THIS!!!!!
version = '1.0.0'
release = False # If this is enabled, then a 'beta' will be applied

def version():
    if release:
        verstring = "v" + str(version)
    else:
        verstring = "v" + str(version) + "beta"
    return verstring
