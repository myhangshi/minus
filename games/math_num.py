from collections import deque
from collections import defaultdict 
from collections import OrderedDict 

def is_valid(letters, words): 
	a, b, c = words 
	n = len(c)

	carry = 0 
	for i in range(n-1, -1, -1): 
		if any(letters[words[i]] is None for word in words): 
			return True 
		elif letters[a[i]] + letters[b[i]] + carry == letter[c[i]]: 
			carry = 0 
		elif letters[a[i]] + letters[b[i]] + carry == letter[c[i]] + 10: 
			carry = 1
		else: 
			return False 

	return True 

def solve(letters, unassigned, nums, words): 
	if not unassigned: 
		if is_valid(letters, words): 
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
	
	return letters 

def normalize(word, n): 
	diff = n - len(word) 
	return ['#']*diff + word 

def math_num(problem): 
	#Input problem is given as [word, word, word]
	words = list(map(list, problem))

	n = len(words[2])
	words[0] = normalize(words[0], n)
	words[1] = normalize(words[1], n)

	letters = ordered_letters(words)
	unassigned = [letter for letter in letters if letter != '#']
	nums = set(range(0, 10))

	return solve(letters, unassigned, nums, words)

problem = ['SEND', 'MORE', 'MONEY']

m_num = math_num(problem)
print(problem)



