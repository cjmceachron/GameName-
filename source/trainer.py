# Project Cheekymon
# Rob D'Andrea
# 5/16/2016
# trainer.py

class Trainer():
	'Base class for human and computer trainers'
	
	def __init__(self, name, cheekymons, saved_mons, location, stats, inventory): #texture ids?
		self. name = name
		self.cheekymons = cheekymons # list of Mon objects between 0-6 mons at a time
		self.saved_mons = saved_mons # list of Mons not in cheekymons but owned
		self.location = location # ["zone", x, y]
		self.stats = stats
		self.inventory = inventory
		
# Split into two children, human and ai
# Human has inputs
# ai has a path and engagement zone
