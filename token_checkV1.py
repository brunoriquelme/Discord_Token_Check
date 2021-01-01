#do not copy the code
#creating by: JS
from os import system
import platform as x0x00
from time import sleep
import requests as x0x01
system('clear')
while True:
    x0x09 = ("""\n\033[1;32m \U0001F525𝐂𝐡𝐞𝐜𝐤 𝐓𝐨𝐤𝐞𝐧𝐕𝟏\U0001F525 \033[1;31m\033[1;0m\n \033[1;31mC\033[1;32mR\033[1;33mE\033[1;34mA\033[1;35mD\033[1;36mO \033[1;31mP\033[1;32mO\033[1;33mR\033[1;34m: \033[1;35mJ\033[1;36mS""")
    print(x0x09)
    x0x05 = input('\033[1;33m token para check: \033[1;0m')
    headers = {'Content-Type': 'application/json', 'authorization': x0x05}
    x0x09 = x0x01.get('https://discordapp.com/api/v6/users/@me/library', headers=headers)
    x0x02 = (x0x09.status_code)
    if x0x02 == 200:       
        print('\033[1;32m token valida!\n de enter para continuar.\033[1;0m')
        sleep(0.6)
    elif x0x02 == 401:
        print('\033[1;31m token invalida\n de enter para continuar.\033[1;0m')
        sleep(0.6)
    elif x0x02 == 429:
        print(""" \033[1;31m[\033[1;33m!\033[1;31m] \033[1;36m você fez muitos checks, para continuar use uma VPN!\033[1;0m""")

    x0x03 = input('')
    if x0x03 == '':
        x0x04 = x0x00.system()
        if x0x04 == 'Windows':
            system('cls')
        else:
            system('clear')
    else:
        x0x04 = x0x00.system()
        if x0x04 == 'Windows':
            system('cls')
        else:
            system('clear')
    
