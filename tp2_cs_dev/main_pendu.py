### Objectifs: créer une première version du jeu de pendu ###
### Date de réalitsation: 30/11/2020 ###
### Créateur: Deschamps Corto ###
### À faire: version plus avancé du pendu ###

## Importation des modules/fonctions ##
import random
import f_pendu

## Variables globales ##
file = open("mots.txt")

ran = random.randint(0, 193)
win = 2

## Programme principal ##
txt = f_pendu.Find_word(file)
hide = f_pendu.Word_to_guess(txt, ran)


result = f_pendu.Game(hide[0], hide[1], txt, ran)
f_pendu.win_defeat(hide, result, txt, ran)