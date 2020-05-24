aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}'))

if aluno['media'] >= 7:

    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >=5 or aluno['media'] >=6:
    aluno['situacao'] = 'RECUPERACAO'
else:
    aluno['situacao'] = 'REPROVADO'


print(aluno)


##090
##Faça um programa que leia nome e media de um aluno, guardando tambem a situação desse aluno.
 ##No final mostre o conteudo final na tela##
