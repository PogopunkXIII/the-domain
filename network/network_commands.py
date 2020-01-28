import subprocess

computers = { "Installation04", "04-D4-C4-54-D3-E9" }

def wake_on_lan(computer_name):
    print("You have accessed The Domain, {}".format(computer_name)
    wol = subprocess.run(["./commands/wol.sh", computers[computer_namecomputers[computer_name])
