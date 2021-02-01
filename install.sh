#!/bin/bash 

setup() {
  # shellcheck disable=SC2154
  file="$Requirements.py"
        # shellcheck disable=SC2086
        python3 $file
        pip3 install requests_toolbelt
        pip install impacket
        sudo apt install exploitdb
        sudo apt install lolcat
        # shellcheck disable=SC2035
        sudo apt install golang
        pip3 install impacket
        # shellcheck disable=SC2035
        chmod +x *
        sudo gem install evil-winrm
        pip install paramiko
        ./BetterSploit.py --bettersploit
}
setup
