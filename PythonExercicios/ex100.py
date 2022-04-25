from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for v in range(0, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += numero
    print(f'Somando os valores pares de {numeros}, temos {pares}')


#Programa Principal
sorteia(numeros)
somapares(numeros)





