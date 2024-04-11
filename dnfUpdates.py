import subprocess


def updates():
    command = "sudo dnf -y upgrade --refresh"

    print("\n>> DNF Update...")

    if (subprocess.run(command, shell=True).returncode) == 0:
        print("Update process successfully finished")
    else:
        print("Error while process updates")
