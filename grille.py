from tkinter import *
from random import shuffle, randrange

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=6
NB_PICT=NB_LINES*NB_COLS//2
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2

LANG=['alfred', 'anita', 'anna', 'charlie', 'clara', 'eric',
      'felix', 'jeremie', 'leon', 'luc', 'lucas', 'manu', 'maria',
       'mario', 'martin', 'max', 'omar', 'oscar', 'romeo', 'samuel',
       'simon', 'suzane', 'timeo', 'tony']


def make_board():
    L=[v % NB_PICT for v in range(2*NB_PICT)]
    shuffle(L)
    board=[]
    k=0
    for line in range(NB_LINES):
        row=[]
        for col in range(NB_COLS):
            row.append(L[k])
            k+=1
        board.append(row)
    return board
    

root=Tk()
cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='LightPink')
cnv.pack()


logos=[PhotoImage(file="./images/%s.png" %filename) for filename in LANG]


board=make_board()
print(board)

# Placement des images
for line in range(NB_LINES):
    for col in range(NB_COLS):
        center=(X0+col*SIDE, Y0+line*SIDE)
        nro_image=board[line][col]
        mon_image=logos[nro_image]
        cnv.create_image(center, image=mon_image)

line=randrange(NB_LINES)
col=randrange(NB_COLS)
print(line, col)

root.mainloop()