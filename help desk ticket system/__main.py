from os import system
import datetime
from _ticketclass import ticket
import random
system("cls")



user = input("Enter you username \n")
location  = input("Enter your location \n")
telephone = input("Enter your telephone number \n")
email = input("Enter your email  \n")
details = input("Enter your problem \n")
date_place = datetime.datetime.now()
date = "{:%Y-%m-%d %H:%M:%S}".format(date_place)



serial = open('w_latestserialnum.txt','r').read()
serialnew = int(serial)+1
writenew = open('w_latestserialnum.txt','w')
writenew.write(str(serialnew))
writenew.close()





my_tic = ticket(user,location,telephone,email,details,date,serial)






