# UDAH OPEN SOURCS JANGAN DI RECODE BNGSD !!
# TAU DIRI LAH ANJING !!
# CODE BY : JUNIOR404
# TEAM : CRABS

import sys
from urllib2 import *
from platform import system
import pyfiglet
import requests, json

os.system('clear')
ascii_banner = pyfiglet.figlet_format("Information Gathering")
print(ascii_banner)
print("[\033[91m01\033[0m] Traceroute")
print("[\033[91m02\033[0m] Test Ping")
print("[\033[91m03\033[0m] DNS lookup")
print("[\033[91m04\033[0m] Reverse DNS")
print("[\033[91m05\033[0m] Host Record")
print("[\033[91m06\033[0m] Subdomain Finder")
print("[\033[91m07\033[0m] Find DNS server")
print("[\033[91m08\033[0m] Zone transfer")
print("[\033[91m09\033[0m] Whois Lookup")
print("[\033[91m10\033[0m] Geo IP Lookup")
print("[\033[91m11\033[0m] Reverse IP Lookup")
print("[\033[91m12\033[0m] TCP Port Scan")
print("[\033[91m13\033[0m] Subnet Lookup")
print("[\033[91m14\033[0m] ASN Lookup")
print("[\033[91m15\033[0m] HTTP Header")
print("[\033[91m16\033[0m] Extract Page Link")
print("[\033[91m17\033[0m] Reverse Analytics Search")
print("[\033[91m18\033[0m] IP Scanner")
print("[\033[91m19\033[0m] Web IP Finder")
print("[\033[91m20\033[0m] About")
print("[\033[91m21\033[0m] EXIT")
pilih = raw_input("Junior:~# \033[91m")

if pilih =='01' or pilih == '1':
	junior = raw_input("\033[0mEnter IP or Domain: ")
	trace = "https://api.hackertarget.com/mtr/?q=" + junior
	route = urlopen(trace).read()
	print (route)
	exit()
	
elif pilih =='02' or pilih =='2':
	junior = raw_input("\033[0mEnter IP or Domain: ")
	test = "https://api.hackertarget.com/nping/?q=" + junior
	ping = urlopen(test).read()
	print (ping)
	exit()
	
elif pilih =='03' or pilih =='3':
	junior = raw_input("\033[0mEnter Domain: ")
	dns = "https://api.hackertarget.com/dnslookup/?q=" + junior
	look = urlopen(dns).read()
	print (look)
	exit()

elif pilih =='04' or pilih =='4':
	junior = raw_input("\033[0mEnter Domain/Ip Address/IP Range: ")
	rev = "https://api.hackertarget.com/reversedns/?q=" + junior
	vers = urlopen(rev).read()
	print (vers)
	exit()

elif pilih =='05' or pilih =='5':
	junior = raw_input("\033[0mEnter Domain: ")
	host = "https://api.hackertarget.com/hostsearch/?q=" + junior
	rec = urlopen(host).read()
	print (rec)
	exit()
	
elif pilih =='06' or pilih =='6':
	masukan = raw_input('\033[0mEnter Domain: ')
	result =  requests.get("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=" + masukan)
	j = json.loads(result.text)
	print "hasil subdomain: " + masukan
	for i in j['subdomains']:
		print i
	
elif pilih =='07' or pilih =='7':
	junior = raw_input("\033[0mEnter Server Name: ")
	aaa = "https://api.hackertarget.com/findshareddns/?q=" + junior
	ab = urlopen(aaa).read()
	print (ab)
	exit()
	
elif pilih =='08' or pilih =='8':
	junior = raw_input("\033[0mEnter Domain: ")
	zon = "https://api.hackertarget.com/zonetransfer/?q=" + junior
	tran = urlopen(zon).read()
	print (tran)
	exit()
	
elif pilih =='09' or pilih =='9':
	junior = raw_input("\033[0mEnter Ip/Domain: ")
	wh = "https://api.hackertarget.com/whois/?q=" + junior
	ios = urlopen(wh).read()
	print (ios)
	exit()
	
elif pilih =='10':
	junior = raw_input("\033[0mEnter IP Address: ")
	geo = "https://api.hackertarget.com/geoip/?q=" + junior
	ip = urlopen(geo).read()
	print (ip)
	exit
	
elif pilih =='11':
	junior = raw_input("\033[0mEnter IP Address: ")
	ak = "https://api.hackertarget.com/reverseiplookup/?q=" + junior
	ab = urlopen(ak).read()
	print (ab)
	exit()
	
elif pilih =='12':
	junior = raw_input("\033[0mEnter IP address: ")
	tc = "https://api.hackertarget.com/nmap/?q=" + junior
	prt = urlopen(tc).read()
	print (prt)
	exit()
	
elif pilih =='13':
	junior = raw_input("\033[0mEnter cidr/IP with Netmask: ")
	sub = "https://api.hackertarget.com/subnetcalc/?q=" + junior
	net = urlopen(sub).read()
	print (net)
	exit()
	
elif pilih =='14':
	junior = raw_input("\033[0mEnter IP Address: ")
	asn = "https://api.hackertarget.com/aslookup/?q=" + junior
	lop = urlopen(asn).read()
	print (lop)
	exit()
	
elif pilih =='15':
	junior = raw_input("\033[0mEnter Web Address: ")
	http = "https://api.hackertarget.com/httpheaders/?q=" + junior
	head = urlopen(http).read()
	print (head)
	exit()
	
elif pilih =='16':
	junior = raw_input("\033[0mEnter Web Address: ")
	extr = "https://api.hackertarget.com/pagelinks/?q=" + junior
	page = urlopen(extr).read()
	print (page)
	exit()
	
elif pilih =='17':
	junior = raw_input("\033[0mEnter Domain: ")
	ana = "https://api.hackertarget.com/analyticslookup/?q=" + junior
	lab = urlopen(ana).read()
	print (lab)
	exit()

elif pilih =='18':
	pil = raw_input('\033[0mEnter IP: ')
	result =  requests.get("https://www.threatcrowd.org/searchApi/v2/ip/report/?ip=" + pil)
	j = json.loads(result.text)
	junior = j['resolutions']
	for i in junior:
		print i['domain']

elif pilih =='19':
	masukan = raw_input('\033[0mEnter Domain: ')
	result =  requests.get("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=" + masukan)
	j = json.loads(result.text)
	kld = j['resolutions']
	for i in kld:
		print i['ip_address']

elif pilih =='20':
	print("\033[0m[\033[91m*\033[0m] Tools Name Vulnerability Scanning Tools \n[\033[91m~\033[0m] Create  : Junior404 \n[\033[91m~\033[0m] Youtube : youtube.com/c/GUNAWANID \n[\033[91m+\033[0m] Team    : CRABS")
	exit()
	
elif pilih =='21':
	print("\033[0mByBy.. :')")
	exit()
	
	
	
	
	
	
	