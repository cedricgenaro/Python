from unidecode import unidecode
frase = str(input('Digite uma frase: ').strip()).split()
fraseinv =''
frase = unidecode(''.join(frase))
for let in range(len(frase)-1, -1, -1):
    fraseinv += frase[let]
print('O Inverso de {} é {}'.format(frase.upper(), fraseinv.upper()))
if frase.upper() == fraseinv.upper():
    print('Temos um palíndromo!')
else:
    print('Não Temos um palíndromo')




