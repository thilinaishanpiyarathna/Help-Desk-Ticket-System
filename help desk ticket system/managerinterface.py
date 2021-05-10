from os import system
from makeque import makeList
import pprint
from displayticket import display
from displayticket import displaycompleted
from thecompletedtickets import thecompletedlist
from addingtoWaitinglist import addtowaitinglist
from thecompletedtickets import getlast


agents_dic = {1:"Mohan",2:"Randika",3:"Nipuni",4:"Ishan",5:"Asha"}
system("cls")
def creds():
    username = input("Input your username \n")
    password = input("Input your password \n")
    return username,password
def certify():
    username,password = creds()
    un,pw="Thilina","1996"
    if un==username and pw==password:
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

allofthem,returned = makeList()
if returned!=None:
    print("The remaining tickets\n\n")
    display(allofthem)
    print("The current ticket\n")
    display([returned])
    pick_An_Agent = input("1 for Mohan , 2 for Randika , 3 for Nipuni , 4 for Ishan , 5 for Asha\n")
    agent_Is = agents_dic[int(pick_An_Agent)]
    print(agent_Is) 
    addtowaitinglist(returned+","+agent_Is)
checkornot = input("Do you want to see the latest information on tickets Y for yes and N for no \n type here...")
if checkornot=='Y'or checkornot=='y':
    displaycompleted([getlast()])
else:
    pass