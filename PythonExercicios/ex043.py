from math import pow
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / pow(altura, 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[1m ATENÇÃO\033[m, você está na faixa de ABAIXO DO PESO!')
elif imc < 25:
    print('\033[1m PARABÉNS!\033[m, você está na faixa de PESO IDEAL!')
elif imc < 30:
    print('\033[1m ATENÇÃO!\033[m, você está na faixa de SOBREPESO!')
elif imc <= 40:
    print('\033[1m CUIDADO!\033[m, você está na faixa de OBESIDADE!')
else:
    print('\033[1m MUITO CUIDADO!\033[m, você está na faixa de OBESIDADE MÓRBIDA!')



