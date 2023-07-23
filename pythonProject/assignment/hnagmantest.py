import random
import tkinter
import time
import string

root=tkinter.Tk()
root.title("the hangman")
root.geometry("800x400")
count_label=tkinter.Label(root,text="welocme",font=("arial",20,"bold")).pack()
count_label=tkinter.Label(root,text="length",font=("arial",13,"bold")).place(x=80,y=120)
count_label=tkinter.Label(root,text="guess left",font=("arial",13,"bold")).place(x=260,y=120)
count_label=tkinter.Label(root,text="wrong gussed",font=("arial",13,"bold")).place(x=460,y=120)
#global lenght
global word
global wrong_guess
global count
count=8
def main():
    global length
    global word
    #global count
    global wrong_guess
    global index
    global already_guessed
    global dip_lab
    global temp
    already_guessed=[]
    wrong_guess=[]
    global display
    words = ['shyam', 'hello', 'karma', 'vintage', 'astronout', 'mobile', 'source', 'gamer', "january",
             "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]


    word=random.choice(words)
    temp=word
    print(word)
    lenght=len(word)
    display="_"*lenght


main()

dip_len=tkinter.Label(root,text=len(word),font=(5)).place(x=140,y=116)

t=tkinter.StringVar()



def counter():
    global word
    global index
    global already_guessed
    global wrong_guess
    global display
    global count
    global temp
    guess=t.get()
    guess.strip()
    if len(guess)>=2 or len(guess)==0 :
        error_msg=tkinter.Label(root,text='ERROR!\n invalid submission',fg="Red",font=("bold")).place(x=200,y=300)

    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+"_" +word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display)
        print(word)
        dip_lab.config(text=display)
        if display==temp:
            print("you won")

    else:

        if count>0:
          count=count-1
          guess_left.config(text=count)
          wrong_guess.extend([guess])
          wrong_g.config(text=wrong_guess)

        else:
            lost = tkinter.Label(root, text='ERROR!\n invalid submission', fg="Red", font=("bold")).place(x=200,y=500)






global alp
global get_button
alp=tkinter.Entry(root,textvariable=t,bg="pink",font="Arial",width=8).place(x=200,y=250)
dip_lab = tkinter.Label(root, text=display, font="bold")
guess_left=tkinter.Label(root,text=8,font=(5))
wrong_g=tkinter.Label(root,text=wrong_guess,font=(5))

get_button=tkinter.Button(root,text="submit",command=counter)
dip_lab.place(x=120, y=60)
guess_left.place(x=350,y=116)
wrong_g.place(x=600,y=116)
get_button.place(x=120, y=250)
















root.mainloop()