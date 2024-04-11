import subprocess


def updates():
    command = "flatpak -y update"

    print("\n>> Flatpak Update...")

    if (subprocess.run(command, shell=True).returncode) == 0:
        print("Update process successfully finished")
    else:
        print("Error while process updates")