### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: tout ###

## Def des fonctions ##
def Pendu1(w):
# Fonction prenant en parramétre un nombre aléatoire correspondant à un mot dans le fichier
# 'mots.txt'. Une fois le mot sélectionné la fonction demande à l'utilisateur une lettre 
# jusqu'à ce que l'utilisateur trouve le mot ou se trompe 8 fois.
# On a donc en sorti un message de victoire ou de défaite.
    
    file = open("mots.txt")
    L = []
    F = []
    win = 2
    loose = 0

    for i in file:
        L.append(i)
    file.close()

    guess = list(L[w][0] + (len(L[w]) - 2) * "-")
    print(''.join(guess))
    
    while win < len(L[w]) and loose < 8:
        l = input("Veuillez saisisr une lettre svp: ")
        
        if l not in L[w]:
            F.append(l)
            loose += 1
            print('Il vous reste', 8-loose,'tentatives. Vous avez déjà essayé les lettres: ', F)
            

        for i in range(len(L[w])):
            if l == L[w][i]:
                guess[i] = L[w][i]
                win += 1

        

        print(''.join(guess))
        

    if win == len(L[w]):
        print('Bravo vous avez deviné le mot')
    else:
        print('Oh niiion vous avez perdu, le mot était: ', L[w])


