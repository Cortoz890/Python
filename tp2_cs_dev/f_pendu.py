### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: garder en mémoire les scores ###


## Importation des modules ##



## Def des fonctions utiles au jeu ##
def Find_word(f):
    # Fonction prenant en parramétre un fichier f contenant les mots pour jouer au pendu. 
    # Retourne une liste contenant tous les mots danns le fichier f.       
    
    L = []
    for i in f:
        L.append(i)
    f.close()

    return L
    

def Word_to_guess(L, r):
    # Cette fonction permet de cacher les lettres du mots choisi au hasard sauf la première et
    # révèle d'autres lettres du mot si ce sont les mêmes que la première.
    # Elle prend en paramètre la liste de mot L ainsi que le nombre choisi au hasard dans le
    # fichier main: r et rend  une liste contenant la première lettre du mot et des "-" pour les 
    # autres lettres ainsi que le nombre de lettres révélés w.
    # On l'initialise à 2 car dans tous les cas on révèle la  première lettre et pour une raison 
    # que j'ignore len(L[r]) vaut 1 de plus que le nombre de lettres qu'elle contient réellement.
       
    w  = 2
    guess = list(L[r][0] + (len(L[r]) - 2) * "-")

    for i in range(len(L[r])):
        if L[r][i] == L[r][0].lower():
            guess[i] = guess[0].lower()
            w += 1

    return guess, w
    
    
def Game(guess, w, L, r): 
    # Fonction gèrant le jeu grâce à une boucle while, tant qu'on ne respecte pas la condition
    # de victoire (toutes les lettres ont été révélés donc w = len(L[r])) ou de défaite (loose
    # = 8 donc le joueur s'est trompé 8 fois) on continue de demander une lettre au joueur en 
    # enlevant ou non une chance au joueur selon si il s'est trompé ou non. Donc en ajoutant 1
    # ou non à loose.
    # Cettte fonction prend en paramètre la liste contenant le mot lorsqu'il est caché: guess,
    # une liste L contenant les lettres du mots, w la condition de victoire et r le nombre 
    # choisit au hasard dans le fichier main.
    # Elle retourne les conditions de victoire et de défaite ainsi que p qui compe le nombre de
    # lettres révélés par l'utilisateur.
    
    F = []                      # Liste contenant les lettres déjà utilisés fausses
    All = [L[r][0].lower()]     # Liste contenant toutes les lettres déjà utilisés
    Allowed_caracs = list('aàâbcçdeéèêfghiïjklmnoôpqrstuùûüvwxyz')
    p = 0
    loose = 0

    print(''.join(guess))
    
    while w < len(L[r]) and loose < 8:
        l = input("Veuillez saisisir une lettre svp: ")

        while l in All or len(l) != 1 or l not in Allowed_caracs:   # Sécurité de saisie
            if len(l) != 1:
                l = input('Veuillez entrez une seule lettre à la fois svp: ')
            elif l not in Allowed_caracs:
                l = input('Veuillez saisir un caractère valide svp: ')
            else:
                l = input('Vous avez déjà utilisé cette lettre veuillez en choisisr une autre: ')
        
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


def win_defeat(w, L, r): 
    # Fonction permettant au joueur de savoir si il a gagnè ou perdu sur sa dernière tentative
    # Pour cela elle vérifie si la condition de victoire (w = len[L[r]]) est bien atteinte
    # Elle prend donc logiquement en paramètre la condition de victoire, la lise de mot et le
    # nombre choisi au hasard dans le fichier main et retourne un message de victoire ou de 
    # défaite.

    if w == len(L[r]):
        print('Bravo vous avez deviné le mot!')
    else:
        print('Oh niiion vous avez perdu, le mot était:', L[r])


def Score(loose, p):
    # Cette fonction gère les scores du joueur et lui propose de rejouer une fois qu'il a 
    # réussi ou échouer à deviner le mot
    # Elle prend en paramètre loose qui compte le nombre d'erreur faites par l'utilisateur et 
    # p qui compte le nombre de lettres révélés par l'utilisateur.
    # L'utilisateur obtient 100 points par lettre deviné et en perd 10 par erreur si il ne 
    # partvient à deviner aucunes lettres il obtiend alors un score de 0

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
    

## Def des fonctions graphiques ##
def C_window():
    Window = Tk()
    Window.title('Jeu du pendu')
