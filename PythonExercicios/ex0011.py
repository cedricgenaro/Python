#Área = comprimento x altura
print('\n{:=^50}'.format('Calculo de Tinta '))
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
tinta = area / 2
print('-'*50)
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m² '.format(larg, alt, area))
print('-'*50)
print('Será necessário {:.4f}l de tinta para pinta-lá'.format(tinta))





