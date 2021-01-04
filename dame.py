from tkinter import *
import random
root = Tk()
root.title("Jeu de Dame")
root.geometry("600x600")


can1 = Canvas(root, width =450, height =500)
can1.pack(side =TOP, padx =5, pady =5)


COLORS = ['red','blue']  
case =40

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
# genère les pions du damier       
def pions ():
	i=0
	j=0
<<<<<<< HEAD
	x= random.randint(100,400) 
	y = random.randint(100,400) 
=======
	x= random.randint(50,400) 
	y = random.randint(50,400) 
>>>>>>> 97b262e68ab46577b93f71ab97d19f35069713bb
	while i < 10:
		while j < 10:
			if (i%2)==0:
				if (j%2)==0:
<<<<<<< HEAD
					can1.create_oval(x,y,x+40,y+40,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					can1.create_oval(x,y,x+40,y+40,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
			else:
				if (j%2)==0:
					can1.create_oval(x,y,x+40,y+40,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					can1.create_oval(x,y,x+40,y+40,fill=(random.sample(COLORS, 1)[0]), 
=======
					can1.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					can1.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
			else:
				if (j%2)==0:
					can1.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					can1.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
>>>>>>> 97b262e68ab46577b93f71ab97d19f35069713bb
					outline = random.sample(COLORS, 1)[0],width=0)
			j=j+1
		i=i+1

button = Button(root, text="jouer", command= pions)
button.pack()

b1 = Button(root, text ="Nouvelle partie ", command =damier)
b1.pack(side=LEFT)

b2 = Button(root, text = "QUITTER " , command =root.destroy)
b2.pack(side= RIGHT)

root.mainloop()


"""
def pions():
	x= random.randint(0,25)
	y = random.randint(0,25)
	w.create_oval(x,y,x+10,y+10 , fill= "red" )


def cercle_bleu():
    x2= randon.randint(0,25)
    y2= random.randint(0,25)
    w.create_oval(x2,y2,x2+10,y2+10 , fill= "bleu" )
    b3.pack(side =BOTTOM,padx =3, pady =3)
	button = Button(root, text='button', command = pions)
button.pack()

b3 = Button(root, text ='Quitter', command =root.destroy)
b3.pack()
"""
