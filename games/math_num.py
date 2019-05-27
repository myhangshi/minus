from collections import deque
from collections import defaultdict 
from collections import OrderedDict 

def is_valid(letters, words): 
	a, b, c = words 
	n = len(c)

	carry = 0 
	for i in range(n-1, -1, -1): 
		if any(letters[word[i]] is None for word in words): 
			return True 
		elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]]: 
			carry = 0 
		elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]] + 10: 
			carry = 1
		else: 
			return False 

	return True 


def is_valid_complete(letters, words): 
	a, b, c = words 
	n = len(c)

	#print("checking.... ", letters )
	#print("words   .... ", words )
	
	carry = 0 
	for i in range(n-1, -1, -1): 
		if any(letters[word[i]] is None for word in words): 
			#print("ANY ", carry, letters[a[i]], letters[b[i]], 
			#	         	 letters[c[i]]    )
			if letters[b[i]] and letters[c[i]] : 
				return letters[b[i]] + carry == letters[c[i]]  
			if letters[a[i]] and letters[c[i]] : 
				return letters[a[i]] + carry == letters[c[i]] 
			return carry == 1 and letters[c[i]]  == carry 
		elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]]: 
			#print("CARRY0 ", carry, letters[a[i]], letters[b[i]], 
			#	         	 letters[c[i]]  )
			carry = 0 
		elif letters[a[i]] + letters[b[i]] + carry == letters[c[i]] + 10: 
			#print("CARRY1 ", carry, letters[a[i]], letters[b[i]], 
			#	         	 letters[c[i]]  )
			
			carry = 1
		else: 
			#print("ELSE ", carry, letters[a[i]], letters[b[i]], 
			#	         	 letters[words[2]]  )
			
			return False 

	return True 

def solve(letters, unassigned, nums, words): 
	if not unassigned: 
		if is_valid_complete(letters, words): 
			#print("SOLUTION ....", letters)
			return letters
		else: 
			return None 

	char = unassigned[0]
	for num in nums: 
		letters[char] = num 
		nums.remove(num)

		if is_valid(letters, words): 
			solution = solve(letters, unassigned[1:], nums, words)
			if solution: 
				return solution 

		nums.add(num)
		letters[char] = None 

	return False 

def ordered_letters(words): 
	n = len(words[2])

	letters = OrderedDict() 
	for i in range(n-1, -1, -1): 
		for word in words: 
			if word[i] not in letters: 
				letters[word[i]] = None 
	#print(letters)
	#print("==================")
	return letters 

def normalize(word, n): 
	diff = n - len(word) 
	return ['#' for _ in range(diff)] + word 

def math_num(problem): 
	#Input problem is given as [word, word, total]
	words = list(map(list, problem))

	n = len(words[2])
	words[0] = normalize(words[0], n)
	words[1] = normalize(words[1], n)
	#print(words)

	letters = ordered_letters(words)
	unassigned = [letter for letter in letters if letter != '#']
	print("letters ", letters, unassigned)
	nums = set(range(0, 10))

	#print(letters)
	return solve(letters, unassigned, nums, words)

problem = ['SEND', 'MORE', 'MONEY']
print(problem)

m_num = math_num(problem)
print(m_num)
words = list(map(lambda x: list(m_num[i] for i in x), problem))
print(words)


