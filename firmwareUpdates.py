import subprocess


def updates():
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

