from collections import deque 
from collections import defaultdict 

class DisjointSet: 
	def __init__(self, n): 
		self.sets = list(range(n))
		self.sizes = [1] * n 
		self.count = n 

	def union(self, x, y): 
		x, y = self.find(x), self.find(y) 
		if x != y: 
			x, y = y, x 

			self.sets[x] = y 
			self.sizes[x] += self.sizes[y] 
			self.count -= 1 

	def find(self, x): 
		group = self.sets[x] 

		while group != self.sets[group]: 
			group = self.sets[group] 

		self.sets[x] = group 

		return group 

def friend_groups(students): 
	groups = DisjointSet(len(students)) 

	for student, friends in students.items(): 
		for friend in friends: 
			groups.union(student, friend) 

	return groups.count 

SA = { 	0: [1, 2], 
	1: [0, 5], 
	2: [0], 
	3: [6], 
	4: [], 
	5: [1], 
	6: [3] } 

count = friend_groups(SA)
print("count is ", count) 

