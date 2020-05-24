'''for c in range(0,5):
       p = input('digite seu peso: ')
       numeros = [p0, p1, p2, p3, p4]
print("Maior número da lista é:", max(numeros))


p = ['python', 'is', 'life']
print(p[2])
'''
n1 = float(input('Digite o peso: '))
n2 = float(input('Digite o peso: '))
n3 = float(input('Digite o peso: '))

if n1 > n2 and n1> n3:
       print('primeiro tem maior peso')
elif n2 > n1 and n2> n3:
       print('segundo tem maior peso ')
elif n3 > n1 and  n3 > n2:
       print('terceiro tem maior peso')

if n1 < n2 and n1< n3:
       print('primeiro tem menor peso')
elif n2 < n1 and n2< n3:
       print('segundo tem menor peso')
elif n3 < n1 and  n3 < n2:
       print('terceiro tem menor peso')



