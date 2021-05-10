def addtowaitinglist(items:list):
    data = items.split(',')
    print(data)
    xx = open('waiting.txt','a')
    xx.write(items+'\n')