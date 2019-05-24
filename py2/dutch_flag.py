def dutch_flag(array): 
	low, mid, high = 0, 0, len(array) - 1

	while mid <= high: 
		if array[mid] == 'R': 
			array[low], array[mid] = array[mid], array[low]
			low += 1 
			mid += 1
		elif array[mid] == 'G': 
			mid += 1
		else: #array[mid] == 'B'
			array[mid], array[high] = array[high], array[mid]
			high -= 1 
	
	return array 

AL = ['R', 'B', 'G', 'R', 'B', 'B', 'G', 'R', 'R']
print(AL)
print(dutch_flag(AL))
