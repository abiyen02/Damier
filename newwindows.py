import tkinter as tk

"""nouvelle fenetre pour importer le jeu """
def createNewWindow():
    newWindow = tk.Toplevel(root)
    newWindow.geometry("800x800")
    
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()



root = tk.Tk()
root.geometry("500x600")

labelexample2 = tk.Label(root ,width=5,height=5,text=" Menu ")
labelexample2.pack( )
buttonExample = tk.Button(root,text="Nouvelle partie", command=createNewWindow)
buttonExample.pack()

root.mainloop()
