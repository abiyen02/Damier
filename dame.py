from tkinter import *
from random import *
root = Tk()
root.title("Jeu de Dame")
can1 = Canvas(root, width =500, height =500)
can1.pack(side =TOP, padx =5, pady =5)
can2 = Canvas(root, width = 500)
case = 50
damier=[]


#Dessiner un le damier 
def damier():
    "Dessine le damier"
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            if (i%2)==0:
                if (j%2)==0:
                    can1.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='black')
                else:
                    can1.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case,fill='white')
            else:
                if (j%2)==0:
                    can1.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='white')
                else:
                    can1.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='black')
            j+=1
        i+=1

def cercle_rouge():
	x= random.randint(0,25)
	y = random.randint(0,25)
	w.create_oval(x,y,x+10,y+10 , fill= "red" )


def cercle_bleu():
    x2= randon.randint(0,25)
    y2= random.randint(0,25)
    w.create_oval(x2,y2,x2+10,y2+10 , fill= "bleu" )

# Les boutons
rouge = Button(root, text='rouge', command = cercle_rouge)
rouge.pack(side=RIGHT, padx=3, pady=3)

bleu = Button(root, text='rouge', command = cercle_rouge)
bleu.pack(side=RIGHT, padx=3, pady=3)

b3 = Button(root, text ='Quitter', command =root.destroy)
b3.pack(side =BOTTOM,padx =3, pady =3)
b4 = Button(root, text ='Nouvelle Partie', command =damier)
b4.pack(side =BOTTOM,padx =3, pady =3)
root.mainloop()
