def maior(* param):
    print('')




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


'''099
Faça um programa que tenha uma funcao maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''