from tkinter import*

root=Tk()


en=Entry(root,width=35,borderwidth=4)
en.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=en.get()
    en.delete(0,END)
    #delete ( first, last=None )
    #Deletes characters from the widget, starting with the one at index first, up to but not including the character at position last.
    #If the second argument is omitted only the single character at position first is deleted.
    en.insert(0,str(current)+str(number))
    #insert ( index, s )
    #Inserts string s before the character at the given index.

def button_clear():
    en.delete(0,END)

def button_add():
    first_number=en.get()
    global f_num
    f_num=int(first_number)
    en.delete(0,END)

def button_equal():
    second_number=en.get()
    en.delete(0,END)
    en.insert(0,f_num+int(second_number))

btn_1=Button(root,text='1',padx=40,pady=20,command=lambda: button_click('1'))
btn_2=Button(root,text='2',padx=40,pady=20,command=lambda: button_click('2'))
btn_3=Button(root,text='3',padx=40,pady=20,command=lambda: button_click('3'))
btn_4=Button(root,text='4',padx=40,pady=20,command=lambda: button_click('4'))
btn_5=Button(root,text='5',padx=40,pady=20,command=lambda: button_click('5'))
btn_6=Button(root,text='6',padx=40,pady=20,command=lambda: button_click('6'))
btn_7=Button(root,text='7',padx=40,pady=20,command=lambda: button_click('7'))
btn_8=Button(root,text='8',padx=40,pady=20,command=lambda: button_click('8'))
btn_9=Button(root,text='9',padx=40,pady=20,command=lambda: button_click('9'))
btn_0=Button(root,text='0',padx=40,pady=20,command=lambda: button_click('0'))
btn_add=Button(root,text='+',padx=39,pady=20,command=button_add)
btn_clear=Button(root,text='Clear',padx=79,pady=20,command=button_clear)
btn_equal=Button(root,text='=',padx=91,pady=20,command=button_equal)



btn_7.grid(row=1,column=0,padx=1,pady=1)
btn_8.grid(row=1,column=1,padx=1,pady=1)
btn_9.grid(row=1,column=2,padx=1,pady=1)
btn_6.grid(row=2,column=0,padx=1,pady=1)
btn_5.grid(row=2,column=1,padx=1,pady=1)
btn_4.grid(row=2,column=2,padx=1,pady=1)
btn_3.grid(row=3,column=0,padx=1,pady=1)
btn_2.grid(row=3,column=1,padx=1,pady=1)
btn_1.grid(row=3,column=2,padx=1,pady=1)
btn_0.grid(row=4,column=0,padx=1,pady=1)

btn_clear.grid(row=4,column=1,columnspan=2)

btn_add.grid(row=5,column=0)
btn_equal.grid(row=5,column=1,columnspan=2)

