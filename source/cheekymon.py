#project cheekymon
#5/16/2016
#Clayton McEachron
#cheekymon.py

from databaseMon import databaseMon
from element import element
from attack import attack
from trainer import Trainer
from mon import Mon
import random
from random import randrange

def getPlayerName():
    print "What is your name?"
    playerName = raw_input()
    print "playerName = %s" %playerName
    return playerName

def buildPlayerTeam(monList, points):
    playerTeam = []
    while points > 0:
        print "points remaining: %s.\nType the name of the cheekymon you want " %points
        monToAdd = raw_input()
        isMon = 0
        for member in monList:
            if member.name == monToAdd:
                isMon = 1
                if int(member.points) <= points:   
                    points = points - int(member.points)
                    playerTeam.append(Mon(member.name, member.element, int(member.hp), int(member.attack), int(member.defense), int(member.speed), member.moves))
                else:
                    print "Not enough points remaining to add that cheekymon to your team."
        if isMon == 0:
            print "not a valid mon name."
    for member in playerTeam:
        member.max_hp = member.hp
    return playerTeam

def buildAiTeam(monList, points):
    aiTeam = []
    while points > 0:
        print "points remaining: %s." %points
        i = randrange(0, 7) # 0 to number of mons
        if int(monList[i].points) <= points:   
                    points = points - int(monList[i].points)
                    print "add %s " % monList[i].name
                    aiTeam.append(Mon(monList[i].name, monList[i].element, int(monList[i].hp), int(monList[i].attack), int(monList[i].defense), int(monList[i].speed), monList[i].moves))
        #else:
             #print "Not enough points remaining to add that cheekymon to your team."
    for member in aiTeam:
        member.max_hp = member.hp
    return aiTeam
        
    
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
    #print ("MonList[3] points: %s" % (monList[3].points))

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
        #print"%s %s %s %s %s %s %s "%(aLineInfo[0], aLineInfo[1], aLineInfo[2], aLineInfo[3], aLineInfo[4], aLineInfo[5], aLineInfo[6])
        attackList.append(attack(aLineInfo[0], aLineInfo[1], aLineInfo[2], aLineInfo[3], aLineInfo[4], aLineInfo[5], aLineInfo[6]))
    #test
    #for member in attackList:
        #print ("name: %s element: %s : accuracy%s " %( member.name, member.element, member.accuracy))

    return monList, elementList, attackList
        
print "main"
#build database in memory
monList, elementList, attackList = buildDatabase("mon.data", "elements.data", "attacks.data")
#initialize game components
player = Trainer(getPlayerName(), buildPlayerTeam(monList, 10), 1, 1, 1, 1)
aiTeam = buildAiTeam(monList, 8)
#main game loop



