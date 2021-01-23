from tkinter import *
from tkinter import messagebox
import mysql.connector
from datetime import datetime
now = datetime.now()
formatted = now.strftime('%Y-%M-%D %H:%M:%S')

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
         sql = "INSERT INTO LOGIN_OUT ("
    else:
        failed()

def logged():
    messagebox.showinfo("LOG IN MESSAGE","Log in successful!")
    myquery = "INSERT INTO LOGIN_OUT VALUES (%s,%s,user_id,time)"
    mycursor.execute("SELECT * FROM LOGIN_OUT")


def failed():
    messagebox.showinfo("LOG IN MESSAGE","login unsuccessful!")
    userEntry.delete(0,END)
    passEntry.delete(0,END)
    window.withdraw()

def admin_log():
    import log_ad


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
    window.config(bg="black")
    # photo = PhotoImage(file="index.png")
    # w = Label(window, image=photo)
    # w.pack()


    myLabel = Label(window,text="REGISTER!",bg="lightgreen")
    myLabel.place(x=200 , y=50)
    myLabel.config(font=("Courier", 30))

    idlabel = Label(window , text="idNumber")
    idlabel.place(x=200 , y=100)
    idEntry = Entry(window , textvariable = "id")
    idEntry.place(x=300 , y=100 , width=120)

    namelabel = Label(window , text="full name" )
    namelabel.place(x=200 , y=140)
    nameEntry = Entry(window , textvariable = "name",width=45 )
    nameEntry.place(x=300,y=135,width=120)

    userlabel = Label(window, text="username")
    userlabel.place(x=200,y=180)
    userEntry = Entry(window, textvariable="username")
    userEntry.place(x=300, y=200, width=120)

    passlabel = Label(window, text="password")
    passlabel.place(x=200,y=220)
    passEntry = Entry(window, textvariable="password")
    passEntry.place(x=300,y=230,width=120)

    regButton = Button(window, text="Register" ,bg="lightgreen",command=insertdb)
    regButton.place(x=280 , y=300,width=80)

    backButton = Button(window, text="Back", bg="lightgreen", command=logged)
    backButton.place(x=320, y=330, width=80)

    window.mainloop()

window  = Tk()
window.geometry("600x400")
window.title("LOGIN")
window.config(bg="lightgreen")
photo = PhotoImage(file = "index.png")
w = Label(window , image = photo)
w.pack()

userlabel = Label(window , text="username")
userlabel.place(x=180 , y = 200)
userEntry = Entry(window , textvariable = "username", width=45)
userEntry.place(x = 300 , y=200 , width =120)

passlabel = Label(window , text="password")
passlabel.place(x=180 , y=250)
passEntry = Entry(window , textvariable = "password",width=45 )
passEntry.place(x=300 ,y= 250,width=120)

logButton = Button(window , text="Login",bg="black",fg="white", command=LOGS)
logButton.place(x=200 , y=300,width=80)

regButton = Button(window , text="Admin", bg="black",fg="white",command=register)
regButton.place(x=320,y=300 ,width=80)

window.mainloop()