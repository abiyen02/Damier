from tkinter import *
import random
   
root = Tk() 
root.geometry("500x500") 
COLORS = ['red','blue']  
w = Canvas(root,width = 400, height =400)
w.pack(pady=20)
def pions ():
	i=0
	j=0
	x= random.randint(50,400) 
	y = random.randint(50,400) 
	while i < 10:
		while j < 10:
			if (i%2)==0:
				if (j%2)==0:
					w.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					w.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
			else:
				if (j%2)==0:
					w.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
				else :
					w.create_oval(x,y,x+20,y+20,fill=(random.sample(COLORS, 1)[0]), 
					outline = random.sample(COLORS, 1)[0],width=0)
			j=j+1
		i=i+1

button = Button(root, text="jouer", command= pions).pack()
root.mainloop()