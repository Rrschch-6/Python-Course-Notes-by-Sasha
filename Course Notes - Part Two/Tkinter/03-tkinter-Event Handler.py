
from tkinter import*
root=Tk()
root.title('My Window')

lb=Label(text='Change my color')
lb.pack()

def change_red():
    lb.config(fg='red')

def change_blue():
    lb.config(fg='blue')

btn1=Button(text='RED',command=change_red)
btn2=Button(text='BLUE',command=change_blue)
btn3=Button(text='CLOSE',command=root.destroy)

btn1.pack()
btn2.pack()
btn3.pack()



