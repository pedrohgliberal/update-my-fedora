import os
import sys
import subprocess
import dnfUpdates
import flatpakUpdates
import firmwareUpdates


app_name = "Update My Fedora"
version = "1.0-beta"


def prompt_sudo(option):
    #check_sudo_cmd = "sudo -n uptime 2>&1 | grep \"load\" | wc -l"
    check_sudo_cmd = "sudo -v"

    if (subprocess.run(check_sudo_cmd, shell=True).returncode) == 0:
        return 0
    else:
        print(f"\nThe {option} option should be run with root privileges...")
        exit(1)


def main() -> int:
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
                dnfUpdates.updates()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 2:
            if prompt_sudo("Flatpak Update") == 0:
                flatpakUpdates.updates()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 3:
            if prompt_sudo("Firmware Update") == 0:
                firmwareUpdates.updates()
            else:
                print(f"\n>>>   Thanks to use {app_name}   <<<")
                return 0
        elif chosen == 4:
            if prompt_sudo("Update all") == 0:
                dnfUpdates.updates()
                flatpakUpdates.updates()
                firmwareUpdates.updates()
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


if __name__ == '__main__':
    sys.exit(main())