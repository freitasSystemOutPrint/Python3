t(input('didite um valor: '))
for c in range(0, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
