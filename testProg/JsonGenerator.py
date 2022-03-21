from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font
import tkinter.filedialog
import json




class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('540x490')
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 540, height = 490)
        ###### PLACEMENT DE TOUS LES "Widjets" ##########
        fichier = open("personnage.Json", "w")
        print(fichier)
        self.label1 = Label(self.w1, text = "Json Generator", font = tkinter.font.Font(family = "Arial Rounded MT Bold", size = 28), cursor = "arrow", state = "normal")
        self.label1.place(x = 110, y = 20, width = 290, height = 82)
        self.label2 = Label(self.w1, text = "nombre de personnages :", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 40, y = 120, width = 130, height = 22)
        self.label3 = Label(self.w1, text = "nombre d'attributs:", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 40, y = 150, width = 100, height = 22)
        self.button3 = Button(self.w1, text = "Done", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 320, y = 150, width = 90, height = 22)
        self.button3['command'] = self.BaseDone
        
        self.spin1 = Spinbox(self.w1, from_ = 1, to = 10, increment = 1,font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin1.place(x = 160, y = 150, width = 40, height = 22)
        self.spin1['command'] = self.SpinAttribut
        self.spin2 = Spinbox(self.w1, from_ = 0, to = 99, increment = 1,font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin2.place(x = 170, y = 120, width = 40, height = 22)
        self.spin2['command'] = self.SpinPersonnages
        self.combo1 = Combobox(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo1.place(x = 40, y = 220, width = 110, height = 22)
        self.combo1['values'] = ("Attributs")
        self.combo1.current(0)
        self.combo1.bind("<<ComboboxSelected>>", self.ComboAttribut)
        self.label5 = Label(self.w1, text = "nombre de réponse :", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label5.place(x = 160, y = 220, width = 110, height = 22)
        self.spin3 = Spinbox(self.w1, from_ = 0, to = 99, increment = 1, value = 0, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin3.place(x = 270, y = 220, width = 40, height = 22)
        self.spin3['command'] = self.Nreponse
        self.button2 = Button(self.w1, text = "Done", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button2.place(x = 320, y = 220, width = 90, height = 22)
        self.button2['command'] = self.AttributDone
        self.label6 = Label(self.w1, text = "Attribut configurator", font = tkinter.font.Font(family = "MS Reference Sans Serif", size = 8), cursor = "arrow", state = "normal")
        self.label6.place(x = 40, y = 190, width = 370, height = 22)
        self.combo2 = Combobox(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo2.place(x = 120, y = 290, width = 110, height = 22)
        self.combo2['values'] = ("Attributs")
        self.combo2.current(0)
        self.combo2.bind("<<ComboboxSelected>>", self.ComboAttribut)
        self.label8 = Label(self.w1, text = "réponse :", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label8.place(x = 230, y = 290, width = 110, height = 22)
        self.combo4 = Combobox(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo4.place(x = 340, y = 290, width = 90, height = 22)
        self.combo4['values'] = ("reponse")
        self.combo4.current(0)
        self.combo4.bind("<<ComboboxSelected>>", self.Reponse)
        self.button3 = Button(self.w1, text = "Done", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button3.place(x = 450, y = 290, width = 90, height = 22)
        self.button3['command'] = self.PersoDone
        self.label7 = Label(self.w1, text = "Personnage configurator", font = tkinter.font.Font(family = "MS Reference Sans Serif", size = 8), cursor = "arrow", state = "normal")
        self.label7.place(x = 50, y = 260, width = 370, height = 22)
        self.combo3 = Combobox(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.combo3.place(x = 10, y = 290, width = 90, height = 22)
        self.combo3['values'] = ("prenom")
        self.combo3.current(0)
        self.combo3.bind("<<ComboboxSelected>>", self.Prenom)
        self.label9 = Label(self.w1, text = "Nombre d'attribut édités : ", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label9.place(x = 0, y = 430, width = 130, height = 22)
        self.label10 = Label(self.w1, text = "Nombre de personnages édités:", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label10.place(x = 0, y = 460, width = 160, height = 22)
        self.button5 = Button(self.w1, text = "crée le fichier", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button5.place(x = 360, y = 420, width = 150, height = 52)
        self.button5['command'] = self.JsonDone
        ############# barre progressive a coder ######################
        self.hprogress1 = Progressbar(self.w1, maximum = 100, cursor = "arrow")
        self.hprogress1.place(x = 155, y = 430, width = 110, height = 22)
        self.hprogress1['value'] = 0
        self.hprogress2 = Progressbar(self.w1, maximum = 100, cursor = "arrow")
        self.hprogress2.place(x = 155, y = 460, width = 110, height = 22)
        self.hprogress2['value'] = 0
        
    ##########Definition des fonctions relatives aux labels #################
    def SpinAttribut(self):
        print('SpinAttribut')
    def SpinPersonnages(self):
        print('SpinPersonnages')
    def ComboAttribut(self, e):
        print('ComboAttribut')

    def Nreponse(self):
        print('Nreponse')

    def AttributDone(self):
        print('AttributDone')
    def PersoDone(self):
        print('PersoDone')
    def Prenom(self, e):
        print('Prenom')
    def Reponse(self, e):
        print("Reponse")
    def BaseDone(self):
        print('BaseDone')
    def JsonDone(self):
        fileName = "personnage.json"
        jsonObject = {
    "images": "personnages/",
    "ligne":"3",
    "colonne":"8",
    "nbCara":"", #a remplir#
    
    "caracteristique": [
        ####a remplir####
        ],
        
   
    "possibilites": [
        ####a remplir####
        
        
        
        
        ]}


        file = open(fileName, "w")
        json.dump(jsonObject, file)
        file.close()
        
        

a = Widget1(0)
a.w1.mainloop()