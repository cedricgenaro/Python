jogador = dict()
gols = []
partidas = somagols = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
if partidas != 0:
    for i in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {i+1}: ')))
jogador['gols'] = gols[:]
for i in jogador['gols']:
    somagols += i
jogador['total'] = somagols
print('-='*35)
print(jogador)
print('-='*35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*35)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'   => Na partida {k + 1}, fez {v} gols. ')
print(f'Foi um total {jogador["total"]} gols.')