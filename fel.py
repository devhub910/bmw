import socket
import time
import random
from colorama import Fore, init
from os import system, name
from threading import Thread
import sys
import subprocess
import json
from urllib import parse
import requests

init(autoreset=True)

uilast = ["       [1]ScanPort", "[2]DDoS", "[3]InfoWeb"]
ports = [21, 23, 25, 45, 53, 80, 110, 111, 113, 135, 139, 143, 199, 256, 443, 445, 554, 587, 912, 993, 995, 1720, 1723, 3306, 3389, 5900, 8080, 8888, 10257]
ddos = ["         [1]TCP", "  [2]UDP", "  [3]HTTP","[4]back to home"]
webtrool = ["[1]LOOKUP","[2]IP INFO","[3]HTTP STATUS","[4]FIND HOST"," [5]EXTRACT LINK","[6]back to home"]
class Color:
    LB = Fore.LIGHTBLUE_EX
    LC = Fore.LIGHTCYAN_EX
    LG = Fore.LIGHTGREEN_EX
    LR = Fore.LIGHTRED_EX
    LY = Fore.LIGHTYELLOW_EX
    RESET = Fore.RESET

############defs############

def home():
    system('cls' if name == 'nt' else 'clear')  
    
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⢞⣁⣤⣤⣘⣗⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣜⣽⣿⣿⣿⣿⣿⣿⣧⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠴⠺⢿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡶⠄⡀⠀⠀⠀
⠀⠀⣸⣿⣷⣦⡀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢀⡿⢣⠀⠀
⠀⢸⣿⣿⣿⡻⣷⡀⢸⣿⢿⣿⣿⡿⣿⡏⠀⠀⠀⣾⠁⢠⣇⠀
⠀⣿⣿⣿⣿⣧⢹⣷⢸⣿⠀⢿⡿⠁⣿⡇⠀⠀⢠⢯⢂⣾⡟⡀
⢀⣿⣿⣿⣿⣿⣧⢹⣿⣿⠀⠸⡇⠀⣿⡇⠀⢀⣾⡿⣼⣞⣼⡁
⢸⣿⣿⣿⣿⣿⣿⣇⢻⡟⠀⠀⠀⠀⠛⠁⠀⡼⢸⣿⣽⡿⢿⣇
⣼⣿⣿⣿⣿⢿⣿⣿⣆⣿⠀⠀⠀⠀⠀⠀⣰⡇⢸⢻⣿⣿⣿⣿
⢻⣿⣿⣭⣿⣸⣿⣿⠃⠈⠇⠀⠀⠀⠀⠀⠸⣷⣸⢸⠿⠷⣿⣿

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Tool-Rex Made By TheRex to 911-Team
 Team-911 Attack in Tool Lol !!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
    print(" | ".join(uilast))  
    print()
    sys.stdout.write(Color.LB + "╔═══" + Color.LR + "[" + Color.LG + "Tool-Rex" + Color.LB + "@" + Color.LG + "Home" + Color.LR + "]" + Color.LB + "\n╚══> " + Color.RESET)
    choice = input()
    return choice  # إرجاع قيمة choice

def scanport():
    ip_hackport = input("IP :> ")

    print(f"\nScanning ports")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip_hackport, port))
        
        if result == 0:
            print(Color.LG+"Port {port} is OPEN")
        else:
            print(Color.LR+"Port {port} is CLOSED")
        
        sock.close()

    home()

#########Def2 Tab


