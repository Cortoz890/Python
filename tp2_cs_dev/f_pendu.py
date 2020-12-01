### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: garder en mémoire les scores/gérer les caracs spétiaux/sécurité pour rentrer une seule lettre à la fois/commenter  ###

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
    All = [L[r][0].lower()]
    p = 0
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
            if loose == 8:
                print("Vous n'avez plus de tentatives.")
            else:
                print('Il vous reste', 8-loose,'tentatives. Vous avez déjà essayé les lettres: ', F)
            
        for i in range(len(L[r])):
            if l == L[r][i]:
                guess[i] = L[r][i]
                w += 1
                p += 1

        print(''.join(guess))
    
    return w, loose, p


def win_defeat(guess, w, L, r): 
    
    if w == len(L[r]):
        print('Bravo vous avez deviné le mot!')
    else:
        print('Oh niiion vous avez perdu, le mot était:', L[r])


def Score(loose, p):
    print(p)
    print(loose)
    if p == 0:
        s = 0
    else:
        s = 100*p - 10*loose
    print('Votre score est:', s)
    
    re = input('Voulez vous rejouer? Veuillez réponder par oui ou non: ')
    if re.lower() == 'oui':
        exec(open('./main_pendu.py').read())
    else:
        print('Revenez vite jouer =)')
    

