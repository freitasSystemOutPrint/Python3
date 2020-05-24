galera = list()
dados = list()
totmai = totmen = 0
for c in range(0,2):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    #galera = dados[:]
    galera.append(dados[:])
    dados.clear()
#print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores de idade e {totmen} menores de idade')

#galera = [['João',19],   ['Ana', 33],   ['Joaquim', 13], ['Maria', 45] ]
#print(galera[2][1])

#for p in galera:
    #print(f'{p[0]} tem {p[1]} anos de idade')



'''teste = list()
teste.append(' Gustavo ' )
teste.append(40)

galera = list()
galera.append(teste[:])
teste[0]  = 'Maria'
teste[1] = 22

galera.append(teste[:])
print(galera)'''
