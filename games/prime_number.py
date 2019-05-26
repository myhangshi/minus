from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 

def prime1(n): 
	is_prime = [False] * 2 + [True]*(n-1)

	for x in range(2, n): 
		if is_prime[x]: 
			for i in range(2 * x, n, x): 
				is_prime[i] = False 

	for i in range(n): 
		if is_prime[i]: 
			yield i 


def prime2(n): 
	is_prime = [False] * 2 + [True]*(n-1)

	for x in range(2, int(n**0.5)): 
		if is_prime[x]: 
			for i in range(x**2, n, x): 
				is_prime[i] = False 

	for i in range(n): 
		if is_prime[i]: 
			yield i 


def prime3(n): 

	composite = [] 
	i = 2 

	while True: 

		if composite and i == composite[0][0]: 
			while composite[0][0] == i: 
				multiple, p = heapq.heappop(composite)
				heapq.heappush(composite, [multiple+p, p])
		else: 
			heapq.heappush(composite, [i * i, i])
			yield i 

		i += 1 

	