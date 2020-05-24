pessoas = {'Nome': 'Freitas',  'Sexo':  'M', 'Idade': 22 }
for k in pessoas.values():
    print(k) #Printa Freitas - M - 22

for k, v in pessoas.items():
    print(k,v) #Printa-  Nome Freitas - Sexo M - Idade 22

 #del pessoas['sexo'] # deleta o sexo
pessoas['Nome'] = 'Leandro' #  troca o nome q estiver por : Leandro
pessoas['peso'] = 98,5 # Adiciona um elemento peso

print()
print()

brasil = []
estado1 = {'uf': 'Rio de Janeiro',  'Sigla': 'RJ '      }
estado2 = {'uf': 'Sao Paulo',  'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]) # printa 'uf': 'Rio de Janeiro',  'Sigla': 'RJ '

print()
print()

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unid Fed:  '))
    estado['sigla'] = str(input('Sigla:  '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')











