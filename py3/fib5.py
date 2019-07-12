
def fib5(n: int) -> int: 
	yield 0 
	yield 1
	first: int = 0 
	second: int = 1
	for _ in range(n-1): 
		first, second = second, first+second 
		yield second 
	
if __name__ == "__main__": 
    for i in fib5(50): 
    	print(i) 


