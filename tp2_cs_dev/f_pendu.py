### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: mettre l'image/ score/ sécurité de saisie ###


## Importation des modules ##
from tkinter import Tk, Label, Button, Entry, Canvas, DISABLED, NORMAL, END


## Variables globales ##
Loose = 0
F = []        # Liste contenant les lettres déjà utilisés fausses
w = 2


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
       
    global w

    guess = list(L[r][0] + (len(L[r]) - 2) * "-")

    for i in range(len(L[r])):
        if L[r][i] == L[r][0].lower():
            guess[i] = guess[0].lower()
            w += 1

    return guess



def Game(guess, L, r): 
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
    
    global Loose, F, w
    
    All = [L[r][0].lower()]     # Liste contenant toutes les lettres déjà utilisés
    Allowed_caracs = list('aàâbcçdeéèêfghiïjklmnoôpqrstuùûüvwxyz')
    p = 0
    
    l = letter.get()
        
    All.append(l)

    if l not in L[r]:
        F.append(l)
        Loose += 1
        end_txt = ['Il vous reste ', str(8-Loose),' tentatives. Vous avez déjà essayé les lettres: ', str(F)]
        letter.delete(0, END)
        if Loose == 8:
            Label_end.configure(text = "Vous n'avez plus de tentatives.")
        else:
            Label_end.configure(text = ''.join(end_txt))
            
    for i in range(len(L[r])):
        if l == L[r][i]:
            guess[i] = L[r][i]
            letter.delete(0, END)
            w += 1
            p += 1
    

    Label_hide.configure(text = ''.join(guess))
    print(w)
    return w, p, Loose




def win_defeat(L, r): 
    # Fonction permettant au joueur de savoir si il a gagnè ou perdu sur sa dernière tentative
    # Pour cela elle vérifie si la condition de victoire (w = len[L[r]]) est bien atteinte
    # Elle prend donc logiquement en paramètre la condition de victoire, la lise de mot et le
    # nombre choisi au hasard dans le fichier main et retourne un message de victoire ou de 
    # défaite.
    
    global w

    loose_txt = ['Oh niiion vous avez perdu, le mot était: ', L[r]]
    if w == len(L[r]):
        Label_end.configure(text = 'Bravo vous avez deviné le mot!')   
        Button_try['text'] = 'Rejouer'
        Button_try['command']  = ''
         

    elif w != len(L[r]) and Loose == 8:
        Label_end.configure(text = ''.join(loose_txt))
        Button_try['text'] = 'Rejouer'
        Button_try['command']  =  ''
        

def Score(loose, p):
    # Cette fonction gère les scores du joueur
    # Elle prend en paramètre loose qui compte le nombre d'erreur faites par l'utilisateur et 
    # p qui compte le nombre de lettres révélés par l'utilisateur.
    # L'utilisateur obtient 100 points par lettre deviné et en perd 10 par erreur si il ne 
    # partvient à deviner aucunes lettres il obtiend alors un score de 0

    if p == 0:
        s = 0
    else:
        s = 100*p - 10*loose
    print('Votre score est:', s)
    

## Def des fonctions graphiques ##
def C_window(guess, L, r):
    # Fonction créant la fenêtre de jeu pour le pendu
    
    global Label_hide, Label_help, Label_end, letter, Button_try
    
    Window = Tk()
    Window.geometry('900x300')
    Window.title('Jeu du pendu')

    Label_hide = Label(Window, text = ''.join(guess), fg = 'black')
    Label_hide.grid(row = 0, column = 1)

    Label_help = Label(Window, text = 'Veuillez saisir une lettre svp:', fg = 'blue')
    Label_help.grid(row = 1, column = 0)

    Label_end = Label(Window, text = '', fg = 'black')
    Label_end.grid(row = 2, column = 1)

    letter = Entry(Window, textvariable = str)
    letter.grid(row = 1, column = 1)

    Picture = Canvas(Window, width = 200, height = 200,  bg ='white')
    Picture.grid(row = 0, column = 4)

    Button_try = Button(Window, text = 'Proposer', command = lambda:[Game(guess, L, r), win_defeat(L, r)], state = NORMAL)
    Button_try.grid(row = 1, column = 2)

    Button_leave = Button(Window, text = 'Quitter', command = Window.destroy)
    Button_leave.grid(row = 1, column = 3)
    
    Window.mainloop()   