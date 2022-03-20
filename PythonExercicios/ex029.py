print('-=-'*30)
print('RADAR ELETRONICO')
print('-=-'*30)
vc = int(input('Qual é a velocidade atual do carro? '))
print('-'*90)
if vc > 80:
    multa = (vc - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

