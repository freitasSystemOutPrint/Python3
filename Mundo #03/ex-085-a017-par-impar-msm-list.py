num = [   [], []       ]

for c in range(1, 8):
    valor = int(input(f'Digite um {c}º: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-' *30)
num[0].sort()
num[1].sort()
print(f'Todos os valors: {num}')
print(f'Os valores pares foram {num[0]}')
print()
print(f'OS valores impares foram {num[1]}')

galera = [['João',19],   ['Ana', 33],   ['Joaquim', 13], ['Maria', 45] ]
print(galera[2][1])








'''galera = []
valores = []
for c in range(0,8):
    valores.append(int(input('Digite um numero:  ')))
    galera.append(valores[:])
for c in galera:
    
        print('par')
    

'''


'''ex:085
Crie um programa onde o usuario
possa digitar sete valores numericos e cadastre-os em um lista unica
que mantenha separados os valores pares i impares. No final
mostre os valores pares e impares em ordem crescente.'''
