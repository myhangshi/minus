from functools import lru_cache 

@lru_cache(maxsize=1000)
def fib3(n: int) -> int: 
    if n < 2: 
    	return n  
    return fib3(n-1) + fib3(n-2) 

if __name__ == "__main__": 
    print(fib3(5)) 
    print(fib3(500)) 


