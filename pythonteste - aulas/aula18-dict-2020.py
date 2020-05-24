pessoas = {
     'nome': 'Maldine',
     'sexo':'M',
     'idade':23}
####################################################


for k,v in pessoas.items():
    print(f'{k} = {v}') 

brasil=[]
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0] ['uf'   ])
print(brasil[1] ['sigla'])



#################################################

estado3 = dict()
brasil3 = dict()

for c in range(0,3):
    estado3['uf'] = str(input('Unidade Federativa'))
    estado3['sigla'] = str(input('Sigla Estado'   ))
    brasil3.append(estado3.copy()) #dando erro n sei pq
    print(brasil3)
