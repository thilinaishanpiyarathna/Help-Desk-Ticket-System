class aticket():
    def __init__(self,data=None):
        self.ticketdata = data
        self.next = None    

class ticketlist():
    def __init__(self):
        self.firstticket = None
    
    def traverse(self):
        cur = self.firstticket
        while cur:
            print(cur.ticketdata)
            cur = cur.next
            
    def addticket(self,data):
        newticket = aticket(data)
        if self.firstticket is None:
            self.firstticket = newticket
            return

        cur = self.firstticket
        while cur.next:
            cur = cur.next
        cur.next = newticket

    def addtofront(self,data):
        newticket =aticket(data)
        newticket.next = self.firstticket
        self.firstticket = newticket
    def insert_after_ticket(self, search, data):
        cur = self.firstticket
        while cur.ticketdata is not search and cur.next !=None:
            cur = cur.next
        if cur.ticketdata!=search and cur.next == None:
            print("no such")      
        else:
            new_ticket = aticket(data)
            new_ticket.next = cur.next
            cur.next = new_ticket
    def getthefirstticket(self,agent):
        cur = self.firstticket
        if cur==None:
            print("No tickets here")
            return
        
        if cur.ticketdata[-1] == agent and cur.next==None:
            self.firstticket =None
            return cur.ticketdata
        elif cur.ticketdata[-1] == agent and cur.next!=None:
            self.firstticket =cur.next
            return cur.ticketdata
        while  cur.next !=None and cur.next.ticketdata[-1] is not agent :
            cur = cur.next
        if cur.ticketdata[-1]==agent and cur.next == None:
            x = cur.ticketdata
            cur = None
            return x  
        elif cur.ticketdata[-1]!=agent and cur.next == None:
            print("Not tickets assigned to you at the moment.")
        else:
            delete = cur.next
            cur.next = delete.next
            delete.next = None
            return delete.ticketdata
        
               
    def makelist(self):
        cur = self.firstticket
        list1 = []
        while cur:
            list1.append(cur.ticketdata)
            cur = cur.next
        return list1


