class thecompletedlist():
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items)<1
    def addtothelist(self,item):
        self.items.append(item)

    def removefromthelist(self,item):
        if self.isempty()!=True:
            return self.items.append()
        else:
            return "no completed tickets"
    def thelastcompleted(self):
        if self.isempty()!=True:
            lt = self.items[-1]
            return lt
            
        else:
            return "empty list"
    
        

def addtothecompletedlisttxt(items):
    file = open("txcompletedtickets.txt",'a')
    _ = ','.join(items)
    __ = "%s%s"%(_,'\n')
    file.write(__) 

def getlast():
    stack = thecompletedlist()
    readit = open('txcompletedtickets.txt','r').read()
    readit = readit.split('\n')
    readit = readit[:len(readit)-1]
    for lines in readit:
        stack.addtothelist(lines)
    return stack.thelastcompleted() 