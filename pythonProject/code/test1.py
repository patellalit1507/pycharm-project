from tkinter import *
import time
import datetime
import winsound

alarm=Tk()
alarm.title("ALARM ")
alarm.geometry('500x400')
format_label=Label(alarm,text='set time in 24 hr format ',fg='red',bg='yellow',font=('Arial',10,'bold')).pack()
set_time=Label(alarm,text='Hrs  Min  Sec',font=('Arial',17,'bold')).place(x=170,y=120)




def ala(set_time):
   while True:
       time.sleep(1)
       current_time=datetime.datetime.now()
       now=current_time.strftime("%H:%M:%S")
       datenow=current_time.date()
       print(now)
       print(set_time)
       if now==set_time:
           print("time to wake up ")
           winsound.PlaySound("systemexit",winsound.SND_ALIAS)

           break






def alarm_time():
     set_time=f'{hours.get()}:{Mins.get()}:{Secs.get()}'
     ala(set_time)

hours=StringVar()
Mins=StringVar()
Secs=StringVar()

hours_time=Entry(alarm,textvariable=hours,bg='pink',font=('Arial',12,"bold"),width='5').place(x=170,y=150)
Min_time=Entry(alarm,textvariable=Mins,bg='pink',font=('Arial',12,"bold"),width='5').place(x=220,y=150)
Sec_time=Entry(alarm,textvariable=Secs,bg='pink',font=('Arial',12,"bold"),width='5').place(x=270,y=150)
set_button=Button(alarm,text='set',font=('arial',15,'bold'),command=alarm_time).place(x=220,y=180)

alarm.mainloop()
