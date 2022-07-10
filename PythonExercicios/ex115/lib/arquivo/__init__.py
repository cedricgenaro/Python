from PythonExercicios.ex115.lib.interface import cabeçalho


def arquivoExiste(nome):
    try:
        with open('bancodados/'+nome, 'rt') as a:
            a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        with open('bancodados/'+nome, 'wt+') as a:
            a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        file = open('bancodados/'+nome, 'rt', encoding='utf-8')

    except:
        print('Houve um erro na leitura do arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(file.read())

