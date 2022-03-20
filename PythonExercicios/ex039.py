from datetime import date
print('\033[1;32m-+-\033[m'*40)
print('\033[1;33m {:^100}\033[m'.format('EXÉRCITO DO BRASIL'))
print('\033[1;32m-+-\033[m'*40)
anoatual = date.today().year
nascimento = int(input('Ano de Nascimento: ').strip())
sexo = str(input('Qual o seu sexo? M / F: ').strip())
if sexo == 'm'.lower():
    idade = anoatual - nascimento
    anoalistamento = nascimento + 18
    print('\033[1;32m---\033[m'*40)
    print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoatual))

    if idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(anoalistamento - anoatual))
        print('Seu alistamento será em {}.'.format(anoalistamento))
    elif anoatual == anoalistamento:
        print('Você deve se alistar \033[1m IMEDIATAMENTE!\033[m')
    else:
        print('Você já deveria ter se ALISTADO!')
        print('Seu ano de Alistamento foi em {}'.format(anoalistamento))
else:
    print('Mulheres não tem o Alistamento Militar obrigatório')
