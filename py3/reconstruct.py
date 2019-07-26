def reconstruct(array): 
	answer = []
	n = len(array) - 1
	stack = [] 

	i = 0 
	while i < n: 
		print("loop in ", i, array[i+1])
		if array[i+1] == '-': 
			stack.append(i) 
		else: 
			
			#answer.append(i) 
			#i = i + 1
			answer.append(i) 
			while stack: 
				answer.append(stack.pop()) 
		i = i + 1 
	
	stack.append(n) 
	while stack: 
		answer.append(stack.pop()) 
	

	return answer 

array = [None, '+', '-', '-','-', '+', '+','-'] 
print("the array is ", array)
print("the answer is ", reconstruct(array)) 



