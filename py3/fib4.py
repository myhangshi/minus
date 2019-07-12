
def fib4_new(n: int) -> int: 
	if n == 0: 
		return n 
	first: int = 0 
	second: int = 1
	for _ in range(n-1): 
		first, second = second, first+second 

	return second 

def fib4(n: int) -> int: 
	if n == 0: 
		return n 
	first: int = 0 
	second: int = 1
	for _ in range(n-1): 
		#first, second = second, first+second 
		tmp = first 
		first = second 
		second = tmp + second 
		
	return second 

if __name__ == "__main__": 
    print(fib4(5)) 
    print(fib4(500)) 


