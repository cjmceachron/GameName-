
class Mon:
	'Container class for cheekymons'
	
	def __init__(self, name, type, hp, attack, defence, speed, moves)
		self.name = name
		self.nick_name = ""
		self.type = type
		self.hp = hp
		self.max_hp = hp
		self.attack = attack
		self.defence = defence
		self.speed = speed
		self.moves = moves #Moves is meant to be a list