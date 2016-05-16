#project cheekymon
#5/16/2016
#Clayton McEachron
#cheekymon.py

    
def buildDatabase(monFilePath, typesFilePath, attacksFilePath):
    #open files
    monFile = open(monFilePath, 'r')
    typesFile = open(typesFilePath, 'r')
    attacksFile = open(attacksFilePath, 'r')
    print (monFile.readline())
    
    lines = monFile.readlines()
    length = len(lines)
    #monlist = [ databaseMon() for i in range(length)]
    i = 0
    for member in lines:
        lineInfo = member.split()
        #1st need to figure out how to do multi file program
        #need to initialize databaseMon using the members of lineInfo as parameters
        for member in lineInfo:
            print "..%s"% member

        
print "main"
#build database in memory
buildDatabase("mon.data", "types.data", "attacks.data")
#initialize game components

#main game loop



