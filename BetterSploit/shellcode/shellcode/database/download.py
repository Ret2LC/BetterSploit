#/usr/bin/python3
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-f", metavar="", help="http://shell-storm.org/shellcode/files/shellcode-700.php", required=True)
parser.add_argument("--name", metavar="", help="/home/user/Desktop/filename.s", required=True)
arguments = parser.parse_args()

class DownloadFunction(object):
    def __init__(self, url_to_file, filename):
        self.url_to_file = url_to_file
        self.filename = filename

    def download(self):
        with open(arguments.name, "w") as downloaded_file:
            response = requests.get(arguments.f)
            
            if response.status_code == 200:
                downloaded_file.write(response.text)
                downloaded_file.close()
                print("\r\n[+]__SUCCESS__[+]")
                exit(0)
            else:
                print("\r\n[+]__FAILED__[+]")
                exit(0)

if __name__ == '__main__':
    functions = DownloadFunction(url_to_file=arguments.f,
    filename=arguments.name)
    functions.download()