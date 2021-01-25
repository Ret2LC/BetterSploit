#!/usr/bin/python3
import os
import sys


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class SshPivoting(object):
    def __init__(self, local_port, local_ip, remote_port, username, ssh_hostname):
        self.local_port = local_port
        self.local_ip = local_ip
        self.username = username
        self.remote_port = remote_port
        self.ssh_hostname = ssh_hostname

    def pivot(self):
        os.system(f"ssh -L {self.local_port}:{self.local_ip}:{self.remote_port} {self.username}@{self.ssh_hostname}")


def enumeration_for_network():
    show_active_connections = os.system("netstat -lnap4")
    print("CURRENT CONNECTIONS AS SHOWN:\n\n\n" + str(show_active_connections))
    exit()


if __name__ == "__main__":
    try:
        if sys.argv[1] == "enumerate":
            enumeration_for_network()
    except IndexError:
        pivot = SshPivoting(
                local_port=input(f"{Colors.red}(SSH PIVOT){Colors.end} [Enter Local Port]"),
                local_ip=input(f"{Colors.red}(SSH PIVOT){Colors.end} [Enter Local Ip]"),
                remote_port=input(f"{Colors.red}(SSH PIVOT){Colors.end} [Enter Remote Port]"),
                ssh_hostname=input(f"{Colors.red}(SSH PIVOT){Colors.end} [Enter Hostname]"),
                username=input(f"{Colors.red}(SSH PIVOT){Colors.end} [Enter Username]"),
            )

        pivot.pivot()
