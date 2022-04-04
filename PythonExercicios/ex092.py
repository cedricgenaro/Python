from datetime import datetime
funcionario = dict()
carteira = 0
anoAtual = datetime.now().year
funcionario['nome'] = str(input('Nome: ')).strip()
funcionario['idade'] = anoAtual - int(input('Ano de Nascimento: '))
carteira = int(input('Carteira de Tarbalho (0 não tem): '))
if carteira != 0:
    funcionario['ctps'] = carteira
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['salário'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + ((funcionario['contratação'] + 35) - datetime.now().year)
print('-='*35)
for i, v in funcionario.items():
    print(f'- {i} tem o valor {v}')



