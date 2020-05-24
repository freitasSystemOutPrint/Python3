nome = input('Digite sue nome: ')
n = int(input('Qual seu salário: '))

val = (n*15) / 100
res = n + val

print(' {} Seu novo salário com almento de 15% vai ser de  ${}'.format(nome, res))
