print('Para sair do programa digite -X- ')
c = ''
while c  !='X' :
       c = str(input('Informe seu sexo: [M/F]')).upper()
       if c == 'M':
              print('Masculino')
       elif c == 'F':
              print('Femenino')
       elif c != 'M' and c != 'F':
             print('Erro digite apenas F ou M')
