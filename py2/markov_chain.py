from collections import defaultdict 
from random import random 

def histogram_counts(start, trans_probs, num_steps): 
	probs_dict = transform_probs(trans_probs)
	count_histogram = defaultdict(int)
	current_state = start 

	for i in range(num_steps): 
		count_histogram[current_state] += 1 
		next_state_val = next_state(current_state, probs_dict)
		current_state = next_state_val 

	return count_histogram

def next_state(current_state, probs_dict):
	r = random() 
	for state, probs in probs_dict[current_state].items(): 
		r -= probs 
		if r <= 0: 
			return state 

def transform_probs(trans_probs): 
	d = defaultdict(dict)
	for start, end, prob in trans_probs: 
		d[start][end] = prob 
	
	print(d)
	return d 

table = [
	('a', 'a', 0.9), 
	('a', 'b', 0.075), 
	('a', 'c', 0.025),

	('b', 'a', 0.15), 
	('b', 'b', 0.8), 
	('b', 'c', 0.05),

	('c', 'a', 0.25), 
	('c', 'b', 0.25), 
	('c', 'c', 0.5)
]

start = 'a'
num_steps = 100

end = histogram_counts(start, table, num_steps)

print(end)