### Objectifs: Créer une dernière version du jeu de pendu avec interface graphique###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: finir l'interface graphique ###
### Lien git Hub: ###


## Importation des modules/fonctions ##
import random
import f_pendu


## Variables globales ##
file = open("mots.txt")

ran = random.randint(0, 193)


## Programme principal ##
txt = f_pendu.Find_word(file)
hide = f_pendu.Word_to_guess(txt, ran)


f_pendu.C_window(hide, txt, ran)


#result = f_pendu.Game(hide[0], hide[1], txt, ran)
#f_pendu.win_defeat(result[0], txt, ran)

#f_pendu.Score(result[1], result[2])
