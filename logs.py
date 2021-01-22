from tkinter import *
from tkinter import messagebox
import mysql.connector




mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices314",database="lifechoicesonline",
                               host="127.0.0.1",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()
def LOGS():
    user=userEntry.get()
    passs= passEntry.get()
    sql='select * from users WHERE username = %s and password = %s'
    mycursor.execute(sql, [(user), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    messagebox.showinfo("LOG IN MESSAGE","Log in successful!")
    import mobile

def failed():
    messagebox.showinfo("login unsuccessful!")
    userEntry.delete(0,END)
    passEntry.delete(0,END)
    window.withdraw()



def register():
    def insertdb():
        id1 = idEntry.get()
        fullname=nameEntry.get()
        user = userEntry.get()
        passs = passEntry.get()
        mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices314", database="lifechoicesonline",
                                       host="127.0.0.1", auth_plugin="mysql_native_password")
        mycursor = mydb.cursor()
        sql = 'INSERT INTO users(id , full_name,username,password) VALUES(%s,%s,%s,%s)'
        val = (id1,fullname,user,passs)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("REGISTRY","Registration successful")

        print(mycursor.rowcount,"inserted")

    print("test")
    # get all values from the entries.
    # Write INSERT sql state to add values in the database
    # Display message confirming user registration
    window = Tk()
    window.title("Registering A User!")
    window.geometry("500x500")
    window.config(bg="green")


    myLabel = Label(window,text="REGISTER!")
    myLabel.pack()

    idlabel = Label(window , text="id")
    idlabel.pack()
    idEntry = Entry(window , textvariable = "id" )
    idEntry.pack()

    namelabel = Label(window , text="full name")
    namelabel.pack()
    nameEntry = Entry(window , textvariable = "name" )
    nameEntry.pack()

    userlabel = Label(window, text="username")
    userlabel.pack()
    userEntry = Entry(window, textvariable="username")
    userEntry.pack()

    passlabel = Label(window, text="password")
    passlabel.pack()
    passEntry = Entry(window, textvariable="password")
    passEntry.pack()

    regButton = Button(window, text="Register" ,command=insertdb)
    regButton.pack()

    window.mainloop()






window  = Tk()
window.geometry("500x500")
window.title("LOGIN")
window.config(bg="green")
photo = PhotoImage(file = "index.png")
w = Label(window , image = photo)
w.pack()


userlabel = Label(window , text="username")
userlabel.pack()
userEntry = Entry(window , textvariable = "username")
userEntry.pack()

passlabel = Label(window , text="password")
passlabel.pack()
passEntry = Entry(window , textvariable = "password" )
passEntry.pack()

logButton = Button(window , text="Login",bg="black",fg="white", command=LOGS)
logButton.pack()

messlabel = Label(window , text="new at lifechoices?")
messlabel.pack()
regButton = Button(window , text="Admin", bg="black",fg="white",command=register)
regButton.pack()
window.mainloop()