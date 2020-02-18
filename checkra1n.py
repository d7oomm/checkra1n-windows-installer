#!/usr/bin/env python

import os
import time



print("""

░░▄███▄███▄
░░█████████
░░▒▀█████▀░
░░▒░░▀█▀
░░▒░░█░
░░▒░█
░░░█
░░█░░░░███████
░██░░░██▓▓███▓██▒
██░░░█▓▓▓▓▓▓▓█▓████
██░░██▓▓▓(◐)▓█▓█▓█
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█     This Tool Coded By Pawa Al-kurdi iG:@342_
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█
░▒░░▒░░██▓██░░░██▓▓██
████████████████████████
█▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█
██─██▀█─██─██─█─███─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

""")
start = input("If You First Time To Use You Need Some Tool To Install\n (Y) For Install Tool (N) For Not Install Tools:")
if start == 'Y' or 'y':
    os.system("sudo apt-get install python3")
    time.sleep(2)
    os.system("""echo "deb https://assets.checkra.in/debian /" | sudo tee -a /etc/apt/sources.list""")
    time.sleep(2)
    os.system("sudo apt-key adv --fetch-keys https://assets.checkra.in/debian/archive.key")
    time.sleep(2)
    os.system("sudo apt update")
    os.system("chmod +x checkra1n")
    print("Thanks For Using This Tool I Hope Enjoy Ur Jailbreal <3")
    os.system("./checkrain")
elif start == 'N' or 'n':
    os.system("./checkra1n")