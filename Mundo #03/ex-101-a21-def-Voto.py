def voto(a=0):
    global res
    if a >=18 and a <= 64:
        res = 'VOTO OBRIGATORIO'
    elif a >=16 and a < 18 and a >= 65:
        res = 'VOTO OPCIONAL'
    else:
        res = 'VOTO OPCIONAL'


n = int(input('DIGITE SUA IDADE '))
voto(n)
print(res)


"""
101
Faça um programa que tenha uma função chamada voto() que vai receber como parêmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
"""