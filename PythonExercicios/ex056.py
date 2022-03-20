media = 0
mjovem = 0
hvelho = 0
for cont in range(1, 5):
    print('{:-^30}'.format(' {}ª PESSOA '.format(cont)))
    nome = str(input('Nome: ').upper().strip())
    idade = int(input('Idade: ').strip())
    sexo = str(input('Sexo [M/F]: ').upper().strip())
    media += idade
    if cont == 1 and sexo == 'M':
        hvelho = idade
        nomehv = nome
    else:
        if sexo == 'M' and idade > hvelho:
            hvelho = idade
            nomehv = nome
        elif idade < 20:
             mjovem += 1
print('A média de idade do grupo é de {:.1f}'.format(media / 4))
print('O homem mais velho tem {} anos e se chma {}'.format(hvelho, nomehv))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mjovem))

