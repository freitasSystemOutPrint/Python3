N = ' '
#cont = menor = caros = baratos = t = 0
cont = 0
menor = 0
caros = 0
baratos = 0
t = 0
while True:
       n = str(input('Nome produto > '))
       p = int(input('Preço > '))
       d =str(input('Deseja continuar ? [s/n]')).upper()
       cont +=1
       #if d == N:
             # break
       t = t + p
       if p > 1000:
              caros += 1
       if  cont == 1 or p < menor:
              menor = p
              baratos = n
       #else:
         #     if p < menor:
           #          menor = p
       if d == 'N':
              break
print('Total da compra R${}'.format(t))
print('Produtos que custam mais de R$1000 = {}'.format(caros))
print('{} foi o  Produto mais barato custando {}'.format(baratos, menor))



"""070
Crie um programa que leia o nome e o preço de vários produtod. O programa deverá perguntar se o usuário vao continiar. No final, mostre:
			A) Qual é o total gasto na compra.
			B) Quantos produtos custam mais de R$1000.
			C) Qual é o nome do produto mais barato.
"""
