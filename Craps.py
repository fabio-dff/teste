#Introdução do Craps
import random
fichas = 1000
game_on = True
while game_on:
    print ('Você possui {0} fichas.'.format(fichas))
    print('Você está na fase Come Out!')
    pergunta_inicial = input('Você quer apostar ou sair do jogo?(apostar/sair): ')
    if pergunta_inicial == 'sair':
        print('FIM DE JOGO')
        break
    else:
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma1 = dado1 + dado2
        pergunta2 = input('Você quer apostar em Field?(s/n): ')
        if pergunta2 == 'n' or pergunta2 == 'não':
            pass
        else:
            aposta2 = int(input('Quantas fichas você quer apostar em Field? '))
        pergunta3 = input('Você quer apostar em Any Craps?(s/n): ')
        if pergunta3 == 'n' or pergunta3 == 'não':
            pass
        else:
            aposta3 = int(input('Quantas fichas você quer apostar em Any Craps? '))
        pergunta4 = input('Você quer apostar em Twelve?(s/n): ')
        if pergunta4 == 'n' or pergunta4 == 'não':
            pass
        else:
            aposta4 = int(input('Quantas fichas você quer apostar em Twelve? '))
        pergunta1 = input('Você quer apostar em Pass Line Bet?(s/n): ')
        if pergunta1 == 'n' or pergunta1 == 'não':
            pass
        else:
            aposta1 = int(input('Quantas fichas você quer apostar em Pass Line Bet? '))
        print('No primeiro dado saiu o número {0}.'.format(dado1))
        print('No segundo dado saiu o número {0}.'.format(dado2))
        print('A soma dos dois dados é {0}.'.format(soma1))
        
        #Field
        if pergunta2 == 'n' or pergunta2 == 'não' :
            pass
        else:
            if 5<=soma1<=8:
                fichas = fichas - aposta2
                print('Você perdeu {0} fichas em Field!'.format(aposta2))
            elif 3<=soma1<=4 or 9<=soma1<=11:
                fichas = fichas + aposta2
                print ('Você ganhou {0} fichas em Field!'.format(aposta2))
            elif soma1==2:
                fichas = fichas + 2*aposta2
                print ('Você ganhou {0} fichas em Field!'.format(2*aposta2))
            else:
                fichas = fichas + 3*aposta2
                print ('Você ganhou {0} fichas em Field!'.format(3*aposta2))

        #Any Craps
        if pergunta3 == 'n' or pergunta3 == 'não':
            pass
        else:
            if soma1 == 2 or soma1 == 3 or soma1 == 12:
                fichas = fichas + aposta3*7
                print('Você ganhou {0} fichas em Any Craps!'.format(7*aposta3))
            else:
                fichas = fichas - aposta3
                print('Você perdeu {0} fichas em Any Craps!'.format(aposta3))

        #Twelve
        if pergunta4 == 'n' or pergunta4 == 'não':
            pass
        else:
            if soma1 == 12:
                fichas = fichas + aposta4*30
                print('Você ganhou {0} fichas em Twelve!'.format(30*aposta4))
            else:
                fichas = fichas - aposta4
                print('Você perdeu {0} fichas em Twelve!'.format(aposta4))


        if pergunta1 == 'n' and pergunta2 == 'n' and pergunta3 == 'n' and pergunta4 == 'n':
            sair = (input('Você quer sair do jogo ou esperar a próxima rodada?(sair/esperar: '))
            if sair == 'sair':
                print('Fim de Jogo')
                break
            else:
                continue
            
        
        #Pass Line Bet
        if pergunta1 == 'n' or pergunta1 == 'nao':
            pass
        else:
            if soma1 == 7 or soma1 == 11:
                fichas = fichas + aposta1
                print('Você ganhou {0} fichas em Pass Line Bet!'.format(aposta1))
            elif soma1 == 2 or soma1 == 3 or soma1 == 12:
                fichas = fichas - aposta1
                print('Você perdeu {0} fichas em Pass Line Bet!'.format(aposta1))
            else:
                Point = True
                while Point:
                    print('Você está na fase Point!')
                    print ('Você possui {0} fichas.'.format(fichas))
                    dado3 = random.randint(1,6)
                    dado4 = random.randint(1,6)
                    soma2 = dado3 + dado4
                    pergunta5 = input('Você quer apostar em Field?(s/n): ')
                    if pergunta5 == 'n' or pergunta5 == 'não':
                        pass
                    else:
                        aposta5 = int(input('Quantas fichas você quer apostar em Field? '))
                    pergunta6 = input('Você quer apostar em Any Craps?(s/n): ')
                    if pergunta6 == 'n' or pergunta6 == 'não':
                        pass
                    else:
                        aposta6 = int(input('Quantas fichas você quer apostar em Any Craps? '))
                    pergunta7 = input('Você quer apostar em Twelve?(s/n): ')
                    if pergunta7 == 'n' or pergunta7 == 'não':
                        pass
                    else:
                        aposta7 = int(input('Quantas fichas você quer apostar em Twelve? '))
                    print('No primeiro dado saiu o número {0}.'.format(dado3))
                    print('No segundo dado saiu o número {0}.'.format(dado4))
                    print('A soma dos dois dados é {0}.'.format(soma2))

                    #Field
                    if pergunta5 == 'n':
                        pass
                    else:
                        if 5<=soma2<=8:
                            fichas = fichas - aposta5
                            print('Você perdeu {0} fichas em Field!'.format(aposta5))
                        elif 3<=soma2<=4 or 9<=soma2<=11:
                            fichas = fichas + aposta5
                            print('Você ganhou {0} fichas em Field!'.format(aposta5))
                        elif soma2==2:
                            fichas = fichas + 2*aposta5
                            print('Você ganhou {0} fichas em Field!'.format(2*aposta5))
                        else:
                            fichas = fichas + 3*aposta5
                            print('Você ganhou {0} fichas em Field!'.format(3*aposta5))

                    #Any Craps
                    if pergunta6 == 'n':
                        pass
                    else:
                        if soma2 == 2 or soma2 == 3 or soma2 == 12:
                            fichas = fichas + aposta6*7
                            print('Você ganhou {0} fichas em Any Craps!'.format(7*aposta6))
                        else:
                            fichas = fichas - aposta6
                            print('Você perdeu {0} fichas em Any Craps!'.format(aposta6))
                    #Twelve
                    if pergunta7 == 'n':
                        pass
                    else:
                        if soma2 == 12:
                            fichas = fichas + aposta7*30
                            print('Você ganhou {0} fichas em Twelve!'.format(aposta7*30))
                        else:
                            fichas = fichas - aposta7
                            print('Você perdeu {0} fichas em Twelve!'.format(aposta7))
                    if soma2 == 7:
                        fichas = fichas - aposta1
                        print('Você perdeu {0} fichas e sairá do Point!'.format(aposta1))
                        break
                    elif soma2 == soma1:
                        fichas = fichas + aposta1
                        print('Você ganhou {0} fichas e sairá do Point!'.format(aposta1))
                        break
                    if fichas <= 0:
                        break
        if fichas <= 0:
            print('Ops! Você faliu amigão!')    
                