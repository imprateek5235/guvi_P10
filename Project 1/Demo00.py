import mysql.connector
myDB=mysql.connector.connect(
host='127.0.0.1',
user="root",
password="manager",
database="guvi_py"
)
cursorDB=myDB.cursor()
queryDB='CREATE TABLE studentContact (name VARCHAR(30),roll_no TINYINT(2),contact_no BIGINT(10),city VARCHAR(30), PRIMARY KEY(roll_no))'
##############################################
# queryDB="DROP TABLE studentContact"
##################################
cursorDB.execute(queryDB)
myDB.commit()
print(cursorDB)


