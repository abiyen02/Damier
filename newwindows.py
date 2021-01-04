import tkinter as tk

"""new fenetre pour le jeu """
def createNewWindow():
    newWindow = tk.Toplevel(app)
    newWindow.geometry("800x800")
    
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()



app = tk.Tk()
app.geometry("500x600")

labelexample2 = tk.Label(app ,width=5,height=5,text=" Menu ")
labelexample2.pack( )
buttonExample = tk.Button(app,text="Nouvelle partie", command=createNewWindow)
buttonExample.pack()

app.mainloop()
