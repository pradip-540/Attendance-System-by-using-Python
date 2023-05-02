import matplotlib.pyplot as plt 
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="attendance_gui")
mycursor = mydb.cursor()

# Count total students
mycursor.execute("SELECT COUNT(*) FROM ce_d_python")
totalS = mycursor.fetchone()[0]

# Count total present students
mycursor.execute("SELECT COUNT(*) FROM ce_d_python WHERE status = 'Present'")
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