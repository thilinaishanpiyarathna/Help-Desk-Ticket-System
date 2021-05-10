from os import system
class ticket():
    def __init__(self,user,location,telephone,email,details,date,serial):
        self.user = user
        self.location = location
        self.telephone = telephone
        self.email = email
        self.details = details
        self.date = date
        self.serial = serial
        
        
        if not str(self.telephone).isdigit():
            print("Enter a valid telephone number")

        elif not "@" in str(self.email):
            print("Enter a valid email")

        elif len(str(self.details))<1:
            print("Your can leave the details-field empty")
        else:
            system("cls")
            print("ticket made\n")
            print("%s,%s,%s,%s,%s,%s,%s\n"%(user,location,telephone,email,details,date,serial))
            open("tickets.txt",'a').write("%s,%s,%s,%s,%s,%s,%s\n"%(user,location,telephone,email,details,date,serial))
            
        