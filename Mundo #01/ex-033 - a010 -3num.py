a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))

if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
print('Menor {}'.format(menor))