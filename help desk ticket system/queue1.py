import copy
class waitingList():
    def __init__(self,item=None):
        self.items=[]

    def insertTicket(self,item):
        self.items.append(item)

    def remainingTickets(self):
        return self.items
    def isempty(self):
        return len(self.items)<1

    def getTicket(self):
        if self.isempty() !=True:
            tic = self.items.pop(0)
            self.updateText()
            return tic
        else:
            print("No tickets in the ticket list")
            return

    def getList(self):
        return self.items
    def updateText(self):
        textfile = open("tickets.txt",'w')
        lines = self.getList()
        linus = copy.deepcopy(lines)
        linus.reverse()
        for line in linus:
            textfile.write(line + "\n")
    
