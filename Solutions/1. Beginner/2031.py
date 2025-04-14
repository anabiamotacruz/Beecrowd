# -*- coding: utf-8 -*-

N = int(input())

for i in range(N):

    jogada1 = input('').lower()

    jogada2 = input('').lower()
    
    if jogada1 == 'ataque':

        if jogada2 == 'papel' or jogada2 == 'pedra':

            print('Jogador 1 venceu')

        else:

            print('Aniquilacao mutua')
    
    elif jogada1 == 'pedra':

        if jogada2 == 'papel':

            print('Jogador 1 venceu')

        elif jogada2 == 'ataque':

            print('Jogador 2 venceu')

        else:

            print('Sem ganhador')
            
    else:

        if jogada2 == 'papel':

            print('Ambos venceram')

        elif jogada2 == 'pedra':

            print('Jogador 2 venceu')

        else:
            
            print('Jogador 2 venceu')
