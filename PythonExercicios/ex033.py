'''numero = int(input('Primeiro Valor: '))
maior = numero
menor = numero
numero = int(input('segundo Valor: '))
if numero > maior:
    maior = numero
if numero < menor:
    menor = numero
numero = int(input('Terceiro Valor: '))
if numero > maior:
    maior = numero
if numero < menor:
    menor = numero
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''

'''a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
c = int(input('Terceiro Valor: '))
if c > maior:
    maior = c
if c < menor:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''

a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))


