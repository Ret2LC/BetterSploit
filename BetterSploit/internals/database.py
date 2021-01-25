import argparse


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


class MODULES(object):
    def __init__(self, exploits, router_exploits, post, auxiliary):
        self.exploits = exploits
        self.router_exploits = router_exploits
        self.post = post
        self.auxiliary = auxiliary

    def display_exploits_details(self, choice):
        choice = self.exploits
        details = {
            1: "NAME: smtplib/2.7.11-3.5.1StartTLS/Stripping   "
               "   DETAILS: https://www.exploit-db.com/exploits/43500",
            2: "NAME: Server/OpenSSL/Heartbleed   "
               "   DETAILS: https://en.wikipedia.org/wiki/Heartbleed",
            3: "NAME: VigileCMS/1.8/Stealth/RCE   "
               "   DETAILS: https://www.exploit-db.com/exploits/4643",
            4: "NAME: ProFTPd/1.3.5/Mod_Copy/RCE   "
               "   DETAILS: https://github.com/t0kx/exploit-CVE-2015-3306",
            5: "NAME: osCommerce/2.3.4.1/AFU   "
               "   DETAILS: https://www.exploit-db.com/exploits/43191",
            6: "NAME: SweetRice/1.5.1/File/Upload   "
               "   DETAILS: https://www.exploit-db.com/exploits/40716",
            7: "NAME: WordPress/4.7.0-4.7.1/Content-Injection   "
               "   DETAILS: https://www.exploit-db.com/exploits/41224",
            8: "NAME: phpMyAdmin/4.6.2/Authenticated/RCE   "
               "   DETAILS: https://packetstormsecurity.com/files/148222/phpMyAdmin-4.x-Remote-Code-Execution.html",
            9: "NAME: Bash/Shellshock/Environment-Variables/CMD-Injection   "
               "  DETAILS: https://www.exploit-db.com/exploits/34766",
            10: "NAME: ManageEngine-opManager/12.3.150/RCE   "
                "  DETAILS: https://www.exploit-db.com/exploits/47255",
            11: "NAME: TinyWebGallery-1.7.6/LFI/RCE   "
                "   DETAILS: https://packetstormsecurity.com/files/77367/TinyWebGallery-1.7.6-Local-File-Inclusion.html",
            12: "NAME: Traq-2.3/RCE   "
                "   DETAILS: https://www.tenable.com/plugins/nessus/62892",
            13: "NAME: TYPO3/Arbitrary-File-Retrieval   "
                "   DETAILS:   https://www.exploit-db.com/exploits/15856",
            14: "NAME: WebAsys/Blind-SQL-Injection   "
                "   DETAILS:   https://www.exploit-db.com/exploits/12724",
            15: "NAME: Dovecot/IMAP/1.0.10-1.1rc2/RED   "
                "   DETAILS: https://www.exploit-database.net/?id=9162",
            16: "NAME: Zomplog/3.8.1/AFU   "
                "   DETAILS: https://www.exploit-db.com/exploits/4466",
            17: "NAME: https://www.exploit-db.com/exploits/25305   "
                "   DETAILS: https://www.exploit-db.com/exploits/25305",
            18: "NAME: Dovecot/IMAP/1.0.10-1.1rc2   "
                "   DETAILS: https://www.exploit-db.com/exploits/5257",
            19: "NAME: Wolf-CMS/0.8.2/AFU   "
                "   DETAILS: https://www.exploit-db.com/exploits/36818",
            20: "NAME: Wordpress-Plugin/Simple-File-List/5.4/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/48349",
            21: "NAME: WordPress-Plugin/Download-Manager/2.7.4/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/35533",
            22: "NAME: WordPress-Plugin/wpDataTables/1.5.3/AFU   "
                "   DETAILS: https://www.exploit-db.com/exploits/35341",
            23: "NAME: Joomla/1.5<3.4.5/Object-Injection/x-forwarded-for/Header/RCE   "
                "   DETAILS: https://github.com/paralelo14/CVE-2015-8562",
            24: "NAME: phosheezy/2.0/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/7780",
            25: "NAME: Multiple-WordPress-Plugins/AFU   "
                "   DETAILS: collection of multiple wordpress plugins containing arbitrary file upload exploits",
            26: "NAME: Microsoft-Windows-7/2008-R2/EternalBlue/SMB  "
                "   DETAILS: https://www.avast.com/c-eternalblue",
            27: "NAME: Microsoft-Windows-8/8.1/2012-R2-(x64)/EternalBlue/SMB   "
                "   DETAILS: https://www.exploit-db.com/exploits/42030",
            28: "NAME: Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion   "
                "   DETAILS: https://www.exploit-db.com/exploits/48143",
            29: "NAME: WordPress-Plugin-Zingiri-2.2.3/ajax_save_name.php   "
                "   DETAILS: https://vulners.com/zdt/1337DAY-ID-17062",
            30: "NAME: Apache+PHP-5.3.12<5.4.2/RCE+Scanner   "
                "   DETAILS: https://www.exploit-db.com/exploits/29290",
            31: "NAME: Apache-CouchDB<2.1.0/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/44913",
            32: "NAME: Apache-James-Server/2.3.2/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/35513",
            33:
                "NAME: Apache-mod_cgi-Shellshock/RCI   "
                "   DETAILS: https://httpd.apache.org/docs/trunk/mod/mod_cgi.html",
            34:
                "NAME: Apache/mod_jk/1.2.19/(Windows x86)/RBO   "
                "   DETAILS: https://www.exploit-db.com/exploits/6100",
            35: "NAME: Apache-Solr-8.2.0/RCE   "
                "   DETAILS: https://github.com/theLSA/solr-rce",
            36:
                "NAME: Apache-Struts/REST-Plugin-With-Dynamic-Method-Invocation/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/43382",
            37:
                "NAME: Apache-Struts/2.0.1<2.3.33<2.5<2.5.10/ACE   "
                "   DETAILS: https://www.exploit-db.com/exploits/44556",
            38:
                "NAME: Apache-Struts/2.3<2.3.34<2.5<2.5.16/RCE   "
                "   DETAILS: https://www.cvedetails.com/cve/CVE-2018-11776/",
            39:
                "NAME: Apache-Struts/2.3.x/Showcase/RCE   "
                "   DETAILS: https://seclists.org/oss-sec/2017/q3/92",
            40:
                "NAME: Apache-Struts/2.5<2.5.12/REST-Plugin-XStream/RCE   "
                "   DETAILS: https://nvd.nist.gov/vuln/detail/CVE-2017-9805",
            41:
                "NAME: Apache-Tomcat/WebDAV/Remote-File-Disclosure   "
                "   DETAILS: https://www.exploit-db.com/exploits/4530",
            42: "NAME: Apache-Tomcat-AJP/Ghostcat/File-Read/Inclusion   "
                "   DETAILS: https://www.exploit-db.com/exploits/48143",
            43: "NAME: Apache-Tomcat<9.0.1<8.5.23<8.0.47<7.0.8/JSP/Upload-Bypass/RCE  "
                "   DETAILS: https://github.com/cyberheartmi9/CVE-2017-12617",
            44:
                "NAME: Joomla-Component-Recerca/SQL-Injection   "
                "   DETAILS: https://www.exploit-db.com/exploits/10058",
            45:
                "NAME: CNC-Telnet/Remote-Command-Execution   "
                "   DETAILS: pre authenticated CNC remote code execution (has to be running telnet)",
            46:
                "NAME: OpenSSH-7.2p1/(Authenticated)/xauth-Command-Injection    "
                "   DETAILS: https://www.exploit-db.com/exploits/39569",
            47:
                "NAME: phpMyAdmin/4.6.2/(Authenticated)/Remote-Code-Execution   "
                "   DETAILS: https://www.exploit-db.com/exploits/40185",
            48:
                "NAME: phpMyAdmin/pmaPWN!/Code-Injection/Remote-Code-Execution   "
                "   DETAILS: https://www.exploit-db.com/exploits/8992",
            49:
                "NAME: phpMyAdmin/3.x/Swekey/Remote-Code-Injection   "
                "   DETAILS: https://www.exploit-db.com/exploits/17514",
            50:
                "NAME: Broken-faq.php-frameork/Remote-Command-Execution   "
                "   DETAILS: remote code execution exploit for the broken faq.php framework",
            51:
                "NAME: pre-authenticated/SSH/RCE   "
                "   DETAILS: pre authenticated remote code execution for ssh",
            52:
                "NAME: Mida-eFramework-2.9.0/RCE   "
                "   DETAILS: https://www.exploit-db.com/exploits/48768",
            53:
                "NAME: Complaint-Management-System-1.0/cid-SQL-Injection   "
                "   DETAILS: https://www.exploit-db.com/exploits/48758",
            54:
                "NAME: Drupal/7.0-7.31/SQL-Injection-ADD-ADMIN-USER   "
                "   DETAILS: https://github.com/Unam3dd/drupal_sqli_add_admin/blob/master/drupal7_71_admin_sqli.py",
            55:
                "NAME: Webmin/Brute-Force/Remote-Command-Execution   "
                "   DETAILS: https://www.exploit-db.com/exploits/746",
            56:
                "NAME: Webmin/<1.290<1.220/Arbitrary-File-Disclosure   "
                "   DETAILS: https://gist.github.com/chrispetrou/067fed94c1bac5b06be2d4134173ff6c",
            57:
                "NAME: Nagios-XI/5.5.6/Remote-Code-Execution/Privilege-Escalation   "
                "   DETAILS: https://www.exploit-db.com/exploits/46221",
            58:
                "NAME: Nagios-XI/5.2.6<5.4-Chained-Remote-Root   "
                "   DETAILS: https://packetstormsecurity.com/files/147413/Nagios-XI-5.x-Chained-Remote-Root.html",
            59:
                "NAME: Apache-Tika-Server/<1.18/Arbitrary-File-Download    "
                "   DETAILS: download any file of the webserver",
            60:
                "NAME: Apache-Tika-server/<1.18/Command-Injection    "
                "   DETAILS: https://www.nmmapper.com/st/exploitdetails/46540/40985/apache-tika-server-118-command-injection/",
            61: "NAME: IOT-DEATH/Telnet-0-Day/Remote-Command-Execution/POC"
                "   DETAILS: just try's unauthenticated login to telnet and attempts remote code execution",
            62:
                "NAME: Imperva-SecureSphere/<13/Remote-Command-Execution   "
                "   DETAILS: https://www.exploit-db.com/exploits/45542",
            63:
                "NAME: WarFTP-1.65/(Windows 2000 SP4)-USER/Remote-Buffer-Overflow   "
                "   DETAILS: https://www.exploit-db.com/docs/english/13063-seh-overwrites-simplified.pdf",
            64:
                "NAME: BraveStarr/Remote-Fedora<31-telnetd-exploit   "
                "   DETAILS: netkit-telnet-0.17 telnetd (Fedora 31) - 'BraveStarr' Remote Code Execution (",
            65:
                "NAME: SSHtranger-Things/Multiple-Exploits   "
                "   DETAILS: https://www.exploit-db.com/exploits/46193",
            66:
                "NAME: ManageEngine-Applications-Manager-Authenticated-RCE   "
                "   DETAILS: https://www.digitalmunition.me/manageengine-applications-manager-authenticated-remote-code-execution-%E2%89%88-packet-storm/",
            67:
                "NAME: libssh-bypass-Authentication   "
                "   DETAILS: https://arstechnica.com/information-technology/2018/10/bug-in-libssh-makes-it-amazingly-easy-for-hackers-to-gain-root-access/",
            68:
                "NAME: ClearPass-Policy-Manager-Unauthenticated-RCE   "
                "   DETAILS: https://packetstormsecurity.com/files/158368/ClearPass-Policy-Manager-Unauthenticated-Remote-Command-Execution.html",
            69:
                "NAME: Cisco-7937G/All-In-One   "
                "   DETAILS: https://packetstormsecurity.com/files/158817/Cisco-7937G.py.txt",
            70:
                "NAME: Agent-Tesla-Botnet/Multi   "
                "   DETAILS: https://github.com/EgeBalci/AgentTesla_RCE",
            71:
                "NAME: Apache-CouchDB/Pre-Authenticated-Remote-Privilege-Escalation   "
                "   DETAILS: https://docs.couchdb.org/en/stable/cve/2017-12635.html",
            72: "NAME: Cayin-Digital-Signage-System-xPost-2.5/RCI"
                "   DETAILS: https://www.exploit-db.com/exploits/48558",
            73:
                "NAME: eGroupWare<1.14-spellchecker/Remote-Command-Execution   "
                "   DETAILS: https://npulse.net/en/exploits/48720",
            74:
                "NAME:  FaceSentry-Access-Control-System<6.4.8/Remote-Root-Exploit  "
                "   DETAILS: remote root exploit for face sentry access control system <6.4.8",
            75:
                "NAME: Joomla-hdwplayer<4.2/search.php/SQL-Injection   "
                "   DETAILS: vulnerable joomla extension exploit=sql injection",
            76:
                "NAME: LibreHealth<2.0-Pre-Authenticated-Remote-Command-Execution   "
                "   DETAILS: https://www.nmmapper.com/st/exploitdetails/48702/42960/librehealth-200-authenticated-remote-code-execution/",
            77:
                "NAME: Online-Course-Registration-1.0/Unauthenticated-RCE   "
                "   DETAILS: https://packetstormsecurity.com/files/158439/OCRv1_Unauth-RCE.py.txt",
            78:
                "NAME: PHPFusion<9.03.50-PHP-Object-Injection-to-SQL-injection   "
                "   DETAILS: https://www.digitalmunition.me/php-fusion-9-03-60-php-object-injection-sql-injection-%E2%89%88-packet-storm/",
            79:
                "NAME: Pi-Hole<4.3.2/Pre-Authenticated-Remote-Command-Execution   "
                "   DETAILS: https://github.com/team0se7en/CVE-2020-8816",
            80:
                "NAME: PulseSecure<9.0/Remote-Command-Execution   "
                "   DETAILS: remote code execution in the PulseSecure software before 9.0 and before",
            81:
                "NAME: rConfig<3.9.4-search.crud.php   "
                "   DETAILS: https://www.nmmapper.com/st/exploitdetails/48241/42510/rconfig-394-searchcrudphp-remote-command-injection/",
            82:
                "NAME: Ruby-On-Rails<5.0.1-Remote-Command-Execution    "
                "   DETAILS: https://packetstormsecurity.com/files/158604/Ruby-On-Rails-5.0.1-Remote-Code-Execution.html",
            83:
                "NAME: Tailor-Management-System/(id)-SQL-Injection-Vulnerability    "
                "   DETAILS: https://www.exploit-db.com/exploits/48797",
            84:
                "NAME: SMBGhost   "
                "   DETAILS: https://us-cert.cisa.gov/ncas/current-activity/2020/06/05/unpatched-microsoft-systems-vulnerable-cve-2020-0796",
            85:
                "NAME: Symantec-Web-Gateway<5.0.2.8-RCE   "
                "   DETAILS: https://packetstormsecurity.com/files/157175/Symantec-Web-Gateway-5.0.2.8-Remote-Code-Execution.html",
            86:
                "NAME: Umbraco<7.12.4/Remote-Command-Execution   "
                "   DETAILS: https://www.nmmapper.com/st/exploitdetails/46153/40673/umbraco-cms-7124-authenticated-remote-code-execution/",
            87:
                "NAME: CGI-In-WebDAV-Yaws-Web-Server<2.0.7/OS-CMD-Injection   "
                "   DETAILS: os command injection in WebDAV's implementation In Yaws web server".lower(),
            88:
                "NAME: WebDAV-implementation-In-Yaws-Web-Server<2.0.7/XXE-injection   "
                "   DETAILS: XXE injection in WebDAV's implementation In Yaws web server".lower(),
            89:
                "NAME: Microsoft-Exchange-Server-Static-Key-Flaw/RCE   "
                "   DETAILS: A remote code execution vulnerability exists in Microsoft Exchange software when the"
                " software fails to properly handle objects in memory, aka 'Microsoft Exchange Memory Corruption Vulnerability'.",
            90:
                "NAME: 'BIG-IP'-Traffic-Management-User<15.1.0.3/RCE   "
                "   DETAILS: https://cxsecurity.com/issue/WLB-2020070045",
            91:
                "NAME: SMBleedingGhost/CVE-2020-0796-RCE-POC   "
                "   DETAILS: https://www.bleepingcomputer.com/news/security/48k-windows-hosts-vulnerable-to-smbghost-cve-2020-0796-rce-attacks/",
            92:
                "NAME: Mambo-com_akogallery/Sql-Injection   "
                "   DETAILS: https://www.exploit-db.com/exploits/11446",
            93:
                "NAME: vBulletin<5.5.4-Pre-Authenticated/Remote-Command-Execution   "
                "   DETAILS: https://packetstormsecurity.com/files/155633/vBulletin-5.5.4-Remote-Command-Execution.html",
            94:
                "NAME: ZeroLogon-Microsoft-Netlogon/set-password-to-empty-string   "
                "   DETAILS: https://www.jaacostan.com/2020/10/zerologon-vulnerability-exploitation.html",
            95:
                "NAME: upload-pwn-RCE(POC)   "
                "   DETAILS: attempts 9 different ways to bypass an uploads page to get remote code execution",
            96:
                "NAME: PHP<7.x/Remote-Command-Execution/CVE-2019-11043   "
                "DETAILS: https://blog.qualys.com/product-tech/2019/10/30/php-remote-code-execution-vulnerability-cve-2019-11043",
            97:
                "NAME: upload-pwn-RS(POC)   "
                "   DETAILS: attempts 9 different ways to bypass an uploads page to get a reverse shell on the webserver",
            98:
                "NAME: FPM+PHP-versions<7.3.11/Remote-Code-Execution   "
                "   DETAILS: https://www.tenable.com/plugins/nessus/130276",
            99:
                "NAME: Pre-Authenticated-Discord-Account-Disabler   "
                "   DETAILS: only requires a discord token and then you can remotely disable any account",
            100:
                "NAME: SpamTitan<7.07/Unauthenticated-RCE   "
                "   DETAILS: https://sploitus.com/exploit?id=EDB-ID:48856",
            101:
                "NAME: ProFTPd<1.3.5-mod_copy/Unauth-Remote-Command-Execution   "
                "   DETAILS: https://github.com/t0kx/exploit-CVE-2015-3306 (older exploit, however this is the one i wrote)",
            102:
                "NAME: ProFTPd<1.3.5-mod_copy/Unauth-Remote-File-Upload   "
                "   DETAILS: CVE-2015-3306 re written to remotely upload a file",
            103:
                "NAME: ProFTPd<1.3.5-mod_copy/Unauth-Invoke-Reverse-Shell   "
                "   DETAILS: 2015-3306 re written to invoke a reverse shell",
            104:
                "NAME: Wordpress-Plugin-File-Manager<6.9/Unauthenticated-RCE   "
                "   DETAILS: vulnerable wordpress plugin vulnerable to remote code execution",
            105:
                "NAME: Wordpress-Plugin-File-Manager<6.9/Unauthenticated-AFU   "
                "   DETAILS: vulnerable wordpress plugin vulnerable to arbitrary file upload",
            106:
                "NAME: Seo-Panel<4.6.0/Authenticated-Remote-Code-Execution   "
                "   DETAILS: vulnerability seo panel <4.6.0 authenticated remote code execution",
            107:
                "NAME: upload-pwn-ASP--POC   "
                "   DETAILS: attempts 9 different ways to bypass an uploads page",
            108:
                "NAME: upload-pwn-PERL--POC   "
                "   DETAILS: attempts 9 different ways to bypass an uploads page",
            109:
                "NAME: upload-pwn-PHP--POC   "
                "   DETAILS: attempts 9 different ways to bypass an uploads page",
            112:
                "NAME: Oracle-WebLogic-Server<12.2.1.4/Unauthenticated-RCE   "
                "   DETAILS: https://www.youtube.com/watch?v=W0IWXYXSHqg",
            111: "NAME: rConfig-3.9.5/Remote-Code-Execution-Unauthenticated   "
                 "   DETAILS: remote code execution and remote command execution vulnerability for rconfig 3.9.5",
            114: "NAME: ReQuest Serious Play F3 Media Server <7.0.3 Unauthenticated RCE   "
                 "DETAILS: vendor ReQuest Serious Play LLC ReQuest Serious Play F3 Media Server <7.0.3 "
                 "Unauthenticated Remote Code Execution "
                 """Affected version: 7.0.3.4968 (Pro)
                   7.0.2.4954
                   6.5.2.4954
                   6.4.2.4681
                   6.3.2.4203
                   2.0.1.823""",
            113: "NAME: CloudMe/1.11.2/Chained-RCE   "
                 "   DETAILS: chain a remote buffer overflow into command execution",
            116: "NAME: Pre-Auth-Django-Password-Reset   "
                 "   DETAILS: reset the password of an admin login for a django page"
        }
        exit(f"{Colors.purple}{details[int(choice)]}{Colors.end}")

    def display_test(self, string):
        string = self.router_exploits
        router_exploits = {
            "Sagem-routers/Remote-Auth-bypass": "DETAILS: https://www.exploit-db.com/exploits/11634",
            "D-Link-DSR-Router-Series/Remote-Code-Execution": "DETAILS: https://packetstormsecurity.com/files/135706"
                                                              "/D-Link-DSL-2750B-Remote-Command-Execution.html ",
            "Netgear-ProSafe/Information-Disclosure": "DETAILS: https://www.exploit-db.com/exploits/27774",
            "Netcore/Netis-Routers/UDP-Backdoor-Access": "DETAILS: https://www.exploit-db.com/exploits/43387",
            "BLUE-COM-Router/5360/52018/Password-Reset": "DETAILS: https://www.exploit-db.com/exploits/31088",
            "Seowonintech-Routers/2.3.9/File-Disclosure": "DETAILS: https://www.exploit-database.net/?id=47966",
            "Netgear-WNR2000v5/Remote-Code-Execution": "DETAILS: https://www.exploit-db.com/exploits/40949",
            "Netgear-DGN2200v1/v2/v3/v4-ping.cgi/RCE": "DETAILS: https://seclists.org/fulldisclosure/2017/Feb/50",
            "PLC-Wireless-Router-GPN2.4P21-C-CN/DOS": "DETAILS: remote dos for the PLC-Wireless-Router-GPN2.4P21-C-CN",
            "Virgin-Media-Hub-3.0-Router/DOS": "DETAILS: https://portforward.com/virgin-media/hub-3.0/",
            "ZTE-ZXV10-W300-Router": "DETAILS: https://seclists.org/nmap-dev/2014/q1/152",
            "RT-N56U-Remote-Root": "DETAILS: https://packetstormsecurity.com/files/124855/",
        }
        exit(f"{Colors.purple}{router_exploits[str(string)]}{Colors.end}")


parser = argparse.ArgumentParser()
parser.add_argument("-e", metavar="number".upper(), help="display details for the given exploit (provide the number)")
parser.add_argument("-r", metavar="name".upper(),
                    help="display details for the given router exploit (provide the name)")
parser.add_argument("-a", metavar="name".upper(),
                    help="display details for the given auxiliary module (provide the name)")
parser.add_argument("-p", metavar="name".upper(), help="display details for the given post module (provide the name)")
argument = parser.parse_args()

display_info = MODULES(
    exploits=argument.e,
    auxiliary=argument.a,
    post=argument.p,
    router_exploits=argument.r
)
if __name__ == "__main__":
    if argument.e:
        display_info.display_exploits_details(choice=argument.e)
    elif argument.r:
        display_info.display_test(string=argument.r)
