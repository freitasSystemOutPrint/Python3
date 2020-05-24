t = s = 0
while True:
      print('='*17)
      print('Para sair digite: 000')
      print('='*17)
      n =  int(input('Tabuada de : '))
      if n == 000:
            break
      for x in range(0, 10):
            t +=1
            s+=1
            
            print('{} x {} = {}'.format(n, s, n*t))
print('FINALIZANDO..........')

       
       

'''067
Faça um programa que mostre a tabuada de vários num,
um de cada vez, para cada valor digitado pelo usuário.
O prograna será interrompido quando o número solicitado for negativo.
'''
