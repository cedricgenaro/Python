soma = 0
cont = 0
for imp in range(3, 500, 2):
    if imp % 3 == 0:
        soma += imp
        cont += 1

print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

