print('-----------------MENU-----------------')
print('                         \n[1]somar  \n[2]multiplicar \n[3]maior \n[3]maior \n[4]novos números \n[5]sair do programa')		
op = int()
while op!=5:
       n1 = int(input('Digte o 1a valor: '))
       n2 = int(input('Ditgite o 2a valor: '))
       op = int(input('Digite a operaçao desejada: [1] [2] [3] [4] [5] :'))

       if op == 1:
              s = n1 + n2
              print('Total da soma = {}'.format(s))
       elif op == 2:
              s = n1 * n2
              print('Total da multiplicaçao = {}'.format(s))
       elif op == 3:
              if n1 > n2:
                     print('{} e maior  que {} '.format(n1, n2))
              elif n2 > n1:
                     print('{} e maior que {}'.format(n2, n1))
              elif n1 == n2:
                     print('Valores iguais ')
       elif op ==4:
              print('Digite novos numeros ')
       elif op == 5:
              print('ate  mais......')
#print('Valor da operaçao  = {}'.format(s))
                     
       
'''
059
Crie um programa que leia 2 valores e mostre um menu na tela:
		[1]somar
		[2]multiplicar
		[3]maior
		[4]novos números
		[5]sair do programa
		seu programa deverá realizar a operação solicitada em cada    caso.
'''
