
from tkinter import*
from tkinter.filedialog import askopenfilename
root=Tk()
root.title('My Window')

#to place the widget in exact coordinates

root.geometry("200x200")

lb1=Label(root,text='Label number 1',bg='red')
lb2=Label(root,text='Label number 2',bg='blue')
lb3=Label(root,text='Label number 3',bg='green')

lb1.place(x=20,y=30,width=120,height=30)
lb2.place(x=20,y=65,width=120,height=30)
lb3.place(x=20,y=100,width=120,height=30)
