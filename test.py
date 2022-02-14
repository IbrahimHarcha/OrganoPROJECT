from tkinter import *

# Creation et paramétrage de la fenêtre :
app = Tk()
app.title("Qui est-ce ?")
app.geometry("800x620+400+100")
app.minsize(800,620)

# Widget :
app.config(bg="black")
lbl = Label(app, text="Qui est-ce ?",font=("Pristina", 40),bg="beige",height=2,width=20)
bn = Button(app, text="Jouer",bg="beige",width=19, height=2, font=("Pristina", 25))

lbl.pack(pady=150) 
bn.pack()

app.mainloop()

