import subprocess

def wake_on_lan(computer_name):
    #need to get the mac address of my computer, stored in a dictionary?
    wol = subprocess.run(["./commands/wol.sh", mac_address_to_wake])
