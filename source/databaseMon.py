#project cheekymon
#5/16/2016
#Clayton McEachron
#databaseMon.py

class databaseMon() :
    def __init__(self, name, points, element, hp, attack, defense, speed, move0, move1, move2 ):
        self.name = name
        self.points = points
        self.element = element
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = [move0, move1, move2]
