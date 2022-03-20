viagem = float(input('Qual é a distância da sua viagem? '))
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(viagem))
print('E o preço da sua passagem será de R${:.2f}'.format(valor))

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distância))
'''if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45'''
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

