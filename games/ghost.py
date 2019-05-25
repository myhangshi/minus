from collections import deque
from collections import defaultdict 

ENDS_HERE='#'

class Trie: 
	def __init__(self, words): 
		self._trie = {}
		for word in words: 
			self.insert(word)

	def insert(self, text): 
		trie = self._trie 
		for c in text: 
			if c not in trie: 
				trie[c] = {}
			trie = trie[c]
		trie[ENDS_HERE] = True 

	def find(self, prefix): 
		trie = self._trie 

		for c in prefix: 
			if c in trie: 
				trie = trie[c]
			else: 
				return None
		return trie 

def is_winning(trie, prefix): 
	root = trie.find(prefix)

	if '#' in root: 
		print('False', prefix)
		return False 
	else: 
		next_moves = [prefix + letter for letter in root]
		print('NE', next_moves)
		if any(is_winning(trie, move) for move in next_moves): 
			print('False', prefix)
			return False 
		else: 
			print('True', prefix)
			return True 

def optimal_starting_letter(words): 
	trie = Trie(words)
	winners = []

	starts = trie._trie.keys() 
	for letter in starts: 
		print(letter, "inside optimal")
		if is_winning(trie, letter): 
			winners.append(letter)

	return winners

#words = ['cat', 'calf', 'dog', 'bear']

words = ['cat', 'coat', 'bear', 'dog']

print(optimal_starting_letter(words))














