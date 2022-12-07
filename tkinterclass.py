import tkinter
from tkinter import *
from PIL import Image, ImageTk

class MainWindow:

    name: str

    def __init__(self, name, title, width, height,color):

        self.name = name = tkinter.Tk()
        name.resizable(False, False)
        name.title(title)
        name.geometry(f"{width}x{height}")
        name['background'] = color

class MyTopLevelWin:
    
    name: str
    
    def __init__(self, name, title, width, height, color, parent):
    
        self.name = name = Toplevel(parent.name)
        name.title(title)
        name.geometry(f"{width}x{height}")
        name['background'] = color
        name.resizable(False,False)
        name.mainloop()

class MyFrame:

    name: str

    def __init__(self, name, width, height, color, side, parent):

        self.name = name = Frame(parent.name, bg=color, width=width, height = height)

        if parent == "false":
            name.pack_forget()
        else:
            name.pack(side = side)

class MyButton:

    name: str
    text: str
    textcolor: str
    buttoncolor: str
    
    def __init__(self, name, text, textcolor, buttoncolor):
        
        self.name = name
        self.text = text
        self.textcolor = textcolor
        self.buttoncolor = buttoncolor
    
    def put(self, width, height, parent,x, y, funcname):
              
        if funcname == "false":
            self.name = Button(parent.name, text = self.text, fg = self.textcolor, bg = self.buttoncolor)
            self.name.config(height=height,width=width)
            self.name.place(x = x, y = y )
        else:
            self.name = Button(parent.name, text = self.text, fg = self.textcolor, bg = self.buttoncolor, command = funcname)
            self.name.config(height=height,width=width)
            self.name.place(x = x, y = y )