# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:14:38 2020

@author: corto
"""

def mesImpots(revenus):
    "Cette fonction calcule le montant de l'impôt sur le revenu d'une personne seule"
    "Entrée: revenus généré par une personne en un an"
    "Sortie: montant de l'impôt sur le revenu d'une personne seule"
    impots = 0;
    if revenus < 9964:
        impots = 0
        
    elif  9964 <= revenus < 27519:
        impots += (revenus - 9964)*(14/100)
        
    elif 27519 <= revenus < 73779:
        impots += (revenus - 27519)*(30/100) + (27519 - 9964)*(14/100)
        
    elif 73779 <= revenus < 156244:
        impots += (revenus - 73779)*(41/100) + (73779 - 27519)*(30/100) + (27519 - 9964)*(14/100)