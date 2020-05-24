pessoas = {'nome': 'FreiFox', 'sexo': 'M', 'idade': 23}
print(pessoas)
print(pessoas['nome'])
print(pessoas.items())
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

for k,v in pessoas.items():
    print(f'{k} = {v}')
