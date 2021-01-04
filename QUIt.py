import tkinter as tk
from tkinter.messagebox import *

# askretrycancel, askyesno ARE SIMILAR TO askokcancel

def quit() :
  ret = askokcancel ("!!!", "Sure to quit ?")
  if ret == True:
    root.destroy()
  if ret == False:
    print("False ?")
    
root = tk.Tk() 
tk.Button(root, width=40, height=10, text="Quit", command=quit).pack()
root.mainloop()


