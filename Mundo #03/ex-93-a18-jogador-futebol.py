jogador = {
    'nome': str(input('Nome do jogador: ')),
    'partidas': int(input('Partidas jogadas: '))}

tam = (jogador['partidas'])
gol = list(); soma = 0; soma2 = 0
for c in range(0, tam):
    gols = int(input('GOLS: '))
    gol.append([gols])
    soma = sum(gol[c])
    soma2 += soma

print(f'Jogador {jogador["nome"]}')
print(f'Partidas jogadas {jogador["partidas"]}')
print(f'Gols nas partidas {gol}')
print(f'Total de gols no campeonato {soma2}')



########### versao do guanabara #############
gjogador = dict()
gpartidas = list()

gjogador['nome'] = str(input('Nome do jogador '))
tot = int(input(f'Quantas partidas {gjogador["nome"]} jogou?'))
for c in range(0, tot):
    gpartidas.append(int(input(f'  Quantos gols na partida {c} ')))
gjogador['gols'] = gpartidas[:]
gjogador['total'] = sum(gpartidas)
print('-='*30)
print(gjogador)
print('-='*30)
for k, v in gjogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {gjogador["nome"]} jogou {len(gjogador["gols"])} partidas')
for i, v in enumerate(gjogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols')
print(f'Foi um total de {gjogador["total"]} gols')


    

    
#user = str(input("Nome do carro:"))
#veiculos.append([user])
    



#093
 #Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele já jogou. Depois vai ler a qauntidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.