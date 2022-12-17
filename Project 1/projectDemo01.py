import mysql.connector
from projectArt import boy

print(f"welcome to student contact console base database application \n{boy}")
from projectLib import *

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
        for result in cursorDB:
            print(result)
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
