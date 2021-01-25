import subprocess as sub
import os


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


scanners = {
    1: "git clone https://github.com/skavngr/rapidscan.git",
    2: "git clone https://github.com/04x/ICG-AutoExploiterBoT.git",
    3: "git clone https://github.com/pradeepjairamani/CMS_Striker.git",
    4: "git clone https://github.com/EnableSecurity/wafw00f.git",
}
print("""
                             _____ _ _ _____
                            |  _  | | |   __|___ ___ ___
                            |     | | |__   |  _| .'|   |
                            |__|__|_|_|_____|___|__,|_|_|\n""")

# Download Parth And Make a function for i
def all_scan():
    print(f"""\n\n{Colors.green}
Name                                Description
----                                -----------
1)   rapidscan                      All In One Vulnerability Scanner
2)   ICG-AutoExploiterBoT           Wordpress, Joomla, Drupal, OsCommerce, Prestashop, Opencart Vulnerability Scanner
3)   CMS_Striker                    AUTOMATED PENETRATION TESTING AND INFORMATION GATHERING FOR CONTENT MANAGEMENT SYSTEMS
4)   wafw00f                        Web Based Vulnerability Scanner
5)   Zap-Proxy                      Automatically Find Security Vulnerabilities In Your Web Applications
    """)
    all_scan_shell = input(f"{Colors.red}[ Enter Option ] :> ")
    if all_scan_shell == "1" or all_scan_shell == "fuxploider" or all_scan_shell == "Fuxploider":
        check_install = input("Do You Already Have fuxploider Installed? (y or n) : ")
        if check_install == "y" or check_install == "Y":
            directory_input = input("Enter Directory That fuxploider Is Located In > ")
            target = input("[ Enter Domain ] > ")
            sub.call(f"python {directory_input}/rapidscan.py {target}", shell=True)
        elif check_install == "n" or check_install == "N":
            sub.call(scanners[1], shell=True)
            directory_input = input("Enter Directory That fuxploider Is Located In > ")
            target = input("[ Enter Domain ] > ")
            sub.call(f"python {directory_input}/rapidscan.py {target}", shell=True)
        else:
            print("Error!")
    elif all_scan_shell == "2" or all_scan_shell == "ICG-AutoExploiterBoT":
        check_install = input("Do You Already Have ICG-AutoExploiterBoT Installed? (y or n) : ")
        if check_install == "y" or check_install == "Y":
            directory_input = input("Enter Directory That ICG-AutoExploiterBoT Is Located In > ")
            sub.call(f"python {directory_input}/icgAutoExploiter.py 1", shell=True)
        elif check_install == "n" or check_install == "N":
            sub.call(scanners[2], shell=True)
            directory_input = input("Enter Directory That ICG-AutoExploiterBoT Is Located In > ")
            sub.call(f"unzip {directory_input}/'ICGAutoExploiterv2.5 [2019 Update].zip'", shell=True)
            sub.call(f"python {directory_input}/icgAutoExploiter.py 1", shell=True)
        else:
            print("Error")
    elif all_scan_shell == "3" or all_scan_shell == "CMS_Striker":
        check_install = input("Do You Already Have ICG-AutoExploiterBoT Installed? (y or n) : ")
        if check_install == "y" or check_install == "Y":
            directory_input = input("Enter Directory That CMS_Striker Is Located In >")
            target_url = input("[ Enter URL ] :> ")
            sub.call(f"python {directory_input}/cms_striker.py -v -t {target_url}")
        elif check_install == "N" or check_install == "n":
            sub.call(scanners[3], shell=True)
            directory_input = input("Enter Directory That CMS_Striker Is Located In >")
            target_url = input("[ Enter URL ] :> ")
            sub.call(f"python {directory_input}/cms_striker.py -v -t {target_url}")
        else:
            print("Error")
    elif all_scan_shell == "wafw00f" or all_scan_shell == "4":
        check_install = input("Do You Already Have WafW00f Installed (y or n) > ")
        if check_install == "y" or check_install == "Y":
            target = input("Enter URL > ")
            sub.call(f"wafw00f -v -a {target}", shell=True)
        elif check_install == "n" or check_install == "N":
            sub.call(scanners[4], shell=True)
            sub.call("sudo python /home/user/wafw00f/setup.py install")
            target = input("Enter URL > ")
            sub.call(f"wafw00f -v -a {target}", shell=True)
        else:
            print("Error")
    elif all_scan_shell == "5" or all_scan_shell == "Zap-Proxy":
        check_install = input("Do You Already Have Zap-Proxy Installed (y or n) > ")
        if check_install == "Y" or check_install == "y":
            sub.call("owasp-zap", shell=True)
        elif check_install == "n" or check_install == "N":
            sub.call("sudo apt install owasp-zap", shell=True)
            sub.call("owasp-zap")
        else:
            print("Error")


if __name__ == "__main__":
    try:
        all_scan()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
