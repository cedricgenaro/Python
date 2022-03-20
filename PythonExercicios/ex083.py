expressao = str(input('Digite a expressão: ')).strip()
pilha = []
for parenteses in expressao:
    # Aqui o laço for irá percorrer A EXPRESSÃO AO ENCONTAR "( " ELE ADICIONA A LISTA PILHA QUANDO ENCONTRA ")"
    # Ele remove  o "(" que abre a expressão.
    if parenteses == '(':
        pilha.append(parenteses)
    else:
        if len(pilha) > 0:
            if parenteses == ')':
                pilha.pop()
# Aqui no if ele verifica o tamanho da lista pilha se caso for maior que 0 a expressão é inválida pois faltou fechar
# algum parenteses.
if len(pilha) > 0:
    print('Sua expressão não é válida!')
else:
    print('Sua expressão é válida!')
    
