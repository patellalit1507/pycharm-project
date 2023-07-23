from tkinter import *
import random
root=Tk()
root.geometry('400x400')

Label(root,text="input range ",font='arial 20 bold').pack()
Button(root,text='hii',font='arial 10').place(x=70,y=120)

n=random.randint(0,100)
print(n)
root.mainloop()