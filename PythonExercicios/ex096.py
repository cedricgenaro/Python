def área(l, c):
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}m².')


print(' CONTROLE DE TERRENOS ')
print('-----------------------')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)
