def shifted_array_search(lst, num): 
	i = len(lst) // 2 
	dist = i // 2 

	while True: 
		if lst[0] > lst[i] and lst[i-1] > lst[i]: 
			break 
		elif dist == 0: 
			break 
		elif lst[0] <= lst[i]: 
			i += dist 
		elif lst[i-1] <= lst[i]: 
			i -= dist 
		else: 
			break 
		dist = dist // 2 

	low = i
	high = i - 1
	dist = len(lst) // 2

	while True: 

		if dist == 0: 
			return None 

		guess_ind = (low + dist) % len(lst)
		guess = lst[guess_ind]

		if guess == num: 
			return guess_ind

		if guess < num: 
			low = (low + dist) % len(lst)
		if guess > num: 
			high = (len(lst) + high - dist) % len(lst)

		dist = dist // 2 


arr = [13, 18, 25, 2, 8, 10]
num = 8
print("find", num, "in arr: ", arr)

ff = shifted_array_search(arr, num)

print("found:", ff)
print("arr: ", arr)