def ddospotins():
    system('cls' if name == 'nt' else 'clear')  # تنظيف الشاشة
    print(Color.LG + """ /-----------------------------------------------------// |              DDoS Tool-Rex.                        | |                      By Made TheRex                | |____________________________________________________|

    """)

    print(Color.LR + " | ".join(ddos))
    print()
    
    # طلب المدخلات بعد كل هجوم
    def request_input():
        sys.stdout.write(Color.LB + "╔═══" + Color.LR + "[" + Color.LG + "Tool-Rex" + Color.LB + "@" + Color.LG + "DDoS" + Color.LR + "]" + Color.LB + "\n╚══> " + Color.RESET)
        return input()

    chddos = request_input()
    while chddos not in ["1", "2", "3", "4"]:
        print(Color.LY + f"Not found Number")
        chddos = request_input()
    
    if chddos == "1":
        ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
        port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
        floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
        size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
        thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
        subprocess.run([f'screen -dm python3 utils/L4/tcp {ip} {port} {floodtime} {size} {thread}'], shell=True)
        print(Color.LG+f"\n [!] Attack sent successfully!\n")
        chddos = request_input()  # طلب المدخلات بعد الهجوم

    elif chddos == "2":
        ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
        port = int(input(f"{Color.LG} [>] Port: "+Color.RESET))
        floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
        size = int(input(f"{Color.LG} [>] Size: "+Color.RESET))
        thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
        subprocess.run([f'screen -dm python3 utils/L4/udp {ip} {port} {floodtime} {size} {thread}'], shell=True)
        print(Color.LG+f"\n [!] Attack sent successfully!\n")
        chddos = request_input()  # طلب المدخلات بعد الهجوم

    elif chddos == "3":
        ip = str(input(f"{Color.LG} [>] IP: "+Color.RESET))
        floodtime = int(input(f"{Color.LG} [>] Time: "+Color.RESET))
        thread = int(input(f"{Color.LG} [>] Thread: "+Color.RESET))
        subprocess.run([f'screen -dm python3 utils/L4/http {ip} {floodtime} {thread}'], shell=True)
        print(Color.LG+f"\n [!] Attack sent successfully!\n")
        chddos = request_input()  # طلب المدخلات بعد الهجوم

    elif chddos == "4":
        home()  # العودة إلى الصفحة الرئيسية
####________Def3 Tab       
        
# تعريف الكلاس response_url
class response_url:
    def __init__(self, headers):
        self.headers = headers

    def lookup(self, url):
        try:
            if url == '':
                return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
            resp = requests.get(f"http://ip-api.com/json/{url}?fields=status,message,country,countryCode,regionName,city,timezone,asname,isp,org,reverse,query", headers=self.headers).json()
            if resp['status'] == 'success':
                return Color.LG+"    [+] IP address: " + resp['query'] + "\n" +Color.LG+ "    [+] Host name: " + resp['reverse'] + "\n" +Color.LG+ "    [+] ISP: "+ resp['isp'] + "\n" +Color.LG+ "    [+] Organization: "+ resp['org'] + "\n" +Color.LG+ "    [+] Country: " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['regionName'] + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] ASN: " + resp['asname'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone']
            else:
                return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid URL"
        except requests.exceptions.RequestException:
            return Color.LR+"Error: Check your Internet Connection."
        except KeyError:
            return Color.LR+"Error: Invalid response data."

    def ip_lookup(self, ip):
        try:
            if ip == '':
                return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
            resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,reverse,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=self.headers).json()
            if resp['status'] == 'success':
                return Color.LG+"    [+] Target IP: " + resp['query'] + "\n" +Color.LG+ "    [+] Country: " + resp['continent'] + " " + resp['country'] + " " + "(" + resp['countryCode'] + ")" + "\n" +Color.LG+ "    [+] Region: " + resp['region'] + " " + "(" + resp['regionName'] + ")" + "\n" +Color.LG+ "    [+] City: " + resp['city'] + "\n" +Color.LG+ "    [+] Zipcode: " + resp['zip'] + "\n" +Color.LG+ "    [+] Timezone: " + resp['timezone'] + "\n\n" +Color.LG+ "    [+] ISP: " + resp['isp'] + "\n" +Color.LG+ "    [+] ASN: " + resp['as'] + " " + resp['asname'] + "\n\n" +Color.LG+ "    [+] Mobile: " + str(resp['mobile']) + "\n" +Color.LG+ "    [+] VPN: " + str(resp['proxy'])+ "\n\n" +Color.LG+ "    [+] Google Map: https://www.google.com/maps/place/" + str(resp['lat']) + "," + str(resp['lon'])
            else:
                return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
        except requests.exceptions.RequestException:
            return Color.LR+"Error: Check your Internet Connection."
        except KeyError:
            return Color.LG+"["+Color.LR+"!"+Color.LG+"]"+Color.LR+" Invalid IP Address"
            
            
