maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('Digite o peso em KG da {}ª pessoa: '.format(pessoa)).strip())
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('---'*15)
print('O maior peso digitado foi {}Kg'.format(maior))
print('O menor peso digitado foi {}Kg'.format(menor))
