def voto (anonasc):
    """
    Função que retorna se uma pessoa vota ou não.
    :param anonasc: O ano de nascimento
    :return: Retorna se uma pessoa vota ou não
    """
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anonasc
    if 18 <= idade <= 70:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 16 or idade > 70:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: NÃO VOTA.')

# Programa Principal


ano = int(input('Em que ano você nasceu? '))
voto(ano)



