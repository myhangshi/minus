EMPTY = 0 

def suduko(board): 

	if is_complete(board): 
		return board

	r, c = find_first_empty(board) 

	for i in range(1, 10): 
		board[r][c] = i 
		if valid_so_far(board): 
			result = suduko(board) 
			if is_complete(board): 
				return result 
		board[r][c] = EMPTY 
	
	return board 

def is_complete(board): 
	return all(all(val is not EMPTY for val in row) for row in board) 

def find_first_empty(board): 
	for i, row in enumerate(board): 
		for j, val in enumerate(row): 
			if int(val) == EMPTY: 
				return i, j 

def valid_so_far(board): 
	if not rows_valid(board): 
		return False
	if not cols_valid(board): 
		return False 
	if not blocks_valid(board): 
		return False
	return True 

def rows_valid(board): 
	for row in board: 
		if duplicates(row): 
			return False
	return True 

def cols_valid(board): 
	for j in range(len(board[0])): 
		if duplicates([board[i][j] for i in range(len(board))]): 
			return False
	return True 

def  blocks_valid(board): 
	for i in range(0, 9, 3): 
		for j in range(0, 9, 3): 
			block = [] 
			for k in range(3): 
				for l in range(3): 
					block.append(board[i+k][j+l])
			if duplicates(block): 
				return False 
	return True 

def duplicates(arr): 
	c = {}
	for val in arr: 
		if val in c and val is not EMPTY: 
			return True 
		c[val] = True 
	return False 

ol = [	'006008070', '100600400', '004210003',
	 	'001080090', '260030184', '080060300', 
	 	'600045700', '005001006', '010900500']

sk = []

for i, nums in enumerate(ol): 
	sk.append(list(nums))

print(sk)

sk1 = [[0]*len(sk[0]) for _ in range(len(sk))]
print(sk1)

#convert to integer type 
for i, row in enumerate(sk): 
	for j, col in enumerate(row):
		sk1[i][j] = int(sk[i][j]) #- int('0')

print("\n\n")
print(sk1)



print("\n\n\n")
print(suduko(sk1))
