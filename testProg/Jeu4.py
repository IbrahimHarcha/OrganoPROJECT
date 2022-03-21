from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font
import json
import random


with open("personnage.json") as mon_fichier:
    data = json.load(mon_fichier)
with open("personnagex.json") as mon_fichier2:
    data2= json.load(mon_fichier2)############################# Deuxieme fichier Json pour les images barrées##############################


with open("personnage2.json") as mon_fichier3:
    data3 = json.load(mon_fichier3)

with open("stat.json") as mon_fichier4:
    data4 = json.load(mon_fichier4)

class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450')
            self.w1.resizable(width=False, height=False)
            
            self.w1.title('Qui  Est - Ce ?')
           
        else:
            self.w1 = Frame(parent)
            
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.label1 = Label(self.w1, text = "Qui  Est - Ce ? ", font = tkinter.font.Font(family = "Showcard Gothic", size = 48, weight = "normal"), cursor = "arrow", state = "normal")
        self.label1.pack()
        
        
        photo = PhotoImage(file=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\Jouer.png")
        self.button4 = Button(self.w1, image=photo)
        self.button4.place(x = 150, y = 260, width = 220, height = 102,)
        self.button4.image = photo
        self.button4['command'] = self.Jouer

    
    def Jouer(self):
        print('Jouer')        
        self.w1.destroy()
        a = Jeu()
        a.w1.mainloop()
        

a = Widget1(0)

a.w1.mainloop()

# app = Tk()
# app.title("Qui est-ce ?")
# app.geometry("1200x620+250+100")
# app.minsize(1100,620)

class Jeu():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.app = Tk()
            self.app.title("Qui est-ce ?")
            self.app.geometry("1200x620+250+100")
            
            self.app.title('Qui  Est - Ce ?')
           
        else:
            self.app=Frame(parent)
            self.app.grid(row=0,column=0)

        self.frame1=Frame(self.app,padx=10,pady=10,bg='beige', borderwidth=1)
        self.frame1.grid(row=0,column=0)
        self.l=int(data["ligne"])
        self.c=int(data["colonne"])
        width=100
        height=150
        s=0
        v=0
        self.list=[]
        self.list2=[]################# Deuxieme Liste pour les images barrées########################
        self.list3=[]
        
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return two_funcs

        def Action2(P1,P2,P3):
            def doit():
                print(data["possibilites"][P1]["prenom"]+"  ")
                for i in range(0,self.l):
                    for j in range(0,self.c):
                        str="img/personnages/"+data["possibilites"][P1]["fichier"]#############################Chemin a modifier
                        
                
                
                self.list.append(PhotoImage(file=str))
                self.buttonZ = Button(self.frame1,image=self.list[P1],command=Action(P1,P2,P3))
                self.buttonZ.grid(row=P2,column=P3,sticky="nsew")    
            return doit 
           
        def Action(P1,P2,P3):
            def doit():
                a=0
                for i in range(0,self.l):
                    for j in range(0,self.c):
                        str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
                        a=a+1
                        self.list2.append(PhotoImage(file=str))
                        
                self.buttonZ = Button(self.frame1,image=self.list2[P1],command=Action2(P1,P2,P3))
                self.buttonZ.grid(row=P2,column=P3,sticky="nsew")
            return doit

        
        for i in range(0,self.l):
            for j in range(0,self.c):
                str="img/personnages/"+data["possibilites"][s]["fichier"]#############################Chemin a modifier
                self.list.append(PhotoImage(file=str))
                self.buttonI = Button(self.frame1,image=self.list[s],command=Action((s),i,j))
                
                self.buttonI.grid(row=i,column=j,sticky="nsew")
                s+=1
            Grid.rowconfigure(self.frame1,i,weight=1) # A régler plus tard....
        for j in range (0,self.c):
            Grid.columnconfigure(self.frame1,j,weight=1)    


        self.l=int(data3["ligne"])
        self.c=int(data3["colonne"])
        self.a=0
        n=int(data["nbCara"])
        self.frame2=Frame(self.app,padx=100,pady=1,bd=1)
        self.frame2.grid(row=1,column=0)
        self.caseX=((self.l*self.c))
        self.nbcase=0
        self.lbl=Label(self.frame2,text="Votre personnage a  :",font=("Arial", 15)) # A modifier !
        self.lbl.grid(row=0,column=0)

        
        self.btn3=Button(self.frame2,text="Valider",command=self.valider,font=("MS PGothic", 15),bg='beige') ####self.modetriche
        self.btn3.grid(row=4,column=4)

        # def valider():
        #         a=0
        #         for i in range(0,self.l):
        #             for j in range(0,self.c):
        #                 str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
        #                 self.list2.append(PhotoImage(file=str))
        #                 a+=1
        #         a=0
        #         for k in range (0,23):
        #             if(self.f(a,self.cbb1.get()) == self.cbb2.get()):
        #                 self.buttonZ = Button(self.frame1,image=self.list2[a],command=Action2(a,i,j))
        #                 self.buttonZ.grid(row=i,column=j,sticky="nsew")
        #             a+=1
            

        self.perso=random.randint(0,23) # INDEX ALEATOIRE, le personnage que le joueur doit trouvé
        
        
        self.cbb1=Combobox(self.frame2,values=["genre","cheveux","lunettes","chauve","chapeau"])
        self.cbb1.bind("<<ComboboxSelected>>", self.justamethod2)
        self.cbb1.grid(row=0,column=5)
        self.cbb1.current(1)
        self.lvide2=Label(self.frame2,text="  ")
        self.lvide2.grid(row=0,column=6)

        

        self.btn4=Button(self.frame2,text="Mode Triche",command=self.modetriche,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)


        for i in range (0,5):
            Grid.rowconfigure(self.frame2,i,weight=1)
        for j in range(0,9):
            Grid.columnconfigure(self.frame2,j,weight=1)

        self.cbb2=Combobox(self.frame2,values=data4["cheveux"])
        self.cbb2.grid(row=0,column=7)
        self.cbb2.bind("<<ComboboxSelected>>", self.estActive)

    def possedeCarac(self,type,carac):
        for i in data3["possibilites"]:
            if(carac==i[type]): print(i)
    
    def from_json(self,json_string):
        json_dict=json.loads(json_string)
        return json_dict

    def f(self,index,type):
        return data3["possibilites"][index][str(type)]


    def valider(self):
        l=int(data3["ligne"])
        c=int(data3["colonne"])
        a=0
        for i in range(0,l):
           for j in range(0,c):
                str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
                self.list3.append(PhotoImage(file=str))
                a+=1
        for k in range (0,23):
            if(self.f(k,self.cbb1.get()) == str(self.cbb2.get())):
                self.buttonZ = Button(self.frame1,image=self.list2[k],command=Jeu.Action(a,i,j))
                self.buttonZ.grid(row=i,column=j,sticky="nsew")
                
    def estActive(self):
        pass


    def justamethod2(self,args):
        self.cbb2=Combobox(self.frame2,values=data4[self.cbb1.get()])
        self.cbb2.grid(row=0,column=7) 

    def modetriche(self):
        if self.a==0 :
            self.a=self.a+1
            
            self.lbl=Label(text="nombre de personnages a cochés :"+str(self.nbcase),font=("Arial", 15))
            self.lbl.grid(row=2,column=0)
            
        else:
                
                self.lbl.grid_forget()
                
                self.a=self.a-1

b=Jeu(0)

b.app.mainloop()