from pickle import FALSE
import tkinter as Tk

from model import Model
from view import View

class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root, self.model)

    def run(self):
        self.root.title("PROYECTO 1 CORTE 1")
        self.root.deiconify()
        self.root.mainloop()