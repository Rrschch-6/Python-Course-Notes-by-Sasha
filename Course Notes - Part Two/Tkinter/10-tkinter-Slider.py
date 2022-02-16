
from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('My Window')

sc1=Scale(root,from_=0,to=50,length=200)
sc1.pack()
sc2=Scale(root,from_=0,to=100,orient='horizontal')
sc2.pack()

sc2.set(40)


def show_value():
    print(sc1.get(),sc2.get())

btn=Button(root,text='Get',command=show_value)
btn.pack()
