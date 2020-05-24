n = float(input('digite a velocidade do carro: '))
n2= n - 80
n3 = n2 * 7
if n>80:
       print('Você foi multado e pagará $7 por cada km acima da média (80km/h)')
       print('O total das multas foi de {:.0f}'.format(n3))

# print('{:.0f}'.format(n2))
