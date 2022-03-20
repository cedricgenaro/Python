# registro = []
# banco = []
# pesadas = []
# leves = []
#
# maiorpeso = menorpeso = cont = 0
# while True:
#     registro.append(str(input('Nome: ')))
#     registro.append(float(input('Peso: ')))
#     resp = str(input('Quer continuar? [S/N] '))[0]
#     banco.append(registro[:])
#     registro.clear()
#     if resp in 'nN':
#         break
# for reg in banco:
#     if cont == 0:
#         maiorpeso = reg[1]
#         menorpeso = reg[1]
#     else:
#         if reg[1] > maiorpeso:
#             maiorpeso = reg[1]
#
#         elif reg[1] < menorpeso:
#             menorpeso = reg[1]
#     cont += 1
# for reg in banco:
#     if reg[1] == maiorpeso:
#         pesadas.append(reg[0])
#     elif reg[1] == menorpeso:
#         leves.append(reg[0])
#
# print('-='*30)
# print(f'Ao todo você cadastrou {len(banco)} pessoas')
# print(f'O Maior peso foi de {maiorpeso}Kg. Peso de {pesadas}')
# print(f'O Menor peso foi de {menorpeso}Kg. Peso de {leves}')
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')



