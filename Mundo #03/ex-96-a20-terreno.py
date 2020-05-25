def calcT(a, b):
    frente = (a*2) /2
    lado   = (b*2) /2
    tot    = lado * frente
    print(frente)
    print(lado)
    print(f'Terreno de {tot} de tamanho')


lar = 12
com = 40
calcT(lar, com)




'''É só somar a metragem da frente e do fundo e dividir por 2. Depois some a metragem do lado direito com o esquerdo e também dividir por 2. Pronto, agora é só multiplicar um resultado pelo outro e vc terá a metragem total do imovel. EX: frente:12,00m ;fundos: 14,00m; lado direito:35,00m; lado esquerdo:40,00m# 12+14=26/2=13 # 35+40=75/2=37,5 # 13x37,5=487,50. O lote tem 487,50 metros quadrados.'''
#096
#Faça um programa que teanha um função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.