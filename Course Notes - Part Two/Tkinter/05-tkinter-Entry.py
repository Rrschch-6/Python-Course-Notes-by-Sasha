
from tkinter import*
root=Tk()
root.title('My Window')

#Entry
en=Entry(root)
en.pack()
en.config(width=100)
en.get()

lb=Label(root)
lb.pack()

btn=Button(root,text='GET TEXT')
btn.pack()

def get_text():
    lb.config(text=en.get())

btn.config(command=get_text)

en.config(show='*')


