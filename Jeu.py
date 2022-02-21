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
            
            self.w1.title('Qui  Est - Ce ?')
           
        else:
            self.w1 = Frame(parent)
            
            self.w1.place(x = 0, y = 0, width = 500, height = 450)
        self.label1 = Label(self.w1, text = "Qui  Est - Ce ? ", font = tkinter.font.Font(family = "Showcard Gothic", size = 48, weight = "normal"), cursor = "arrow", state = "normal")
        self.label1.pack()
        
        
        photo = PhotoImage(file =  r"C:\Users\Megaport\Documents\FAC\testProg\Jouer.png")
        self.button4 = Button(self.w1, image=photo,)
        self.button4.place(x = 150, y = 260, width = 220, height = 102,)
        self.button4.image = photo
        self.button4['command'] = self.Jouer

        
        
        

    def Jouer(self):
        print('Jouer')
        

        
        self.w1.destroy()
        a = app(0)
        a.w1.mainloop()
        

a = Widget1(0)

a.w1.mainloop()

app = Tk()
app.title("Qui est-ce ?")
app.geometry("1200x620+250+100")
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
        def Action(P1):
            def doit():
                
                print(data["possibilites"][P1]["prenom"])
                
            return doit 
        for i in range(0,l):
            for j in range(0,c):
                str=r"C:\Users\Megaport\Documents\FAC\testProg\personnages/"+data["possibilites"][s]["fichier"]
                self.list.append(PhotoImage(file=str))
                self.buttonI = Button(root, image=self.list[s],command=Action(v))
                
                v+=1
                
                
                self.buttonI.grid(row=i,column=j,sticky="nsew")
                s+=1
            Grid.rowconfigure(root,i,weight=1)
        for j in range (0,c):
            Grid.columnconfigure(root,j,weight=1)    



class Frame1():
    def __init__(self,root):
        frame=Frame(root,padx=50,pady=50,bd=1)
        frame.grid(row=0,column=1)
        
        self.b=Button(frame,text="Jouer en mode solo",command=self.solo,font=("MS PGothic", 12),bg='beige')
        self.b.grid(row=0,column=0)
        self.lvide=Label(frame,text="")
        self.lvide.grid(row=1,column=0)
        self.b2=Button(frame,text="Jouer contre l'ordinateur",command=self.ordi,font=("MS PGothic", 12),bg='beige')
        self.b2.grid(row=2,column=0)
        self.lvide2=Label(frame,text="")
        self.lvide2.grid(row=3,column=0)

        self.lbl=Label(frame,text="Nombres de lignes : ",font=("MS PGothic", 12))
        self.sp=Spinbox(frame,from_=0,to=3, width=3,justify='center',state='readonly')
        self.lbl.grid(row=4,column=0)
        self.sp.grid(row=4,column=1)
        self.lvide3=Label(frame,text="")
        self.lvide3.grid(row=5,column=0)
        self.lbl2=Label(frame,text="Nombres de colonnes : ",font=("MS PGothic", 12))
        self.sp2=Spinbox(frame,from_=0,to=8, width=3,justify='center',state='readonly')
        self.lbl2.grid(row=6,column=0)
        self.sp2.grid(row=6,column=1)  
        self.lvide4=Label(frame,text="")
        self.lvide4.grid(row=7,column=0) 

        for i in range (0,8):
            Grid.rowconfigure(frame,i,weight=1)
        for j in range(0,2):
            Grid.columnconfigure(frame,j,weight=1)
    def solo():
        pass
    def ordi():
        pass

class Frame2():
    def __init__(self,root):
        frame=Frame(root,padx=100,pady=1,bd=1)
        frame.grid(row=1,column=0)
        
        self.lbl=Label(frame,text="Votre question :",font=("Arial", 15))
        self.lbl.grid(row=0,column=0)
        self.btn=Button(frame,text="Ajouter",command=self.ajouter,font=("MS PGothic", 12),bg='beige')
        self.btn.grid(row=2,column=0)
        self.btn2=Button(frame,text="Enlever",command=self.enlever,font=("MS PGothic", 12),bg='beige')
        self.btn2.grid(row=2,column=1)
        self.btn3=Button(frame,text="Valider",command=self.valider,font=("MS PGothic", 15),bg='beige')
        self.btn3.grid(row=4,column=4)
        self.cbb1=Combobox(frame,values=["genre","cheveux","lunettes","chauve","chapeau"])
        self.cbb1.grid(row=0,column=5)
        self.lvide2=Label(frame,text="  ")
        self.lvide2.grid(row=0,column=6)
        self.cbb2=Combobox(frame,values=["genre","cheveux","lunettes","chauve","chapeau"]) # Faire algo !
        self.cbb2.grid(row=0,column=7)

        self.btn4=Button(frame,text="Mode Triche",command=self.modetriche,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)

        for i in range (0,5):
            Grid.rowconfigure(frame,i,weight=1)
        for j in range(0,9):
            Grid.columnconfigure(frame,j,weight=1)

        
    def ajouter():
        pass
    def enlever():
        pass
    def valider():
        pass     
    def modetriche():
        pass   

mainframe = Frame(app,padx=10,pady=10,bg='beige', borderwidth=1)
mainframe.grid(row=0,column=0)
t=Grid(mainframe)
h=Frame1(app)
h2=Frame2(app)

Grid.rowconfigure(app,0,weight=1)
Grid.columnconfigure(app,0,weight=1)
Grid.columnconfigure(app,1,weight=1)
Grid.rowconfigure(app,1,weight=1)

app.mainloop()
