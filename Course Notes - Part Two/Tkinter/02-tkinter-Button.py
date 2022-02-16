
from tkinter import*
root=Tk()
root.title('My Window')

#Buttons

btn=Button(root,text='Click')
btn.pack()
#configurations of button
btn.config(font='Arial')
btn.config(foreground='red') #or fg
btn.config(border=10)#or bd
btn.config(activebackground='blue')
btn.config(activeforeground='orange')
btn.config(padx=10)
btn.config(pady=10)
btn.config(state='disable')
btn.config(state='active')

#check button

x=StringVar()
y=StringVar()

cb1=Checkbutton(root,text='Tomato',variable=x,onvalue='Yes',offvalue='No')
cb2=Checkbutton(root,text='Cheese',variable=y,onvalue='Yes',offvalue='No')
cb1.pack()
cb2.pack()

x.get()
y.get()

#RadioButton
#differance with check button is the fact that we can only choose one item.
rb1=Radiobutton(root,text='High')
rb2=Radiobutton(root,text='Low')
option=IntVar()
rb1.config(variable=option,value=5)
rb2.config(variable=option,value=0)
rb1.pack()
rb2.pack()
option.get()
