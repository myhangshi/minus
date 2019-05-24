class BIT: 
	def __init__(self, nums): 
		self.tree = [0 for _ in range(len(nums)+1)] 
		for i, num in enumerate(nums): 
			self.update(i+1, num) 

	def update(self, index, value): 
		while index < len(self.tree): 
			self.tree[index] += value 
			index += index & -index 

	def query(self, index): 
		total = 0 
		while index > 0: 
			total += self.tree[index]
			index -= index & -index 
		return total 
	

class Subscribers: 
	def __init__(self, nums): 
		self.bit = BIT(nums) 
		self.nums = nums 

	def update(self, hour, value): 
		self.bit.update(hour+1, value - self.nums[hour]) 
		self.nums[hour] = value 

	def query(self, start, end): 
		return self.bit.query(end+1) - self.bit.query(start) 

sub = Subscribers([0]*24)
print(sub.query(3, 11)) 
print(sub.query(10, 13)) 
sub.update(1, 10) 
sub.update(3, 2)
sub.update(10,2) 
sub.update(12, 4) 

print(sub.query(3, 11)) 
print(sub.query(10, 13)) 
print(sub.query(0, 13)) 
