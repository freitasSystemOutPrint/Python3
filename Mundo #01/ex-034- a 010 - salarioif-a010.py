salario = float(input('Salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario +(salario * 10 /100)
print('Seu salário com aumento de 10% vai ser de {}'.format(novo))
