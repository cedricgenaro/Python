# ced50 = ced20 = ced10 = ced1 = contador = 0
# print('='*38)
# print(f'{"BANCO CEV":^35}')
# print('='*38)
# valor = int(input('Qual o valor que você quer sacar? R$'))
# contador = valor
# while True:
#     contador -= 50
#     if contador < 0:
#         if ced50 >= 1:
#             print(f'Total de {ced50} cédulas de R$50.00')
#         break
#     ced50 += 1
# contador = valor - (ced50 * 50)
# while True:
#     contador -= 20
#     if contador < 0:
#         if ced20 >= 1:
#             print(f'Total de {ced20} cédulas de R$20.00')
#         break
#     ced20 += 1
# contador = valor - (ced50 * 50) - (ced20 * 20)
# while True:
#     contador -= 10
#     if contador < 0:
#         if ced10 >= 1:
#             print(f'Total de {ced10} cédulas de R$10.00')
#         break
#     ced10 += 1
# contador = valor - (ced50 * 50) - (ced20 * 20) - (ced10 * 10)
# while True:
#     contador -= 1
#     if contador < 0:
#         if ced1 >= 1:
#             print(f'Total de {ced1} cédulas de R$1.00')
#         break
#     ced1 += 1
# print('='*38)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
print('='*38)
print(f'{"BANCO CEV":^35}')
print('='*38)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
totced = 0
céd = 50
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced > 0:
           print(f'O total de {totced} cédulas de R${céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
              céd = 1
        totced = 0
        if total == 0:
            break
print('='*38)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')




