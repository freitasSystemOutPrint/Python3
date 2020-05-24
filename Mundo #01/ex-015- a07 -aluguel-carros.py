d = float(input('Qaunto dias de aluguel? :'))
km = float(input('Quantos Km rodados ? :'))

sd = d*60
skm = km*0.15
st = sd + skm

print('Total a ser pago : R${:.2f}'.format(st))

# ou use esta linha sd = (d*60) + (km * 0.15)
