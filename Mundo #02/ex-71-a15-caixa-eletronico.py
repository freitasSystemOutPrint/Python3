valor =  int(input('Qaul valor do saque:  '))
total = valor
ced = 50
totced  = 0
while True:
       if total >= ced:
              total = total - ced
              totced +=1
       else:
              print('Total de {} cedulas de R${}'.format(totced, ced))
              if ced == 50:
                     ced =20
              elif ced == 20:
                     ced = 10
              elif ced ==10:
                     ced = 1
              totced = 0
              if total == 0:
                     break




'''071
Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual valor a ser
sacado (num int) e o programa informará quantas cédulas de cada valor serão entregues.
			OBS: Considere que o caixa possui cédulas de
			R$50, R$20, R$10 e R$1.

'''
