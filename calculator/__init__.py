import tkinter as tk
from .controls import Display

WIDTH = 272
HEIGHT = 300

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        display = Display(self)
        display.pack()

        display.typing("probando")