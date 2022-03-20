from datetime import date

nascimento = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação:\033[1m MIRIN \033[m')
elif idade <= 14:
    print('Classificação:\033[1m INFANTIL \033[m')
elif idade <= 19:
    print('Classificação:\033[1m JÚNIOR \033[m')
elif idade <= 25:
    print('Classificação:\033[1m SÊNIOR \033[m')
else:
    print('Classificação: \033[1m MASTER \033[m')
