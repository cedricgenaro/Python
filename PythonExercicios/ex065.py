# soma = maior = menor = núm = cont = med = 0
# continua = ' '
# while continua not in 'Nn':
#     núm = int(input('Digite um número: '))
#     continua = str(input('Quer continuar? [S/N]: ').strip())
#     if núm >= maior:
#         maior = núm
#     else:
#         menor = núm
#     cont += 1
#     soma += núm
# med = soma / cont
# print('Você digitou {} números e a média foi {}'.format(cont, med))
# print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
num = soma = cont = med = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
med = soma / cont
print('Você digitou ao todo {} números e a média entre eles é {}'.format(cont, med))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
