n = float(input('Qual a distância da sua viagem? :'))
if (n<=200):
    n = n*0.5
else:
    n = n*0.45
print('O valor da sua passagem vai ser {}'.format(n))

