## Appel des librairies ##
from tkinter import Tk, Canvas

## Definition de la classe  window ##

class window():
    def __init__(self, wi, h, r, c):
        self.w = Tk()
        
        self.canevas = Canvas(self.w, width = wi, height = h, bg = "white")

        self.wi = wi
        self.h = h
        self.r = r
        self.c = c
        

    def windowDivision(self):
        self.w.geometry("3500x1650")
        self.w.title("Chests game")

        self.canevas.grid(row = 0, column = 1)


    def grid(self):
        color = 0
        for i in range(self.r):
            color += 1

            for j in range(self.c):
                color += 1
                
                if color % 2 == 0:
                    self.canevas.create_rectangle(i*self.wi/8,  j*self.h/8, (i+1)*self.wi/8, (j+1)*self.h/8, fill = "white")  
                else:
                    self.canevas.create_rectangle(i*self.wi/8,  j*self.h/8, (i+1)*self.wi/8, (j+1)*self.h/8, fill = "black")  

        

    def mainLoop(self):    
        self.w.mainloop()

    
        