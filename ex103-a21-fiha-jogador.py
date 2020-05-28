def ficha(n='<nao infomado>',g='nao informados'):
    global gol
    global nome
    gol = g
    nome = n




#ficha('TESTE', 3)
#ficha('RONALDINHO','1400')
ficha('Freitas')
print(f'JOGADOR> {nome}  GOLS: {gol}')

#njog = str(input('Digite o nome do jogador: '))
#gjog = str(input(f'Gold marcados pelo jogador {njog}'))








'''
103
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
	O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''