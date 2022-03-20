from random import randint
from time import sleep
import enumerator as enumerator
numeros = []
numero = 0
quant = 0
jogos = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3)
for c in range(0, quant):
    while True:
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
        if len(numeros) == 6:
            numeros.sort()
            break
    jogos.append(numeros[:])
    numeros.clear()
for i, j in enumerate(jogos):
    sleep(1.5)
    print(f'Jogo {i+1}', f':{j}')
print(f'{"BOA SORTE":-^30}')


