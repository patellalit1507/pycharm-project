import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):


        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy).pack(side='left')
        self.label=tk.Label(self,text="hiii",fg='green',font=("arial",20)).pack(side='bottom')
        self.hi_there.pack()

    def texxt(self):
        ls = random.choice(['kai', 'che', 'bhiai', 'aru'])
        return ls


    def say_hi(self):

        print("hi there, everyone!")
        ls = ["hiii", 'ssdsd', 'sdsadsa', 'sadsdasd', 'adada']
        t=self.texxt()
       # My_text=random.choice(ls2)
        self.hi_there.configure(text=random.choice(ls))
        self.hi_there.text = random.choice(ls)
        self.label.config(text=t)







root = tk.Tk()
root.geometry('400x400')
root.title("congig")
app = Application(master=root)
app.mainloop()