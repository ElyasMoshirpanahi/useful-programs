import os
from time import sleep


def change_dns(primary:str="178.22.122.100",secondary=None,clear=False):
	try:
		if clear:
			os.system('netsh interface ip set dnsservers "Ethernet" dhcp')
		else:
			os.system(f'netsh interface ip set dnsservers "Ethernet" static {primary} primary')
			if secondary:
				os.system(f'netsh interface ip add dnsservers "Ethernet" {secondary} index=2')
				sleep(1.5)	
			print("DNS changed successfully")


	except Exception as e:
		raise "Error couldn't change the dns server"

def show_dns():
	os.system('netsh interface ip show dnsservers "Ethernet"')



dns_list = [("1.1.1.1","1.0.0.1",False),("178.22.122.100" , "185.51.200.2",False),("","",True)]

print("Current dns is :")
show_dns()

print("""
Enter your desiered dns:
0.cloudflare
1.shecan
2.none
3.custom""")

dns_type = int(input("Desiered dns type:"))


if dns_type == 3 :
	dns_1 = input("Enter the primary dns: ")
	dns_2 = input("Enter the secondary dns: ")
	change_dns(dns_1,dns_2)
else:
	primary,secondary,clear = dns_list[dns_type]
	change_dns(primary,secondary,clear)