def notas(*n, sit=False):
    """
    → Função para analisar notas e situaçãoes de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação .
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict()
    maior = menor = média = soma = 0
    turma['total'] = len(n)
    for k, v in enumerate(n):
        if k == 0:
            maior = v
            menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        soma += v
    turma['maior'] = maior
    turma['menor'] = menor
    turma['média'] = soma / len(n)
    if sit:
        if turma['média'] > 7:
            turma['situação'] = 'BOA'
        elif 7 >= turma['média'] >= 5:
            turma['situação'] = 'REGULAR'
        else:
            turma['situação'] = 'RUIM'

    return turma


# Programa principal:


# resp = notas(5.5, 9.5, 10, 6.5, 0)
# print(resp)
help(notas)
