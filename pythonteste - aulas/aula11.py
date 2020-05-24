#print('\033[1;35;43mOlá, Mundo!\033[m')
#a = 3
#b = 5
nome = 'Freitas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

#print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

print('Olá, {}{}{} !!!'.format(cores['amarelo'], nome, cores['limpa']))