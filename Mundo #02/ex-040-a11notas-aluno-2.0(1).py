n = input('Digite seu nome: ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
r = (n1 + n2) / 2
if r <5:    
    print('{}, você está REPROVADO, com média {} !'.format(n,r))
elif r >= 5 and r <=6.9:
    print('{} você está de RECUPERAÇÃO, com média {}'.format(n,r))
elif r >=7:
    print('{} você está APROVADO, com média {} !'.format(n,r))
input('DIGITE ENTER PARA SAIR')




"""> Média abaixo de 5.0:
- Reprovado
> Média entre 5.0 e 6.9:
- Recuperação
> Média 7.0 ou superior:
- Aprovado """
