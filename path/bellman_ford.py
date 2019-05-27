from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 
import bisect 
from math import log 



class Network: 
	def __init__(self, N, edges): 
		self.vertices = range(N+1)
		self.edges = edges 

	def make_graph(self): 
		graph = {v:[] for v in self.vertices}

		for u, v, w in self.edges: 
			graph[u].append((v,w))

		return graph 

def arbitrage(graph): 

	transformed_graph = [[-log(float(graph[row][edge] + 10.0)) for edge in graph[row] ] for row in edges_1]

	source = 0 
	n = len(transformed_graph)

	min_dist = [float('inf')] * n 
	print(n)
	print(transformed_graph)
	print(min_dist)

	min_dist[source] = 0 

	for i in range(n - 1): 
		for v in range(n): 
			for w in range(n): 
				if min_dist[w] > min_dist[v] + transformed_graph[v][w]: 
					min_dist[w] = min_dist[v] + transformed_graph[v][w] 

	for v in range(n): 
		for w in range(n): 
			if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
				return (v, w)

	return None 

 


edges_1 = {
	'USD': {'USD':1.00, 'GBP':0.77, 'INR':71.71, 'EUR':0.87 }, 

	'GBP': {'USD':1.30,  'GBP':1.00, 'INR':93.55, 'EUR':1.14}, 

	'INR': {'USD':0.014, 'GBP':0.011, 'INR':1.00, 'EUR':0.014}, 

	'EUR': {'USD':1.14, 'GBP':0.88, 'INR':81.95, 'EUR':1.00}, 
}

times = arbitrage(edges_1)
print(times)


print("Second Time ", "*" * 30)
edges_1 = {
	'USD': {'USD':1.00, 'GBP':0.77, 'INR':71.71, 'EUR':0.87 }, 

	'GBP': {'USD':1.30,  'GBP':1.00, 'INR':93.55, 'EUR':1.14}, 

	'INR': {'USD':0.014, 'GBP':0.011, 'INR':1.00, 'EUR':0.014}, 

	'EUR': {'USD':1.14, 'GBP':0.88, 'INR':81.95, 'EUR':1.00}, 
}

times = arbitrage(edges_1)
print(times)






























