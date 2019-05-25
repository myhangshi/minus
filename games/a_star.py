import heapq 
from copy import copy 

class Board: 
	def __init__(self, nums, goal='123456780'):
		self.goal = list(map(int, goal))
		self.tiles = nums 
		self.empty = self.tiles.index(0) 
		self.original = copy(self.tiles)
		





