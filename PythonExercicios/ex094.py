dados = dict()
registro = list()
mulheres = list()
mediaidade = 0

while True:
    dados['nome'] = str(input('Nome: ')).upper().strip()
    while True:
        dados['sexo'] = str(input('Sexo: '))[0].upper()
        if dados['sexo'] in 'FM':
            break
        print('ERRO! Responda apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    registro.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp not in 'sSnN':
            print('ERRO! Responda apenas S ou N')
        else:
            break
    if resp in 'nN':
        break
totalpessoas = len(registro)
print('-='*35)
print(f'A) Ao todo temos {len(registro)} pessoas cadastradas.')
for k, v in enumerate(registro):
    mediaidade += v['idade']
    if v['sexo'] == 'F':
        mulheres.append(v['nome'])

mediaidade = mediaidade / totalpessoas
print(f'B) A média de idade é de {mediaidade:.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for v in mulheres:
    print(f' {v}', end='')
print()
print('D) Lista das pessoas que estão acima da média:')
for r in registro:
    if r['idade'] > mediaidade:
        print(f'  nome= {r["nome"]}; sexo= {r["sexo"]}; idade= {r["idade"]} ')


