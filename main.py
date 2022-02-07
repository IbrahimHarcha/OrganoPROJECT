import json

with open("personnage2.json") as mon_fichier:
    data = json.load(mon_fichier)

#--- Fonction qui retourne la liste des perso, et ce en fonction du nombre de "ligne" et "colonne" du fichier JSON ---#

def getPerso():
    f=(int(data["colonne"])*int(data["ligne"]))
    for i in range(0,f):
        print(data["possibilites"][i])

h=getPerso()  #-- On peut stocker une sortie standard dans une chaine(ici h), car c'est langage de haut niveau, on pourra alors
              # charger cette chaine dans un objet...

print(h)

#---- Fonction qui renvoie une caractéristique(du perso), et ce,
# à partir de l'index du personnage et du type de caractéristique(nom fichier, yeux...) ----#

def getCaract(index,type):
    for i in data["possibilites"]:
        if(index==i["index"]): return i[type]

print(getCaract('0','cheveux')) # ---TEST---#

#---- Fonction qui a partir d'une carac et de son type, renvoie tout les objets des perso ayant cette carac. ----#

def possedeCarac(type,carac):
    for i in data["possibilites"]:
            if(carac==getCaract(i["index"],type)): print(i)

c=possedeCarac("cheveux","blanc") 

# print(possedeCarac("cheveux","blanc"))

#---- Fonction fesant l'inverse de la fonction précédente, on se servira de cette fonction pour barrer les personnages... ----#

def nePossedePasCarac(type,carac):
    for i in data["possibilites"]:
            if(carac!=getCaract(i["index"],type)): print(i)

print(nePossedePasCarac("cheveux","blanc")) 

#---- Fonction 



