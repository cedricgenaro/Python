valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um número: ')))
    if valores[len(valores)-1] % 2 == 0:
        par.append(valores[len(valores)-1])
    else:
        impar.append(valores[len(valores)-1])
    op = ' '
    while op not in 'sn':
        op = str(input('Quer continuar? [S/N] '))
        if op not in 'sn':
            print('Opção inválida! Tente novamente.. ', end='')
    if 'n' in op:
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

