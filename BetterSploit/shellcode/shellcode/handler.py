import subprocess
import os

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    green = '\033[0;32m'
    end = '\033[m'

def handler():
    print(f"""
╔═══════════════════════════════════╗
║   [{Colors.green}1{Colors.end}]  Query Shellcode Database   ║
║   [{Colors.green}2{Colors.end}]  Download From URL          ║
║   [{Colors.green}3{Colors.end}]  exit                       ║
╚═══════════════════════════════════╝
""")
    while True:
        shell = input(f"{Colors.red}(Shellcode@CLI){Colors.end} [Handler]:~#")
        if shell == "1":
            keyword = input(f"{Colors.red}(Shellcode@CLI){Colors.end} [Enter Keyword]:~#")
            subprocess.call(f"python3 database/query.py {keyword}", shell=True)
        elif shell == "2":
            filename = input(f"{Colors.red}(Shellcode@CLI){Colors.end} [Enter Filename To Save Results]:~#")
            url_to_file = input(f"{Colors.red}(Shellcode@CLI){Colors.end} [Enter URL To File]:~#")
            subprocess.call(f"python3 database/download.py -f {url_to_file} --name {filename}", shell=True)
        elif shell == "3":
            break
        else:
            print(f"[{Colors.green}-{Colors.end}] Invalid Option...")
if __name__ == '__main__':
    try:
        handler()
    except KeyboardInterrupt:
        exit(0)
