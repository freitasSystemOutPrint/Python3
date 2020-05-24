aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media: '))

if aluno['Media'] >= 7:
    aluno['situacao']  = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'
print(aluno.items())

for k, v in aluno.items():  
    print(   f'  {k} é igual a {v} '  )
for b, c in range(0,5):
    print(f'{b} --- {c}')

'''
Faça um programa que leia o nome e média de
um aluno, guardando tambem a situaçao
em um dicionario. No final mostre
o conteudo da estrutura na tela.

'''

