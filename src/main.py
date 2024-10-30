import platform

def mac_welcome():

    mac_type = str(platform.mac_ver())
    mac_system = platform.system()

    if mac_type != "('', ('', '', ''), '')" and mac_system == "Darwin":
        return "You are on a Mac!"
    
    return "You are NOT on a Mac!"


