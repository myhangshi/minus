from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import random 

class Deck(object): 
	def __init__(self, seed=None): 
		self.cards = [ i for i in range(1,10) for _ in range(4) ]\
								+ [10] * 16

		random.seed(seed)
		random.shuffle(self.cards)

	def deal(self, start, n): 
		return self.cards[start:start + n]

class Player(object): 
	def __init__(self, hand): 
		self.hand = hand 
		self.total = 0 

	def deal(self, cards): 
		self.hand.extend(cards)
		self.total = sum(self.hand)

def cmp(x, y): 
	return (x > y) - (x < y)

def play(deck, start, scores): 
	player = Player(deck.deal(start, 2))
	dealer = Player(deck.deal(start+2, 2))

	results = [] 

	for i in range(49 - start): 
		count = start + 4 
		player.deal(deck.deal(count, i))
		count += i 

		if player.total > 21: 
			results.append((-1, count))
			break 

		while dealer.total < 17 and count < 52: 
			dealer.deal(deck.deal(count, 1))
			count += 1

		if dealer.total > 21: 
			results.append((1, count))
		else: 
			results.append((cmp(player.total, dealer.total),count))

	options = []
	for score, next_start in results: 
		options.append(score+scores[next_start] \
			if next_start <= 48 else score)

	scores[start] = max(options)


def blackjack(seed=None): 
	deck = Deck(seed)
	scores = [ 0 for _ in range(52)]

	for start in range(48, -1, -1): 
		play(deck, start, scores)

	return scores 

scores = blackjack()
print(scores)
