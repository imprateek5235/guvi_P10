name, roll_no, contact_no, city = None, None, None, None
values = [name, roll_no, contact_no, city]

class BadChoicError(Exception):
    def __init__(self, msg="Bad Choice Entered"):
        Exception.__init__(self, msg)


def newRecord():
    global values
    values = [input("Enter your name : "), int(input("Enter your roll_no : ")), int(
        input("Enter your contact_no : ")), input("Enter your city : ")]


def searchRoll_no():
      return [int(input("Enter your roll_no : ")), ]


def updateRecord(roll_no):
    value= [input("Enter your name : "), int(input("Enter your contact_no : ")), input("Enter your city : "),
            roll_no[0]]
    return value


def userInput():
    return int(input(
        "1 for show all records of students\n2 for add student Record\n3 for search by roll_no\n4 for delete student "
        "record by roll_no\n5 for update student record by roll_no\n0 for EXIT\nEnter your choice: "))
