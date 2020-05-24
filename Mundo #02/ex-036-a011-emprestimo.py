sal= int(input('Quanto você ganha por mês? :'))
par = int(input('Em quantos anos deseja pagar? :'))

tot = sal / 5
print(tot)

if par == (sal*30) / 100:
    print('APROVADO')
else:
    print('REPROVADO')
