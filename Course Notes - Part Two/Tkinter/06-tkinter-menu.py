
from tkinter import*
root=Tk()
root.title('My Window')

#menu
#01-define menubar and put it inside root
menubar=Menu(root)
root.config(menu=menubar)

#02-define filemenu object in menubar
filemenu=Menu(menubar)

def null():
    pass
#03-Add file menue commands
filemenu.add_command(label='New',command=null)
filemenu.add_command(label='Open',command=null)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.destroy)

#04-Add filemenu in menubar
menubar.add_cascade(label='File',menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label='select',command=null)

menubar.add_cascade(label='Edit',menu=editmenu)



