def notas(*n sit=False):
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)


resposta = notas{5,5, 2,5, 9, 10}






'''105
Faça um programa que tenha um função chamada notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informaçoes:
	- Quantidade de notas
	- A maior nota
	- A menor nota
	- A media da turma
	- A situação (opcional)

	Adicione tambem as docstrings da funçao.'''

