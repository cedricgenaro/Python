print('{:=^40}'.format(' LOJAS GUANABARA '))
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão 
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    valorfinal = compras - compras * (10 / 100)
    print('Sua compra de\033[1m R${:.2f}\033[m vai custar \033[1mR${:.2f}\033[m no final.'.format(compras, valorfinal))
elif opcao == 2:
    valorfinal = compras - compras * (5 / 100)
    print('Sua compra de \033[1m R${:.2f}\033[m vai custar \033[1mR${:.2f}\033[m no final.'.format(compras, valorfinal))
elif opcao == 3:
    print('Sua compra será parcelada em 2X de {:.2f} SEM JUROS'.format(compras / 2))
    print('Sua compra de R${0:.2f} vai custar R${0:.2f} no final.'.format(compras))
elif opcao == 4:
    valorfinal = compras + compras * (20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS.'.format(parcelas, valorfinal / parcelas))
    print('Sua compra de R${:.2f} vai custar no final R${:.2f} no final.'.format(compras, valorfinal))
else:
    print('OPÇÃO INVÁLIDA! POR FAVOR DIGITE O NÚMERO DE UMA DAS OPÇÕES ACIMA!')
    print('''
  @@@@@@@@                         @@@@@@ 
,@@      @@(                @@@@@@@@@@& 
 @@      @@@            &@@@@@@@@@      
   @@@@@@@@@         @@@@@@@@@          
           @@@@@ @@@@@@@@@              
              @@@@@@@@                  
           @@@@@ @@@@@@@@@              
  *@@@@@@@@@         @@@@@@@@@          
 @@      @@@            .@@@@@@@@@      
,@@      @@/                .@@@@@@@@@@ 
 @@@@@@@@                           @@@@@@ 
      ''')




