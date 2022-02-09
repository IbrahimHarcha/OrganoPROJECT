from tkinter import *
import json

with open("personnage2.json") as mon_fichier:
    data = json.load(mon_fichier)

app = Tk()
app.geometry("640x480")
app.title("GRILLE")

class Grid:
    def __init__(self,root):
        l=int(data["ligne"])
        c=int(data["colonne"])
        s=0
        for i in range(0,l):
            for j in range(0,c):
                self.e = Entry(root,width=10,fg='blue',font=('Arial',16,'bold'))
                self.e.grid(row=i,column=j)
                self.e.insert(END,data["possibilites"][s]["fichier"])
                s+=1

t=Grid(app)

app.mainloop()