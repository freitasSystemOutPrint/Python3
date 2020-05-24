#coding: utf-8
op= op2 = op3 = op4 = op5 = op6 = op7 = op8 = op9 = op10 = ' '
#p1 = p2 = p3 = p4  = p5 = 20
pontos = 0

print(20*'=')
print('Bem Vindo(a) ao quiz de idade mental ')
print('Responda as perguntas abaixo e no final sera mostrado sua idade mental')
print('QUIZ IDADE MENTAL')
print(20*'=')

print('RESPONDA COM  -A-   -B-  -C- OU -D-  : ')

#1a Pergunta
while  op != 'A' or op != 'B' or op !=  'C' or op != 'D':
       print(20*'--')
       print('[ 1a PERGUNTA ] \n ')
       print(20*'--')
       print('COMO VOCE GOSTARIA DE COMEMORAR SEU ANIVERSSARIO? \n')

       print('A. COM UMA FESTA COM BOLO')
       print('B. COMEMORAR ANIVERSSARIO E COISA DE CRIANÇA')
       print('C. ALMOÇANDO OU JANTANDO COM SEUS FAMILIARES')
       print('D. BEBENDO E SE DIVERTINDO')

       op = str(input('RESPOSTA >: ' )).upper()

       if op == 'A' or op == 'B' or op ==  'C' or op == 'D':
              break
       elif op != 'A' or op != 'B' or op != 'C' or op != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')

#2a Pergunta
while op2 != 'A' or op2 != 'C' or op2 !=  'C' or op2 != 'D':
       print(20*'--')
       print('[ 2a PERGUNTA ]\n')
       print(20*'--')
       print('COMO SERIA SUAS FERIAS PERFEITAS? \n')
       print('A. CONHECENDO NOVAS CULTURAS')
       print('B. VIAJANDO PELA FRANÇA, NOVA YORK, ITALIA...')
       print('C. QUALQUER LUGAR COM PRAIA E MUITO SOL')
       print('D. EM UM SUPER PARQUE, COMO A DISNEYLANDYA\n')

       op2 = str(input('RESPOSTA > : ')).upper()


       if op2 == 'A' or op2 == 'B' or op2 ==  'C' or op2 == 'D':
              break
       elif op2 != 'A' or op2 != 'B' or op2!=  'C' or op2 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')


#3a Pergunta
while op3 != 'A' or op3 != 'C' or op3!=  'C' or op3 != 'D':
       print(20*'--')
       print('[ 3a PERGUNTA ]\n')
       print(20*'--')
       print('QUAL DESSAS BEBIDAS VOCE PREFERE TOMAR EM SUAS REFEIÇOES?\n')
       print('A. REFRIGERANTE')
       print('B. VINHO')
       print('C. CERVEJA')
       print('D. SUCO DE FRUTAS\n')
       op3 = str(input('RESPOSTA >: ')).upper()

       if op3 == 'A' or op3 == 'B' or op3 ==  'C' or op3 == 'D':
              break
       elif op3 != 'A' or op3 != 'B' or op3!=  'C':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')
              
#4a Pergunta
while op4 != 'A' or op4 != 'B' or op4 != 'C' or op4 != 'D':
       print(20*'--')
       print('[ 4a PERGUNTA ]\n')
       print(20*'--')
       
       print('O QUE VOCE ACHA DE MUSICA CLASSICA?')
       print('A. LEGAL')
       print('B. EU ADORO')
       print('C. EU ODEIO')
       print('D. ACHO RELAXANTE \n')

       op4 = str(input('RESPOSTA >: ' )).upper()

       if  op4 == 'A' or op4 == 'B' or op4 == 'C' or op4 == 'D':
              break
       elif op4 != 'A' or op4 != 'B' or op4 != 'C' or op4 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')

#5a Pergunta
while op5 != 'A' or op5 != 'B' or op5 != 'C' or op5 != 'D':
       print(20*'--')
       print('[ 5a PERGUNTA ]\n')
       print(20*'--')

       print('ESCOLHA UMA DAS COMIDAS ABAIXO')
       print('A. FRUTOS DO MAR')
       print('B. COMIDA GELADA')
       print('C. FAST FOOD')
       print('D. SOPAS E CALDOS\n')

       op5 = str(input('RESPOSTA >: ')).upper()

       if op5 == 'A' or op5 == 'B' or op5 ==  'C' or op5 == 'D':
              break
       elif op5 != 'A' or op5 != 'B' or op5 != 'C' or op5 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')

#6
while op6 != 'A' or op6 != 'B' or op6 != 'C' or op6 != 'D':
       print(20*'--')
       print('[ 6a PERGUNTA ]\n')
       print(20*'--')

       print('QUE TIPO DE PROGRAMAÇAO VOCE GOSTA DE ASSISTIR?')
       print('A. UM FILME DE SUSPENSE OU DRAMA')
       print('B. UM FILME DE AÇAO OU COMEDIA')
       print('C. DESENHOS ANIMADOS')
       print('D. DOCUMENTARIOS\n')

       op6 = str(input('RESPOSTA >: ')).upper()

       if op6 == 'A' or op6 == 'B' or op6 == 'C' or op6 == 'D':
              break
       elif op6 != 'A' or op6 != 'B' or op6!= 'C' or op6 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')

#7
while op7 != 'A' or op7 != 'B' or op7 != 'C' or op7 != 'D':
       print(20*'--')
       print('[ 7a PERGUNTA ]\n')
       print(20*'--')

       print('OQUE VOCE ACHA DAS REDES SOCIAIS?')
       print('A. FUNDAMENTAL PARA MINHA VIDA')
       print('B. ELAS SAO CONFUSAS')
       print('C. ELAS SAO UTEIS')
       print('D. PERDA DE TEMPO\n')

       op7 = str(input('RESPOSTA >: ')).upper()

       if op7 == 'A' or op7 == 'B' or op7 ==  'C' or op7 == 'D':
              break
       elif op7 != 'A' or op7 != 'B' or op7 != 'C' or op7 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')
