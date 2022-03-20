from random import randint
comp = randint(0, 10)
tentativas = 0
palpite = -1
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while palpite != comp:
    palpite = int(input('Qual é o seu palpite? ').strip())
    if palpite > comp:
        print('Menos...Tente mais uma vez.')
    elif palpite < comp:
        print('Mais...Tente mais uma vez.')
    tentativas += 1
print('Acertou com {} tentativas. Parabèns!'.format(tentativas))

