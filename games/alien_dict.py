from collections import deque
from collections import defaultdict 
from collections import OrderedDict 


def create_graph(words): 
	letters = set(''.join(words))

	graph = {letter: set() for letter in letters}

	for pair in zip(words, words[1:]): 
		for before, after in zip(*pair): 
			if before != after: 
				graph[after].add(before)
				break 
	return graph 


def topo_sort(graph): 
	todo = deque([letter for letter, prev in graph.items() 
					if not prev])

	letter_to_next = defaultdict(list)
	for letter, prevs in graph.items(): 
		for prev in prevs: 
			letter_to_next[prev].append(letter)

	result = []
	while todo: 
		letter = todo.popleft() 
		result.append(letter)

		for n in letter_to_next[letter]: 
			graph[n].remove(letter)
			if not graph[n]: 
				todo.append(n)

	if len(result) < len(graph): 
		return None 

	return result 

def alien_letter_order(words): 
	graph = create_graph(words)
	return topo_sort(graph)

words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
result = alien_letter_order(words)
print(result)




