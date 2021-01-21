from tkinter import *
from tkinter import messagebox
import mysql.connector
mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices314",database="lifechoicesonline",
                               host="127.0.0.1",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

def LOGS():
    user=userEntry.get()
    passs= passEntry.get()
    sql='select * from LOGIN_OUT WHERE username = %s and password = %s'
    mycursor.execute(sql, [(user), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            messagebox.showinfo("Log in successful!")
            break
    else:
        failed()

def logged():
    messagebox.showinfo("Log in successful!")

def failed():
    messagebox.showinfo("login unsuccessful!")
    userEntry.delete(0,END)
    passEntry.delete(0,END)
    window.withdraw()
    import reg
    reg.status()

window  = Tk()
window.geometry("500x500")
window.title("LOGIN")
window.config(bg="white")
photo = PhotoImage(file = "index.png")
w = Label(window , image = photo)
w.pack()





userlabel = Label(window , text="username")
userlabel.pack()
userEntry = Entry(window , textvariable = "username" ,fg="black")
userEntry.pack()

passlabel = Label(window , text="password")
passlabel.pack()
passEntry = Entry(window , textvariable = "password" ,fg="black")
passEntry.pack()

logButton = Button(window , text="Login", command=LOGS)
logButton.pack()

messlabel = Label(window , text="new at lifechoices?")
messlabel.pack()
regButton = Button(window , text="Register", command=LOGS)
regButton.pack()
window.mainloop()