from tkinter import *
import random

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("800x800")
        self.theCanvas = Canvas(self, width=800,height=800, bg="#AAAAFF") # The canvas will fill our window
        self.theCanvas.grid(row=1, column=0)                              # We will use it for all our interface
        
        self.theCanvas.bind("<Button>", self.clicked)
        self.theCanvas.bind("<Motion>", self.moved)

        self.mainloop() # this is needed to start checking for clicks
        

    def clicked(self,e):
        print(f"Clicked at {e.x},{e.y}")


    def moved(self,e):
        print(f"Moved to {e.x},{e.y}")


 

if __name__ == "__main__":
    app = App()
