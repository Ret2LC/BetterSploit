import os


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, url):
        self.url = url

    def exploit_send(self):
        os.system(f"php-code-exec.py -u {self.url}")


if __name__ == '__main__':
    send = Exploit(url=input(
        f"{Colors.red}(PHP <7.x Remote Command Execution){Colors.end} [Enter URL (Example: https://localhost/index.php)]:~#"))
