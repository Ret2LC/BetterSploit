# Remote Command Execution
# SQL Injection
import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'


def main(url, command):
    sub.call(f"python3 ../0days/Agent-Tesla-Botnet-Arbitrary-command-exec.py -c {command} {url}", shell=True)


main(url=input(f"{Colors.red}(Agent Tesla Botnet Remote Command Execution){Colors.end} [Enter Target URL]:~#"),
     command=input(f"{Colors.red}(Agent Tesla Botnet Remote Command Execution){Colors.end} [Enter Command]:~#"))
