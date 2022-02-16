
from tkinter import*
from tkinter.filedialog import askopenfilename
root=Tk()
root.title('My Window')

#open Dialog Box

def Open_file():
    name=askopenfilename(filetype=(("Text File","*.txt"),("All Files","*.*")))
    print(name)

btn=Button(root,text='Open File',command=Open_file)
btn.pack()

from tkinter.colorchooser import*
def getcolor():
    color=askcolor()
    print(color) #prints RGB and HEX

btn1=Button(root,text='Choose Color',command=getcolor)
btn1.pack()
