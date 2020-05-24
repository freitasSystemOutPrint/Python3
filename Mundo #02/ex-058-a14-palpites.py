from random import randint
p = int()
t = 0
ran = randint(0, 10)
print(ran)
while  p != ran:
       p =  int(input('Digite seu palpite ente 0 e 10: '))
       t += 1
       if p == ran:
              print('voce acertou com {} tentativas '.format(t))
       elif  p != ran:
              print('Tente novamente')
       if p > 10:
              print("Com valores menores ou iguais a 10")
       #elif p > 10:
         #     print('Apenas palpites menores ou iguais a 10')
       #else:
         #     print('bad')


'''

058
Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10.
Só que agora tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
