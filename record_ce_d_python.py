from subprocess import call
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from tkinter import font
import mysql.connector
from tkcalendar import DateEntry
import matplotlib.pyplot as plt 


#creating window
add_student_window = Tk()
add_student_window.geometry('500x300')
add_student_window.title('Add New Student')

#Define fontStyles
fontStyle_p = "arial 16 bold"
fontStyle_e = "arial 16"

#function of back button to move back to the previous page
def back():
    add_student_window.destroy()
    call(("python", "home.py"))
    
#creating back button
back_btn = Button(add_student_window, text="~ HOME", command = lambda : back())
back_btn.configure(font=('arial', 12, 'bold'), bg='yellow', fg='black')
back_btn.grid(column=0, row=0)


#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=1) 
e_date = DateEntry(add_student_window, width=12, background='darkblue', foreground='white', borderwidth=2)
e_date.grid(column=1, row=1)

#function of submit button to add new student into database
def submit_student():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="attendance_gui"
            )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ce_d_python WHERE date=%s"
    val = (e_date.get(),)
    mycursor.execute(sql, val)
    records = mycursor.fetchall()
    for i, attendance_gui in enumerate(records):
        date, sEnroll, sName, sRoll, status = attendance_gui
        ttk.Label(add_student_window, text=date).grid(row=i+8, column=2, sticky="nsew")   
        ttk.Label(add_student_window, text=sEnroll).grid(row=i+8, column=0, sticky="nsew")
        ttk.Label(add_student_window, text=sName).grid(row=i+8, column=1, sticky="nsew")
        ttk.Label(add_student_window, text=sRoll).grid(row=i+8, column=2, sticky="nsew")   
        ttk.Label(add_student_window, text=status).grid(row=i+8, column=2, sticky="nsew")   
        
    # Count total students
    sql = "SELECT * FROM ce_d_python WHERE date=%s"
    val = (e_date.get(),)
    mycursor.execute(sql, val)
    totalS = mycursor.fetchone()[0]

    # Count total present students
    sql = "SELECT * FROM ce_d_python WHERE date=%s AND status='Present'"
    val = (e_date.get(),)
    mycursor.execute(sql, val)
    presentS = mycursor.fetchone()[0]

    # Count total absent students
    absentS = totalS - presentS

    # Data to plot
    labels = 'Present Students', 'Absent Students'
    sizes = [presentS, absentS]
    colors = ['green', 'red']
    explode = (0.05, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%0.2f%%')

    #plt.axis('equal')
    plt.show()

#blank row  
blank = Label(add_student_window, text="").grid(column=0, row=55) 
#creating submit button
submit_btn = Button(add_student_window, text="Submit", command = lambda : submit_student())
submit_btn.configure(font=('arial', 14, 'bold'), bg='blue', fg='white')
submit_btn.grid(column=1, row=56)


add_student_window.mainloop()
    