
from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('My Window')
#Top level
root.resizable(False,False)

def openhelp():
    top=Toplevel()
    top.title('help')
    btn=Button(top,text='Exit',command=top.destroy)
    btn.pack()

btn1=Button(root,text='Open Help',command=openhelp)
btn1.pack()

root.destroy()#this will close both parent and child

top1=Toplevel()
top1.title('This is child of root')
top1.resizable(True,True)
    

top1.maxsize(500,500)
top1.minsize(150,150)
