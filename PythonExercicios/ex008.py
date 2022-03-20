print('\n {:=^100}'.format('Convertendo'))
mt = float(input('\n Digite o valor de metros a ser convertido: '))
cm = mt * 100
mm = mt * 1000
km = mt / 1000
hm = mt / 100
dam = mt / 10
dm = mt * 10

print('-'*50)
print('A medida de {}m corresponde a \n {:.3f}km \n {:.2f}hm \n {:.1f}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm '.format(mt, km, hm, dam, dm, cm, mm))
