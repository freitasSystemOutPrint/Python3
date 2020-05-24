menor = maior = 0
n = int()
while n != 777:
       for c in range(0, 10000):
              n = int(input('Digite os valores: '))
              m = n + m / c
              if n == 1:
                     maior = n
                     menor = n
              else:
                     if n > maior:
                            maior = n
                     if n < menor:
                            menor = n


print('media entre nums {}'.format(m))
print('maior num {}'.format(maior))
print('menor peso {}'.fotmat(menor))

'''
065
Crie um programa que leia vãrios nũmeros inteiros pelo teclado,
no final da execução, mostre a média enre todos os valores e qual
foi o maior e menor valores lidos.O programa deve perguntar ao usuário
se ele quer ou não voltar a digitar valores.




maior = 0
menor = 0
for p in range(1, 3):
       peso  = float(input('Digite o peso da {} pessoa'.format(p)))
       print(p)
       if p == 1:
              maior = peso
              menor = peso
       else:
              if peso > maior:
                     maior = peso
              if peso < menor:
                     menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))

'''



                     
