ficha = list()
while True:
    
    nome = str(input('Nome:         '))
    nota1 = float(input('Nota 1:    '))
    nota2 = float(input('Nota2:     '))
    media = (nota1 + nota2) / 2

    ficha.append( [nome, [nota1, nota2], media  ]  )
    resp = str(input('Quer continuar?  s/n '))
    if resp in 'Nn':
        break
print('-=' *30)
print(f'  {"No.":<4}  {"NOME":<10}{"MEDIA":>8}')
print('_' *26)
for i, a in enumerate(ficha):
    print(f'{i:<4}   {a[0]:<10}  {a[2]:>8.1f}')
while True:
    print('_' *35)
    opc = int(input('Mostrar notas de qual aluno? (999 intenrrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')



'''ex:089
Crie um programa que leia nome e duas notas
de varios alunos e guarde tudo em uma lista composta.
No final mostre o blotetim contendo a media de cada um e permita que o
usuario possa mostrar as notas de aluno individualmente.'''
