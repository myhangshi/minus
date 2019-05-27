from collections import deque
from collections import defaultdict 
from collections import OrderedDict 
import heapq 
import bisect 

def find_matches_1(pattern, string): 
	matches = []
	k = len(pattern)

	for i in range(len(string) - k + 1):  
		if string[i:i+k] == pattern: 
			matches.append(i)
	return matches 

def value(letter): 
	return ord(letter) - 96 

def simple_hash(prev, start, new): 
	return prev - value(start) + value(new)

def find_matches_2(pattern, string): 
	matches = [] 
	k = len(pattern)

	pattern_val = 0 
	for i, char in enumerate(pattern): 
		pattern_val += value(char)

	hash_val = 0 
	for i, char in enumerate(string[:k]): 
		hash_val += value(char)

	if pattern_val == hash_val: 
		if string[:k] == pattern: 
			matches.append(0)

	for i in range(len(string) - k): 
		hash_val = simple_hash(hash_val, string[i], string[i+k])
		if hash_val == pattern_val: 
			if string[i+1:i+k+1] == pattern: 
				matches.append(i+1)

	return matches 

def power_value(letter, power): 
	return (26**power) * (ord(letter)-96)

def rabin_hash(prev, start, new, k): 
	return (prev - power_value(start, k-1))*26 + power_value(new, 0)




def find_matches_3(pattern, string): 
	matches = [] 
	k = len(pattern)

	pattern_val = 0 
	for i, char in enumerate(pattern): 
		pattern_val += power_value(char, k-i-1)

	hash_val = 0 
	for i, char in enumerate(string[:k]): 
		hash_val += power_value(char, k-i-1)

	if pattern_val == hash_val: 
		if string[:k] == pattern: 
			matches.append(0)

	for i in range(len(string) - k): 
		hash_val = rabin_hash(hash_val, string[i], string[i+k], k)
		if hash_val == pattern_val: 
			if string[i+1:i+k+1] == pattern: 
				matches.append(i+1)

	return matches 


pattern = 'abr'
string = 'abracadabra'

print("Result from First match:  ")
result = find_matches_1(pattern, string) 
print("    ", result)


print("Result from Second match:  ")
result = find_matches_2(pattern, string) 
print("    ", result)


print("Result from Third match:  ")
result = find_matches_3(pattern, string) 
print("    ", result)






















