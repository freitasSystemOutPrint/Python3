n = int()
cs  = cn = 0
print('Para sair digite 999')

while n !=999:
       n = int(input('Digite os  valores para a soma: '))
       if n !=999:
               cs += n
               cn += 1
print('{} valores digitados com  total da soma de {}'.format(cn, cs))

'''064
Crie um programa que leia vãrios nũmeros inteiros pelo teclado.
O programa sõ vai parar quando o usuãrio digitar o valor 999, que é a
condição de parada, no final mostre qantos nũmeros foram
digitados e qual foi a soma entre eles
(desconsiderando a flag).'''
