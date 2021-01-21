from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices314",database="lifechoicesonline",
                               host="127.0.0.1",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

window  = Tk()
window.geometry("250x150")
window.title("mobile")
window.config(bg="green")

numlabel = Label(window , text="Mobile-number")
numlabel.pack()
numEntry = Entry(window , textvariable = "number" ,fg="black")
numEntry.pack()

okButton = Button(window , text="OK" , bg = "black", fg="white")
okButton.pack()

window.mainloop()