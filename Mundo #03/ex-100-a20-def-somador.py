'''from random import randint
def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(0,10))

def somaPar():
    num = [   [],[]   ]
    for c in range(len(numeros)):
        if numeros[c] % 2 == 0:
            num[0].append(numeros)
            print(f'PARES {num[0]}')
        else:
            num[1].append(numeros)
            print(f'IMPARES {num[1]}')
            
#########n noa dei conta - que vergonha em

numeros = list()
sorteia(numeros)
print(numeros)
somaPar()
'''

#era tao simples
from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f' {n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO')
    

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        print(f'Valor-> {valor} Lista -> {lista}')
    print(f'Somando os valoes pares de {lista}, temos {soma}')

 


numeros = list()
sorteia(numeros)
somaPar(numeros)








'''#100
#Faça um programa que tenha uma lista chamada números() e duas funções chamadas sorteio() e somaPar().
#A primeira função vai sortear 5 números e vai coloca-los dentro da lista
 #e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''