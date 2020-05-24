s = 0
for c in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s = s + n
print('A soma dos pares foi > {}'.format(s))
