
from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('My Window')
#Frame

lb=Label(root,text='Top')
frame=Frame(root,bd=5,relief='sunken')
frame.pack()#its empty now so it is not visible

btn1=Button(frame,text='Click1')
btn1.pack()

btn2=Button(frame,text='Click2')
btn2.pack(side='left')

btn3=Button(frame,text='Click3')
btn3.pack(side='left')

#15 pixel gap frame and root borders
frame.pack(fill='x',padx=15,pady=15)
#20 pixel gap bet  ween widgets and frame border
frame.config(padx=20,pady=20)

#Label Frame
lf=LabelFrame(root,text='I am Label Frame')
lf.pack()
lb3=Label(lf,text='I am inside the frame')
lf.config(labelanchor='n')
lb3.pack()
