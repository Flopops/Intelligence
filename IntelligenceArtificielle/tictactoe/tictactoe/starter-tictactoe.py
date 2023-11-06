# -*- coding: utf-8 -*-

import time
import Tictactoe 
from random import randint,choice

def RandomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles'''
    return choice(b.legal_moves())

def deroulementRandom(b):
    '''Effectue un déroulement aléatoire du jeu de morpion.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == 1:
            print("Victoire de X")
        elif res == -1:
            print("Victoire de O")
        else:
            print("Egalité")
        return
    b.push(RandomMove(b))
    deroulementRandom(b)
    b.pop()


def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0


board = Tictactoe.Board()
print(board)

### Deroulement d'une partie aléatoire
deroulementRandom(board)

print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
print(board)


def getResultatX(b):
    cpt=[0,0,0]
    ResultatX(b,"X",cpt)
    print("V:", cpt[0])
    print("F:", cpt[1])
    print("E:", cpt[2])
    print("Paries totales :", cpt[0]+cpt[1]+cpt[2])




def ResultatX(b, current_player, cpt):
    if (b.is_game_over()):
        res = getresult(b)
        if res == 1:
            cpt[0] += 1
        elif res == -1:
            cpt[1] += 1
        else:
            cpt[2] += 1
        return

    for move in b.legal_moves():
        b.push(move)
        ResultatX(b, 'X' if current_player == 'O' else 'O', cpt)
        b.pop()
       
    
   






getResultatX(board)



def rechercheStrategie(b, current_player):
        if b.is_game_over():
            result = getresult(b)
            if result == 1:
                return 1
            elif result == -1:
                return -1
            else:
                return 0

        for move in b.legal_moves():
            b.push(move)
            opp_result = rechercheStrategie(b, 'X' if current_player == 'O' else 'O')
            b.pop()
            if opp_result == -1:
                return 1
        return 0


def evalue(joueur, board): 

    if board.result() == board._X and joueur == 'X':
        return 1
    elif board.result() == board._O and joueur == 'O':
        return -1
    else:
        return 0


def EstFeuille(board):
    return board.is_game_over()


def MaxMin(board, AMI):
    if EstFeuille(board):
        return evalue(AMI, board)
    
    Meilleur = float('-inf')
    for successeur in board.legal_moves():
        board.push(successeur)
        Meilleur = max(Meilleur, MinMax(board, AMI))
        board.pop()
    
    return Meilleur

def MinMax(board, ENNEMI):
    if EstFeuille(board):
        return evalue(ENNEMI, board)
    
    Pire = float('inf')
    for successeur in board.legal_moves():
        board.push(successeur)
        Pire = min(Pire, MaxMin(board, ENNEMI))
        board.pop()
    
    return Pire


def jouer_au_morpion(board, current_player):
    AMI = 'X'
    ENNEMI = 'O'

    while not board.is_game_over():
        if current_player == AMI:
            move = MaxMin(board, AMI)
        else:
            move = MinMax(board, ENNEMI)

            return

        for move in board.legal_moves():
            board.push(move)
            jouer_au_morpion(board, 'X' if current_player == 'O' else 'O')
            

    if board.result() == board._X:
        print("Le joueur AMI a gagné !")
    elif board.result() == board._O:
        print("Le joueur ENNEMI a gagné !")
    else:
        print("Match nul.")


jouer_au_morpion(board, 'X')

strategy_result = rechercheStrategie(board, 'X')
if strategy_result == 1:
        print("Il existe une stratégie gagnante pour 'X'.")
else:
        print("Aucune stratégie gagnante pour 'X' n'a été trouvée.")








