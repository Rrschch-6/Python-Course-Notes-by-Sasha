
from tkinter import*
from tkinter.filedialog import askopenfilename
root=Tk()
root.title('My Window')

#we have 3 layout manager pack() grid() place()
#only one can be used

btn1=Button(root,text='Apple')
btn2=Button(root,text='Orange')
btn3=Button(root,text='Cherry')

btn1.pack()
btn2.pack()
btn3.pack()

btn1.pack(fill='x')
btn1.pack(fill='x',padx=10,pady=10)

btn2.pack(ipadx=10,ipady=10)

btn1.pack(fill='x',padx=10,pady=10,side='left')
btn2.pack(fill='x',padx=10,pady=10,side='left')
btn3.pack(fill='x',padx=10,pady=10,side='left')

