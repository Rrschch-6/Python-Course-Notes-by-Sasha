#step 1
from tkinter import*

#step2
win=Tk()
win.title('My Window')

#step3
#creating widgets
#step4
#calling mainloop function

#widget=wisget(master or parent window,options1,opten2,option3,...)

#label

#lb=Label(win,text='Hello label').pack()
#as a method in this way we cannot config it later so:

lb=Label(win,text='Hello label')
lb.pack()
lb.config()  #shows all configurations


lb.config(font='mitrea')
lb.config(font=('Helvetica', 12,'bold'))
lb['font']='mitrea'
lb.config(wraplength=100) #number of characters in one line. change it to one and see the change

#for changing the test more easily
var=StringVar() #class

lb1=Label(win,textvariable=var)
var.set('This is text variable')
lb1.pack()
var.set('Changed variable')

lb.config(justify='left') #or you can use it as capital without ''
lb.config(bitmap='error')
lb.config(bitmap='question')
lb.config(bitmap='hourglass')
lb.config(bitmap='warning')
lb.config(bitmap='gray50')
lb.config(bitmap='gray75')
lb.config(bitmap='questhead')
lb.config(bitmap='info')

#changing background and foreground
lb.config(foreground='red')
lb.config(background='blue')

#pack is geometry managment function which has different options.
#as defult it places in top center. We will talk about this later

lb.pack(side='left')
