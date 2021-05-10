def display(listis:list):
    print("{:<20}".format("USERNAME"),"{:<20}".format("CITY"),"{:<13}".format("TELEPHONE"),"{:<30}".format("EMAIL"),"{:<40}".format("PROBLEM"),"{:<25}".format("Opened Date"),"{:<10}".format("Serial"),"{:<10}".format("Agent"),"{:<30}".format("Closed date"))
    print("*"*220)
    for lines in listis:
        data = lines.split(',')
        
        name = str(data[0])
        city = str(data[1])
        tele = str(data[2])
        email =str(data[3])
        problem = str(data[4])
        o_Date = str(data[5])
        serial = str(data[6])
         

        print("{:<20}".format(name),"{:<20}".format(city),"{:<13}".format(tele),"{:<30}".format(email),"{:<40}".format(problem),"{:<25}".format(o_Date),"{:<10}".format(serial))
        print("*"*220)
def displaycompleted(items):
    print("{:<20}".format("USERNAME"),"{:<20}".format("CITY"),"{:<13}".format("TELEPHONE"),"{:<30}".format("EMAIL"),"{:<40}".format("PROBLEM"),"{:<25}".format("Opened Date"),"{:<10}".format("Serial"),"{:<10}".format("Agent"),"{:<30}".format("Closed date"))
    print("*"*220)
    for lines in items:
        data = lines.split(',')
        
        name = str(data[0])
        city = str(data[1])
        tele = str(data[2])
        email =str(data[3])
        problem = str(data[4])
        o_Date = str(data[5])
        serial = str(data[6])
        agent = str(data[7])
        c_Date = str(data[8])

        print("{:<20}".format(name),"{:<20}".format(city),"{:<13}".format(tele),"{:<30}".format(email),"{:<40}".format(problem),"{:<25}".format(o_Date),"{:<10}".format(serial),"{:<10}".format(agent),"{:<30}".format(c_Date))
        print("*"*220)
