from random import randint
maior = menor = cont = 0
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for c in numeros:
  print(c, end=' ')
  if cont == 0:
         maior = menor = c
         cont = 1
  if c > maior:
         maior = c
  elif c < menor:
         menor = c
print('')
print(f'O Maior valor sorteado foi {maior}')
print(f'O Menor valor sorteado foi {menor}')



