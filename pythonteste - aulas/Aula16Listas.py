#num = (2, 5, 9, 1)
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2,9) #Insere o numero 9 na posicao 2
print(num)
num.pop() #Remove o utimo numero
num.pop(2) #Remove o 2 elemento
num.remove(2) #Remove o valor 2

if 4 in num:
     num.remove(4)
else:
    print('Não achei o numero 4')     

num.sort(reverse=True)
print(num)

#print(f'Essa lista tem {len(num)} elementos. ')


valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor')))


#valores.append(5)
#valores.append(9)
#valores.append(4)

for c, v in enumerate(valores):
     print('Na posicao' ,c, 'encontrei o valor', v)
print('Cheguei ao final da lista')


a = [2,3,4,7]
b = a #Faz uma ligacao das listas
b = a[:] #Faz uma copia da lista



 # ''Tupla->() Lista->[]''
