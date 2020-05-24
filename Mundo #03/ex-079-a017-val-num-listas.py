numeros = list()

while True:
    r = 0
    n = int(input('Digite um valor: [000 para sair] '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não adicionado.')
    if n == 000:
        break
print('=-' *30)
numeros.sort()
print(f'{numeros}')
    
    
    
     






'''Ex:079
Crie um programa onde o usuario possa digitar varios
valores numericos e cadastre-os em uma lista.
Caso o numero ja exista, ele nao sera adicionado.
No final, serao mostrados todos os valores unicos digitados em ordem
crescente.

   '''
