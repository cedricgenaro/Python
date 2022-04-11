jogadores = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for k in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {k+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*35)
print(f'cod ', end='')
for i, v in enumerate(jogadores):
    for k, d in v.items():
        if i == 0:
            print(f'{k:<14}', end='')
print()
print('--'*25)
for i, v in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*25)
while True:
    op = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if op == 999:
        break
    elif op <= (len(jogadores)-1):
        print(f'-- LEVANTAMENTO DO JOGAOR {jogadores[op]["nome"]}')
        for k, v in enumerate(jogadores[op]['gols']):
            print(f'  No jogo {k+1} fez {v} gols.')
    else:
        print(f'ERRO! Não existe jogador com o código {op}!')
    print('--' * 25)
print('<< Volte Sempre >>')


