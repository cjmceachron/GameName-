#project cheekymon
#5/16/2016
#Clayton McEachron
#cheekymon.py

from databaseMon import databaseMon
from element import element
from attack import attack
    
def buildDatabase(monFilePath, elementFilePath, attacksFilePath):
    #open files
    monFile = open(monFilePath, 'r')
    elementFile = open(elementFilePath, 'r')
    attackFile = open(attacksFilePath, 'r')
    
    #create monList
    #ignore first line
    monFile.readline()
    #readlines
    lines = monFile.readlines()
    monList = []
    #split line and append new mon to monList
    for member in lines:
        mLineInfo = member.split()
        monList.append(databaseMon(mLineInfo[0], mLineInfo[1], mLineInfo[2], mLineInfo[3], mLineInfo[4], mLineInfo[5], mLineInfo[6], mLineInfo[7], mLineInfo[8], mLineInfo[9] ))
    print ("MonList[3] points: %s" % (monList[3].points))

    #create elementList
    #ignore first line
    elementFile.readline()
    #readlines
    lines = elementFile.readlines()
    elementList = []
    #split line and append new element to elementList
    for member in lines:
        eLineInfo = member.split()
        elementList.append(element(eLineInfo[0], eLineInfo[1], eLineInfo[2] ))
    #test
    #for member in elementList:
        #print ("name: %s strength: %s weakness: %s " %( member.name, member.strength, member.weakness))

    #create attackList
    #ignore first line
    attackFile.readline()
    #readlines
    lines = attackFile.readlines()
    attackList = []
    #split line and append new attack to attackList
    for member in lines:
        aLineInfo = member.split()
        attackList.append(attack(aLineInfo[0], aLineInfo[1], aLineInfo[2], aLineInfo[3], aLineInfo[4], aLineInfo[5], aLineInfo[6]))
    #test
    #for member in attackList:
        #print ("name: %s element: %s : accuracy%s " %( member.name, member.element, member.accuracy))

        
print "main"
#build database in memory
buildDatabase("mon.data", "elements.data", "attacks.data")
#initialize game components

#main game loop



