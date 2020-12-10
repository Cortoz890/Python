### Objectifs: créer les fonctions utiles pour le jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: rendre l'affichage des scores beau/changer les commentaires plus d'actualités ###


## Importation des modules ##
from tkinter import Tk, Label, Button, Entry, Canvas, DISABLED, NORMAL, END, PhotoImage 
import random

## Variables globales ##
Loose = 0   # Compteur de la condition de défaite
w = 2       # Compteur de la condition de victoire # On initialise à 2 car dans tous les cas on révèle la  première lettre et pour une raison      que j'ignore len(L[r]) vaut 1 de plus que le nombre de lettres qu'elle contient réellement
p = 0       # Compteur de nombres de lettres révélés
 
## Def des fonctions utiles au jeu ##
def Find_word(f):
    # Fonction prenant en parramétre un fichier f contenant les mots pour jouer au pendu. 
    # Retourne une liste contenant tous les mots danns le fichier f.       
    
    L = []
    for i in f:
        L.append(i)
    f.close()

    return L
    

def Word_to_guess(L, r, al):
    # Cette fonction permet de cacher les lettres du mots choisi au hasard sauf la première et
    # révèle d'autres lettres du mot si ce sont les mêmes que la première.
    # Elle prend en paramètre la liste de mot L, le nombre choisi au hasard dans le
    # fichier main: r ainsi que la liste al qui contiendra tous les caractères rentrés par l'utilisateur  
    # Rend  une liste contenant la première lettre du mot et des "-" pour les autres lettres. 
    
       
    global w 

    guess = list(L[r][0] + (len(L[r]) - 2) * "-")
    al.append(L[r][0].lower())

    for i in range(len(L[r])):
        if L[r][i] == L[r][0].lower():
            guess[i] = guess[0].lower()
            w += 1

    return guess, al


def Game(guess, L, r, l, f): 
    # Fonction gèrant le jeu grâce, tant qu'on ne respecte pas la condition
    # de victoire (toutes les lettres ont été révélés donc w = len(L[r])) ou de défaite (loose
    # = 8 donc le joueur s'est trompé 8 fois) on continue de demander une lettre au joueur en 
    # enlevant ou non une chance au joueur selon si il s'est trompé ou non. Donc en ajoutant 1
    # ou non à loose.
    # Cettte fonction prend en paramètre la liste contenant le mot lorsqu'il est caché: guess,
    # une liste L contenant les lettres du mots, r le nombre choisit au hasard dans le
    # fichier main, l la lettre rentré par l'utilisateur et f la liste contenant les lettres 
    # fausses rentrés par l'utilisateur.
    
    global Loose, w, p
    
    letter.delete(0, END)

    if l not in L[r]:
        f.append(l)
        Loose += 1
        item = Canevas.create_image(140, 140, anchor = 'center', image = Pictures[Loose - 1])
        end_txt = ['Vous avez déjà essayé les lettres: ', ', '.join(f)]
        if Loose == 8:
            Label_end.configure(text = "Vous n'avez plus de tentatives.")
        else:
            Label_end.configure(text = ''.join(end_txt))
            
    for i in range(len(L[r])):
        if l == L[r][i]:
            guess[i] = L[r][i]
            w += 1
            p += 1
    
    Label_hide.configure(text = ''.join(guess))
    

def Security(guess, L, r, al, f):
    # Fonction vérifiant si ce que rentre l'utilisateur est bien une lettre qu'il n'a pas déjà
    # saisi et exécute la fonction de jeu si la lettre est valide.
    # Prent en paramètre la liste contenant le mot caché guess, la liste de tous les mots du 
    # fichier texte L, le nombre choisi au hasard r ,al la liste contenant toutes les lettres
    # déjà saisi par l'utilisateurs et f la liste contenant toutes les lettres fausses déjà 
    # rentrés par l'utilisateur.  

    Allowed_caracs = list('aàâbcçdeéèêfghiïjklmnoôpqrstuùûüvwxyz')
    let = letter.get()
    letter.delete(0, END)
    
    Label_help.configure(text = 'Veuillez saisir une letre svp: ')
    if len(let) != 1:
        Label_help.configure(text = 'Veuillez saisir une lettre à la fois: ')
    elif let not in Allowed_caracs:
        Label_help.configure(text = 'Veuillez saisir un caractère valide: ')
    elif let in al:
        Label_help.configure(text = "Veuillez saisir une lettre que vous n'avez pas déjà utilisé: ")
    else:
        al.append(let)
        Game(guess, L, r, let, f)


