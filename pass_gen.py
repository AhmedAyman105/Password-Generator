# imports 
from tkinter import *
import random
from tkinter import messagebox

# root
my_app = Tk()
my_app.geometry("550x300")
my_app.resizable(False,False)
my_app.title("Password Generator")
my_app.iconbitmap(r"images\logo.ico")
my_app.configure(bg="#75C2F6")


# Functionality
def generate() :
    if input.get() != '' :
        try :
            letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSUVWXYZ123456789!@#$%^&*()_+"
            Length = int(input.get())
            word = "".join(random.sample(letters,Length))
            password.set(word)
        except Exception :
            messagebox.showerror("Error","Password length must be integer number not float , character")
    else:
        messagebox.showerror("Error","Please input password length")


########################################################
#######################   GUI   ########################
########################################################

title = Label(my_app,text='@? Password Generator @!',font=('cairo','16','bold'),bg="#75C2F6",fg='#f2f2f2')
title.place(relx=.5,rely=.1,anchor='center')


input = Entry(my_app,font=('cairo','10'),width=50,justify='center',highlightcolor='#231f20',highlightthickness=1)
input.place(relx=.5,rely=.5,anchor='center',y=-50)


btn1 = Button(text=" Generate ",font=('cairo',11,'bold'),borderwidth=0,fg="white",bg='#0a369d',activebackground='#00a6fb',command=generate)
btn1.place(relx=.5,rely=.5,anchor='center',y=30)


password = IntVar()
password.set('')


result = Entry(my_app,font=('cairo','10'),width=50, textvariable = password ,justify='center',highlightcolor='#231f20',highlightthickness=1)
result.place(relx=.5,rely=.5,anchor='center',y=100)


my_app.mainloop()