from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 
import bisect 


class HitCounter1(object):
	def __init__(self): 
		self.hits = []

	def record(self, timestamp): 
		#self.hits.append(timestamp)
		bisect.insort_left(self.hits, timestamp)


	def total(self): 
		return len(self.hits)

	def range(self, lower, upper): 
		'''
		count = 0 
		for hit in self.hits: 
			if lower <= hit <= upper: 
				count += 1
		return count 

		'''
		left = bisect.bisect_left(self.hits, lower)
		right = bisect.bisect_right(self.hits, upper)

		return right - left 


		
class HitCounter2(object):
	def __init__(self): 
		self.hits = []
		self.counter = 0 

	def record(self, timestamp): 
		self.counter += 1 

		minute = floor(timestamp / 60)
		i = bisect.bisect_left([hit[0] for hit in self.hits], minute)

		if i < len(self.hits) and self.hits[0][0] == minute: 
			self.hits[i] = (minute, self.hits[i][1] + 1)
		else: 
			self.hits.insert(i, (minute, 1))


	def total(self): 
		return self.counter 

	def range(self, lower, upper): 
		'''
		count = 0 
		for hit in self.hits: 
			if lower <= hit <= upper: 
				count += 1
		return count 

		'''

		lower_minute = floor(lower / 60)
		upper_minute = floor(upper / 60)

		lower_i = bisect.bisect_left([hit[0] for hit in self.hits], 
							lower_minute)
		upper_i = bisect.bisect_right([hit[0] for hit in self.hits], 
							upper_minute)

		return sum(self.hits[i][1] for i in range(lower_i, upper_i))

		
