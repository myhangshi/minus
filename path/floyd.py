from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 
import bisect 

class Network: 
	def __init__(self, N, edges): 
		self.vertices = range(N+1)
		self.edges = edges 

	def make_graph(self): 
		graph = {v:[] for v in self.vertices}

		for u, v, w in self.edges: 
			graph[u].append((v,w))

		return graph 


def closure(graph): 
	n = len(graph)
	reachable = [ [0 for _ in range(n)] for _ in range(n)]

	print(reachable)
	print("*******************")

	for i, node in enumerate(graph): 
		for neighbor, cost in graph[node]: 
			reachable[node][neighbor] = 1

	print(reachable)
	print("*******************")
	
	for k in range(n): 
		for i in range(n): 
			for j in range(n): 
				reachable[i][j] |= (reachable[i][k] and reachable[k][j])

	return reachable


edges = [ 
	(0, 0, 5), 
	(0, 1, 3), 
	(0, 2, 4), 
	(0, 3, 8),
	(1, 1, 1), 
	(1, 2, 10),
	(2, 1, 5),
	(2, 2, 7),
	(3, 3, 8), 
]

N = 4

network = Network(N, edges)
graph = network.make_graph() 

print(edges)
print("Graph==================")
print(graph)


reach = closure(graph) 
print("Reach==================")
print(reach)





















