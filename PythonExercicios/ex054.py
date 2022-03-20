import datetime
from datetime import date
maioridade = 0
naomaiores = 0
idade = 0
anoatual = date.today().year
for pessoa in range(1, 8):
    anonasc = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = anoatual - anonasc
    if idade >= 18:
        maioridade += 1
    else:
        naomaiores += 1
print('Dessas 7 pessoas {} ainda não atingiram a maioridade'.format(naomaiores))
print('{} atingiram a maioridade'.format(maioridade))
