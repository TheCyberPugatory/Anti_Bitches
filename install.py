#!/usr/bin/python3
import os
os.system("clear")
print("[@] Installing The Tools That May Take A While..")
print("""
[@] We Will Install 
1-Nmap
2-SQLMap
3-Sublist3r
4-EYEWitnese
5-Metasploit
6-SEToolkit
7-Wfuzz
8-Wifite
9-Sherlock
10-PhoneInfoga
""")
os.system("pkg install git curl perl ruby wget -y")
os.system("sudo apt install git curl perl ruby wget -y")
os.system("sudo apt install nmap -y") and os.system("pkg install nmap -y")
os.system("git clone https://github.com/aboul3la/Sublist3r.git")
os.system("https://github.com/trustedsec/social-engineer-toolkit.git setoolkit/")
os.system("git clone https://github.com/sherlock-project/sherlock.git")
os.system("git clone https://github.com/FortyNorthSecurity/EyeWitness.git")
os.system("git clone https://github.com/xmendez/wfuzz.git")
os.system("git clone  https://github.com/derv82/wifite2.git")
os.system("gti clone https://github.com/sundowndev/PhoneInfoga.git")
os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \  chmod 755 msfinstall")
