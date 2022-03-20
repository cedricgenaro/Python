print('{:=^50}'.format(' Conversor Temperatura °C para °F '))
tempC = float(input('\n Qual a temperatura em °C? '))
tempF = ((tempC * 9)/5) + 32
print('-'*50)
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(tempC, tempF))
