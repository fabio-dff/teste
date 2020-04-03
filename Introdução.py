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