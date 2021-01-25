import os
import time


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


class BeginEnumeration(object):
    def __init__(self, target_source_code):
        self.target_source_code = target_source_code

    def call_enumerator(self):
        print(f"[{Colors.green}Beginning Enumeration On {self.target_source_code}{Colors.end}]")
        time.sleep(2)
        os.system(f"./enumerator.sh {self.target_source_code}")
        print(f"[{Colors.green}+{Colors.end}] DONE!")


if __name__ == '__main__':
    begin = BeginEnumeration(target_source_code=input(f"{Colors.red}(AnyLizer){Colors.end} [Enter File]:~#"))
    begin.call_enumerator()