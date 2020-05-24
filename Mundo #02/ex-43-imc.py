nome = input('Escreva seu nome ')
peso = float(input('PESO '))
altura = float(input('ALTURA '))

imc = peso / (altura * altura)

while imc:

    if  (imc <=18.5):
        print(nome, ' você está abaixo do peso ')
        break

    if (imc >= 18.6) and (imc <=24.9):
        print(nome, 'Peso ideal ')
        break

    if(imc >= 25) and (imc <= 29.9):
        print(nome, ' você está levemente acima do peso ')
        break

    if(imc >= 30) and (imc <= 34.9):
        print(nome, ' vocêestá na faixa de  obesidadegrau I ')
        break

    if (imc >= 35) and (imc <= 39.9):
        print(nome, ' você está na faixa de  obesidade grau II (SEVERA ')
        break

    if (imc >= 40):
        print(nome, ' você está na faixa de  obesidade III(MÓRBIDA)')

print('%.2f' % imc)
