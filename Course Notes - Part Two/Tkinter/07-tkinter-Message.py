
from tkinter import*
root=Tk()
root.title('My Window')

#Message
M=StringVar()
ms=Message(root,textvariable=M)
ms.pack()
M.set('This is the Message') #Despite Label it aligns automaticly

#Message Box

from tkinter import messagebox
def Hello():
    messagebox.showinfo('BOX','This is a message box')


btn=Button(root,text='Click',command=Hello)
btn.pack()

