import subprocess


def updates():
    command_refresh = "sudo fwupdmgr refresh --force"
    command_get_updates = "sudo fwupdmgr get-updates"
    command_update = "sudo fwupdmgr update"

    print("\n>> Firmware Update...")

    if (subprocess.run(command_refresh, shell=True).returncode) == 0:
        print("Refresh... success")

        if (subprocess.run(command_get_updates, shell=True).returncode) == 0:
            print("Get updates... success")

            if (subprocess.run(command_update, shell=True).returncode) == 0:
                print("Firmare update... success")
            else:
                print("Error while process firmware updates")
        else:
            print("Error while get firmware updates")
        
        print("Update process successfully finished")
    else:
        print("Error while process updates")