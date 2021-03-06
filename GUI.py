from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import json

with open("personnage.json") as mon_fichier:
    data = json.load(mon_fichier)



class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
            self.w1.resizable(width=False, height=False)
            self.w1.configure(bg="blue")
            self.w1.title('Qui  Est - Ce ?')
           
        else:
            self.w1 = Frame(parent)
            
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.label1 = Label(self.w1, text = "Qui  Est - Ce ? ", font = tkinter.font.Font(family = "Showcard Gothic", size = 48, weight = "normal"),bg ='blue', cursor = "arrow", state = "normal")
        self.label1.pack()
        
        
        photo = PhotoImage(file =  r"C:\Users\Megaport\Documents\FAC\testProg\Jouer.png")
        self.button4 = Button(self.w1, image=photo,bg="blue",activebackground = "blue", highlightbackground="blue",)
        self.button4.place(x = 150, y = 260, width = 220, height = 102,)
        self.button4.image = photo
        self.button4['command'] = self.Jouer

        
        
        
        
        
        
        
    

    

    def Jouer(self):
        print('Jouer')
        

        
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
            self.w2 = Tk()
            
            self.w2.geometry('500x430')
            self.w2.resizable(width=False, height=False)
        else:
            self.w2 = Frame(parent)
            self.w2.place(x = 0, y = 0, width = 500, height = 450)
        
        
        
        
        self.check1 = Checkbutton(self.w2, text = "mode facile", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.check1.place(x = 410, y = 50, width = 90, height = 22)
        self.check1.deselect()
        self.check1['command'] = self.Mfacile
        self.check3 = Checkbutton(self.w2, text = "vs IA", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.check3.place(x = 410, y = 70, width = 90, height = 22)
        self.check3.deselect()
        self.check3['command'] = self.vsIA
        self.spin2 = Spinbox(self.w2, from_=1, to=5, increment = 1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin2.place(x = 410, y = 20, width = 30, height = 22)
        self.spin2['command'] = self.V1
        
        self.label1 = Label(self.w2, text = "X", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label1.place(x = 440, y = 20, width = 90, height = 22)
        self.spin3 = Spinbox(self.w2, from_ = 1, to = 5, increment = 1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin3.place(x = 450, y = 20, width = 40, height = 22)
        self.spin3['command'] = self.V2 
        self.label3 = Label(self.w2, text = "Nombre personnages", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 390, y = 0, width = 110, height = 22)
        self.button2 = Button(self.w2, text = "Nouvelle partie", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button2.place(x = 400, y = 90, width = 90, height = 22)
        self.button2['command'] = self.NouvellePartie
        self.button3 = Button(self.w2, text = "Abandonner la partie", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 390, y = 390, width = 110, height = 22)
        self.button3['command'] = self.Abandon
        self.combo4 = Combobox(self.w2, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo4.place(x = 0, y = 390, width = 230, height = 22)
        self.combo4['values'] = ("Question")
        self.combo4.current(0)
        self.combo4.bind("<<ComboboxSelected>>", self.QuestionBox)
        self.button4 = Button(self.w2, text = "oui", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4.place(x = 240, y = 390, width = 40, height = 22)
        self.button4['command'] = self.Roui
        self.button4_copy = Button(self.w2, text = "non", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4_copy.place(x = 280, y = 390, width = 40, height = 22)
        self.button4_copy['command'] = self.Rnon
        self.button6 = Button(self.w2, text = "Home", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button6.place(x = 0, y = 0, width = 40, height = 22)
        self.button6['command'] = self.Home
        # Reglage de la grille de jeu
        self.widget1 = Frame(self.w2)
        self.widget1.place(x = 10, y = 20, width = 380, height = 360)
        self.button4 = Button(self.widget1, text='Premiere Case du tableau Int??gr??', font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button4.grid(row=0, column=0, sticky="nsew")
        
        self.widget1.rowconfigure(self.spin2.get(), weight=1)
        self.widget1.columnconfigure(self.spin3.get(), weight=1)
	

    def Mfacile(self):
        print('Mfacile')

    def vsIA(self):
        print('vsIA')

    def V1(self):
        value1=self.spin2.get()
        print(value1)

    def V2(self):
        value2=self.spin3.get()
        print(value2)
    
    def NouvellePartie(self):
        self.w2.destroy()
        a = Widget2(0)

    def QuestionBox(self, e):
        print('QuestionBox')

    def Abandon(self):
        print('Abandon')

    def Roui(self):
        print('Roui')

    def Rnon(self):
        print('Rnon')
    
    def Home(self):
        print('Home')

        self.w2.destroy()
        a = Widget1(0)
        a.w2.mainloop()
        print('Home')
        
     

a = Widget2(0)
a.w2.mainloop()
