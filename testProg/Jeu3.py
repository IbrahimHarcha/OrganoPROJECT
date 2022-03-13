from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
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

with open("personnage.json") as mon_fichier:
    data = json.load(mon_fichier)
    

class Grid(Frame):
    def __init__(self,root):
        l=int(data["ligne"])
        c=int(data["colonne"])
        width=100
        height=150
        s=0
        v=0
        self.list=[]
        self.list2=[]################# Deuxieme Liste pour les images barrées########################
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
            return two_funcs
            
        def Action2(P1,P2,P3):
            def doit():
                
                print(data["possibilites"][P1]["prenom"]+"  ")
                for i in range(0,l):
                    for j in range(0,c):
                        str="img/personnages/"+data["possibilites"][P1]["fichier"]#############################Chemin a modifier
                        
                
                
                self.list.append(PhotoImage(file=str))
                self.buttonZ = Button(root,image=self.list[P1],command=Action(P1,P2,P3))
                self.buttonZ.grid(row=P2,column=P3,sticky="nsew")    
            return doit 
        
     
               
        
        def Action(P1,P2,P3):
            def doit():
                a=0
                print(data2["possibilites"][P1]["prenom"]+"  ")
                for i in range(0,l):
                    for j in range(0,c):
                        
                        str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
                        a=a+1
                        self.list2.append(PhotoImage(file=str))
                        
                
                        
                self.buttonZ = Button(root,image=self.list2[P1],command=Action2(P1,P2,P3))
                self.buttonZ.grid(row=P2,column=P3,sticky="nsew") 
                print(a)
                print(data2["possibilites"][P1]["fichier"])
            return doit
        
        for i in range(0,l):
            for j in range(0,c):
                str="img/personnages/"+data["possibilites"][s]["fichier"]#############################Chemin a modifier
                self.list.append(PhotoImage(file=str))
                self.buttonI = Button(root,image=self.list[s],command=Action((s),i,j))
                
                self.buttonI.grid(row=i,column=j,sticky="nsew")
                s+=1
            Grid.rowconfigure(root,i,weight=1)
        for j in range (0,c):
            Grid.columnconfigure(root,j,weight=1)    


class Frame1():
    def __init__(self,root):
        self.root=root
        
        self.frame=Frame(root,padx=50,pady=50,bd=1)
        self.frame.grid(row=0,column=1)
        
        self.b=Button(self.frame,text="Jouer en mode solo",command=self.solo,font=("MS PGothic", 12),bg='beige')
        self.b.grid(row=0,column=0)
        self.lvide=Label(self.frame,text="")
        self.lvide.grid(row=1,column=0)
        self.b2=Button(self.frame,text="Jouer contre l'ordinateur",command=self.ordi,font=("MS PGothic", 12),bg='beige')
        self.b2.grid(row=2,column=0)
        self.lvide2=Label(self.frame,text="")
        self.lvide2.grid(row=3,column=0)

        self.lbl=Label(self.frame,text="Nombres de lignes : ",font=("MS PGothic", 12))
        self.sp=Spinbox(self.frame,from_=0,to=3, width=3,justify='center',state='readonly')
        self.lbl.grid(row=4,column=0)
        self.sp.grid(row=4,column=1)
        self.lvide3=Label(self.frame,text="")
        self.lvide3.grid(row=5,column=0)
        self.lbl2=Label(self.frame,text="Nombres de colonnes : ",font=("MS PGothic", 12))
        self.sp2=Spinbox(self.frame,from_=0,to=8, width=3,justify='center',state='readonly')
        self.lbl2.grid(row=6,column=0)
        self.sp2.grid(row=6,column=1)  
        self.lvide4=Label(self.frame,text="")
        self.lvide4.grid(row=7,column=0) 

        for i in range (0,8):
            Grid.rowconfigure(self.frame,i,weight=1)
        for j in range(0,2):
            Grid.columnconfigure(self.frame,j,weight=1)
    def solo():
        pass
    def ordi():
        pass

