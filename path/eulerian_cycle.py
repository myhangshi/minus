from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
from itertools import product 

import heapq 
import bisect 

def make_graph(C, k):
	# Use Cartesian product to get all strings of length k+1 
	vertices = product(C, repeat=k-1)
	print(vertices)

	edges = {}
	for v in vertices: 
		edges[v] = [ v[1:] +  (char,)  for char in C]
	
	print(edges)
	return edges 

def find_eulerian_cycle(graph): 
	cycle = []
	start = list(graph)[0]
	before = after = []
	#print(list(graph))

	while graph: 
		if cycle: 
			#Find the next vertex to expand into a cycle 
			start = next(vertex for vertex in cycle if vertex in graph)
			index = cycle.index(start)
			before = cycle[:index] 
			after = cycle[index+1:]

		cycle = [start]
		prev = start 

		while True:
			curr = graph[prev].pop() 
			if not graph[prev]: 
				graph.pop(prev)

			cycle.append(curr)
			if curr == start: 
				break 

			prev = curr 

		cycle = before + cycle + after 


	return cycle 

def debruijin(C, k): 
	graph = make_graph(C, k)

	cycle = find_eulerian_cycle(graph)
	sequence = [v[-1] for v in cycle[:-1]]

	return sequence 



C = {0, 1}
k = 3

graph = debruijin(C, k)

print("Graph==================")
print(graph)





















