n = input('Digite seu nome: ')
i = int(input('digite sua idade: '))
if i <=9:
       print('{} você está na clasificação  > MIRIM'.format(n))
elif i >=10 and i<=14:
       print('{} você está na clasificação  > INFANTIL'.format(n))
elif i >=15 and i<=19:
       print('{} você está na clasificação  > JUNIOR'.format(n))
elif i ==20:
       print('{} você está na clasificação  > SENIOR'.format(n))
elif i >20 and i <=65:
       print('{} você está na clasificação  > MASTER'.format(n))
else:
       print('ERROR !!!')
       


s = input('Pressione a tecla ENTER para sair: ')



'''> Até 9 anos: Mirim
> Até 14 anos: INFANTIL
> Até 19 anos: JUNIOR
> Até 20 anos: SÊNIOR
> Acima: MASTER'''