class Frame2():
    
    def __init__(self,root):
        
        def two_funcs(*funcs):
            def two_funcs(*args, **kwargs):
                for f in funcs:
                    f(*args, **kwargs)
                return two_funcs
        self.l=int(data3["ligne"])
        self.c=int(data3["colonne"])
        self.a=0
        n=int(data["nbCara"])
        self.frame=Frame(root,padx=100,pady=1,bd=1)
        self.frame.grid(row=1,column=0)
        self.caseX=((self.l*self.c))
        self.nbcase=0
        self.list=[]
        self.list2=[]
        self.list3=[]
        self.listR=[]
        self.lbl=Label(self.frame,text="Votre personnage a  :",font=("Arial", 15)) # A modifier !
        self.lbl.grid(row=0,column=0)

        
        self.btn3=Button(self.frame,text="Valider",command=Jeu.valider,font=("MS PGothic", 15),bg='beige') ####self.modetriche
        self.btn3.grid(row=4,column=4)
    
        self.perso=random.randint(0,23) # INDEX ALEATOIRE, le personnage que le joueur doit trouvé
        
        
        self.cbb1=Combobox(self.frame,values=["genre","cheveux","lunettes","chauve","chapeau"])
        self.cbb1.bind("<<ComboboxSelected>>", self.justamethod2)
        self.cbb1.grid(row=0,column=5)
        self.cbb1.current(1)
        self.lvide2=Label(self.frame,text="  ")
        self.lvide2.grid(row=0,column=6)

        

        self.btn4=Button(self.frame,text="Mode Triche",command=self.modetriche,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)


        for i in range (0,5):
            Grid.rowconfigure(self.frame,i,weight=1)
        for j in range(0,9):
            Grid.columnconfigure(self.frame,j,weight=1)

        self.cbb2=Combobox(self.frame,values=data4["cheveux"])
        self.cbb2.grid(row=0,column=7)
        self.cbb2.bind("<<ComboboxSelected>>", self.estActive)
    

    def estActive():
        pass


    def justamethod2(self,args):
        self.cbb2=Combobox(self.frame,values=data4[self.cbb1.get()])
        self.cbb2.grid(row=0,column=7) 
    
    def valider():
        pass

    
    # def Action(P1,P2,P3):
    #         def doit():
    #             a=0
    #             print(data2["possibilites"][P1]["prenom"]+"  ")
    #             for i in range(0,l):
    #                 for j in range(0,c):
                        
    #                     str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
    #                     a=a+1
    #                     self.list2.append(PhotoImage(file=str))
                        
                
                        
    #             self.buttonZ = Button(root,image=self.list2[P1],command=Action2(P1,P2,P3))
    #             self.buttonZ.grid(row=P2,column=P3,sticky="nsew") 
    #             print(a)
    #             print(data2["possibilites"][P1]["fichier"])
    #         return doit

    # def valider(self):
    #     a=0
    #     type=self.cbb1.get()
    #     carac=self.cbb2.get()
    #     b=str(self.possedeCarac(self.cbb1.get(),self.cbb2.get()))
    #     licarac=json.loads(str(self.possedeCarac(self.cbb1.get(),self.cbb2.get())))
    #     for i in range(0,self.l):
    #         for j in range(0,self.c): 
    #             if(data3["possibilites"][a] in licarac):
    #                 str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data3["possibilites"][a]["fichier"]#############################Chemin a modifier
    #                 self.list2.append(PhotoImage(file=str))    
    #                 self.buttonZ = Button(m,image=self.list2[a],command=m.Action2(a,i,j))
    #                 self.buttonZ.grid(row=i,column=j,sticky="nsew") 
    #                 a=a+1

    def modetriche(self):
        if self.a==0 :
            self.a=self.a+1
            
            self.lbl=Label(text="nombre de personnages a cochés :"+str(self.nbcase),font=("Arial", 15))
            self.lbl.grid(row=2,column=0)
            
        else:
                
                self.lbl.grid_forget()
                
                self.a=self.a-1

        # if self.a==0:
        #     self.listR.clear()
        #     l=int(data["ligne"])
        #     c=int(data["colonne"])
                        
        # if self.a==1 :
        #     self.nbcase=0
            
            
        #     l=int(data["ligne"])
        #     c=int(data["colonne"])
            
            
        #     for i in range(0,((l*c)-1)):
        #         if((data2["possibilites"][i][self.current_table1.get()])==self.current_table2.get()) :
        #             print(data2["possibilites"][i]["prenom"])
        #             if not data2["possibilites"][i]["prenom"] in self.listR :
        #                 self.listR.append(data2["possibilites"][i]["prenom"])
        #                 self.caseX=self.caseX-1
        #                 print(self.caseX)
                    
        #             self.nbcase=len(self.listR)
                    
        #     print(self.listR)
        #     self.lbl=Label(text="nombre de personnages a cochés :"+str(self.caseX),font=("Arial", 15))
        #     self.lbl.grid(row=2,column=0)
        #     if(self.caseX)==(1):
        #                 self.lbl=Label(text="PERDU",font=("Arial", 15))
        #                 self.lbl.grid(row=0,column=0)
        #     if(self.caseX)==(2):
        #                 self.lbl=Label(text="GAGNIER",font=("Arial", 15))
        #                 self.lbl.grid(row=0,column=0)
            
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

        self.mainframe = Frame(self.app,padx=10,pady=10,bg='beige', borderwidth=1)
        self.mainframe.grid(row=0,column=0)
        self.t=Grid(self.mainframe)
        self.h=Frame1(self.app)
        self.h2=Frame2(self.app)
        Grid.rowconfigure(self.app,0,weight=1)
        Grid.columnconfigure(self.app,0,weight=1)
        Grid.columnconfigure(self.app,1,weight=1)
        Grid.rowconfigure(self.app,1,weight=1)

    def possedeCarac(self,type,carac):
        for i in data["possibilites"]:
            if(carac==i[type]): print(i)
    
    def valider(self):
        a=0
        b=self.possedeCarac(self.h2.self.cbb1.get(),self.h2.self.cbb2.get())
        licarac=json.loads(str(b))
        for i in range(0,self.l):
            for j in range(0,self.c): 
                if(data3["possibilites"][a] in licarac):
                    self.t.Action(a,i,j)

    
        # str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data3["possibilites"][a]["fichier"]#############################Chemin a modifier
                # self.h2.list2.append(PhotoImage(file=str))    
                    # self.buttonZ = Button(m,image=self.list2[a],command=m.Action2(a,i,j))
                    # self.buttonZ.grid(row=i,column=j,sticky="nsew") 
                    # a=a+1
        

# mainframe = Frame(app,padx=10,pady=10,bg='beige', borderwidth=1)
# mainframe.grid(row=0,column=0)
# t=Grid(mainframe)
# h=Frame1(app)
# h2=Frame2(app)

# Grid.rowconfigure(app,0,weight=1)
# Grid.columnconfigure(app,0,weight=1)
# Grid.columnconfigure(app,1,weight=1)
# Grid.rowconfigure(app,1,weight=1)


b=Jeu(0)

b.app.mainloop()