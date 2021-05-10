import thewaitinglist
from displayticket import display

def maketheticketlist(agent):
    file = open('waiting.txt','r').read()
    file = file.split('\n')
    listoftickets = thewaitinglist.ticketlist()

    for values in file:
        x = values.split(',')
        x[-1] = x[-1]
        if len(values)>2:
            listoftickets.addticket(x)

      
    agenttix = listoftickets.getthefirstticket(agent)
    newlist = listoftickets.makelist()
    return (agenttix,newlist)
def updatethewaitinglist(items:list):
    if len(items)>0:
        x = open("waiting.txt",'w')
        for lines in items:
            _ = ','.join(lines)
            _ = "%s%s"%(_,'\n')
            x.write(_)

    else:
        x = open("waiting.txt",'w')
        return "No items to add."


