## Appel des fonctions/librairies ##
from pawn import pawn

## Def des variables ##
height = 1600
width = 1600

rows = 8
columns = 8


## Programme principal ##
p = pawn(width, height, rows, columns)

p.windowDivision()
p.grid()
p.figures()

p.move()
p.mainLoop()