from random import randint
from time import sleep
lista = list()
jogos = list()
print('ACUMULOU 1.300,000,00')
print('-=' *30)
quant = int(input('Quantos jogos quer sortear? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista: # se o num nao estiver la lista entao adicione
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-' *3, f'SORTEANDO {quant} jogos ',  '=-' *3 )
for i, l in enumerate(jogos):
    print(f' jogo {i+1}: {l}')
    sleep(1)
print('=-' *5, '< BOA SORTE!  >',  '=-' *5 )



'''sorteio = [   ]
tot = 2

from random import randint
for c in range(0,6):
    sorteio.append((randint(1,60)))
print(sorteio)

'''
#Do Stack
'''from random import randint
print(randint(0,9))
from random import *
random.seed() #inicia a semente dos número pseudo randômicos
random.randrange(0, 9, 2) # pares entre 0 e 9
random.choice('abcdefghij') # seleciona um dos elementos aleatoriamente
items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) # embaralha os itens aleatoriamente


'''

'''
ex:087 
Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos jogos serao
gerados e vai sortear 6 mumros entre 1 e 60 para
cada jogo, cadastrando em uma lista composta.

'''
