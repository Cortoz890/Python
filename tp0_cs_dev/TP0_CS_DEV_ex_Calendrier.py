# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

### Objectif: réaliser exo Calendrier TP0 CS-DEV ###
### Date de réalisation: 23/11/2020 ###
### Par Deschamps Corto ###
### To do : questions 3  et 4 ###


## Apportation des fonctions ##
from f_cal import Check_bissextile

## Variables globales ##
Y = int(input("Saisissez l'année de la date que vous souhaitez tester sous forme de chiffres svp: "))

#m = int(input("Saisissez l'année de la date que vous souhaitez tester sous forme de chiffres svp: "))

#d = int(input("Saisissez l'année de la date que vous souhaitez tester sous forme de chiffres svp: "))

#date = [d, m, Y]



def Check_month(Year, month):
    "Cette fonction permet compter le nbr de jours dans un mois après avoir vérifié si le mois existait"
    "sortie: nbr de jours dans le mois donné"
    
    
    L30 = [1, 3, 5, 7, 8, 10, 12]
    L31 = [4, 6, 9, 11]
    
    if month in L30:
        print("Ce mois est en 30 jours")
        
    elif month in L31:
        print("Ce mois est en 31 jours")
    
    elif Check_bissextile(Y) == True and month == 2:
        print("Ce mois est en 29 jours")
        
    else:
        print("Ce mois est en 28 jours")
        
   
## Programme principal ##     
print(Check_bissextile(Y))

#Check_month(Y, m)
