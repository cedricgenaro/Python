from time import sleep
from colorama import Fore, Back, init, Style
import os
init(convert=True, autoreset=True)


def linha():
    print(f'{Back.BLUE}-='*35)


def maior(*num):
    linha()
    maior = 0
    sleep(0.6)
    print('Analisando os valores passados...')
    for n in num:
        if n > maior:
            maior = n
        sleep(0.5)
        print(Style.BRIGHT + Fore.CYAN + f'{n} ', end='')
    sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {Fore.LIGHTGREEN_EX} {maior}.')


#PROGRAMA PRINCIPAL
print(Fore.YELLOW + Style.BRIGHT + 'Este Texto está amarelo')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
#os.system("cls")
maior()
