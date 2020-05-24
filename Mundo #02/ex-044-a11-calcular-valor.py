n = float(input('Digite o valor do produto: ' ))



print('digite 1 para > À vista dinheiro/cheque 10 % de desconto: ')
print()
print('digite 2 para > À vista no cartão - 5 % de desconto : '        )
print()
print('digite 3 para >  Em até 2x nos cartão Preço normal : '         )
print()
print('digite 4 para > 3x ou mais no cartão - 20% de juros: ')
print()


forma = int(input('Qual a forma de pagamento? (1) (2) (3) ou (4) :'    ))

#opção 1
calc1 = (n * 10) / 100
op1 = n - calc1


#opção 2
calc2 = (n * 5) / 100
op2 = n - calc2

#opção 3
calc3 = n
op3 = calc3

#opção 4
calc4 = (n * 20) / 100
op4 = n + calc4




#>>>
if forma == 1:
       print('valor final do produto {}'.format(op1))
elif forma == 2:
       print('valor final do produto {}'.format(op2))
elif forma == 3:
       print('valor final do produto {}'.format(op3))
elif forma ==4:
       print('valor final do produto {}'.format(op4))
else:
       print('ERRO ! >Tente novamente digitando apenas 1,2,3 ou 4 ')
input('pressione a tecla ENTER para sair: ')





'''> À vista dinheiro/cheque:
- 10 % de desconto

> À vista no cartão:
- 5 % de desconto

> Em até 2x nos cartão:
- Preço normal

> 3x ou mais no cartão:
- 20% de juros'''
