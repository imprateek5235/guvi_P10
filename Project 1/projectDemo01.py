import mysql.connector
from projectArt import boy
from tkinter import *
from projectLib import *


window=Tk()
window.title("Project_1__p-10")
print(f"welcome to student contact console base database application \n{boy}")

myDB = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="manager",
    database="guvi_py"
)

cursorDB = myDB.cursor()

while True:
    inp = userInput()
    if inp == 0:
        exit()
    elif inp == 1:
        queryDB = 'SELECT * FROM studentContact'
        cursorDB.execute(queryDB)
        list1=list()
        for result in cursorDB:
            list1.append(result)
        lbl = Label(window, text=f"{list1}", fg='black', bg='skyblue',width=50,height=10 )
        lbl.pack()
        window.mainloop()
    elif inp == 2:
        newRecord()
        queryDB = 'INSERT INTO studentContact (name, roll_no, contact_no, city) VALUES (%s,%s,%s,%s)'
        cursorDB.execute(queryDB, values)
    elif inp == 3:
        queryDB = 'SELECT * FROM studentContact WHERE roll_no LIKE %s'
        cursorDB.execute(queryDB, searchRoll_no())
        for result in cursorDB:
            print(result)
    elif inp == 4:
        queryDB = "DELETE FROM studentContact WHERE roll_no= %s"
        cursorDB.execute(queryDB, searchRoll_no())
    elif inp == 5:
        queryDB = 'UPDATE studentContact SET name=%s,contact_no=%s,city=%s WHERE roll_no= %s'
        cursorDB.execute(queryDB, updateRecord(searchRoll_no()))
    else:
        raise BadChoicError
    myDB.commit()

