from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(user="lifechoices",password="@Lifechoices314",database="lifechoicesonline",
                               host="127.0.0.1",auth_plugin="mysql_native_password")


window = Tk()
window.title("Admin")
window.geometry("500x500")
window.config(bg="green")


my_conn = mydb.cursor()
my_conn.execute("SELECT full_name FROM users limit 0,5")
i=0
for users in my_conn:
    for j in range(len(users)):
        my_listbox = Listbox(window, width="50",height="1")
        my_listbox.pack()
        my_listbox.insert(END , users[j])
        i=i+1




# my_listbox = Listbox(window , width="50")
# my_listbox.pack(pady = 15)

# my_listbox.insert(END, "This is a second item")
# my_listbox.insert(END, "second item")

# my_list = ["one" , "two" , "three","one" , "two" , "three"]

# for item in my_list:
#     my_listbox.insert(END , item)

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text="")

def select():
    my_label.config(text = my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0 , END)

my_button = Button(window , text = "Delete" ,bg="black",fg="white", command =delete)
my_button.pack()

my_button2 = Button(window , text = "Add User" , bg="black",fg="white",command =select)
my_button2.pack()

my_button3 = Button(window , text = "delete all" ,bg="black",fg="white", command =delete_all)
my_button3.pack()

global my_label
my_label = Label(window , text="")
my_label.pack()



window.mainloop()



