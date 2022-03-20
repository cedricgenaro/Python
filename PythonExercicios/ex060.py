# numero = int(input('Digite um número para calcular seu Fatorial: '))
# fatorial = 1
# print('Calculando {}! = '.format(numero), end='')
# while numero != 0:
#     fatorial *= numero
#     if numero == 1:
#         print('{} = {}'.format(numero, fatorial))
#     else:
#         print('{} x '.format(numero), end='')
#     numero -= 1
from math import factorial
numero = int(input('Digite um número para calcular o fatorial: '))
c =numero
print('Calculando {}! = '.format(numero), end='')
for c in range(c, 0, -1):
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
f = factorial(numero)
print(f)




