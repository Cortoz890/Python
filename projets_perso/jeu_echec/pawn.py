## Appel des bibliothèques ##
from window import window
from tkinter import Canvas

## Création de la classe pawn ##

class pawn(window):
    def __init__(self, wi, h, r, c):
        window.__init__(self, wi, h, r, c) 
        self.p_white = []
        self.p_black = []

    
    def figures(self):
        self.canevas.tag_raise("A")
        for i in range(8):
            self.p_white.append(self.canevas.create_oval(i*self.wi/8 , self.h/8, (i+1)*self.wi/8, self.h/4, fill = "white", outline = "black"))
            self.p_black.append(self.canevas.create_oval(i*self.wi/8 , self.h*(6/8), (i+1)*self.wi/8, self.h*(7/8), fill = "black", outline = "white"))

    
    def coords(self, event):
        x = event.x
        y = event.y
        print(x, y)

    
    def move(self):
        self.canevas.bind("<Button-1>", self.coords)
