import heapq 

from collections import defaultdict 

def get_itenerary(flights, source, destination, k): 
	prices = defaultdict(dict)

	for u, v, cost in flights: 
		prices[u][v] = cost 

	path = [source]
	visited = set() 
	heap = [(0, source, k+1, path)]

	while heap: 
		cost, u, k, path = heapq.heappop(heap)
		visited.add(u)
		
		if u == destination: 
			return cost, path 

		if k > 0: 
			for v in prices[u]: 
				if v not in visited: 
					heapq.heappush(heap, 
						(prices[u][v] + cost, v, k-1, path+[v])
						)

	return -1 

flights = [ 
('JFK', 'ATL', 150), 
('ATL', 'SFO', 400), 
('ORD', 'LAX', 200), 
('LAX', 'DFW', 80), 
('JFK', 'HKG', 800), 
('ATL', 'ORD', 90), 
('JFK', 'LAX', 500), 
]

cost, path = get_itenerary(flights, 'JFK', 'LAX', 3)
print(cost)
print(path)


