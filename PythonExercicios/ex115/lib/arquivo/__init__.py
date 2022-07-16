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
        for linha in file:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f'{dados[0]:<30}{dados[1]:>3} anos')
    finally:
        file.close()


def cadastrar(arquivo, nom='desconhecido', id=0):
    try:
       a = open('bancodados/'+arquivo, 'at', encoding='utf-8')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nom};{id}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nom} adicionado.')
        finally:
            a.close()





