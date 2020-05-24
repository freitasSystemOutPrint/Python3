from random import randint
user = int(input('digite um numero de 0  a 5: '))
ran = randint(0, 5)
print(ran)
if user == ran:
       print('ACERTOU')
else:
       print('TENTE NOVAMENTE')



"""from random import randrange, uniform
print(randrange(0, 9)) #faixa de inteiro
print(uniform(0, 9)) #faixa de ponto flutuante
"""
