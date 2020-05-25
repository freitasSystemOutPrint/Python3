def escreva(*lista):
    pos = 0
    while pos < len(lista):
        print('~'*len(lista[pos]))
        print(lista[pos])
        print('~'*len(lista[pos]))
        pos += 1

        
frase1 = 'Frase'
frase2 = 'Frase grande'
frase3 = 'Frase muito mais grande'
escreva(frase1, frase2, frase3)



def frase():
    print('x'*30)

frase()
print('oi')
frase()


###097
#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma #mensagem com tamanho adaptavel.
	#Ex:
	 #Escreva(Olá, Mundo!)

	 #Saída:
	  #~~~~~~~~~~~
	  #Olá, Mundo!
	  #~~~~~~~~~~~
      ###