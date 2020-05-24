nome = str(input('Digite seu nome'))
n1 = int(input('digite a 1º nota Ling Tec Programacao'))
n2 = int(input('digite a 2º nota Ling Tec Programacao'))

s = (n1 + n2) / 2

if s <= 6:
    sit = 'REPROVED'

elif s >= 7:
    sit = 'APROVED'

print('Aluno {} com média {} : '.format(nome,s))
print('Situacao {} : '.format(sit))
