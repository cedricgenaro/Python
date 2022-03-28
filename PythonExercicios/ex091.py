# from random import randint
# from time import sleep
# r = 1
# jogadores = dict()
# jogadores['jogador1'] = randint(1, 6)
# jogadores['jogador2'] = randint(1, 6)
# jogadores['jogador3'] = randint(1, 6)
# jogadores['jogador4'] = randint(1, 6)
# print('Valores sorteados:')
# sleep(1.5)
# for k, v in jogadores.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1.5)
# print('-='*50)
# print('== RANKING DOS JOGADORES ==')
# for i in sorted(jogadores, key = jogadores.get, reverse=True ):
#     print(f'{r}º lugar: {i} com {jogadores[i]} ')
#     sleep(0.9)
#     r+=1
from operator import itemgetter
alunos = {'aluno1': 8, 'aluno2': 9.5, 'aluno3': 7.5}
ranking = list()
ranking = sorted(alunos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º {v[0]} com nota {v[1]}')

