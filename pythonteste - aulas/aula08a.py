import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual  a {:.2f}'.format(num, raiz))

'''  Para arredondar para cima use o ceil e para baixo florr e para casas
 decimais dentro dos '{}' use ':' dois pontos {:.2f} em vez de '%'
 
 
 print('A raiz de {} é igual  a {}'.format(num, math.ceil(raiz)))

 '''