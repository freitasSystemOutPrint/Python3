n = str(input('digite uma frase: ')).upper().strip()
print('A letra a apareceu {} vezes '.format(n.count('A')))
print('a primeira letra a apareceu na pos: {}'.format(n.find('A')+1))
print('A ultima letra A  apareceu na pos: {}'.format(n.rfind('A')+1))
