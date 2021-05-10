from os import system
from makeque import makeList
import pprint
from displayticket import display
from makealist import maketheticketlist
from makealist import updatethewaitinglist
import datetime
from thecompletedtickets import addtothecompletedlisttxt
system("cls")
username = ''
def creds():
    global username
    username = input("Input your username \n")
    password = input("Input your password \n")
    return username,password
def certify():
    user = ["Ishan"]
    username,password = creds()
    if username in user and password == "1999":
        return True
    else:
        return False
def log():
    if certify():
        system("cls")
        print("Login successful \n\n ")
    else:
        system("cls")
        print("Invalid credentials input the credentials again \n")
        log()
log()
newticket,update = maketheticketlist(username)
if type(newticket) ==list:
    display([','.join(newticket)])
    closeddate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if len(newticket)>3:
        newticket.append(closeddate)
        addtothecompletedlisttxt(newticket)
        updatethewaitinglist(update)