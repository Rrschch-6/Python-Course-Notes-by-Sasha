from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


def callExcel():
    dirExcel.set(askopenfilename(filetypes=(("Excel Files","*.xlsx"),("All Files","*.*"))))
def saveExcel():
    dirOutput.set(askdirectory())

#window creation
win=Tk()
win.geometry('360x440')
win.title('Pandas Exercise')
win.resizable(width=False,height=False)

menubar=Menu(win)
win.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)
#filemenu.add_command(label='Reset',command=reset)
filemenu.add_command(label='Exit',command=win.destroy)
menubar.add_cascade(label='File',menu=filemenu)

dirExcel=StringVar()
dirOutput=StringVar()

def callExcel():
    dirExcel.set(askopenfilename(filetypes=(("Excel Files","*.xlsx"),("All Files","*.*"))))
def saveExcel():
    dirOutput.set(askdirectory())
def prnt():
    print(dirExcel.get())
    print(dirOutput.get())

#file_open=askopenfilename(filetypes=(("Excel Files","*.xlsx"),("All Files","*.*")))
#print(file)

#file_save=askdirectory()
#print(file_save)

#btn1=Button(win,text='Input')
#btn2=Button(win,text='Output')

#btn1.pack()
#btn2.pack()

btn1=Button(win,text='Input',command=callExcel)
btn2=Button(win,text='Output',command=saveExcel)
btn3=Button(win,text='print',command=prnt)
btn1.pack()
btn2.pack()
btn3.pack()


