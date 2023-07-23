from tkinter import *

root=Tk()
root.geometry('400x400')
root.title("my first programm ")
Label(root,text='hello world ',font="arial 20 bold").pack()
Label(root,text='this is jhon doe',font="arial 20 bold").pack()

def madlib1():
   # Label(root,text='hii we are here ',font='arial 30 bold').place(x=60,y=100)
    print('hiii')

    return 1;
def madlib2():
    print("hello")
    return 2
def madlib3():
    print("john doe")
    return 4

Button(root,text="adventure",font='arial 10',command=madlib1).place(x=60,y=120)
Button(root,text="home",font='arial 10',command=madlib2).place(x=60,y=160)
Button(root,text="garden garden",font='arial 10',command=madlib3).place(x=60,y=200)


root.mainloop()
