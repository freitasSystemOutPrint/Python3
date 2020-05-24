n = input('Digite seu nome: ')
n2 = int(input('Digite sua idade: '))
f = 18 - n2
p = n2 - 18
if n2 <=17:
    print('{}, você ainda não pode se alistar, ainda faltam {} anos para que isso seja possivel'.format(n,f))
elif n2 > 18 and n2 <=45:
    print('{}, você deveria ter se alistado á {} anos atrás'.format(n,p))
elif n2 >=46:
    print('{}, você passou do tempo de se alistar'.format(n))
elif n2 ==18:
    print(' {}, É hora de se alistar !'.format(n))
    
print('Boa Sorte !')
