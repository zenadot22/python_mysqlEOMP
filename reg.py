from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices314",database="lifechoicesonline",
                               host="127.0.0.1",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

window  = Tk()
window.geometry("500x500")
window.title("Register")
window.config(bg="green")
photo = PhotoImage(file = "index.png")
w = Label(window , image = photo)
w.pack()

idlabel = Label(window , text="id")
idlabel.place(x=200 , y=180)
idEntry = Entry(window , textvariable = "id" ,fg="white")
idEntry.pack()

namelabel = Label(window , text="full name")
namelabel.pack()
nameEntry = Entry(window , textvariable = "name" ,fg="white")
nameEntry.pack()

userlabel = Label(window , text="username")
userlabel.pack()
userEntry = Entry(window , textvariable = "username" ,fg="white")
userEntry.pack()

passlabel = Label(window , text="password")
passlabel.pack()
passEntry = Entry(window , textvariable = "password" ,fg="white")
passEntry.pack()

regButton = Button(window , text="Register" , bg = "black",fg="white")
regButton.pack()

window.mainloop()