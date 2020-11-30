### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: fonction score ###

## Importation des modules ##
import random

## Def des fonctions ##
def Find_word(f):
# Fonction prenant en parramétre un fichier contenant les mots pour jouer au pendu  
# Retourne une liste contenant tous les mots danns le fichier f      
    L = []
    for i in f:
        L.append(i)
    f.close()

    return L
    

def Word_to_guess(L, r):
# Fonction prenant en paramétre une liste de mots et un nombre aléatoire correspondant au mot à
# deviner
# Retourne une liste contenant la première lettre du mot à deviner et des - pour les autres
    w  = 2
    guess = list(L[r][0] + (len(L[r]) - 2) * "-")

    for i in range(len(L[r])):
        if L[r][i] == L[r][0].lower():
            guess[i] = guess[0].lower()
            w += 1

    return guess, w
    
    
def Game(guess, w, L, r): 
  
    F = []
    All = []
    loose = 0

    print(''.join(guess))
    
    while w < len(L[r]) and loose < 8:
        l = input("Veuillez saisisir une lettre svp: ")

        if l in All:
            l = input('Vous avez déjà utilisé cette lettre veuillez en choisisr une autre: ')
        
        else:
            All.append(l)

        if l not in L[r]:
            F.append(l)
            loose += 1
            print('Il vous reste', 8-loose,'tentatives. Vous avez déjà essayé les lettres: ', F)
            
        for i in range(len(L[r])):
            if l == L[r][i]:
                guess[i] = L[r][i]
                w += 1

        print(''.join(guess))
    
    return w

def win_defeat(L, r, w):    
    if w == len(L[r]):
        print('Bravo vous avez deviné le mot')
    else:
        print('Oh niiion vous avez perdu, le mot était: ', L[r])


    #re = input('Voulez vous rejouez? Répondez par oui ou non: ')

    #if re == 'oui':
    #    Game(random.randint(0, 193))
        
    #else:
    #    print('Revenez vite jouer =)')




def Score():
    score = Pendu(r)

