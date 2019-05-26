from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import random 

def has_valid_word_length(grid): 
	for row in grid: 
		word_length = 0 

		for square in row: 
			if square == 0: 
				word_length += 1 
			else: 
				if 0 < word_length < 3: 
					return False 
				word_length = 0

		if 0 < word_length < 3: 
			return False 
	
	return True 

def is_rotationally_symmetric(grid): 
	transpose = list(zip(*grid))
	reverse = transpose[::-1]

	#transpose = list(zip(*grid))
	#reverse = transpose[::-1]

	return grid == list(map(list, reverse))

def is_connected(grid): 
	#check how many white squares there are in the grid 
	count = sum([1-square for row in grid for square in row])

	start = None 
	for i, row in enumerate(grid): 
		for j in row: 
			if grid[i][j] == 0: 
				start = (i, j)
				break 

	if not start: 
		return False 

	queue = deque([start])
	visited = set() 
	connected_count = 0 

	while queue: 
		square = queue.popleft() 

		if square not in visited: 
			visited.add(square)
			connected_count += 1 

			i, j = square 
			for adj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]: 
				row, col = adj 
				if (0 <= row < len(grid) and 0 <= col <len(grid) and \
					grid[row][col] == 0): 
					queue.append(adj)

	return count == connected_count

def is_valid(grid): 
	return has_valid_word_length(grid) and \
			has_valid_word_length(zip(*grid)) and \
			is_rotationally_symmetric(grid) and is_connected(grid) 






