from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font
import json
import random  
#!/usr/bin/env python
# -*- coding: utf-8 -*-



## data["possibilites"] = renvoie un tableau de persos, les persos sont chacun caractérisé par un dict (dictionnaire)


with open("personnage.json",encoding='utf-8') as mon_fichier:   
    data = json.load(mon_fichier)                    ### Json pour les images non barrées ###
with open("personnagex.json",encoding='utf-8') as mon_fichier2:
    data2= json.load(mon_fichier2)      ### Json pour les images barrées ####  

with open("stat.json",encoding='utf-8') as mon_fichier4:
    data4 = json.load(mon_fichier4)

class Widget1():     
    def __init__(self, parent): 
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.geometry('500x450+400+180')
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
        # a = Jeu(0)
        Jeu.w1.mainloop()
        

a = Widget1(0)

a.w1.mainloop()

class Jeu():     # Fenêtre qui sera composé de 3 frames, nommées : self.frame1(les images en grid), self.frame2(le bas,button validé, combobox...) et self.frame3 (côté droit...)
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.app = Tk()       
            self.app.title("Qui est-ce ?")
            self.app.geometry("1200x620+250+100")
            
        else:
            self.app=Frame(parent)
            self.app.grid(row=0,column=0)

        self.frame1=Frame(self.app,padx=10,pady=10,bg='beige', borderwidth=1) # Dans laquel on disposera un tableau d'images (grace au grid)...
        self.frame1.grid(row=0,column=0)
        self.l=int(data["ligne"])
        self.c=int(data["colonne"])
        self.s=0
        self.list=[]    ## Liste dans laquel on mettra les images (barrées ou non barrées)
        self.list2=[]   ##### Deuxieme Liste pour les images barrées ####  
        self.list4=[]   #### Liste qui contient les indices des personnages barrées en cliquant (voir Action et Action2)
        self.triche=False   ### Valeur booléene permmettant de differencier le mode triche au normal...
        
        
        ## Placement des images 
        for i in range(0,self.l):
            for j in range(0,self.c):
                self.str="img/personnages/"+data["possibilites"][self.s]["fichier"]#############################Chemin a modifier
                self.list.append(PhotoImage(file=self.str))
                self.buttonZ = Button(self.frame1,image=self.list[self.s],command=self.Action((self.s),i,j))
                
                self.buttonZ.grid(row=i,column=j,sticky="nsew")
                self.s+=1
            Grid.rowconfigure(self.frame1,i,weight=1) # A régler plus tard....
        for j in range (0,self.c):
            Grid.columnconfigure(self.frame1,j,weight=1)    
        
        # Initialisation des variables :
        self.l=int(data["ligne"])  # nombre de ligne
        self.c=int(data["colonne"]) # nombre de colonne
        self.frame2=Frame(self.app,padx=100,pady=1,bd=1) # la frame du bas, celle qui contiendra les questions...
        self.frame2.grid(row=1,column=0)
        self.lbl=Label(self.frame2,text="Votre personnage a  :",font=("Arial", 15))
        self.lbl.grid(row=0,column=0)
        self.btn3=Button(self.frame2,text="Valider",command=self.valider,font=("MS PGothic", 15),bg='beige')
        self.btn3.grid(row=4,column=4)

        self.perso=random.randint(0,int(self.l)*int(self.c)-1) # INDEX ALEATOIRE, le personnage que le joueur doit trouver, il s'agit en fait de l'index du personnage que l'on doit trouver

        print("le perso a trouver est le num : "+str(self.perso))
        print(data["possibilites"][self.perso]["prenom"])
        
        
        self.cbb1=Combobox(self.frame2,values=list(data4.keys())) # Combobox contenant la liste des types de carac (cheveux....)
        self.cbb1.bind("<<ComboboxSelected>>", self.justamethod2) # A chaque changement de type (exemple on passe de cheveux a lunettes) 
        #on déclanche la methode justamethod, cette methode permet d'ajuster les carac selon les types.
        self.cbb1.grid(row=0,column=5)
        self.cbb1.current(1) 
        self.lvide2=Label(self.frame2,text="  ")
        self.lvide2.grid(row=0,column=6)

        self.cbb=self.cbb1.get() # var dans laquelle on stocke self.cbb1 pour etre sur de ne pas perdre de données

        self.entry=Entry() # Sert a entrer le nom du perso quand on a trouvé 
        self.label=Label()


        self.btn4=Button(self.frame2,text="Mode Triche",command=self.modetriche,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)
        self.lbl1=Label()

        for i in range (0,5):
            Grid.rowconfigure(self.frame2,i,weight=1)
        for j in range(0,9):
            Grid.columnconfigure(self.frame2,j,weight=1)

        self.cbb2=Combobox(self.frame2,values=data4[self.cbb1.get()])  ## Combobox contenant les carac selon le type (a partir de data)
        self.cbb2.grid(row=0,column=7)
        self.cbb2.bind("<<ComboboxSelected>>", self.estActive) ### On declanche la methode estActive lorsqu'on change de carac (blanc->noir...)


        self.liRepere=[] # On stocke a l'intèrieur tout les persos qui ont été supprimer !
       
        
    # Lorsqu'une question a été poser on supprimme de data4 (càd le fichier stat.json) le type de carac et la cara,
    #  afin que le joueur ne puisse pas poser deux fois la mm question

        for _ in range(0,self.c*self.l): # Afin d'avoir acces a tout les indices de self.liRepere...
            self.liRepere.append("")

        for _ in range(0,self.c*self.l): # Afin d'avoir acces a tout les indices de self.list4...
            self.list4.append("")

        self.frame3=Frame(self.app,padx=50,pady=50,bd=1) ## Frame a droite
        self.frame3.grid(row=0,column=1)
        self.b=Button(self.frame3,text="Entrer le nom du personnage",command=self.trouver,font=("MS PGothic", 12),bg='beige')
        self.b.grid(row=0,column=0)
        self.lbl5=Label(self.frame3,text=" ")
        self.lbl5.grid(row=1,column=0)
        self.btn5=Button(self.frame3, text="Rejouer", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal",bg="beige")
        self.btn5.grid(row=2,column=0)
        self.btn5['command']=self.rejouer

    def trouver(self):   ## Fenêtre permettant de vérifier si on a bien deviné le bon personnage
        app2=Toplevel(self.app)
        app2.title("Qui est-ce ?")
        app2.geometry("550x200+400+300")
        app2.resizable(width=False, height=False)
        
        lbl=Label(app2,text="Veuillez entrer le nom du personnage :",font=tkinter.font.Font(family="MS Shell Dlg 2", size = 14), cursor = "arrow", state = "normal")
        lbl.place(x = 50, y = 20, width = 350, height = 82)
        self.entry=Entry(app2,bd=3)
        self.entry.place(x=150,y=100,width=100,height=30)
        btn1=Button(app2, text="Verifier", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 11), cursor = "arrow", state = "normal",bg="beige")
        btn1.place(x = 300, y = 100, width = 100, height = 30)
        btn1['command']=self.testNom
    
    def testNom(self): # Cette méthode permet de faire coincider (càd qu'ils sont écrient de la même manière) le nom du perso :
        # a savoir -> le nom du perso a trouver (data["possibilites"][self.perso]["prenom"]) et ce que l'utilisateur saisie (self.entry.get())
        # Cela permet de faire abstraction les défauts d'écriture, par ex : si le joueur a entré le nom tout en miniscule/majuscule, avec/sans accent... 
        # Pour cela on fait appel a une methode qui transforme une chaine avec accent en chaine sans accent, on fait egalement appel
        # a la fonction upper() permettant de mettre en majuscule les deux chaînes

        # Si les deux chaines sont égaux on appele la methode gagner(), sinon perdu()
        if(self.sansAccentChaîne(data["possibilites"][self.perso]["prenom"])).upper()==self.sansAccentChaîne(self.entry.get()).upper():
            self.gagner()
        else:
            self.perdu()

    def sansAccentChar(self,c):
        # Repère table ASCII...
        table_correspondance={192 : 65,193 : 65,194 : 65,195 : 65,196 : 65, 197 : 65,198 : 65,199 : 67,200 : 69,201 : 69, 202 : 69,203 : 69,
                            204 : 73,205 : 73, 206 : 73,207 : 73,208 : 68, 209 : 78, 210 : 79, 211 : 79,212 : 79,213 : 79,214 : 79,
                            216 : 79, 217 : 85,218 : 85,219 : 85,220 : 85,221 : 89,224 : 97,225 : 97,226 : 97,227 : 97,228 : 97,229 : 97,230 : 97,
                            231 : 99,232 : 101,233 : 101,234 : 101,235 : 101,236 : 105,237 : 105,238 : 105,239 : 105,240 : 111,241 : 110,
                            242 : 111,243 : 111,244 : 111,245 : 111,246 : 111, 248 : 111, 249 : 117, 250 : 117, 251 : 117, 252 : 117, 253 : 121}
        if(192<=ord(c) <= 214 or 216 <= ord(c) <=253): # Si le caractère c est une lettre avec accent alors on l'a transforme en lettre sans accent,
            return chr(table_correspondance[ord(c)]) # et ce grâce a la table ASCII
        else:
            return c

    def sansAccentChaîne(self,s): # Pour la fonction trouver, elle sert a transformer une chaîne contenant des accents en un chaîne sans accent.
        """Retire tous les accents d'un mot"""
        new_string = ""
        for char in s:
            new_string+=self.sansAccentChar(char)
        return new_string

    def Action2(self,P1,P2,P3): # Methode qui "débarre" une image (après avoir cliqué dessus) en remplaçant l'image "barrée" par une "non barrée"...
        def doit():             # P2 désigne la ligne, P3 la colonne
            k=0
            for _ in range(0,self.l):
                for _ in range(0,self.c):
                    str="img/personnages/"+data["possibilites"][P1]["fichier"]############Chemin a modifier
                    self.list[P1]=(PhotoImage(file=str))
                    if(int(data["possibilites"][P1]["index"]) in self.list4):
                        self.list4[k]=""
                    k+=1
            self.buttonZ = Button(self.frame1,image=self.list[P1],command=self.Action(P1,P2,P3))
            self.buttonZ.grid(row=P2,column=P3,sticky="nsew") 
        return doit 
           
    def Action(self,P1,P2,P3): # Methode qui "barre" une image (après avoir cliqué dessus) en remplaçant l'image "non barrée" par une "barrée".
        def doit():            # P2 désigne la ligne, P3 la colonne
            a=0
            if(self.perso==P1):
                self.perdu()
            for _ in range(0,self.l):
                for _ in range(0,self.c):
                    str=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][a]["fichier"]#############################Chemin a modifier
                    a=a+1
                    self.list2.append(PhotoImage(file=str))
                    if(P1 not in self.list4):
                        self.list4[P1]=P1
            self.buttonI = Button(self.frame1,image=self.list2[P1],command=self.Action2(P1,P2,P3))
            self.buttonI.grid(row=P2,column=P3,sticky="nsew")
        return doit

    def modeNormal(self):
        self.btn4.destroy()
        self.btn4=Button(self.frame2,text="Mode Triche ",command=self.modetriche,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)
        self.lbl1.destroy()
        self.triche=False

    def modetriche(self):
        self.btn4.destroy()
        self.btn4=Button(self.frame2,text="Mode Normal",command=self.modeNormal,font=("MS PGothic", 12),bg='beige')
        self.btn4.grid(row=3,column=8)
        self.triche=True

    def valider(self):
        s=0
        self.lbl1.destroy()
        
        if(self.triche):
            for i in range(0,len(self.list4)):
                if(self.list4[i] not in self.liRepere):
                    self.liRepere[i]=self.list4[i]

            if(data["possibilites"][self.perso][str(self.cbb1.get())]==str(self.cbb2.get())):
                self.label=Label(self.frame2, text="True", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)
                for k in range(0,self.c*self.l):
                    if(self.liRepere[k]==""):
                        if(data["possibilites"][k][str(self.cbb)]!=str(self.cbb2.get())):
                            self.liRepere[s]=s
                    s+=1
            else:
                self.label=Label(self.frame2, text="False", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)
                for k in range(0,self.c*self.l):
                    if(self.liRepere[k]==""):
                        if(data["possibilites"][k][str(self.cbb)]==str(self.cbb2.get())):
                            self.liRepere[s]=s
                    s+=1
            s=0

            for i in range(0,self.l):
                for j in range(0,self.c):
                    if(int(data["possibilites"][s]["index"]) in self.liRepere):
                        str2=r"C:\Users\ibrah\OneDrive\Bureau\ProjetProg\personnagex/"+data2["possibilites"][s]["fichier"]
                        self.list[s]=PhotoImage(file=str2)
                        self.buttonI = Button(self.frame1,image=self.list[s],command=self.Action2((s),i,j)) 
                        self.buttonI.grid(row=i,column=j,sticky="nsew")
                    s+=1
        else:
            if(data["possibilites"][self.perso][str(self.cbb)]==str(self.cbb2.get())):
                self.label=Label(self.frame2, text="True", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)
            else:
                self.label=Label(self.frame2, text="False", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)



    def perdu(self):
        app2=Toplevel(self.app)
        app2.title("Qui est-ce ?")
        app2.geometry("550x200+400+300")
        app2.resizable(width=False, height=False)
        
        lbl=Label(app2,text="Vous avez perdu la partie !",font=tkinter.font.Font(family="MS Shell Dlg 2", size = 13), cursor = "arrow", state = "normal",fg="red")
        lbl.place(x = 90, y = 20, width = 300, height = 82)
        btn1=Button(app2, text="Rejouer", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal",bg="beige")
        btn1.place(x = 170, y = 100, width = 100, height = 30)
        btn1['command']=self.rejouer
        btn2=Button(app2, text="Quitter le jeu", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal",bg="beige")
        btn2.place(x = 300, y = 100, width = 100, height = 30)
        btn2['command']=self.quitter

    def gagner(self):
        app2=Toplevel(self.app)
        app2.title("Qui est-ce ?")
        app2.geometry("550x200+400+300")
        app2.resizable(width=False, height=False)
        
        lbl=Label(app2,text="Bravo, vous avez remporté la partie !",font=tkinter.font.Font(family="MS Shell Dlg 2", size = 13), cursor = "arrow", state = "normal",fg="green")
        lbl.place(x = 90, y = 20, width = 300, height = 82)
        btn1=Button(app2, text="Rejouer", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal",bg="beige")
        btn1.place(x = 170, y = 100, width = 100, height = 30)
        btn1['command']=self.rejouer
        btn2=Button(app2, text="Quitter le jeu", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 10), cursor = "arrow", state = "normal",bg="beige")
        btn2.place(x = 300, y = 100, width = 100, height = 30)
        btn2['command']=self.quitter
        
    def quitter(self):
        self.app.destroy()

    def rejouer(self):
        self.app.destroy()
        b=Jeu(0)
        b.app.mainloop()

    def estActive(self,args):
        self.label.destroy()
        self.cmt=0
        self.cmt2=0
        if(self.triche):
            self.liRpere=self.list4
            for k in self.liRepere:
                if(k==""):
                    self.cmt2+=1
            if(data["possibilites"][self.perso][str(self.cbb)]==str(self.cbb2.get())):
                self.label=Label(self.frame2, text="True", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)
                self.lbl1.destroy()
                for k in range(0,self.c*self.l):
                    if(self.liRepere[k]==""):
                        if(data["possibilites"][k][str(self.cbb)]!=str(self.cbb2.get())):
                            self.cmt+=1
            else:
                self.label=Label(self.frame2, text="False", font=tkinter.font.Font(family="MS Shell Dlg 2", size = 12), cursor = "arrow", state = "normal")
                self.label.grid(row=3,column=5)
                self.lbl1.destroy()
                for k in range(0,self.c*self.l):
                    if(self.liRepere[k]==""):
                        if(data["possibilites"][k][str(self.cbb)]==str(self.cbb2.get())):
                            self.cmt+=1
            self.lbl1=Label(self.frame2,text="Elimination : "+str(self.cmt)+" sur "+str(self.cmt2),font=("Arial", 12)) # A modifier !
            self.lbl1.grid(row=4,column=6)


    def justamethod2(self,args):
        self.cbb2=Combobox(self.frame2,values=data4[str(self.cbb1.get())])
        self.cbb2.grid(row=0,column=7) 
        self.cbb2.bind("<<ComboboxSelected>>", self.estActive)
        self.cbb=self.cbb1.get()
        self.lbl1.destroy()
        self.label.destroy()

b=Jeu(0)

b.app.mainloop()
