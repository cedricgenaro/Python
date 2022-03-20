from time import sleep
from random import choice
print('{:=^50}'.format('JOKENPO'))
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
opção = int(input('Qual é a sua jogada? '))
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if opção < 0 or opção > 2:
    print('[Erro!] Opção inválida tente Novamente!')
else:
    if opção == 0:
        jogador = 'PEDRA'
    elif opção == 1:
        jogador = 'PAPEL'
    else:
        jogador = 'TESOURA'
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('-=-'*10)
    print('Computador jogou {}'.format(computador))
    print('Jogador jogou {}'.format(jogador))
    print('-=-'*10)
    if jogador == computador:
        print('DEU EMPATE!')
    elif jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador == 'TESOURA' and computador == 'PAPEL':
        print('JOGADOR VENCE!')
    else:
        print('COMPUTADOR VENCEU!')


