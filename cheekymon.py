#project cheekymon
#5/16/2016
#Clayton McEachron
#cheekymon.py

def main ():
    print ("main")
    #build database in memory
    buildDatabase("mon.data", "types.data", "attacks.data")
    #initialize game components

    #main game loop


def buildDatabase(monFilePath, typesFilePath, attacksFilePath):
    #open files
    file_object = open(filename, mode)
    monFile = open(monFilePath, r)
    typesFile = open(typeFilePath, r)
    attacksFile = open(attacksFilePath, r)
    print (file.readline(monFile))