def webtool():
    system('cls' if name == 'nt' else 'clear')  # تنظيف الشاشة
    print(Color.LG + """
/-----------------------------------------------------//
|              WebTool Tool-Rex.                        |
|                      By Made TheRex                |
|____________________________________________________|

""")
    print(" | ".join(webtrool))  
    print()

    # طلب المدخلات بعد كل خيار
    def request_input():
        sys.stdout.write(Color.LB + "╔═══" + Color.LR + "[" + Color.LG + "Tool-Rex" + Color.LB + "@" + Color.LG + "InfoWeb" + Color.LR + "]" + Color.LB + "\n╚══> " + Color.RESET)
        return input()

    chweb = request_input()
    while chweb not in ["1", "2", "3", "4", "5", "6"]:
        print(Color.LY + f"Not found Number")
        chweb = request_input()

    headers = {}  # تخصيص أو إضافة رؤوس HTTP إذا لزم الأمر
    response = response_url(headers)  # إنشاء كائن من الكلاس response_url

    if chweb == "1":
        while True:
            lookup = input(Color.LR+"["+Color.LG+"LOOKUP"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
            parser = parse.urlparse(lookup)
            host = parser.netloc
            if parser.scheme == 'https' or parser.scheme == 'http':
                host = parser.netloc
            elif parser.scheme == '':
                url = "http://"+parser.path
                parser = parse.urlparse(url)
                host = parser.netloc

            # تحويل الدومين إلى عنوان IP
            try:
                ip_address = socket.gethostbyname(host)
                print(f"Response for {host}: {ip_address}")
                print(response.lookup(host))  # استدعاء دالة lookup
            except socket.gaierror:
                print(f"Could not resolve host {host}.")
            break

        chweb = request_input()  # طلب المدخلات بعد كل عملية

    elif chweb == "2":
        while True:
            ip_lookup = input(Color.LR+"["+Color.LG+"IP INFO"+Color.LR+"]"+Color.LC+" Enter Target IP: "+Color.RESET)
            print(response.ip_lookup(ip_lookup))  # استدعاء دالة ip_lookup
            break

        chweb = request_input()  # طلب المدخلات بعد كل عملية

    elif chweb == "3":
        while True:
            http = input(Color.LR+"["+Color.LG+"HTTPCHECK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
            print(response.lookup(http))  # استدعاء دالة http_status
            break

        chweb = request_input()  # طلب المدخلات بعد كل عملية

    elif chweb == "4":
        while True:
            findhost = input(Color.LR+"["+Color.LG+"FINDHOST"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
            parser = parse.urlparse(findhost)
            host = parser.netloc
            path = parser.path.replace("/", "")
            if parser.scheme == 'https' or parser.scheme == 'http':
                print(response.lookup(host))  # استدعاء دالة findhost
            elif host == '':
                print(response.lookup(path))  # استدعاء دالة findhost
            break

        chweb = request_input()  # طلب المدخلات بعد كل عملية

    elif chweb == "5":
        while True:
            excractlink = input(Color.LR+"["+Color.LG+"EXCRACTLINK"+Color.LR+"]"+Color.LC+" Enter Target URL: "+Color.RESET)
            print(response.lookup(excractlink))  # استدعاء دالة extractlink
            break

        chweb = request_input()  # طلب المدخلات بعد كل عملية

    elif chweb == "6":
        home()

    else:  
        while True:    
            print(Color.LY + f"Not found Number")
            chweb = request_input()
            if chweb in ["1", "2", "3", "4", "5", "6"]:
                break

############The End Defs############

##########__StartHome#######
choice = home()  # الحصول على قيمة choice من دالة home

if choice == "1":
    scanport()
elif choice == "2":
    ddospotins()
elif choice == "3":
    webtool()
else:  
    while True:    
        print(Color.LY + f"Not found Number")
        choice = home()  # إعادة طلب المدخلات إذا كان الاختيار غير صحيح
        if choice in ["1", "2", "3"]:
            break
