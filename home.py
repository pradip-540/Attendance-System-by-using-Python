import calendar
from subprocess import call
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import mysql.connector as mysql

root = Tk()
root.title("Home")
root.geometry('550x450')
root.iconbitmap("logo.png")
        
def insert():
    branch = e_branch.get()
    division = e_division.get()
    subject = e_subject.get()
    
    if(branch=="B.Tech" and division=="CE-D" and subject=="Python"):
        root.destroy()
        call(["python", "ce_d_python.py"])
    elif(branch=="B.Tech" and division=="CE-D" and subject=="Operating System"):
        root.destroy()
        call(["python", "ce_d_os.py"])
        
    elif(branch=="BCA" and division=="BCA-D" and subject=="Python"):
        root.destroy()
        call(["python", "bca_d_python.py"]) 
    elif(branch=="BCA" and division=="BCA-D" and subject=="Operating System"):
        root.destroy()
        call(["python", "bca_d_os.py"]) 
    else:
        messagebox.showinfo("Alert", "Please select right choices!") 


fontStyle_h = "arial 20 bold underline"
fontStyle_p = "arial 14 bold"

img_s = Image.open("logo.png")
img_s = img_s.resize((250,150))
img = ImageTk.PhotoImage(img_s)
lable = Label(image = img).grid(column=1,row=0)

l1 = Label(root, text="Student Attendence Page", font=fontStyle_h).grid(column=1, row=1)
blank = Label(root, text="").grid(column=0, row=2)   
   
#Label's  
branch = Label(root, text="Select Branch: ", font=fontStyle_p)
branch.grid(column=0, row=3)
division = Label(root, text="Select Division: ", font=fontStyle_p)
division.grid(column=0, row=5)
subject = Label(root, text="Select Subject: ", font=fontStyle_p)
subject.grid(column=0, row=4)

#Entry's
e_branch = StringVar(root)
e_branch.set("Select Branch") # default value
w = OptionMenu(root, e_branch, "B.Tech", "BCA")
w.configure(font=('arial', 12), bg='lightgray', fg='black')
w.grid(column=1, row=3)
e_division = StringVar(root)
e_division.set("Select Division") # default value
w1 = OptionMenu(root, e_division, "CE-D", "BCA-D")
w1.configure(font=('arial', 12), bg='lightgray', fg='black')
w1.grid(column=1, row=5)
e_subject = StringVar(root)
e_subject.set("Select Subject") # default value
w = OptionMenu(root, e_subject, "Python", "Operating System")
w.configure(font=('arial', 12), bg='lightgray', fg='black')
w.grid(column=1, row=4)

blank = Label(root, text="").grid(column=1, row=6)   
insert = Button(root, text="Mark Attendance", command =insert, font="arial 12 bold")
insert.configure(font=('arial', 16, 'bold'), bg='blue', fg='white')
insert.grid(column=1, row=7)

#close function
def back():
    root.destroy()
    
blank = Label(root, text="").grid(column=0, row=8)   
#creating close button
back_btn = Button(root, text="X Close", command = lambda : back())
back_btn.configure(font=('arial', 13, 'bold'), bg='red', fg='white')
back_btn.grid(column=1, row=9)


root.mainloop()