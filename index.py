from subprocess import call
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox


home = Tk()
home.title("Varification Page")
home.geometry('450x350')
home.iconbitmap("logo.png")
        
def login():
    username = e_username.get()
    password = e_password.get()
    
    if(username=="admin" and password=="123"):
        home.destroy()
        call(["python", "home.py"])  
    else:
        messagebox.showinfo("Worng Password", "Incorrect username or password!")

img_s = Image.open("logo.png")
img_s = img_s.resize((250,150))
img = ImageTk.PhotoImage(img_s)
lable = Label(image = img).grid(column=2,row=1)

fontStyle_h = "arial 20 bold underline"
fontStyle_p = "arial 16 bold"
fontStyle_e = "arial 14"

l1 = Label(home, text="Validation Page", font= fontStyle_h).grid(column=2, row=2)

#blank row
blank = Label(home, text="").grid(column=1, row=4)
#Label's   
username = Label(home, text="Username: ", font= fontStyle_p)
username.grid(column=1, row=5)
password = Label(home, text="Password: ", font= fontStyle_p)
password.grid(column=1, row=6)

#Entry's
e_username = StringVar()
username = Entry(home, textvariable=e_username, font= fontStyle_e)
username.grid(column=2, row=5)
e_password = StringVar()
password = Entry(home, textvariable=e_password, font= fontStyle_e)
password.grid(column=2, row=6)

blank1 = Label(home, text="").grid(column=1, row=7)

login = Button(home, text="Login", command = login, height=1, width=10, font="arial 16 bold")
login.configure(font=('arial', 15, 'bold'), bg='blue', fg='white')
login.grid(column=2, row=8)

home.mainloop()