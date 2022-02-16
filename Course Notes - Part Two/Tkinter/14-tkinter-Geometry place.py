
from tkinter import*
from tkinter.filedialog import askopenfilename
root=Tk()
root.title('My Window')

#place
#to place the widget in exact coordinates

root.geometry("200x200")

btn1=Button(root,text='Apple')
btn1.place(x=10,y=10)

btn2=Button(root,text='Orange')
btn2.place(relx=0.2,rely=0.2)#btween 0-1
btn2.place(relx=0.2,rely=0.2,relheight=0.2,relwidth=0.2)
