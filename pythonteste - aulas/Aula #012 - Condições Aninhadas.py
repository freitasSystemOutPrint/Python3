nome = str(input('Digite seu nome: '))
if nome == 'Freitas: ' or 'freitas ':
       print('Que nome bonito: ')
elif nome == 'Maria' or 'Pedro' or 'Paulo: ':
       print( ' {}, seu nome é bem comun no Brasil'.format(nome))
else:
       print('Seu nome é bem normal. ')
print('Tenha um bom dia {}'.format(nome))
