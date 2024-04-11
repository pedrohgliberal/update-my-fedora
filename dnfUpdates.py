import subprocess


def updates():
    command = ["sudo", "dnf", "-y", "upgrade", "--refresh"]

    print("\n>> Flatpak Update...")

    try:
        if (subprocess.run(command).returncode) == 0:
            print(">> Update process successfully finished<< ")
    except subprocess.CalledProcessError as e:
        print("Error:", e)