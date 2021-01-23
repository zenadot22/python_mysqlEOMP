from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Admin")
window.geometry("600x400")
window.config(bg="lightgreen")

def mylog():
    from logs import register
    register()

    messagebox.showinfo("LOG MESSAGE","Logged in successfully")

H_label = Label(window, text="ADMIN LOG!",bg="lightgreen")
H_label.place(x=220 , y=50)
H_label.config(font=("Courier", 44))

mylabel = Label(window , text="username")
mylabel.place(x=200 , y=100)
myEntry = Entry(window , textvariable = "username")
myEntry.place(x=300 , y=100 , width=120)

nlabel = Label(window , text="password" )
nlabel.place(x=200 , y=140)
nEntry = Entry(window , textvariable = "password",width=45 )
nEntry.place(x=300,y=135,width=120)

logButton = Button(window , text="Login",bg="black",fg="white",command=mylog)
logButton.place(x=200 , y=220,width=80)



window.mainloop()