from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.messagebox
import tkinter.font
import tkinter.filedialog
import json

# Utiliser "sort_keys=True" pour trier par ordre croissant...


class Widget1():
    def __init__(self, parent):
        self.gui(parent)
        

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('540x490')
            self.w1.title("Generateur Json")
            self.w1.resizable(width=False, height=False)
        else:
            self.w1 = Frame(parent)
            self.w1.place(x = 0, y = 0, width = 540, height = 490)
        self.data = {
            "ligne":"",
            "colonne":"",
            "possibilites":[]
        }
        with open('write.json','w') as monfichier:
            json.dump(self.data, monfichier, indent=4)

        self.li=[]      # Liste qui contiendra les Types d'attributs (par ex : nom, fichier...)
        self.li2=[]     # Liste qui contiendra les Valeurs d'attributs
        self.var=0      # Variable qui sert de repère afin de guider l'utilisateur dans la navigation (càd lorsqu'il appuie sur le bouton "Completer l'objet N°...)        
        self.nbElement=0    # On l'initialise a la taille de la grille (ligne x colonne) afin de connaitre le nombre d'objet au total
        ###### PLACEMENT DE TOUS LES "Widjets" ##########
        self.label1 = Label(self.w1, text = "Json Generator", font = tkinter.font.Font(family = "Arial Rounded MT Bold", size = 28), cursor = "arrow", state = "normal")
        self.label1.place(x = 110, y = 20, width = 290, height = 82)
        self.label2 = Label(self.w1, text = " Nombre de lignes ", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 40, y = 120, width = 130, height = 22)
        self.label3 = Label(self.w1, text = "  Nombre de colonnes  ", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 50, y = 150, width = 100, height = 22)
        self.button3 = Button(self.w1, text = "Validation grille", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
        self.button3.place(x = 320, y = 150, width = 150, height = 30)
        self.button3['command'] = self.valideGrille
        self.spin2 = Spinbox(self.w1, from_ = 0, to = 6, increment = 1,font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin2.place(x = 160, y = 150, width = 40, height = 22)
    
        self.spin1 = Spinbox(self.w1,from_ = 0, to = 10, increment = 1,font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.spin1.place(x = 170, y = 120, width = 40, height = 22)
        

        self.label6 = Label(self.w1, text = "Liste des attributs", font = tkinter.font.Font(family = "MS Reference Sans Serif", size = 10), cursor = "arrow", state = "normal")
        self.label6.place(x = 40, y = 190, width = 370, height = 22)
        self.btnPlus1 = Button(self.w1, text = "+1", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.btnPlus1.place(x = 140, y = 220, width = 50, height = 22)
        self.btnPlus1['command'] = self.plusUn
        self.btnMoins1 = Button(self.w1, text = "-1", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.btnMoins1.place(x = 200, y = 220, width = 50, height = 22)
        self.btnMoins1['command'] = self.moinsUn
        self.entryAttr = Entry(self.w1, cursor = "arrow", state = "normal")
        self.entryAttr.place(x = 140, y = 250, width = 170, height = 22)

        self.label7 = Label(self.w1, text = "Valeurs des attributs", font = tkinter.font.Font(family = "MS Reference Sans Serif", size = 10), cursor = "arrow", state = "normal")
        self.label7.place(x = 50, y = 280, width = 370, height = 22)

        self.cbb = Combobox(self.w1, values=self.li)
        self.cbb.place(x = 110, y = 310, width = 120, height = 22)

        self.entryVal = Entry(self.w1, cursor = "arrow", state = "normal")
        self.entryVal.place(x = 250, y = 310, width = 120, height = 22)

        self.ValiderAtt = Button(self.w1, text = "Valider", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
        self.ValiderAtt.place(x = 300, y = 340, width = 90, height = 30)
        self.ValiderAtt['command']=self.valAtt

        self.cplObj = Button(self.w1, text ="Completer l'objet N°"+str(self.var+1), font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.cplObj.place(x = 300, y = 380, width = 200, height = 30)
        self.cplObj['command']=self.completeObj

        self.test = Button(self.w1, text="Tester la cohérence de votre fichier json", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
        self.test.place(x = 30, y = 420, width = 250, height = 30)
        self.test['command']=self.testJson

    def testJson(self):         
        cmt1=0      # Ces deux valeurs servent de repère, afin de lancer le bon type d'erreur
        cmt2=0
        a=0
        if(self.nbElement>0):
            for j in self.data["possibilites"]:
                for k in self.li:
                    if(str(j[str(k)])=="vide" or str(j[str(k)])=="" or j[str(k)]==None):
                        cmt1=1
                while(a<0):
                    if(j.values()==self.data["possibilites"][a].values()):
                        cmt2+=1
                    a+=1
            if(cmt1==1):
                tkinter.messagebox.showerror("Erreur","Attention, certains attributs sont vides !",parent=self.w1)
            if(cmt2>1):
                tkinter.messagebox.showerror("Erreur","Au moins deux objets sont equivalents",parent=self.w1)
            if(cmt1==0 and cmt2==0):
                tkinter.messagebox.showinfo("Bravo !","Votre fichier json est cohérent",parent=self.w1)
        else:
            tkinter.messagebox.showwarning("Attention","Votre grille contient aucun personnage...",parent=self.w1)
                                    
    def backObj(self): # Cette fonction permet de retourner en arrière en soustrayant 1 à self.var...
        if(self.var!=0):
            self.var-=1
            self.cplObj=Button(self.w1, text="Completer votre objet N°"+str(self.var+1), font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
            self.cplObj.place(x = 300, y = 380, width = 200, height = 30)
            self.cplObj['command']=self.completeObj
        else:
            self.backObjet.destroy()

    def completeObj(self):
        liDict=dict(zip(self.li,self.li2))      # On créer un dict tel que pour chaque clef self.li on lui attribue une valeur self.li2 (ce sont les "restes" de la fonction validerAtt, càd les vals que l'utilisateur a entrées)
        print(liDict)
        self.data["possibilites"][self.var]=liDict # On initialise l'objet a l'indice self.var (le compteur...) les valeurs que l'utilisateur entre
        if(self.var<self.nbElement): # On est loins de déborder sur les indices...
            self.var+=1   
            if(self.var==self.nbElement): # Si jamais on est le dernier objets+1 càd self.data["possibilites"][self.nbElement] alors on enleve 1 à self.var afin de faire du "surplace"
                self.var-=1   
            self.cplObj=Button(self.w1, text="Completer votre objet N°"+str(self.var+1), font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
            self.cplObj.place(x = 300, y = 380, width = 200, height = 30)
            self.cplObj['command']=self.completeObj
        if(self.var>0): # Il est maintenant possible de pouvoir revenir en arrière car cela signifie qu'on a déjà initialisé self.data["possibilites"][0]
            self.backObjet = Button(self.w1, text="Retour à l'objet précédent", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal")
            self.backObjet.place(x = 300, y=420, width = 200, height = 30)
            self.backObjet['command']=self.backObj
        with open('write.json','w') as monfichier:
            json.dump(self.data, monfichier, indent=4)
        for i in range(0,len(self.li2)): # On n'oublie pas de reset les valeurs du tableau self.li2 qui va pouvoir nous servir a compléter le prochain objet...
             self.li2[i]="vide"
        
    def valideGrille(self):
        self.data["possibilites"]=[] # Afin que l'utilisateur puisse revenir sur les dimensions de la grille en cas d'erreur/oublie... 
        self.data["ligne"]=self.spin1.get()
        self.data["colonne"]=self.spin2.get()
        self.nbElement=int(self.spin1.get())*int(self.spin2.get()) # C'est ici que l'on initialise self.nbElement le nombre d'objet
        print("Votre grille va contenir "+str(self.nbElement)+" objet !") # Pas nécessaire...
        for _ in range(self.nbElement):     # On remplie la liste de valeur "vide", cette liste est de taille Ligne x Colonne (grille), cela permet de manipuler la liste plus aisement...
            self.data["possibilites"].append("vide")
        with open('write.json','w') as monfichier:
            json.dump(self.data, monfichier, indent=4)


    def plusUn(self):            # Fonction +1 : permet d'ajouter des nouveaux attributs
        if(str(self.entryAttr.get()) not in self.li): # Si l'attribut n'est pas déjà dans self.li (la liste des attributs) alors on l'ajoute
            self.li.append(str(self.entryAttr.get()))
            for i in range(0,self.nbElement):         # On parcours tout les objets pour leur ajouter le nouveau attribut avec une valeur "vide"
                if(self.var>0):
                    self.data["possibilites"][i][str(self.entryAttr.get())]="vide"
        for _ in range(0,len(self.li)):  # On fait en sorte que la liste self.li2 (la liste des valeurs d'attributs) soit de même taille que self.li, l'objectif etant de les "fusionner" avec dict(zip(..))
            if(len(self.li2)<len(self.li)): # Avec des valeurs initialiser a vide...
                self.li2.append("vide") 
        # print(self.li)
        # print(self.li2) 
        self.cbb = Combobox(self.w1, values=self.li) 
        self.cbb.place(x = 110, y = 310, width = 120, height = 22)
        liDict=dict(zip(self.li,self.li2))
        print(liDict)
        for i in range(0,self.nbElement): # Si c'est le premier attributs que l'on ajoute alors, tout les objets sont definies tq le premier attribut a pour valeur "vide"  
            if(self.var==0):
                self.data["possibilites"][i]=liDict
        with open('write.json','w') as monfichier:
            json.dump(self.data, monfichier, indent=4)

    def moinsUn(self): # Fonction -1 : permet d'enlever un attribut (en entrant le nom de l'attribut + cliquer sur -1..)
        for i in range(0,len(self.li)): # On procède a l'elimination de l'attribut de la liste self.li mais aussi la valeur de l'attribut correspondant self.li2.. 
            if(self.li[i]==str(self.entryAttr.get())):
                self.li.pop(i)
                self.li2.pop(i)
        self.cbb = Combobox(self.w1, values=self.li) # Nouveau combobox 
        self.cbb.place(x = 110, y = 310, width = 120, height = 22)
        for j in range (0,self.nbElement):     # Ici on supprime pour chaques objets (càd chaque data["possibilites"] l'attribut avec la val correspondant/attribué
            if(str(self.entryAttr.get()) in self.data["possibilites"][j]):
                self.data["possibilites"][j].pop(str(self.entryAttr.get()))
        with open('write.json','w') as monfichier:
            json.dump(self.data, monfichier, indent=4)

    def valAtt(self): # La validation permet de remplir les self.list et selflist2 (liste d'attribut et val d'attribut...)
        if(len(self.li)!=0 and len(self.li2)!=0):
            for i in range(0,len(self.li)):
                if(self.li[i]==str(self.cbb.get())):
                    self.li2[i]=str(self.entryVal.get())
            print(self.li)
            print(self.li2)
            
a = Widget1(0)
a.w1.mainloop()