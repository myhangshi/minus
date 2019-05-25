def binary_search(array, x): 
	low = 0
	high = len(array) - 1

	while low <= high: 
		mid = low + (high - low) // 2 

		if x == array[mid]: 
			return mid
		elif array[mid] > x: 
			high = mid -1 
		else: 
			low = mid + 1

	return -1 


print(binary_search([3, 5, 7, 9, 11, 13], 9))
