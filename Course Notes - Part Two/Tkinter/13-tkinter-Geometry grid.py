
from tkinter import*
from tkinter.filedialog import askopenfilename
root=Tk()
root.title('My Window')

#grid creats a table in our window 0,0
#number of column and rows depend on number of widgets

btn1=Button(root,text='Apple')
btn1.grid(row=0,column=0)
btn2=Button(root,text='Orange')
btn2.grid(row=0,column=1)
btn3=Button(root,text='Cherry')
btn3.grid(row=1,column=0,columnspan=2) #ocupies 2 columns
btn4=Button(root,text='banana')
btn4.grid(row=0,column=2,rowspan=2) #ocupies 2 rows
btn5=Button(root,text='melon')
btn5.grid(row=1,column=3,padx=20,pady=20)
