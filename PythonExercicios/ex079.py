listnum = []
valor = 0

while True:
    valor = int(input('Digite um valor: '))
    if listnum.count(valor) == 0:
        listnum.append(valor)

        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] ').lower().strip())[0]
        if op not in 'sn':
            print('Opção inválida tente novamente..', end='')
    if op == 'n':
        listnum.sort()
        break
print('-='*40)
print(f'Você digitou os valores {listnum}')



