from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 
import bisect 

class Quack
	def __init__(self): 
		self.right = [] 
		self.left = []
		self.buffer = []

	def push(self, x): 
		self.left.append(x) 

	def pop(self): 
		if not self.left and not self.right: 
			print("No more elements pop")
			return 

		if not self.left: 
			size = len(self.right)

			for _ in range(size // 2): 
				self.buffer.append(self.right.pop())

			while self.right: 
				self.left.append(self.left.pop())

			while self.buffer: 
				self.right.append(self.buffer.pop())

		return self.left.pop() 

	def pull(self): 
		if not self.left and not self.right: 
			print("No more elements pull")
			return 

		if not self.right: 
			size = len(self.left)

			for _ in range(size): 
				self.buffer.append(self.left.pop())

			while self.left: 
				self.right.append(self.left.pop())

			while self.buffer: 
				self.left.append(self.buffer.pop())

		return self.right.pop() 












