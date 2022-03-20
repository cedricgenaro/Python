print('-=-'*20)
print('analisador de triângulos'.upper())
print('-=-'*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('O segmentos acima\033[1m PODEM FORMAR\033[m triângulo!')
    if s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2:
        print('O triângulo \033[1m Isósceles \033[m')
    elif s1 == s2 and s1 == s3:
        print('O triângulo \033[1m Equilátero \033[m')
    else:
        print('O triângulo \033[m Escaleno \033[m ')
else:
    print('Os Segmentos acima\033[m NÃO PODEM \033[m formar um Triângulo!')