# Project Cheekymon
# Rob D'Andrea
# 5/16/2016
# mon.py

class Mon:
	'Container class for cheekymons'
	
	def __init__(self, name, element, hp, attack, defence, speed, moves):
		self.name = name
		self.nick_name = ""
		self.element = element
		self.hp = hp
		self.max_hp = hp
		self.attack = attack
		self.defence = defence
		self.speed = speed
		self.moves = moves #Moves is meant to be a list
