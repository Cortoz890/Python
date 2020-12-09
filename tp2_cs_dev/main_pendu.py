### Objectifs: Créer une dernière version du jeu de pendu avec interface graphique###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: finir l'interface graphique ###
### Lien git Hub: https://github.com/Cortoz890/Python###


## Importation des modules/fonctions ##

import random
import f_pendu


## Variables globales ##
file = open("mots.txt")
ran = random.randint(0, 193)
F = []       # Liste contenant les lettres déjà utilisés fausses
All = []

## Programme principal ##
txt = f_pendu.Find_word(file)
hide = f_pendu.Word_to_guess(txt, ran, All)


f_pendu.C_window(hide[0], txt, ran, hide[1], F)


#result = f_pendu.Game(hide[0], hide[1], txt, ran)
#f_pendu.win_defeat(result[0], txt, ran)

#f_pendu.Score(result[1], result[2])