#8
while op8 != 'A' or op8 != 'B' or op8 != 'C' or op8 != 'D':
       print(20*'--')
       print('[ 8a PERGUNTA ]\n')
       print(20*'--')

       print('COMO VOCE ENCARA DOCES E BALAS?')
       print('A. EU ADORO')
       print('B. LEGAL')
       print('C. DOCES E BALAS SAO COISAS DE CRIANÇAS')
       print('D. NAO SAO SAUDAVEIS PREFIRO EVITAR\n')

       op8 = str(input('RESPOSTA >: ')).upper()

       if op8 == 'A' or op8 == 'B' or op8 ==  'C' or op8 == 'D':
              break
       elif op8 != 'A' or op8 != 'B' or op8 !=  'C' or op8 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')
#9
while op9 != 'A' or op9 != 'B' or op9!=  'C' or op9 != 'D':
       print(20*'--')
       print('[ 9a PERGUNTA ]\n')
       print(20*'--')

       print('O QUE VOCE ACHA DOS ESMARTPHONES?')
       print('A. MUITO CAROS E DESNECESSARIOS')
       print('B. TOTALMENTE NECESSARIOS')
       print('C. EXTREMAMENTE COFUSOS')
       print('D. UTEIS, EU ACHO\n')

       op9 = str(input('RESPOSTA >: ')).upper()

              
       if op9 == 'A' or op9 == 'B' or op9 ==  'C' or op9 == 'D':
              break
       elif op9 != 'A' or op9 != 'B' or op9 !=  'C' or op9 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')
#10
while op10 != 'A' or op10 != 'B' or op10 != 'C' or op10 != 'D':
       print(20*'--')
       print('[ 10a PERGUNTA ]\n')
       print(20*'--')

       print('QUAL DESSES GRUPOS DE CORES E SEU FAVORITO?')
       print('A. ROSA PINK, AZUL CLARO, NAPOLITANO')
       print('B. CINZA ESCURO, CINZA CLARO, MARRON FORTE')
       print('C. AMARELA, VERDE, AZUL FORTE')
       print('D. VERDE BEM FRACO, SALMAO BEM FRACO, AMARELO BM FRACO\n')

       op10 = str(input('RESPOSTA >: ')).upper()

       if op10 == 'A' or op10 == 'B' or op10 ==  'C' or op10 == 'D':
              break
       elif op10 != 'A' or op10 != 'B' or op10 !=  'C' or op10 != 'D':
              print('ALTERNATIVA INVALIDA\n')
              print(35*'-')
              print('TENTE NOVAMENTE')
              print(35*'-')
              
#1
if op == 'A':
       pontos += 40
elif op == 'B':
       pontos += 10
elif op == 'C':
       pontos += 20
elif op == 'D':
       pontos += 30
#2
if op2 == 'A':
       pontos += 10
elif op2 == 'B':
       pontos += 20
elif op2 == 'C':
       pontos += 30
elif op2 == 'D':
       pontos += 40
#3
if op3 == 'A':
       pontos += 40
elif op3 == 'B':
       pontos += 20
elif op3 == 'C':
       pontos += 10
elif op3 == 'D':
       pontos += 30
#4
if op4 == 'A':
       pontos += 30
elif op4 == 'B':
       pontos += 10
elif op4 == 'C':
       pontos += 40
elif op4 == 'D':
       pontos += 20
#5
if op5 == 'A':
       pontos += 10
elif op5 == 'B':
       pontos += 30
elif op5 == 'C':
       pontos += 40
elif op5 == 'D':
       pontos += 20
#6
if op6 == 'A':
       pontos += 20
elif op6 == 'B':
       pontos += 30
elif op6 == 'C':
       pontos += 40
elif op6 == 'D':
       pontos += 10
#7
if op7 == 'A':
       pontos += 40
elif op7 == 'B':
       pontos += 10
elif op7 == 'C':
       pontos += 30
elif op7 == 'D':
       pontos += 20
#8
if op8 == 'A':
       pontos += 40
elif op8 == 'B':
       pontos += 30
elif op8 == 'C':
       pontos += 20
elif op8 == 'D':
       pontos += 10
#9
if op9 == 'A':
       pontos += 20
elif op9 == 'B':
       pontos += 40
elif op9 == 'C':
       pontos += 10
elif op9 == 'D':
       pontos += 30
#10
if op10 == 'A':
       pontos += 40
elif op10 == 'B':
       pontos += 20
elif op10 == 'C':
       pontos += 30
elif op10 == 'D':
       pontos += 10
print(20*'=')
print('RESUTADO')
print(20*'=')

if pontos >= 350 and pontos <= 400:
       print('IDADE MENTAL ENTRE 4 E 9 ANOS')
elif pontos >= 300 and pontos <= 340:
       print('IDADE MENTAL EENTRE 9 E 16 ANOS')
elif pontos >= 250 and pontos <= 290:
       print('IDADE MENTAL ENTRE 16 E 21 ANOS')
elif pontos >= 200 and pontos <= 240:
       print('IDADE MENTAL ENTRE 21 E 29 ANOS')
elif pontos >= 150 and pontos <= 190:
       print('IDADE MENTAL ENTRE 29 E 55 ANOS')
elif pontos >= 100 and pontos <= 140:
       print('IDADE MENTAL ACIMA DE 55 ANOS')

print(pontos)

print(25*'x')
print('PARA SAIR DIGITE Q:')
print(25*'x')
