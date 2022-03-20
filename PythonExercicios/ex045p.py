from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura'''.upper())
jogador = int(input('Qual a sua jogada? '))
print('-='*15)
print('O Jogador escolheu {}'.format(item[jogador].upper()))
print('O computador escolheu {}'.format(item[computador].upper()))
print('-='*15)
if computador == 0: #Computador Escolheu Pedra
    if jogador == 0:
        print('Deu EMPATE!')
    elif jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('O Computador VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador Escolheu Papel
    if jogador == 0:
        print('O Computador VENCEU!')
    elif jogador == 1:
        print('DEU EMPATE!')
    elif jogador == 2:
        print('O Jogador VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador escolheu Tesoura
    if jogador == 0:
        print('O Jogador VENCEU!')
    elif jogador == 1:
        print('O computador VENCEU!')
    elif jogador == 2:
        print('DEU EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')