## Définition des fonctions ##   
def Check_bissextile(Year):
   "Cette fonction permet de tester si une année est bissextile ou non"
   "sortie: True or False"
   
   if Year % 100 == 0 and Year % 4 == 0:
       return True
                                                                               
   elif int(Year) % 400 == 0:
       return True
       
   else:
       return False

