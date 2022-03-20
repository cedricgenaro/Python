soma = 0
contador = 0
for cont in range(0, 6):
    numero = int(input('Digite o {}º número: '.format(cont+1)).strip())
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('O resultado da soma dos {} números pares é {}'.format(contador, soma))
