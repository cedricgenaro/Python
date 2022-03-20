sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'fFMm':
    sexo = str(input('Dado inválido! Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso! '.format(sexo))
