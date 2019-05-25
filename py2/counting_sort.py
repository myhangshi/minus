def counting_sort(array, digit, base=10): 
	counts = [[] for _ in range(base)]

	bs = base ** digit 
	for num in array: 
		d = (num // bs) % base 
		counts[d].append(num)

	result = []
	for bucket in counts: 
		result.extend(bucket)

	return result 

def radix_sort(array, digit=10): 
	for digit in range(digit): 
		array = counting_sort(array, digit)

	return array 

arr = [4, 100, 54, 537, 2, 89]

new_arr = radix_sort(arr, 10)

print("arr: ", arr)
print("new arr:", new_arr)




