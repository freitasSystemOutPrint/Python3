lista = []
lis_par = []
lis_impar = []
stp = 0

while True:
    v = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [s/n]'))
    

    lista.append(v)
    if v%2 == 0:
        lis_par.append(v)
    else:
        lis_impar.append(v)
    if r == 'n' or r == 'N':
            break
   
print(f'Valores digitados: {lista}')
print(f'Valores pares digitados: {lis_par}')
print(f'Valores impares digitatos: {lis_impar}')    


'''

a = [2,3,4,7]
b = a #Faz uma ligacao das listas
b = a[:] #Faz uma copia da lista

EX:082
Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, crie duas listas extras que vao conter apenas os valores pares
e impares digitados, respectivamente.

'''
