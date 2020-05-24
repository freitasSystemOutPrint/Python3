listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posicao {c}')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' *30)
print(f'Voce digitou os valores {listanum}')

print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for i,v in enumerate(listanum):
    if v == maior:
        print(f'{i}...',end='')
print()    
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i,v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end='')
print()

'''Ex:078
Faça um programa que leia 5 valores númericos e guarde-os em
uma lista.
    -> No final, mostre qual foi o maior e o menor valor digitado
       e as suas respectivas posições na lista.'''
