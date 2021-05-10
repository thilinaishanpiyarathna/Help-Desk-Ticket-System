from queue1 import waitingList
import os
os.system=('cls')
def makeList():
    newtix = waitingList()
    textfile = open("tickets.txt","r").read()
    lines = textfile.split('\n')
    lines = lines[:-1]
    for a_line in lines:
        newtix.insertTicket(a_line)
    return newtix.remainingTickets(),newtix.getTicket()