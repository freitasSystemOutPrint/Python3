cont = 0
cont1 = 0
c = 0

'''while (c >=7):
       n = input('Digite sua idade: ')
       r = n - 2018
       if r >=18:
              cont = cont + 1
       else:
              cont1 = cont1 + 1
'''

contador = 0
contador1 = 0
for c in range(0, 8):
       idade = int(input('Digite seu ano de nascimento: '))
       res = 2018 - idade
       if res >= 18:
              contador = contador + 1
       else:
              contador1 = contador1 + 1
              
print(' {} Pessoas maiores e {} Menores'.format(contador, contador1))
              
