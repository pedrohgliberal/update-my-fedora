import subprocess


def updates():
    dnf_command = "sudo dnf -y upgrade --refresh"

    print("\n>> DNF Update...")

    if (subprocess.run(dnf_command, shell=True).returncode) == 0:
        print("Sucesso")
