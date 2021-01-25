import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


target_host = input(f"{Colors.red}(LibSSH Bypass Authentication){Colors.end} [Enter Target Host]:~#")
target_port = int(input(f"{Colors.red}(LibSSH Bypass Authentication){Colors.end} [Enter Target Port]:~#"))
log_file = input(f"{Colors.red}(LibSSH Bypass Authentication){Colors.end} [Enter Log File]:~#")
sub.call(f"python3 ../0days/libssh-bypass-authentifaction.py --host {target_host} -p {target_port} -log {log_file}", shell=True)