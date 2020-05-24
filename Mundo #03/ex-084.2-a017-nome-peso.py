temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

        
    princ.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('=-' *30)
print(f'Os dados foram {princ}')
print(f'Ao todo foram cadastrados {len(princ)} pessoas')
#for p in princ:
    #print(princ)
print(f'O maior peso foi de {mai}Kg')
for p in princ:
    if p[1] == mai:
        print(p[0])

print(f'O menor peso foi de {men}Kg')
for p in princ:
    if p[1] == men:
        print(p[0])
#print(princ)
























#Meu codigo

'''nome = []
peso = []
maior = 0
menor = 0
cad = 0

for c in range(0,2):
    nome.append(str(input('Digite seu nome: ')))
    cad +=1
    peso.append(int(input('Digite seu peso: ')))

    if c == 0:
        maior = menor = peso[c]
    else:
        if peso[c] > maior:
            maior < peso[c]
        if peso[c] < menor:
            menor = peso[c]

print(nome, peso)
print(f'O maior peso digitado foi {maior}')

print(f'O menor peso digitado foi {menor}')
print(f'Pessoas cadastradas {cad}')
'''




'''ex:084
Faça um programa que leia nome e peso de varias pessoas, guardando
tudo em uma lista. No final mostre:

    ->A) Quantas pessoas foram cadastradas.
    ->B) Uma listagem com as pessoas mais pesadas.
    ->C) Uma listagem com as pessoas mais leves.
'''