def Reload(L, scores):
    # Fonction servant à relancer la partie une fois qu'on appuie sur le boutton rejouer
    # Pour cela elle remet les différents éléments de l'interface graphique comme ils étaient 
    # avant que l'utilisateur commmence sa partie et prend un nouveau mot dans L en prenant
    # un nouveau nombre aléatoire que l'on place en paramètre de Word_to_guess pour obtenir
    # la listecontenant le nouveau mot caché.
    # Le parmètre scores est une liste stockant les scores des différentes parties 

    global Loose, w, p

    Loose = 0
    w = 2
    p = 0
    r = random.randint(0, 193)

    al = []
    f = []

    item = Canevas.create_image(140, 140, anchor = 'center', image = Pictures[7])

    Label_end.configure(text = '')
    Label_score_message.configure(text = '')
    Label_scores.configure(text = '')

    guess = Word_to_guess(L, r, al)[0]

    Label_hide.configure(text = ''.join(guess))

    Button_try['text'] = 'Proposer'
    Button_try['command']  =  lambda:[Security(guess, L, r, al, f), Win_defeat(L, r, scores), Score(L,r,scores)]


def Win_defeat(L, r, scores): 
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
        Button_try['command']  = lambda:[Reload(L, scores)]
    elif w != len(L[r]) and Loose == 8:
        Label_end.configure(text = ''.join(loose_txt))
        Button_try['text'] = 'Rejouer'
        Button_try['command']  =  lambda:[Reload(L, scores)]


def Score(L, r, scores):
    # Cette fonction gère les scores du joueur
    # Elle prend en paramètre loose qui compte le nombre d'erreur faites par l'utilisateur et 
    # p qui compte le nombre de lettres révélés par l'utilisateur.
    # L'utilisateur obtient 100 points par lettre deviné et en perd 10 par erreur si il ne 
    # partvient à deviner aucunes lettres il obtiend alors un score de 0
    global Loose, p
    
    if w == len(L[r]) or Loose == 8:
        if p == 0:
            s = 0
        else:
            s = 100*p - 10*Loose

        scores.append(str(s))

        txt_score_message = 'Votre score est de ', str(s),' points'
        txt_score = 'Vos précédent score sont: ', '/ '.join(scores[:-1])

        
        Label_score_message.configure(text = ''.join(txt_score_message))
        
        if len(scores) > 1:
            Label_scores.configure(text = ''.join(txt_score))          


## Def des fonctions graphiques ##
def C_window(guess, L, r, al, f, scores):
    # Fonction créant la fenêtre de jeu pour le pendu

    global Label_hide, Label_help, Label_end, letter, Canevas, Pictures, item, Button_try,  Label_score_message, Label_scores
    
    Window = Tk()
    Window.geometry('2400x500')
    Window.title('Jeu du pendu')

    Label_hide = Label(Window, text = ''.join(guess), fg = 'black')
    Label_hide.grid(row = 0, column = 1)
    Label_hide.configure(font = 30)

    Label_help = Label(Window, text = 'Veuillez saisir une lettre svp:', fg = 'blue')
    Label_help.grid(row = 1, column = 0)
    Label_help.configure(font = 30)

    Label_end = Label(Window, text = '', fg = 'black')
    Label_end.grid(row = 2, column = 1)
    Label_end.configure(font = 30)

    Label_score_message = Label(Window, text = '', fg = 'black')
    Label_score_message.grid(row = 3, column = 1)
    Label_score_message.configure(font = 30)

    Label_scores = Label(Window, text = '', fg = 'black')
    Label_scores.grid(row = 4, column = 1)
    Label_scores.configure(font = 30)

    letter = Entry(Window, textvariable = str)
    letter.grid(row = 1, column = 1)
    letter.configure(font = 10)

    Pictures = [PhotoImage(file = 'bonhomme1.gif'), PhotoImage(file = 'bonhomme2.gif'), PhotoImage(file = 'bonhomme3.gif'), PhotoImage(file = 'bonhomme4.gif'), PhotoImage(file = 'bonhomme5.gif'), PhotoImage(file = 'bonhomme6.gif'), PhotoImage(file = 'bonhomme7.gif'), PhotoImage(file = 'bonhomme8.gif')]

    Canevas = Canvas(Window, width = 280, height = 280,  bg ='white')
    Canevas.grid(row = 0, column = 4)
    item = Canevas.create_image(140, 140, anchor = 'center', image = Pictures[7])
       
    Button_try = Button(Window, text = 'Proposer', command = lambda:[Security(guess, L, r, al, f), Win_defeat(L, r, scores), Score(L,r, scores)])
    Button_try.grid(row = 1, column = 2)
    Button_try.configure(font = 20)

    Button_leave = Button(Window, text = 'Quitter', command = Window.destroy)
    Button_leave.grid(row = 1, column = 3)
    Button_leave.configure(font = 20)
    
    Window.mainloop()   