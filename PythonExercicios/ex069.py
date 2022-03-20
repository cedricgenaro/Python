homens = mulhermenor = mais18 = 0
sexo = continua = ''
while True:
    print('---'*10)
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('---'*10)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Dado inválido! Tente novamente. Sexo: ')).strip().upper()[0]
    print('---' * 10)
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulhermenor += 1
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continua not in 'SN':
        continua = str(input('Dado inválido! Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.' if homens > 1 else f'Ao todo temos {homens} homen cadastrado')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos' if mulhermenor > 1 else f'E temos {mulhermenor} mulher com menos de 20 anos')





