def soma(a, b):
     s = a + b
     print(s)

soma(5, 5)


#EMPACOTADO
def contador(*num):
    print(num)


contador(2,3,5)

#DOBRAR VALOR DA LISTA
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos]*= 2
        pos += 1


valores = [10,20]
dobra(valores)
print(valores)


#EMPACOTAR COM SOMA
def soma2(* valores):
    s2 = 0
    for num in valores:
        
        print(f'num-> {num} valores-> {valores} s-> {s2}')
        s2 += num
    print(f'Somando os valores {valores} temos {s2}')
    print('+='*30)


soma2(30, 50)
soma2(5,7,8)

#teste = [0,2,3]
#for c in teste:
#    print(f'c-> {c} teste-> {teste}')