from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font


class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.label1 = Label(self.w1, text = "Qui-est-ce?", font = tkinter.font.Font(family = "MS PGothic", size = 45), cursor = "arrow", state = "normal")
        self.label1.place(x = 110, y = 30, width = 310, height = 132)
        self.button1 = Button(self.w1, text = "Jouer", font = tkinter.font.Font(family = "Pristina", size = 28), cursor = "arrow", state = "normal")
        self.button1.place(x = 150, y = 260, width = 220, height = 102)
        self.button1['command'] = self.Jouer

    

    def Jouer(self):
        print('Jouer')

        self.label1.place(x = 180, y = 40, width = 170, height = 132)
        self.button1 = Button(self.w1, text = "Jouer", font = tkinter.font.Font(family = "Pristina", size = 28, weight = "normal"), cursor = "arrow", state = "normal")
        self.button1.place(x = 150, y = 260, width = 220, height = 102)
        self.button1['command'] = self.Jouer
        self.w1.destroy()
        a = Widget2(0)
        a.w1.mainloop()
        

    

a = Widget1(0)
a.w1.mainloop()

class Widget2():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.check1 = Checkbutton(self.w1, text = "mode facile", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.check1.place(x = 410, y = 50, width = 90, height = 22)
        self.check1.deselect()
        self.check1['command'] = self.Mfacile
        self.check3 = Checkbutton(self.w1, text = "vs IA", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.check3.place(x = 410, y = 70, width = 90, height = 22)
        self.check3.deselect()
        self.check3['command'] = self.vsIA
        self.spin2 = Spinbox(self.w1, from_ = 1, to = 5, increment = 1, value = 1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin2.place(x = 410, y = 20, width = 30, height = 22)
        self.spin2['command'] = self.V1
        self.label1 = Label(self.w1, text = "X", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label1.place(x = 440, y = 20, width = 90, height = 22)
        self.spin3 = Spinbox(self.w1, from_ = 1, to = 5, increment = 1, value = 1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin3.place(x = 450, y = 20, width = 40, height = 22)
        self.spin3['command'] = self.V2
        self.label3 = Label(self.w1, text = "Nombre personnages", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 390, y = 0, width = 110, height = 22)
        self.button2 = Button(self.w1, text = "Nouvelle partie", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button2.place(x = 400, y = 90, width = 90, height = 22)
        self.button2['command'] = self.NouvellePartie
        self.button3 = Button(self.w1, text = "Abandonner la partie", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 390, y = 390, width = 110, height = 22)
        self.button3['command'] = self.Abandon
        self.combo4 = Combobox(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo4.place(x = 0, y = 390, width = 230, height = 22)
        self.combo4['values'] = ("Question")
        self.combo4.current(0)
        self.combo4.bind("<<ComboboxSelected>>", self.QuestionBox)
        self.button4 = Button(self.w1, text = "oui", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4.place(x = 240, y = 390, width = 40, height = 22)
        self.button4['command'] = self.Roui
        self.button4_copy = Button(self.w1, text = "non", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4_copy.place(x = 280, y = 390, width = 40, height = 22)
        self.button4_copy['command'] = self.Rnon
        self.button6 = Button(self.w1, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button6.place(x = 0, y = 0, width = 40, height = 22)
        self.button6['command'] = self.Home
	

    def Mfacile(self):
        print('Mfacile')

    def vsIA(self):
        print('vsIA')

    def V1(self):
        print('V1')

    def V2(self):
        print('V2')

    def NouvellePartie(self):
        print('NouvellePartie')

    def QuestionBox(self, e):
        print('QuestionBox')

    def Abandon(self):
        print('Abandon')

    def Roui(self):
        print('Roui')

    def Rnon(self):
        print('Rnon')
    
    def Home(self):
        self.w1.destroy()
        a = Widget1(0)
        a.w1.mainloop()
        print('Home')

a = Widget2(0)
a.w1.mainloop()