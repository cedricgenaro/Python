# PROGRAMA CALCULA AUMENTO
print('\033[1;34m-=-\033[m' * 50)
print('{}{:^140}{}'.format('\033[1;97;44m', 'CALCULANDO AUMENTO SALARIAL', '\033[m'))
print('\033[1;34m-=-\033[m' * 50)
salário = float(input('QUAL O VALOR DO SEU SALÁRIO ATUAL? R$').strip())
# aumento = salário + (salário * (10/100)) if salário > 1250 else salário + (salário * (15/100))
if salário <= 1250:
    aumento = salário + (salário * (15/100))
else:
    aumento = salário + (salário * (10 / 100))
print('Quem ganhava R${:.2f} passa a ganhar \033[1;97;44mR${:.2f}\033[m agora.'.format(salário, aumento))
