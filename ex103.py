def ficha(nj='<desconhecido>', g=0):
    """
    → Função que mostra a ficha de um jogador
    :param nj: [Informar o nome do jogador]
    :param g: [O número de gols]
    :return: A ficha com as informações
    """
    return f'O jogador {nj} fez {g} gol(s)'


# Programa principal


print('-' * 15)
nomeJogador = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
  gols = 0
if nomeJogador.strip() == '':
    print(ficha(g=gols))
else:
    print(ficha(nomeJogador, gols))



