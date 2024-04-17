import os
import sys
import pathlib
import subprocess


app_name = "Update My Fedora"
version = "1.0"


def prompt_sudo(option):
    check_sudo_cmd = "sudo -v"

    if (subprocess.run(check_sudo_cmd, shell=True).returncode) == 0:
        return 0
    else:
        print(f"\nThe {option} option should be run with root privileges...")
        exit(1)


def dnf_update():
    command = ["sudo", "dnf", "-y", "upgrade", "--refresh"]

    print("\n>> DNF Update...")

    try:
        if (subprocess.run(command).returncode) == 0:
            print(">> Update process successfully finished<< ")
    except subprocess.CalledProcessError as e:
        print("Error:", e)


def flatpak_update():
    command = ["flatpak", "-y", "update"]

    print("\n>> Flatpak Update...")

    try:
        if (subprocess.run(command).returncode) == 0:
            print(">> Update process successfully finished<< ")
    except subprocess.CalledProcessError as e:
        print("Error:", e)


def firmware_update():
    command_refresh = ["sudo", "fwupdmgr", "refresh", "--force"]
    command_get_updates = ["sudo", "fwupdmgr", "get-updates"]
    command_update = ["sudo", "fwupdmgr", "update"]

    print("\n>> Firmware Update...")

    try:
        if (subprocess.run(command_refresh).returncode) == 0:
            print(">> Refresh... success <<\n")

        get_updates_status = subprocess.run(command_get_updates).returncode
        
        if (get_updates_status == 0 or
            get_updates_status == 2):            
            print(">> Get updates... success <<\n")
        
        if (subprocess.run(command_update).returncode == 0):
            print(">> Firmware update... success <<")

        print(">> Update process successfully finished<< ")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

def app_menu():
    while True:
        menu_opts = ({"id": 1, "info": "DNF Update"}, {"id": 2, "info": "Flatpak Update"}, 
                     {"id": 3, "info": "Firmware Update"}, {"id": 4, "info": "Update all"}, 
                     {"id": 0, "info": "Quit"})
        quit_opts = ({"id": 1, "info": "Return to Main menu"}, {"id": 0, "info": "Quit"})

        os.system("clear")

        print(f">>>   {app_name} v{version}   <<<\n")

        print("Main menu:")
        for opt in menu_opts:
            print("{id}. {info}".format(**opt))

        chosen = int(input("\nWhat should I update? "))
        
        while (chosen < 0) or (chosen > 4):
            print(f"\n>> WARNING: Invalid option was choosen: {chosen}!")
            chosen = int(input("\nWhat should I update? "))
        
        if chosen == 0:
            print(f"\n>>>   Thanks to use {app_name} v{version}   <<<")
            return 0
        elif chosen == 1:
            if prompt_sudo("DNF Update") == 0:
                dnf_update()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 2:
            if prompt_sudo("Flatpak Update") == 0:
                flatpak_update()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 3:
            if prompt_sudo("Firmware Update") == 0:
                firmware_update()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 4:
            if prompt_sudo("Update all") == 0:
                dnf_update()
                flatpak_update()
                firmware_update()
            else:
                print(f"\n>>>   Thanks to use {app_name} v{version}   <<<")
                return 0
        
        print("\nQuit menu:")        
        for opt in quit_opts:
            print("{id}. {info}".format(**opt))
        
        chosen = int(input("\nWhat should I do? "))

        while (chosen < 0) or (chosen > 1):
            print(f">> WARNING: Invalid option was choosen")
            chosen = int(input("What should I do? "))
        
        if chosen == 0:
            print(f"\n>>>   Thanks to use {app_name} v{version}   <<<")
            return 0


def main() -> int:
    check_sudo_command = ["sudo", "-n", "true", ">", "/dev/null", "2>&1"]

    if subprocess.run(check_sudo_command).returncode == 0:
        app_menu()
    else:
        app_command = ["sudo", "python"]
        app_command.append(str(pathlib.Path(__file__)))

        print("This app should run with root privileges...\nEnter your sudo password...")
        subprocess.run(app_command)


if __name__ == '__main__':
    sys.exit(main())