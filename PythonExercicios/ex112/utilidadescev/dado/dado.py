def leiaDinheiro(msg=''):
    """

    :param msg: Mensagem para solicitar o dado do usuario
    :return: Retorna o numero digitado.
    """
    while True:
        dado = input(str(msg)).strip().replace(',', '.')
        if dado.isalpha() or dado.strip() == '' or not dado.replace('.', '').isnumeric():
            print(f'\033[31m ERRO: "{dado}" é um preço inválido!\033[m')
        else:
            break

    return float(dado)
