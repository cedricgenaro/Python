from random import randint
from time import sleep
print('-=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)
comp = randint(0, 5)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('VOCÊ PERDEU! Eu pensei no {}'.format(comp))


