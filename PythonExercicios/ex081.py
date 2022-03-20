lnum = list()
while True:
    lnum.append(int(input('Digite um valor: ')))
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continura? [S/N] ')).lower()[0]
        if op not in 'sn':
            print('Opção inválida! Tente novamente.. ', end='')

    if op == 'n':
        break
print('-='*35)
lnum.sort(reverse=True)
print(f'Você digitou {len(lnum)} elementos')
print(f'Os valores em ordem decrescente são {lnum}')
print('O valor 5 faz parte da lista! ' if 5 in lnum else 'O valor 5 não faz parte da lista')

